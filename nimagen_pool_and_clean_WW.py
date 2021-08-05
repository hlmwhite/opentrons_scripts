from opentrons import protocol_api
import json
from decimal import Decimal

metadata = {
    'protocolName': 'nimagen plate pooling and library clean up for wastewater samples',
    'author': 'Mark Whitehead <hlmwhite@liverpool.ac.uk>',
    'apiLevel': '2.10'
    }

######### USER INPUT

# 4 plates max
plate1="yes"
plate2="yes"
plate3="no"
plate4="no"

plate_col_range_1=12
plate_col_range_2=12
plate_col_range_3=12
plate_col_range_4=12

####################





########## PROTOCOL


#list_A=["A1", "B1", "C1", "D1", "E1", "F1", "G1", "H1"]
#list_B=["A2", "B2", "C2", "D2", "E2", "F2", "G2", "H2"]

list=["A", "B", "C", "D", "E", "F", "G", "H"]


if plate1 == "yes":
    if plate_col_range_1 >= 5:
        _strip_vol_1 = 4
        _pool_plate_vol_1 = (plate_col_range_1 * _strip_vol_1)
        _prop_vol_1 = (_pool_plate_vol_1/6)
        _pool_tube_vol_1 = (_pool_plate_vol_1 - _prop_vol_1)
    elif plate_col_range_1 <= 4:
        _strip_vol_1 = 8
        _pool_plate_vol_1 = (plate_col_range_1 * _strip_vol_1)
        _prop_vol_1 = (_pool_plate_vol_1/6)
        _pool_tube_vol_1 = (_pool_plate_vol_1 - _prop_vol_1)
    elif plate_col_range_1 <= 2:
        _strip_vol_1 = 12
        _pool_plate_vol_1 = (plate_col_range_1 * _strip_vol_1)
        _prop_vol_1 = (_pool_plate_vol_1/6)
        _pool_tube_vol_1 = (_pool_plate_vol_1 - _prop_vol_1)

if plate2 == "yes":
    if plate_col_range_2 >= 5:
        _strip_vol_2 = 4
        _pool_plate_vol_2 = (plate_col_range_2 * _strip_vol_2)
        _prop_vol_2 = (_pool_plate_vol_2/6)
        _pool_tube_vol_2 = (_pool_plate_vol_2 - _prop_vol_2)
    elif plate_col_range_2 <= 4:
        _strip_vol_2 = 8
        _pool_plate_vol_2 = (plate_col_range_2 * _strip_vol_2)
        _prop_vol_2 = (_pool_plate_vol_2/6)
        _pool_tube_vol_2 = (_pool_plate_vol_2 - _prop_vol_2)
    elif plate_col_range_2 <= 2:
        _strip_vol_2 = 12
        _pool_plate_vol_2 = (plate_col_range_2 * _strip_vol_2)
        _prop_vol_2 = (_pool_plate_vol_2/6)
        _pool_tube_vol_2 = (_pool_plate_vol_2 - _prop_vol_2)

if plate3 == "yes":
    if plate_col_range_3 >= 5:
        _strip_vol_3 = 4
        _pool_plate_vol_3 = (plate_col_range_3 * _strip_vol_3)
        _prop_vol_3 = (_pool_plate_vol_3/6)
        _pool_tube_vol_3 = (_pool_plate_vol_3 - _prop_vol_3)
    elif plate_col_range_3 <= 4:
        _strip_vol_3 = 8
        _pool_plate_vol_3 = (plate_col_range_3 * _strip_vol_3)
        _prop_vol_3 = (_pool_plate_vol_3/6)
        _pool_tube_vol_3 = (_pool_plate_vol_3 - _prop_vol_3)
    elif plate_col_range_3 <= 2:
        _strip_vol_3 = 12
        _pool_plate_vol_3 = (plate_col_range_3 * _strip_vol_3)
        _prop_vol_3 = (_pool_plate_vol_3/6)
        _pool_tube_vol_3 = (_pool_plate_vol_3 - _prop_vol_3)

