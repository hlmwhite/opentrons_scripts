from opentrons import protocol_api
import json
from decimal import Decimal

metadata = {
    'protocolName': 'RT lunascript distribution',
    'author': 'Mark Whitehead <hlmwhite@liverpool.ac.uk>',
    'apiLevel': '2.5'
    }

### user setup
# DONT HAVE PLATE 1 AND PLATE 3, OR PLATE 2 AND 3....
#   only use plates 1, 1 and 2, or 1, 2 and 3
#plate 1 setup
plate1 = 'yes'
plate1_col_range = 12

#plate 2 setup
plate2 = 'yes'
plate2_col_range = 12

#plate 3 setup
plate3 = 'no'
plate3_col_range = 12

#plate 4 setup
plate4 = 'no'
plate4_col_range = 12

def run(protocol_context):
    #load labware 
    #For testing
    '''
    with open('4titude_96_Well_Plate_200µL.json') as labware_file:
        labware_def = json.load(labware_file)
        if plate1 == "yes":
            pl1 = protocol_context.load_labware_from_definition(labware_def, 1, label='sample_plate1')
        if plate2 == "yes":
            pl2 = protocol_context.load_labware_from_definition(labware_def, 4, label='sample_plate2')
        if plate3 == "yes":
            pl3 = protocol_context.load_labware_from_definition(labware_def, 7, label='sample_plate3')
    '''
    if plate1 == "yes":
        pl1 = protocol_context.load_labware('4titude_96_wellplate_200ul', 1, label='sample_plate1')
    if plate2 == "yes":
        pl2 = protocol_context.load_labware('4titude_96_wellplate_200ul', 4, label='sample_plate2')
    if plate3 == "yes":
        pl3 = protocol_context.load_labware('4titude_96_wellplate_200ul', 7, label='sample_plate3')
    if plate4 == "yes":
        pl4 = protocol_context.load_labware('4titude_96_wellplate_200ul', 10, label='sample_plate4')    

    tube_rack = protocol_context.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 2)

    #load tips
    _1_tips = protocol_context.load_labware('opentrons_96_tiprack_20ul', 3)

    #load pipette
    p20 = protocol_context.load_instrument('p20_single_gen2', 'right', tip_racks=[_1_tips])

    # run distribution of RT mix

    if plate1 == "yes":
        for i in range(1, (plate1_col_range + 1)):
            p20.pick_up_tip()
            _col = str(i)
            p20.distribute(1.8, tube_rack.wells_by_name()['A3'], pl1.columns_by_name()[_col], new_tip='never', touch_tip='True')
            p20.drop_tip()

    if plate2 == "yes":
        for i in range(1, (plate2_col_range + 1)):
            p20.pick_up_tip()
            _col = str(i)
            p20.distribute(1.8, tube_rack.wells_by_name()['A3'], pl2.columns_by_name()[_col], new_tip='never', touch_tip='True')
            p20.drop_tip()

    if plate3 == "yes":
        for i in range(1, (plate3_col_range + 1)):
            p20.pick_up_tip()
            _col = str(i)
            p20.distribute(1.8, tube_rack.wells_by_name()['A3'], pl3.columns_by_name()[_col], new_tip='never', touch_tip='True')
            p20.drop_tip()

    if plate4 == "yes":
        for i in range(1, (plate4_col_range + 1)):
            p20.pick_up_tip()
            _col = str(i)
            p20.distribute(1.8, tube_rack.wells_by_name()['A3'], pl4.columns_by_name()[_col], new_tip='never', touch_tip='True')
            p20.drop_tip()
