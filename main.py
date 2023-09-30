from time import sleep
import utime


# ------------------ CONSTANTS --------------------------

letters = [
    'E', 'S', 'O', 'N', 'X', 'L', 'A', 'S', 'U', 'N', 'A', # 0-10
    'D', 'O', 'S', 'X', 'T', 'R', 'E', 'S', 'X', 'A', 'M', # 11-21
    'C', 'U', 'A', 'T', 'R', 'O', 'C', 'I', 'N', 'C', 'O', # 22-32
    'S', 'E', 'I', 'S', 'X', 'S', 'I', 'E', 'T', 'E', 'X', # 33-43
    'O', 'C', 'H', 'O', 'N', 'U', 'E', 'V', 'E', 'P', 'M', # 44-54
    'D', 'I', 'E', 'Z', 'O', 'N', 'C', 'E', '.', '.', '.', # 55-65
    'D', 'O', 'C', 'E', 'Y', 'M', 'E', 'N', 'O', 'S', '.', # 66-76
    'X', 'V', 'E', 'I', 'N', 'T', 'E', 'D', 'I', 'E', 'Z', # 77-87
    'V', 'E', 'I', 'N', 'T', 'I', 'C', 'I', 'N', 'C', 'O', # 88-98
    'M', 'E', 'D', 'I', 'A', 'C', 'U', 'A', 'R', 'T', 'O'] # 99-109

modes = ['letters', 'digital1', 'digital2', 'digital3', 'analogic']

mode = modes[4]

leds = []

# ------------------- LETTER CONSTANTS -------------------

extra_minute_letters = {
    0: [],
    1: [63],
    2: [63, 64],
    3: [63, 64, 65],
    4: [63, 64, 65, 76],
}

minute_letters = { # 70 = y // 71, 72, 73, 74, 75 = menos
    0: [],
    5: [70, 94, 95, 96, 97, 98],
    10: [70, 84, 85, 86, 87],
    15: [70, 104, 105, 106, 107, 108, 109],
    20: [70, 78, 79, 80, 81, 82, 83],
    25: [70, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98],
    30: [70, 99, 100, 101, 102, 103],
    35: [71, 72, 73, 74, 75, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98],
    40: [71, 72, 73, 74, 75, 78, 79, 80, 81, 82, 83],
    45: [71, 72, 73, 74, 75, 104, 105, 106, 107, 108, 109],
    50: [71, 72, 73, 74, 75, 84, 85, 86, 87],
    55: [71, 72, 73, 74, 75, 94, 95, 96, 97, 98],
}

hour_letters = {
    0: [1, 2, 3, 5, 6, 7, 66, 67, 68, 69],
    1: [0, 1, 5, 6, 8, 9, 10],
    2: [1, 2, 3, 5, 6, 7, 11, 12, 13],
    3: [1, 2, 3, 5, 6, 7, 15, 16, 17, 18],
    4: [1, 2, 3, 5, 6, 7, 22, 23, 24, 25, 26, 27],
    5: [1, 2, 3, 5, 6, 7, 28, 29, 30, 31, 32],
    6: [1, 2, 3, 5, 6, 7, 33, 34, 35, 36],
    7: [1, 2, 3, 5, 6, 7, 38, 39, 40, 41, 42],
    8: [1, 2, 3, 5, 6, 7, 44, 45, 46, 47],
    9: [1, 2, 3, 5, 6, 7, 48, 49, 50, 51, 52],
    10: [1, 2, 3, 5, 6, 7, 55, 56, 57, 58],
    11: [1, 2, 3, 5, 6, 7, 59, 60, 61, 62],
    12: [1, 2, 3, 5, 6, 7, 66, 67, 68, 69],
}

# ------------------- DIGITAL CONSTANTS ------------------

digital_letters = {
    0: [0, 1, 2, 11, 13, 22, 24, 33, 35, 44, 45, 46],
    1: [1, 12, 23, 34, 45],
    2: [0, 1, 2, 13, 22, 23, 24, 33, 44, 45, 46],
    3: [0, 1, 2, 13, 22, 23, 24, 35, 44, 45, 46],
    4: [0, 2, 11, 13, 22, 23, 24, 35, 46],
    5: [0, 1, 2, 11, 22, 23, 24, 35, 44, 45, 46],
    6: [0, 1, 2, 11, 22, 23, 24, 33, 35, 44, 45, 46],
    7: [0, 1, 2, 13, 24, 35, 46],
    8: [0, 1, 2, 11, 13, 22, 23, 24, 33, 35, 44, 45, 46],
    9: [0, 1, 2, 11, 13, 22, 23, 24, 35, 44, 45, 46],
}

