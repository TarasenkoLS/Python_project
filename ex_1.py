from sys import argv


def scr_wade():
    try:
        scr_wade, time, rate, bonus = argv
        print(f"Заработная плата сотрудника - {(float(time) * float(rate)) + float(bonus)}")
    except ValueError:
        print("Ошибка! Введены не корректные данные!")


# def scr_wade():
#   try:
#        time2, rate2, bonus2 = map(float, argv[1:])
#        print(f"Заработная плата сотрудника - {time2 * rate2 + bonus2}")
#    except ValueError:
#        print("Ошибка! Введены не корректные данные!")

scr_wade()
