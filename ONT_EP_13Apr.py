from opentrons import protocol_api
import json
from decimal import Decimal

metadata = {
    'protocolName': '2nd ONT EP script, as github desktop is a pile of wank 6th OCT',
    'author': 'Mark Whitehead <hlmwhite@liverpool.ac.uk>',
    'apiLevel': '2.9'
    }

#user setup

#plate setup (6 max)
plate_col_range = 12

reag_col = 2

single_plate = "no"

# water plate - 44 ul into each well

def run(protocol_context):
    #load plates
    
    #therm_mod = protocol_context.load_module('thermocycler', 7)
    '''
    #for testing
    with open('4titude_96_wellplate_200ul') as labware_file:
        labware_def = json.load(labware_file)
        src_pl = protocol_context.load_labware_from_definition(labware_def, 3, label='source_plate')
        reag_pl = protocol_context.load_labware_from_definition(labware_def, 4, label='reagent_plate')
        PCR_pl = therm_mod.load_labware_from_definition(labware_def, label='PCR_plate')

    '''

    '''
    dil_pl = protocol_context.load_labware('4titude_96_wellplate_200ul', 4, label='dil_plate')
    p1_plate = protocol_context.load_labware('4titude_96_wellplate_200ul', 1, label='p1_plate')
    p2_plate = protocol_context.load_labware('4titude_96_wellplate_200ul', 2, label='p2_plate')
    reagent_plate = protocol_context.load_labware('4titude_96_wellplate_200ul', 3, label='reag_plate')
    EP_pl = protocol_context.load_labware('4titude_96_wellplate_200ul', 7, label='EP_plate')
    #EP_pl = therm_mod.load_labware('4titude_96_wellplate_200ul', label='EP_plate')
    '''

    dil_pl = protocol_context.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 4, label='dil_plate')
    p1_plate = protocol_context.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 1, label='p1_plate')
    p2_plate = protocol_context.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 2, label='p2_plate')
    reagent_plate = protocol_context.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 3, label='reag_plate')
    EP_pl = protocol_context.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 7, label='EP_plate')
    
    #resevoir_plate = protocol_context.load_labware('nest_12_reservoir_15ml', 10, label='reag_plate')

    #load tips
    tip_racks_20 = [protocol_context.load_labware('opentrons_96_tiprack_20ul', slot) for slot in [5, 6]]
    
    #tip_rack_300 = [protocol_context.load_labware('opentrons_96_tiprack_300ul', slot) for slot in [11]]

    #load pipettes
    p20 = protocol_context.load_instrument('p20_multi_gen2', 'left', tip_racks=tip_racks_20)
    #p20 = protocol_context.load_instrument('p10_multi', 'left', tip_racks=tip_racks_20)

    #p300 = protocol_context.load_instrument('p300_multi_gen2', 'right', tip_racks=tip_rack_300)
    '''
    # add 44 ul of water to dil plate
    p300.pick_up_tip()
    for i in range(1, (plate_col_range + 1)):
        _tipCol = "A" + str(i)
        p300.transfer(44, resevoir_plate.wells_by_name()['A1'], 
            dil_pl.wells_by_name()[_tipCol], new_tip='never')
    p300.drop_tip()
    '''

    #load EP mix to EP plate on block
    #therm_mod.open_lid()
    
    p20.pick_up_tip()
    for i in range(1, (plate_col_range + 1)):
        _tipCol = "A" + str(i)
        _reagCol = "A" + str(reag_col)
        p20.transfer(6.6, reagent_plate.wells_by_name()[_reagCol], 
            EP_pl.wells_by_name()[_tipCol], new_tip='never')
    p20.drop_tip()
    #p20.return_tip()

    # make 1 in 10 dilution, mix and put into EP plate

    if single_plate == "yes":
        for i in range(1, (plate_col_range + 1)):
            _tipCol = "A" + str(i)
            _newCol = "A" + str(i + 6)
            p20.pick_up_tip()
            p20.transfer(3, p1_plate.wells_by_name()[_tipCol], 
                dil_pl.wells_by_name()[_tipCol], new_tip='never')
            p20.transfer(3, p1_plate.wells_by_name()[_newCol], 
                dil_pl.wells_by_name()[_tipCol], new_tip='never', mix_after=(6, 20))
            p20.transfer(3.4, dil_pl.wells_by_name()[_tipCol], 
                EP_pl.wells_by_name()[_tipCol], new_tip='never', mix_after=(4, 8))
            p20.drop_tip()
    elif single_plate == "no":
        for i in range(1, (plate_col_range + 1)):
            _tipCol = "A" + str(i)
            p20.pick_up_tip()
            p20.transfer(3, p1_plate.wells_by_name()[_tipCol], 
                dil_pl.wells_by_name()[_tipCol], new_tip='never')
            p20.transfer(3, p2_plate.wells_by_name()[_tipCol], 
            dil_pl.wells_by_name()[_tipCol], new_tip='never', mix_after=(6, 20))
            p20.transfer(3.4, dil_pl.wells_by_name()[_tipCol], 
                EP_pl.wells_by_name()[_tipCol], new_tip='never', mix_after=(4, 8))
            p20.drop_tip()
            #p20.return_tip()
    '''
    # run end prep on block
    therm_mod.close_lid()

    therm_mod.set_lid_temperature(75)

    therm_mod.set_block_temperature(20, hold_time_minutes=15, block_max_volume=10)
    therm_mod.set_block_temperature(65, hold_time_minutes=15, block_max_volume=10)

    therm_mod.set_block_temperature(4, hold_time_minutes=2, block_max_volume=10)

    protocol_context.pause(msg='protocol paused. EP finished')
    therm_mod.deactivate()
    therm_mod.open_lid()
    '''
    









