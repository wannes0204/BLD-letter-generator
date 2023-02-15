import numpy as np


dict = {
    1:'A',
    2:'B',
    3:'C',
    4:'D',
    5:'E',
    6:'F',
    7:'G',
    8:'H',
    9:'I',
    10:'J',
    11:'K',
    12:'L',
    13:'M',
    14:'N',
    15:'O',
    16:'P',
    17:'Q',
    18:'R',
    19:'S',
    20:'T',
    21:'U',
    22:'V',
    23:'W',
    24:'X',
    25:'Y',
    26:'Z',
}

stop_test = 'Not done yet'


while stop_test not in ['stop', 'Stop', 'quit', 'Quit', 'Abort', 'abort', 'clear']:
    lst = np.random.randint(1, 26, np.random.randint(8,12))
    lst_dict = [dict[element] for element in lst]
    print(' '.join(lst_dict))
    stop_test = input('')
    