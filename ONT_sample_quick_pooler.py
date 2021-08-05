from opentrons import protocol_api
import json
from decimal import Decimal

metadata = {
    'protocolName': 'sample pooler for ONT',
    'author': 'Mark Whitehead <hlmwhite@liverpool.ac.uk>',
    'apiLevel': '2.9'
    }

######### USER INPUT

first_well="C6"

last_well="D11"   # advised to add controls separately for now
                 # add them in first over two tubes, so that the Opentrons can pipette into liquid
                 # ALSO assumes controls are at the end of the plate and not in the middle

sample_vol=5.7

same_tip_opt="yes"    # only use "yes" or "no" only!!


######### USER INPUT END





_split = 1
_row, _col = last_well[:_split], last_well[_split:]

_well_list = {
    'A1':'1',
    'B1':'2',
    'C1':'3',
    'D1':'4',
    'E1':'5',
    'F1':'6',
    'G1':'7',
    'H1':'8',
    'A2':'9',
    'B2':'10',
    'C2':'11',
    'D2':'12',
    'E2':'13',
    'F2':'14',
    'G2':'15',
    'H2':'16',
    'A3':'17',
    'B3':'18',
    'C3':'19',
    'D3':'20',
    'E3':'21',
    'F3':'22',
    'G3':'23',
    'H3':'24',
    'A4':'25',
    'B4':'26',
    'C4':'27',
    'D4':'28',
    'E4':'29',
    'F4':'30',
    'G4':'31',
    'H4':'32',
    'A5':'33',
    'B5':'34',
    'C5':'35',
    'D5':'36',
    'E5':'37',
    'F5':'38',
    'G5':'39',
    'H5':'40',
    'A6':'41',
    'B6':'42',
    'C6':'43',
    'D6':'44',
    'E6':'45',
    'F6':'46',
    'G6':'47',
    'H6':'48',
    'A7':'49',
    'B7':'50',
    'C7':'51',
    'D7':'52',
    'E7':'53',
    'F7':'54',
    'G7':'55',
    'H7':'56',
    'A8':'57',
    'B8':'58',
    'C8':'59',
    'D8':'60',
    'E8':'61',
    'F8':'62',
    'G8':'63',
    'H8':'64',
    'A9':'65',
    'B9':'66',
    'C9':'67',
    'D9':'68',
    'E9':'69',
    'F9':'70',
    'G9':'71',
    'H9':'72',
    'A10':'73',
    'B10':'74',
    'C10':'75',
    'D10':'76',
    'E10':'77',
    'F10':'78',
    'G10':'79',
    'H10':'80',
    'A11':'81',
    'B11':'82',
    'C11':'83',
    'D11':'84',
    'E11':'85',
    'F11':'86',
    'G11':'87',
    'H11':'88',
    'A12':'89',
    'B12':'90',
    'C12':'91',
    'D12':'92',
    'E12':'93',
    'F12':'94',
    'G12':'95',
    'H12':'96'
}


start_num = int(_well_list[first_well])
final_num = int(_well_list[last_well])

list=["A", "B", "C", "D", "E", "F", "G", "H"]
samples=[]
for i in range(1, 13):
    for _letter in list:
        _samp = _letter + str(i)
        _samp_num = int(_well_list[_samp])
        if _samp_num >= start_num and _samp_num <= final_num:
            samples.append(_samp)

def run(protocol_context):
    #load plates
    #therm_mod = protocol_context.load_module('thermocycler', 7)
    
    #for testing
    '''  
    with open('4titude_96_Well_Plate_200µL.json') as labware_file:
        labware_def = json.load(labware_file)
        src_pl = protocol_context.load_labware_from_definition(labware_def, 2, label='source_plate')
    '''
    src_pl = protocol_context.load_labware('nest_96_wellplate_100ul_pcr_full_skirt', 2, label='source_plate')

    #load tips
    _20_tips = protocol_context.load_labware('opentrons_96_tiprack_20ul', 6)

    #load eppendorf tubes and rack
    tube_rack = protocol_context.load_labware('opentrons_24_tuberack_eppendorf_1.5ml_safelock_snapcap', 3)

    #load pipettes    
    p20 = protocol_context.load_instrument('p20_single_gen2', 'right', tip_racks=[_20_tips])


    if same_tip_opt == "yes":
        p20.pick_up_tip()
        for pos in samples:
            p20.transfer(sample_vol, src_pl.wells_by_name()[pos],
                tube_rack.wells_by_name()['A1'], new_tip='never', touch_tip='True')
            p20.blow_out()
        p20.drop_tip()
    elif same_tip_opt == "no":
        for pos in samples:
            p20.pick_up_tip()
            p20.transfer(sample_vol, src_pl.wells_by_name()[pos],
                tube_rack.wells_by_name()['A1'], new_tip='never', touch_tip='True')
            p20.drop_tip()        


