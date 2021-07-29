from opentrons import protocol_api
import json
from decimal import Decimal

metadata = {
    'protocolName': 'magnetic bead clean up DNA',
    'author': 'Mark Whitehead <hlmwhite@liverpool.ac.uk>',
    'apiLevel': '2.9'
    }

### user setup

# bead mix vol
mix_bead_vol = 56

#Column range
col_range = 12

#starting sample volume
samp_vol = 20

#bead volume to add (ul)
bead_vol = 36

#water volume to add (ul)
water_vol = 9.5

#water volume for final elution (ul)
water_vol_elute = 8

#ethanol volume (ul)
eth_vol = 80

#incubation on beads time
incubate_time = 5


##### PROTOCOL

def run(protocol_context):
    #load plates
    #for testing
    mag_deck = protocol_context.load_module('magnetic module gen2', '6')

    mag_plate = mag_deck.load_labware('thermoscientific_96_wellplate_200ul', label='mag_plate')
    final_plate = protocol_context.load_labware('thermoscientific_96_wellplate_200ul', 1, label='final_plate')
    int_plate = protocol_context.load_labware('thermoscientific_96_wellplate_200ul', 3, label='intermidiate_plate')

    #engage_height=mag_plate._dimensions['zDimension']
    engage_height=9.5

    #load reagents: 
    # Column 12-beads   Column 1-water  Column 6-ethanol1  Column 7-ethanol2
    resevoir_plate = protocol_context.load_labware('nest_96_wellplate_2ml_deep', 2, label='reag_plate')

    waste_plate = protocol_context.load_labware('nest_12_reservoir_15ml', 9, label='waste_plate')

    #load tips
    _beads_tips = protocol_context.load_labware('opentrons_96_tiprack_300ul', 8)
    _eth1_tips = protocol_context.load_labware('opentrons_96_tiprack_300ul', 7)
    _eth2_tips = protocol_context.load_labware('opentrons_96_tiprack_300ul', 11)
    _water_tips = protocol_context.load_labware('opentrons_96_tiprack_20ul', 10)
    _20tips2 = protocol_context.load_labware('opentrons_96_tiprack_20ul', 4)

    #load pipettes
    p300 = protocol_context.load_instrument('p300_multi_gen2', 'right', tip_racks=[_beads_tips, _eth1_tips, _eth2_tips])
    p20 = protocol_context.load_instrument('p20_multi_gen2', 'left', tip_racks=[_water_tips, _20tips2])

    #change flow rates
    p300.flow_rate.aspirate = 140
    p20.flow_rate.dispense = 140

    # 1. transfer beads and mix

    mag_deck.disengage()
    

    for i in range(1, (col_range + 1)):
        _tipCol = "A" + str(i)
        _new_bead_vol = float(bead_vol) + float(10)
        p300.pick_up_tip(_beads_tips.wells_by_name()[_tipCol])
        if i == 1:
            p300.mix(5, mix_bead_vol, resevoir_plate.wells_by_name()['A12'])
            p300.blow_out()
        p300.transfer(bead_vol, resevoir_plate.wells_by_name()['A12'], 
            mag_plate.wells_by_name()[_tipCol], new_tip='never', mix_after=(8, _new_bead_vol), touch_tip='True')
        p300.drop_tip()

    # incubate off then on magnet
    protocol_context.delay(minutes=incubate_time)
    
    mag_deck.engage(height=engage_height)
    protocol_context.delay(minutes=5)
  
    #aspirate ethanol 1, take off supernatent then add ethanol
    spt_vol = (float(samp_vol) + float(bead_vol)) - float(5)
    for i in range(1, (col_range + 1)):
        _tipCol = "A" + str(i)
        p300.pick_up_tip(_eth1_tips.wells_by_name()[_tipCol])
        p300.aspirate(eth_vol, resevoir_plate.wells_by_name()['A6'])
        p300.air_gap(30)
        p300.dispense(30, int_plate.wells_by_name()[_tipCol])
        p300.dispense(eth_vol, int_plate.wells_by_name()[_tipCol])

        p300.aspirate(spt_vol, mag_plate.wells_by_name()[_tipCol])
        p300.dispense(spt_vol, waste_plate.wells_by_name()[_tipCol])
        protocol_context.delay(seconds=3)
        p300.blow_out()                  

        p300.aspirate(eth_vol, int_plate.wells_by_name()[_tipCol])
        p300.air_gap(30)
        p300.dispense(30, mag_plate.wells_by_name()[_tipCol])
        p300.dispense(eth_vol, mag_plate.wells_by_name()[_tipCol])

        p300.drop_tip()

    #aspirate ethanol 2, take off ethanol 1 then add ethanol

    new_eth_vol = float(eth_vol) + 20

    for i in range(1, (col_range + 1)):
        _tipCol = "A" + str(i)
        p300.pick_up_tip(_eth2_tips.wells_by_name()[_tipCol])
        p300.aspirate(eth_vol, resevoir_plate.wells_by_name()['A7'])
        p300.air_gap(30)
        p300.dispense(30, int_plate.wells_by_name()[_tipCol])
        p300.dispense(eth_vol, int_plate.wells_by_name()[_tipCol])

        p300.aspirate(new_eth_vol, mag_plate.wells_by_name()[_tipCol])
        p300.dispense(new_eth_vol, waste_plate.wells_by_name()[_tipCol])

        p300.aspirate(eth_vol, int_plate.wells_by_name()[_tipCol])
        p300.air_gap(30)
        p300.dispense(30, mag_plate.wells_by_name()[_tipCol])
        p300.dispense(eth_vol, mag_plate.wells_by_name()[_tipCol])

        p300.return_tip()

    # remove ethanol 2, air dry and add water then incubate

    for i in range(1, (col_range + 1)):
        _tipCol = "A" + str(i)
        p300.pick_up_tip(_eth2_tips.wells_by_name()[_tipCol])
        p20.pick_up_tip(_20tips2.wells_by_name()[_tipCol])
        p300.transfer(new_eth_vol, mag_plate.wells_by_name()[_tipCol], 
            waste_plate.wells_by_name()[_tipCol], new_tip='never')
        p300.drop_tip()
        p20.transfer(18, mag_plate.wells_by_name()[_tipCol], 
            waste_plate.wells_by_name()[_tipCol], new_tip='never')
        p20.drop_tip()


    
    protocol_context.delay(minutes=2)
    mag_deck.disengage()
             

    p20.flow_rate.aspirate = 140
    p20.flow_rate.dispense = 180

    elute_vol = float(water_vol) + float(2.5)
    for i in range(1, (col_range + 1)):
        _tipCol = "A" + str(i)
        p20.pick_up_tip(_water_tips.wells_by_name()[_tipCol])
        p20.transfer(elute_vol, resevoir_plate.wells_by_name()['A1'], 
            mag_plate.wells_by_name()[_tipCol], new_tip='never', mix_after=(10, water_vol))
        p20.return_tip()
    
    # incubate on magnet then transfer final elution to final plate
    protocol_context.pause(msg='Remove Plate to handle pellets')
    protocol_context.delay(minutes=2)
    mag_deck.engage(height=engage_height)
    protocol_context.delay(minutes=3)

    p300.flow_rate.aspirate = 110
    p300.flow_rate.dispense = 110
    
    for i in range(1, (col_range + 1)):
        _tipCol = "A" + str(i)
        p20.pick_up_tip(_water_tips.wells_by_name()[_tipCol])
        p20.transfer(water_vol_elute, mag_plate.wells_by_name()[_tipCol], 
            final_plate.wells_by_name()[_tipCol], new_tip='never')
        p20.drop_tip()

