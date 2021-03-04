import math
import time
from pygame import init()


def integer_to_vietnamese_numeral(n, region='north', activate_tts=False):
    """Convert integer number to vietnamese numeral, saying and display it

    Args:
        n (int): A integer number
        region (str, optional): local region in Vietnam'north', 'south'.
            Defaults to 'north'.
        activate_tts (bool, optional): Repalce False = True to activate
            text to speech. Defaults to False.

    Raises:
        TypeError: If 'n' is Not an integer, Argument "region" is not a string,
            'Argument "activate_tts" is not a boolean'
        OverflowError: number 'n' greater than 999,999,999,999
        ValueError: 'n' is Not a positive integer, Argument "region" has
            not a correct value

    Returns:
        [str]:Say and Display vietnamese numeral
    """
    if not isinstance(n, int):
        raise TypeError('Not an integer')
    if n >= math.pow(10, 12):
        raise OverflowError("Integer greater than 999,999,999,999")
    if n < 0:
        raise ValueError('Not a positive integer')
    if not isinstance(region, str):
        raise TypeError('Argument "region" is not a string')
    if region not in ('south', 'north'):
        raise ValueError('Argument "region" has not a correct value')
    if not isinstance(activate_tts, bool):
        raise TypeError('Argument "activate_tts" is not a boolean')

    dict_cardinal_num = {
        0: 'không', 1: 'một', 2: 'hai', 3: 'ba', 4: 'bốn',
        5: 'năm', 6: 'sáu', 7: 'bảy', 8: 'tám', 9: 'chín'
    }
    dict_place_value = ['tỷ', 'triệu', 'nghìn', ""]
    dict_path = {
        'không': 'khong', 'một': 'mot1', 'hai': 'hai', 'ba': 'ba',
        'bốn': 'bon', 'năm': 'nam', 'sáu': 'sau', 'bảy': 'bay',
        'tám': 'tam', 'chín': 'chin', 'mười': 'muoi1', 'mươi': 'muoi2',
        'mốt': 'mot2', 'linh': 'linh', 'lẻ': 'le', 'nghìn': 'nghin',
        'ngàn': 'ngan', 'trăm': 'tram', 'triệu': 'trieu', 'tỷ': 'ty',
        'lăm': 'lam'
    }
    sound_basedir_N = "./sounds/vie/north"
    sound_basedir_S = "./sounds/vie/south"
    list_cardinal_numeral = []
    count = 0
    for i in range(4):
        base_num = n // math.pow(10, 9 - i * 3)
        if base_num > 0:
            count += 1
            list_cardinal_numeral.append(
                base_number(base_num, count, dict_cardinal_num)
            )
            list_cardinal_numeral.append(dict_place_value[i])
            n = n % pow(10, 9 - i * 3)
    string_cardinal_numeral = " ".join(list_cardinal_numeral)
    if region == 'south':
        string_cardinal_numeral =\
            string_cardinal_numeral.replace("linh", "lẻ")
        string_cardinal_numeral =\
            string_cardinal_numeral.replace("nghìn", "ngàn")
    list_numerals = string_cardinal_numeral.split()
    if activate_tts:
        for numeral in list_numerals:
            if region == "south":
                path = sound_basedir_S + "/" + dict_path[numeral] + ".ogg"
            else:
                path = sound_basedir_N + "/" + dict_path[numeral] + ".ogg"
            sound = pygame.mixer.Sound(path)
            sound.play()
            time.sleep(sound.get_length())
            sound.stop()
    return string_cardinal_numeral


def base_number(number, count, dict_cardinal_num):
    """This function convert interger number < 1000 to vietnamese numeral

    Args:
        number (int): The function give number < 1000
        count (int): 'count' is a ordinal
        dict_cardinal_num (dict): This is a dictionary of cardinal numerals

    Returns:
        str: return a string cardinal numerals of number
    """
    special_numeral = ["trăm", "mười", "mươi", "linh", "lăm", "mốt"]
    list_cardinal_numeral = []
    # Divide number (abc) and follow place's number
    a = number // 100           # hundreds
    b = (number % 100) // 10    # Tens
    c = number % 10             # Ones
    # check a
    if a > 0:
        list_cardinal_numeral.append(dict_cardinal_num[a])
        list_cardinal_numeral.append(special_numeral[0])
    elif a == 0:
        if count > 1 and (b > 0 or c > 0):
            list_cardinal_numeral.append(dict_cardinal_num[a])
            list_cardinal_numeral.append(special_numeral[0])
    # check b
    if b == 0:
        if c > 0:
            if a > 0 or count > 1:
                list_cardinal_numeral.append(special_numeral[3])
    elif b > 0:
        if b == 1:
            list_cardinal_numeral.append(special_numeral[1])
        elif b > 1:
            list_cardinal_numeral.append(dict_cardinal_num[b])
            list_cardinal_numeral.append(special_numeral[2])
    # check c
    if c == 0:
        if count == 1 and a == 0 and b == 0:
            list_cardinal_numeral.append(dict_cardinal_num[c])
    elif c > 0:
        if b >= 1 and c == 5:
            list_cardinal_numeral.append(special_numeral[4])
        elif b >= 2 and c == 1:
            list_cardinal_numeral.append(special_numeral[5])
        else:
            list_cardinal_numeral.append(dict_cardinal_num[c])

    return " ".join(list_cardinal_numeral)

for i in range(455,459) :
    print(integer_to_vietnamese_numeral(i,'north', True))

for i in range(455,459) :
    print(integer_to_vietnamese_numeral(i,'south', True))