# ------------------- ANALOGICAL CONSTANTS ---------------

analogic_hours = {
    0: [27, 38, 49],
    1: [29, 39, 49],
    2: [39, 40, 41, 42, 49],
    3: [49, 50, 51, 52],
    4: [49, 61, 62, 63],
    5: [49, 61, 73],
    6: [49, 60, 71],
    7: [49, 59, 69],
    8: [49, 57, 58, 59],
    9: [46, 47, 48, 49],
    10: [35, 36, 37, 49],
    11: [25, 37, 49],
}

analogic_minutes = {
    0: [5, 16, 27, 38, 49], 
    5: [8, 18, 29, 39, 49], 
    10: [31, 32, 39, 40, 41, 42, 49],
    15: [49, 50, 51, 52, 53, 54],
    20: [49, 61, 62, 63, 75, 76],
    25: [49, 61, 73, 84, 96],
    30: [49, 60, 71, 82, 93],
    35: [49, 59, 69, 80, 90],
    40: [49, 57, 58, 59, 66, 67],
    45: [44, 45, 46, 47, 48, 49],
    50: [22, 23, 35, 36, 37, 49],
    55: [2, 14, 25, 37, 49],
}

# ------------------- FUNCTIONS --------------------------

def move_digital_nums(nums: list, coords: tuple):
    x, y = coords
    moved = nums.copy()
    for i in range(0, len(nums)):
        moved[i] = nums[i] + x + 11*y
    return moved

def print_leds(leds: list):
    leds.sort()
    print("-------------")
    print('|', end='')
    for i in range(len(letters)):
        if i in leds:
            print(letters[i], end='')
        else:
            print(' ', end='')
        if i%11 == 10:
            print('|')
            print('|', end='')
    
    print("-----------|")

def get_time():
    current_time = utime.localtime()
    hour = current_time[3]
    minute = current_time[4]
    return hour, minute

# --------------------------------------------------------
while True:
    leds.clear()
    hour, minute = get_time()

    if mode == 'letters':
        if hour>=12: # PM
            hour = hour - 12
            leds.extend((53, 54))
        else: # AM
            leds.extend((20, 21))

        # Get minute after :X0 or :X5
        extra_minute = minute % 5
        leds.extend(extra_minute_letters.get(extra_minute)) if extra_minute > 0 else None

        # Add minute
        minute = minute - extra_minute
        leds.extend(minute_letters.get(minute))

        # Add hour
        hour = hour + 1 if minute > 30 else hour
        leds.extend(hour_letters.get(hour))


    elif mode == 'digital1':
        leds.extend(move_digital_nums(digital_letters.get(hour // 10), (1, 0)))
        leds.extend(move_digital_nums(digital_letters.get(hour % 10), (5, 0)))

        leds.extend(move_digital_nums(digital_letters.get(minute // 10), (2, 5)))
        leds.extend(move_digital_nums(digital_letters.get(minute % 10), (6, 5)))

    elif mode == 'digital2':
        leds.extend(move_digital_nums(digital_letters.get(hour // 10), (2, 0)))
        leds.extend(move_digital_nums(digital_letters.get(hour % 10), (6, 0)))

        leds.extend(move_digital_nums(digital_letters.get(minute // 10), (2, 5)))
        leds.extend(move_digital_nums(digital_letters.get(minute % 10), (6, 5)))

    elif mode == 'digital3':
        leds.extend(move_digital_nums(digital_letters.get(hour // 10), (0, 0)))
        leds.extend(move_digital_nums(digital_letters.get(hour % 10), (5, 0)))

        leds.extend(move_digital_nums(digital_letters.get(minute // 10), (5, 5)))
        leds.extend(move_digital_nums(digital_letters.get(minute % 10), (8, 5)))

    elif mode == 'analogic':
        hour = hour - 12 if hour >= 12 else hour
        
        leds.extend(analogic_hours.get(hour))
        leds.extend(analogic_minutes.get(minute - (minute % 5)))

    print_leds(leds)
    
    sleep(10)
