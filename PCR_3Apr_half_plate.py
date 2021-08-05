import json
from decimal import Decimal
from opentrons import protocol_api

metadata = {
    'protocolName': 'PCR distribution',
    'author': 'Mark Whitehead <hlmwhite@liverpool.ac.uk>',
    'apiLevel': '2.5'
    }

### user setup

# plate 1 primer mix 1 - A2
# plate 1 primer mix 2 - A4

# plate 2 primer mix 1 - A7
# plate 2 primer mix 2 - A9


#plate 1 setup
plate1 = 'yes'
plate1_col_range = 12

#plate 2 setup
plate2 = 'yes'
plate2_col_range = 12


###########



def run(protocol_context):
    #load labware 
    #For testing
    '''
    with open('4titude_96_Well_Plate_200µL.json') as labware_file:
        labware_def = json.load(labware_file)
        if plate1 == "yes":
            pl1_PA = protocol_context.load_labware_from_definition(labware_def, 4, label='RT_pl1')
            pl1_PB = protocol_context.load_labware_from_definition(labware_def, 1, label='pl1_primer2')
        if plate2 == "yes":
            pl2_PA = protocol_context.load_labware_from_definition(labware_def, 6, label='RT_pl2')
            pl2_PB = protocol_context.load_labware_from_definition(labware_def, 3, label='pl2_primer2')
        reag_pl = protocol_context.load_labware_from_definition(labware_def, 2, label='reag_plate')
    '''
    if plate1 == "yes":
        pl1_PA = protocol_context.load_labware('4titude_96_wellplate_200ul', 4, label='RT_pl1')
        pl1_PB = protocol_context.load_labware('4titude_96_wellplate_200ul', 1, label='pl1_primer2')
    if plate2 == "yes":
        pl2_PA = protocol_context.load_labware('4titude_96_wellplate_200ul', 6, label='RT_pl2')
        pl2_PB = protocol_context.load_labware('4titude_96_wellplate_200ul', 3, label='pl2_primer2')
    reag_pl = protocol_context.load_labware('4titude_96_wellplate_200ul', 2, label='reag_plate')


    #load tips
    _1_tips = protocol_context.load_labware('opentrons_96_tiprack_20ul', 7)
    _2_tips = protocol_context.load_labware('opentrons_96_tiprack_20ul', 8)
    _3_tips = protocol_context.load_labware('opentrons_96_tiprack_20ul', 10)
    _4_tips = protocol_context.load_labware('opentrons_96_tiprack_20ul', 11)
    _5_tips = protocol_context.load_labware('opentrons_96_tiprack_20ul', 9)

    #load pipette
    p20 = protocol_context.load_instrument('p20_multi_gen2', 'left', tip_racks=[_1_tips, _2_tips, _3_tips, _4_tips, _5_tips])

    #add in primer 2 to primer2 plates
    if plate1 == "yes":
        if plate1_col_range > 6:
            p20.pick_up_tip()
            for i in range(1, (plate1_col_range + 1)):
                _col="A" + str(i)
                p20.transfer(8.1, reag_pl.wells_by_name()['A4'], pl1_PB.wells_by_name()[_col], new_tip='never')
            p20.drop_tip()
        elif plate1_col_range <= 6:
            p20.pick_up_tip()
            for i in range(1, (plate1_col_range + 1)):
                _col="A" + str(i + 6)
                #print(_col)
                p20.transfer(8.1, reag_pl.wells_by_name()['A4'], pl1_PA.wells_by_name()[_col], new_tip='never')
            p20.drop_tip()
    
    #add in samples from plate 1 to primer2
    if plate1 == "yes":
        if plate1_col_range > 6:
            for i in range(1, (plate1_col_range + 1)):
                p20.pick_up_tip()
                _col="A" + str(i)
                p20.transfer(4.1, pl1_PA.wells_by_name()[_col], pl1_PB.wells_by_name()[_col], new_tip='never')
                p20.drop_tip()
        elif plate1_col_range <= 6:
            for i in range(1, (plate1_col_range + 1)):
                p20.pick_up_tip()
                _src_col="A" + str(i)
                _col="A" + str(i + 6)
                p20.transfer(4.1, pl1_PA.wells_by_name()[_src_col], pl1_PA.wells_by_name()[_col], new_tip='never')
                p20.drop_tip()

    #add in primer1 to plate 1
    if plate1 == "yes":
        for i in range(1, (plate1_col_range + 1)):
            p20.pick_up_tip()
            _col="A" + str(i)
            p20.transfer(8.1, reag_pl.wells_by_name()['A2'], pl1_PA.wells_by_name()[_col], new_tip='never')
            p20.drop_tip()


    #add in primer 2 to primer2 plates
    if plate2 == "yes":
        if plate2_col_range > 6:
            p20.pick_up_tip()
            for i in range(1, (plate2_col_range + 1)):
                _col="A" + str(i)
                p20.transfer(8.1, reag_pl.wells_by_name()['A9'], pl2_PB.wells_by_name()[_col], new_tip='never')
            p20.drop_tip()
        elif plate2_col_range <= 6:
            p20.pick_up_tip()
            for i in range(1, (plate2_col_range + 1)):
                _col="A" + str(i + 6)
                #print(_col)
                p20.transfer(8.1, reag_pl.wells_by_name()['A9'], pl2_PA.wells_by_name()[_col], new_tip='never')
            p20.drop_tip()


    #add in samples from plate 2 to primer2
    if plate2 == "yes":
        if plate2_col_range > 6:
            for i in range(1, (plate2_col_range + 1)):
                p20.pick_up_tip()
                _col="A" + str(i)
                p20.transfer(4.1, pl2_PA.wells_by_name()[_col], pl2_PB.wells_by_name()[_col], new_tip='never')
                p20.drop_tip()
        elif plate2_col_range <= 6:
            for i in range(1, (plate2_col_range + 1)):
                p20.pick_up_tip()
                _src_col="A" + str(i)
                _col="A" + str(i + 6)
                p20.transfer(4.1, pl2_PA.wells_by_name()[_src_col], pl2_PA.wells_by_name()[_col], new_tip='never')
                p20.drop_tip()

    #add in primer1 to plate 2
    if plate2 == "yes":
        for i in range(1, (plate2_col_range + 1)):
            p20.pick_up_tip()
            _col="A" + str(i)
            p20.transfer(8.1, reag_pl.wells_by_name()['A7'], pl2_PA.wells_by_name()[_col], new_tip='never')
            p20.drop_tip()