if plate4 == "yes":
    if plate_col_range_4 >= 5:
        _strip_vol_4 = 4
        _pool_plate_vol_4 = (plate_col_range_4 * _strip_vol_4)
        _prop_vol_4 = (_pool_plate_vol_4/6)
        _pool_tube_vol_4 = (_pool_plate_vol_4 - _prop_vol_4)
    elif plate_col_range_4 <= 4:
        _strip_vol_4 = 8
        _pool_plate_vol_4 = (plate_col_range_4 * _strip_vol_4)
        _prop_vol_4 = (_pool_plate_vol_4/6)
        _pool_tube_vol_4 = (_pool_plate_vol_4 - _prop_vol_4)
    elif plate_col_range_4 <= 2:
        _strip_vol_4 = 12
        _pool_plate_vol_4 = (plate_col_range_4 * _strip_vol_4)
        _prop_vol_4 = (_pool_plate_vol_4/6)
        _pool_tube_vol_4 = (_pool_plate_vol_4 - _prop_vol_4)


def run(protocol_context):
    # load plates
    mag_deck = protocol_context.load_module('magnetic module gen2', '6')
    #mag_deck = protocol_context.load_module('magnetic module', '6')
    mag_plate = mag_deck.load_labware('biorad_96_wellplate_200ul_pcr', label='mag_plate')

    PCR_plate1 = protocol_context.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', 1, label='PCR_A')
    PCR_plate2 = protocol_context.load_labware('opentrons_96_aluminumblock_generic_pcr_strip_200ul', 2, label='PCR_B')

    waste_plate = protocol_context.load_labware('nest_1_reservoir_195ml', 9, label='waste_plate')

    # load tips
    #tip_rack_20 = [protocol_context.load_labware('opentrons_96_tiprack_20ul', slot) for slot in [7, 8, 10]]
    #tip_rack_20 = [protocol_context.load_labware('opentrons_96_tiprack_20ul', slot) for slot in [10]]
    tips20_1 = protocol_context.load_labware('opentrons_96_tiprack_20ul', 4)
    tips20_2 = protocol_context.load_labware('opentrons_96_tiprack_20ul', 5)
    tips20_3 = protocol_context.load_labware('opentrons_96_tiprack_20ul', 10)
    tip_rack_300 = [protocol_context.load_labware('opentrons_96_tiprack_300ul', slot) for slot in [11]]

    # load eppendorf tubes and rack
    # C4 beads,  B6 TE-buffer,    B2 int pool A, B3 int pool B ,    D1 final pool A, D2 final pool B
    #### ignore that layout ^^
    tube_rack = protocol_context.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 3)
    ## B1 ethanol
    tube_15ml = protocol_context.load_labware('opentrons_10_tuberack_falcon_4x50ml_6x15ml_conical', 7)

    # load pipettes
    p20 = protocol_context.load_instrument('p20_multi_gen2', 'left', tip_racks=[tips20_1, tips20_2, tips20_3])
    p300 = protocol_context.load_instrument('p300_single_gen2', 'right', tip_racks=tip_rack_300)

    #engage_height=mag_plate._dimensions['zDimension']
    engage_height=9.5
    mag_deck.disengage()

    # functions

    def _pooling(_colNum, stripVol, _magPlateCol):
        for i in range(1, (_colNum + 1)):
            _poolCol = "A" + str(_magPlateCol)
            _col="A" + str(i)
            p20.pick_up_tip(tips20_1.wells_by_name()[_col])
            p20.transfer(stripVol, PCR_plate1.wells_by_name()[_col],
                mag_plate.wells_by_name()[_poolCol], new_tip='never')
            #p20.drop_tip()
            p20.return_tip()

        for i in range(1, (_colNum + 1)):
            _poolCol = "A" + str(_magPlateCol + 1)
            _col="A" + str(i)
            p20.pick_up_tip(tips20_2.wells_by_name()[_col])
            p20.transfer(stripVol, PCR_plate2.wells_by_name()[_col],
                mag_plate.wells_by_name()[_poolCol], new_tip='never')
            #p20.drop_tip()
            p20.return_tip()

    def _pool_to_tube(_poolVol, _colToPool, _destEppendorfWell_A, _destEppendorfWell_B):
        p300.pick_up_tip()
        #mix_vol = _pool_tube_vol
        mix_vol = _poolVol
        list_A = []
        for _row in list:
            _well = str(_row) + str(_colToPool)
            list_A.append(_well)
        for pos in list_A:
            if mix_vol == _poolVol:
                p300.transfer(_poolVol, mag_plate.wells_by_name()[pos],
                    tube_rack.wells_by_name()[_destEppendorfWell_A], new_tip='never')
            elif mix_vol > _poolVol:
                _tube_mix_vol = (mix_vol - 10)
                if _tube_mix_vol > 200:
                    _tube_mix_vol = 200
                p300.transfer(_poolVol, mag_plate.wells_by_name()[pos],
                    tube_rack.wells_by_name()[_destEppendorfWell_A], new_tip='never', mix_after=(2, _tube_mix_vol))
            mix_vol = (mix_vol + _poolVol)
        p300.drop_tip()

        p300.pick_up_tip()
        #mix_vol = _pool_tube_vol
        mix_vol = _poolVol
        _2colToPool = _colToPool + 1
        list_A = []
        for _row in list:
            _well = str(_row) + str(_2colToPool)
            list_A.append(_well)
        for pos in list_A:
            if mix_vol == _poolVol:
                p300.transfer(_poolVol, mag_plate.wells_by_name()[pos],
                    tube_rack.wells_by_name()[_destEppendorfWell_B], new_tip='never')
            elif mix_vol > _poolVol:
                _tube_mix_vol = (mix_vol - 10)
                if _tube_mix_vol > 200:
                    _tube_mix_vol = 200
                p300.transfer(_poolVol, mag_plate.wells_by_name()[pos],
                    tube_rack.wells_by_name()[_destEppendorfWell_B], new_tip='never', mix_after=(2, _tube_mix_vol))
            mix_vol = (mix_vol + _poolVol)
        p300.drop_tip()

    def _dilute_pool(_poolA_PlatePos, _poolB_PlatePos):
        p300.transfer(37.5, tube_rack.wells_by_name()['D6'], mag_plate.wells_by_name()[_poolA_PlatePos], new_tip='never')
        p300.transfer(37.5, tube_rack.wells_by_name()['D6'], mag_plate.wells_by_name()[_poolB_PlatePos], new_tip='never')

    _wells_to_clean1 = []
    def _add_pool(_poolA_TubePos, _poolB_TubePos, _poolA_PlatePos, _poolB_PlatePos):
        p300.pick_up_tip()
        #p300.transfer(37.5, tube_rack.wells_by_name()[_poolA_TubePos], mag_plate.wells_by_name()[_poolA_PlatePos], new_tip='never')
        p300.transfer(70, tube_rack.wells_by_name()[_poolA_TubePos], mag_plate.wells_by_name()[_poolA_PlatePos], new_tip='never')
        p300.drop_tip()
        p300.pick_up_tip()
        #p300.transfer(37.5, tube_rack.wells_by_name()[_poolB_TubePos], mag_plate.wells_by_name()[_poolB_PlatePos], new_tip='never')
        p300.transfer(70, tube_rack.wells_by_name()[_poolB_TubePos], mag_plate.wells_by_name()[_poolB_PlatePos], new_tip='never')
        p300.drop_tip()
        _wells_to_clean1.append(_poolA_PlatePos)
        _wells_to_clean1.append(_poolB_PlatePos)

    _wells_to_clean2 = []
    def _elute_clean1(_srcCol, _destCol):
        p300.pick_up_tip()
        p300.transfer(70, mag_plate.wells_by_name()[_srcCol], mag_plate.wells_by_name()[_destCol], new_tip='never')
        p300.drop_tip()
        _wells_to_clean2.append(_destCol)


    def _get_elute2(_srcWell, _destTube):
        p300.pick_up_tip()
        p300.transfer(20, mag_plate.wells_by_name()[_srcWell], tube_rack.wells_by_name()[_destTube], new_tip='never')
        p300.drop_tip()
    
    #### PLATE POOLING

    protocol_context.set_rail_lights(True)
    
    if plate1=="yes":
        #protocol_context.set_rail_lights(True)
        protocol_context.pause(msg='swap p20 tips 4 and 5 and add PCR plates A and B...')
        #protocol_context.set_rail_lights(False)
        _pooling(plate_col_range_1, _strip_vol_1, 1)
    if plate2=="yes":
        #protocol_context.set_rail_lights(True)
        protocol_context.pause(msg='swap p20 tips 4 and 5 and add PCR plates A and B...')
        #protocol_context.set_rail_lights(False)
        _pooling(plate_col_range_2, _strip_vol_2, 3)
    if plate3=="yes":
        #protocol_context.set_rail_lights(True)
        protocol_context.pause(msg='swap p20 tips 4 and 5 and add PCR plates A and B...')
        #protocol_context.set_rail_lights(False)
        _pooling(plate_col_range_3, _strip_vol_3, 5)
    if plate4=="yes":
        #protocol_context.set_rail_lights(True)
        protocol_context.pause(msg='swap p20 tips 7 and 8 and add PCR plates A and B...')
        #protocol_context.set_rail_lights(False)
        _pooling(plate_col_range_4, _strip_vol_4, 7)
    
    protocol_context.pause(msg='remove PCR plates to fridge/freezer')

    #protocol_context.set_rail_lights(False)

    # pool samples in to tubes


    if plate1=="yes":
        _pool_to_tube(_pool_tube_vol_1, 1, "A1", "B1")
    if plate2=="yes":
        _pool_to_tube(_pool_tube_vol_2, 3, "A2", "B2")
    if plate3=="yes":
        _pool_to_tube(_pool_tube_vol_2, 5, "A3", "B3")
    if plate4=="yes":
        _pool_to_tube(_pool_tube_vol_2, 7, "A4", "B4")


    '''
    p300.pick_up_tip()
    if plate1=="yes":
        _dilute_pool("A10", "B10")
    if plate2=="yes":
        _dilute_pool("C10", "D10")
    if plate3=="yes":
        _dilute_pool("E10", "F10")
    if plate4=="yes":
        _dilute_pool("G10", "H10")
    p300.drop_tip()
    '''

    if plate1=="yes":
        _add_pool("A1", "B1", "A10", "B10")
    if plate2=="yes":
        _add_pool("A2", "B2", "C10", "D10")
    if plate3=="yes":
        _add_pool("A3", "B3", "E10", "F10")
    if plate4=="yes":
        _add_pool("A4", "B4", "G10", "H10")

    '''
    p300.pick_up_tip()
        p300.mix(10, 200, tube_rack.wells_by_name()['A6'])
        p300.drop_tip()
    '''
    protocol_context.set_rail_lights(False)

    protocol_context.pause(msg='vortex beads tube...')
        
    protocol_context.set_rail_lights(True)

    for _well in _wells_to_clean1:
        p300.pick_up_tip()
        p300.transfer(59.5, tube_rack.wells_by_name()['A6'], mag_plate.wells_by_name()[_well], 
            mix_after=(6, 100), new_tip='never')
        p300.drop_tip()

    # incubate off and on magnent
    protocol_context.delay(minutes=5)
    
    mag_deck.engage(height=engage_height)
    protocol_context.delay(minutes=5)
    
    # remove supernatent and add 100 uL ethanol
    for _well in _wells_to_clean1:
        p300.pick_up_tip()
        p300.transfer(130, mag_plate.wells_by_name()[_well], waste_plate.wells_by_name()['A1'], new_tip='never')
        p300.drop_tip()
        p300.pick_up_tip()
        p300.transfer(100, tube_15ml.wells_by_name()['B1'], mag_plate.wells_by_name()[_well], new_tip='never')
        p300.drop_tip()

    # remove ethanol 1 and add 100 uL ethanol
    for _well in _wells_to_clean1:
        p300.pick_up_tip()
        p300.transfer(100, mag_plate.wells_by_name()[_well], waste_plate.wells_by_name()['A1'], new_tip='never')
        p300.drop_tip()
        p300.pick_up_tip()
        p300.transfer(100, tube_15ml.wells_by_name()['B1'], mag_plate.wells_by_name()[_well], new_tip='never')
        p300.drop_tip()

    # remove ethanol 2 and go back in with p20 to get residue
    for _well in _wells_to_clean1:
        p300.pick_up_tip()
        p300.transfer(100, mag_plate.wells_by_name()[_well], waste_plate.wells_by_name()['A1'], new_tip='never')
        p300.drop_tip()

    p20.pick_up_tip()
    p20.transfer(20, mag_plate.wells_by_name()['A10'], waste_plate.wells_by_name()['A1'], new_tip='never')
    p20.drop_tip()

    #incubate to air air dry on magnet, resuspend in 100 ul TE
    protocol_context.delay(minutes=1)

    mag_deck.disengage()
    for _well in _wells_to_clean1:
        p300.pick_up_tip()
        p300.transfer(75, tube_rack.wells_by_name()['D6'], mag_plate.wells_by_name()[_well], new_tip='never', mix_after=(5, 65))
        p300.drop_tip()
    
    protocol_context.delay(minutes=2)

    # incubate on magnet and elute into a new well for second clean up
    mag_deck.engage(height=engage_height)
    protocol_context.delay(minutes=4)

    if plate1=="yes":
        _elute_clean1("A10", "A12")
        _elute_clean1("B10", "B12")
    if plate2=="yes":
        _elute_clean1("C10", "C12")
        _elute_clean1("D10", "D12")
    if plate3=="yes":
        _elute_clean1("E10", "E12")
        _elute_clean1("F10", "F12")
    if plate4=="yes":
        _elute_clean1("G10", "G12")
        _elute_clean1("H10", "H12")

    
    ## CLEAN UP NUMBER 2, ELECTRIC BOOGALOO
    mag_deck.disengage()
    '''
    p300.pick_up_tip()
    p300.mix(10, 200, tube_rack.wells_by_name()['A6'])
    p300.drop_tip()
    '''
    protocol_context.set_rail_lights(False)

    protocol_context.pause(msg='vortex beads tube and check ethanol...')
        
    protocol_context.set_rail_lights(True)

    for _well in _wells_to_clean2:
        p300.pick_up_tip()
        p300.transfer(52.5, tube_rack.wells_by_name()['A6'], mag_plate.wells_by_name()[_well], 
            mix_after=(6, 100), new_tip='never')
        p300.drop_tip()

    # incubate off and on magnent
    protocol_context.delay(minutes=5)
    
    mag_deck.engage(height=engage_height)
    protocol_context.delay(minutes=5)

    # remove supernatent and add 100 uL ethanol
    for _well in _wells_to_clean2:
        p300.pick_up_tip()
        p300.transfer(118, mag_plate.wells_by_name()[_well], waste_plate.wells_by_name()['A1'], new_tip='never')
        p300.drop_tip()
        p300.pick_up_tip()
        p300.transfer(100, tube_15ml.wells_by_name()['B1'], mag_plate.wells_by_name()[_well], new_tip='never')
        p300.drop_tip()

    # remove ethanol 1 and add 100 uL ethanol
    for _well in _wells_to_clean2:
        p300.pick_up_tip()
        p300.transfer(100, mag_plate.wells_by_name()[_well], waste_plate.wells_by_name()['A1'], new_tip='never')
        p300.drop_tip()
        p300.pick_up_tip()
        p300.transfer(100, tube_15ml.wells_by_name()['B1'], mag_plate.wells_by_name()[_well], new_tip='never')
        p300.drop_tip()

    # remove ethanol 2 and go back in with p20 to get residue
    for _well in _wells_to_clean2:
        p300.pick_up_tip()
        p300.transfer(100, mag_plate.wells_by_name()[_well], waste_plate.wells_by_name()['A1'], new_tip='never')
        p300.drop_tip()

    p20.pick_up_tip()
    p20.transfer(20, mag_plate.wells_by_name()['A12'], waste_plate.wells_by_name()['A1'], new_tip='never')
    p20.drop_tip()

    #incubate to air air dry on magnet, resuspend in 25 ul TE
    protocol_context.set_rail_lights(False)

    protocol_context.delay(minutes=1)

    protocol_context.set_rail_lights(True)

    mag_deck.disengage()

    p300.flow_rate.aspirate = 140
    p300.flow_rate.dispense = 140

    for _well in _wells_to_clean2:
        p300.pick_up_tip()
        p300.transfer(25, tube_rack.wells_by_name()['D6'], mag_plate.wells_by_name()[_well], new_tip='never', mix_after=(10, 20))
        p300.drop_tip()

    protocol_context.delay(minutes=2)

    # incubate on magnet and elute into a new well for second clean up
    mag_deck.engage(height=engage_height)
    protocol_context.delay(minutes=4)

    p300.flow_rate.aspirate = 140
    p300.flow_rate.dispense = 140
    
    p300.flow_rate.aspirate = 80
    p300.flow_rate.dispense = 80

    if plate1=="yes":
        _get_elute2("A12", "C1")
        _get_elute2("B12", "D1")
    if plate2=="yes":
        _get_elute2("C12", "C2")
        _get_elute2("D12", "D2")
    if plate3=="yes":
        _get_elute2("E12", "C3")
        _get_elute2("F12", "D3")
    if plate4=="yes":
        _get_elute2("G12", "C4")
        _get_elute2("H12", "D4")

    ### finished!
    protocol_context.set_rail_lights(False)

    protocol_context.pause(msg='Protocol finished!!')

