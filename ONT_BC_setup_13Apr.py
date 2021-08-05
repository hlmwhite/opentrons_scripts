from opentrons import protocol_api
import json
from decimal import Decimal

metadata = {
    'protocolName': 'barcoding set up ONT',
    'author': 'Mark Whitehead <hlmwhite@liverpool.ac.uk>',
    'apiLevel': '2.9'
    }

#user setup

#plate setup (6 max)
plate_col_range = 12

reag_col = 11

# 280 water, 560 mm, 28 enhancer

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
    reagent_plate = protocol_context.load_labware('4titude_96_wellplate_200ul', 1, label='reag_plate')
    #EP_pl = therm_mod.load_labware('4titude_96_wellplate_200ul', label='EP_plate')
    BC_plate = protocol_context.load_labware('4titude_96_wellplate_200ul', 3, label='BC_plate')
    EP_pl = protocol_context.load_labware('4titude_96_wellplate_200ul', 7, label='EP_plate')
    '''
    reagent_plate = protocol_context.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 1, label='reag_plate')
    #EP_pl = therm_mod.load_labware('4titude_96_wellplate_200ul', label='EP_plate')
    BC_plate = protocol_context.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 3, label='BC_plate')
    EP_pl = protocol_context.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 7, label='EP_plate')


    #load tips
    tip_racks_20 = [protocol_context.load_labware('opentrons_96_tiprack_20ul', slot) for slot in [2, 4]]

    #load pipettes
    p20 = protocol_context.load_instrument('p20_multi_gen2', 'left', tip_racks=tip_racks_20)
    #p20 = protocol_context.load_instrument('p10_multi', 'left', tip_racks=tip_racks_20)

    #add DNA to BC plate
    #therm_mod.open_lid()
    
    for i in range(1, (plate_col_range + 1)):
        _tipCol = "A" + str(i)
        p20.pick_up_tip()
        p20.transfer(1.2, EP_pl.wells_by_name()[_tipCol], 
            BC_plate.wells_by_name()[_tipCol], new_tip='never')
        p20.drop_tip()
        #p20.return_tip()

    # add LM mix to BC plate and mix
    for i in range(1, (plate_col_range + 1)):
        _tipCol = "A" + str(i)
        _reagCol = "A" + str(reag_col)
        p20.pick_up_tip()
        p20.transfer(7.7, reagent_plate.wells_by_name()[_reagCol], 
            BC_plate.wells_by_name()[_tipCol], new_tip='never', mix_after=(2, 8))
        p20.drop_tip()
        #p20.return_tip()
    

