
# 0 is no ticket | 1 is small ticket | 2 is big ticket
# speed <= 60 return 0 | 61 <= speed <= 80 return 1 | speed >= 81 return 2
# if birthday, speed > 5

def caught_speeding(speed, is_birthday):
    if is_birthday:
        speed = speed - 5
        if speed <= 60:
            return 0
        elif 61 <= speed <= 80:
            return 1
        elif speed >= 81:
            return 2
    else:
        if speed <= 60:
            return 0
        elif 61 <= speed <= 80:
            return 1
        elif speed >= 81:
            return 2