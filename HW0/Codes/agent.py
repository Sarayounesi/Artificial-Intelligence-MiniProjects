from queue import PriorityQueue
import random


def ai_action(Pos):  # return opacity
    ''' Generate and play move from tic tac toe AI'''
    # اببتدا برای حالت های موجود تکی بهینه و دوتایی برد کامپیوتر و دوتایی برد انسان و سه تایی برد انسان و سه تایی برد کامپیوتر حالت بندی می کنیم
    choiceSpace = firstStep(Pos)
    choiceSpace = secondAIWin(Pos, choiceSpace)
    choiceSpace = secondPersonWin(Pos, choiceSpace)
    choiceSpace = thirdAIWin(Pos, choiceSpace)
    choiceSpace = thirdPersonWin(Pos, choiceSpace)

    return choiceSpace
    pass
# بهینه حالت تکی


def firstStep(Pos):
    choiceSpace = 0
    FirstPIC = [12]
    SEcondPIC = [6, 7, 8, 11, 13, 16, 17, 18]
    ThirdPIC = [1, 3, 5, 9, 15, 19, 21, 23]
    ForthPIC = [2, 10, 14, 22]
    FithPIC = [0, 4, 20, 24]
    PICchoicUswe = [FirstPIC, SEcondPIC, ThirdPIC, ForthPIC, FithPIC]

    select_1 = False
    for PX_FirstCome in PICchoicUswe:
        for i in PX_FirstCome:
            if Pos[i] is None:
                choiceSpace = i
                select_1 = True
                break
        if select_1:
            break

    return choiceSpace


def thirdAIWin(Pos, opacity):
    choiceSpace = opacity
    Loc = [

        (10, 11, 12, 13), (11, 12, 13, 14), (2, 7, 12, 17), (7, 12, 17, 22),(8, 12, 16, 20), (6, 12, 18, 24), (0, 6, 12, 18),(4, 8, 12, 16), (6, 7, 8, 9), (15, 16, 17, 18),
        (16, 17, 18, 19), (1, 6, 11, 16), (6, 11, 16, 21),(3, 8, 13, 18), (8, 13, 18, 23), (5, 6, 7, 8),
        (1, 7, 13, 19), (5, 11, 17, 23), (9, 13, 17, 21),(3, 7, 11, 15), (0, 1, 2, 3), (1, 2, 3, 4),
        (20, 21, 22, 23), (21, 22, 23, 24), (0, 5, 10, 15),(5, 10, 15, 20), (4, 9, 14, 19), (9, 14, 19, 24),

    ]

    for assign in Loc:
        Set_1 = [assign[0], assign[1], assign[2], assign[3]]
        FirstPlace, SecondPlace, ThirdPlace, FourthPlace = Set_1

        Satsfyloc = (Pos[FirstPlace], Pos[SecondPlace],
                     Pos[ThirdPlace], Pos[FourthPlace])
        if (Satsfyloc == (None, False, False, False)) or Satsfyloc == (False, None, False, False) or Satsfyloc == (False, False, None, False) or Satsfyloc == (False, False, False, None):
            if Pos[FirstPlace] != False:
                choiceSpace = FirstPlace
            elif Pos[SecondPlace] != False:
                choiceSpace = SecondPlace
            elif Pos[ThirdPlace] != False:
                choiceSpace = ThirdPlace
            elif Pos[FourthPlace] != False:
                choiceSpace = FourthPlace
            break

    return choiceSpace


def thirdPersonWin(Pos, opacity):
    choiceSpace = opacity

    Loc = [

        (10, 11, 12, 13), (11, 12, 13, 14), (2, 7, 12, 17),(7, 12, 17, 22), (8, 12, 16, 20), (6, 12, 18, 24),
        (0, 6, 12, 18), (4, 8, 12, 16), (6, 7, 8, 9),(15, 16, 17, 18), (16, 17, 18, 19), (1, 6, 11, 16),(6, 11, 16, 21), (3, 8, 13, 18), (8, 13, 18, 23),
        (5, 6, 7, 8), (1, 7, 13, 19), (5, 11, 17, 23),(9, 13, 17, 21), (3, 7, 11, 15), (0, 1, 2, 3),
        (1, 2, 3, 4), (20, 21, 22, 23), (21, 22, 23, 24),(0, 5, 10, 15), (5, 10, 15, 20), (4, 9, 14, 19), (9, 14, 19, 24),

    ]

    for assign in Loc:
        Set_1 = [assign[0], assign[1], assign[2], assign[3]]
        FirstPlace, SecondPlace, ThirdPlace, FourthPlace = Set_1

        Satsfyloc = (Pos[FirstPlace], Pos[SecondPlace],
                     Pos[ThirdPlace], Pos[FourthPlace])
        if (Satsfyloc == (None, True, True, True)) or Satsfyloc == (True, None, True, True) or Satsfyloc == (True, True, None, True) or Satsfyloc == (True, True, True, None):
            if Pos[FirstPlace] != True:
                choiceSpace = FirstPlace
            elif Pos[SecondPlace] != True:
                choiceSpace = SecondPlace
            elif Pos[ThirdPlace] != True:
                choiceSpace = ThirdPlace
            elif Pos[FourthPlace] != True:
                choiceSpace = FourthPlace
            break

    return choiceSpace


def secondAIWin(Pos, opacity):
    choiceSpace = opacity
    Loc = [

        (10, 11, 12, 13),(11, 12, 13, 14), (2, 7, 12, 17), (7, 12, 17, 22),(8, 12, 16, 20), (6, 12, 18, 24), (0, 6, 12, 18),
        (4, 8, 12, 16), (6, 7, 8, 9), (15, 16, 17, 18),(16, 17, 18, 19), (1, 6, 11, 16), (6, 11, 16, 21),
        (3, 8, 13, 18), (8, 13, 18, 23), (5, 6, 7, 8),(1, 7, 13, 19), (5, 11, 17, 23), (9, 13, 17, 21),(3, 7, 11, 15), (0, 1, 2, 3), (1, 2, 3, 4),
        (20, 21, 22, 23), (21, 22, 23, 24), (0, 5, 10, 15),(5, 10, 15, 20), (4, 9, 14, 19), (9, 14, 19, 24),

    ]

    for assign in Loc:
        Set_1 = [assign[0], assign[1], assign[2], assign[3]]
        FirstPlace, SecondPlace, ThirdPlace, FourthPlace = Set_1

        Satsfyloc = (Pos[FirstPlace], Pos[SecondPlace],
                     Pos[ThirdPlace], Pos[FourthPlace])

        if (Satsfyloc == (None, None, False, False)) or Satsfyloc == (None, False, None, False) or Satsfyloc == (None, False, False, None) or Satsfyloc == (False, None, None, False) or Satsfyloc == (False, None, False, None) or Satsfyloc == (False, False, None, None):

            if Pos[SecondPlace] != False:
                choiceSpace = SecondPlace
            elif Pos[ThirdPlace] != False:
                choiceSpace = ThirdPlace
            elif Pos[FirstPlace] != False:
                choiceSpace = FirstPlace
            elif Pos[FourthPlace] != False:
                choiceSpace = FourthPlace
            break

    return choiceSpace


def secondPersonWin(Pos, opacity):
    choiceSpace = opacity
    Loc = [

        (10, 11, 12, 13),(11, 12, 13, 14), (2, 7, 12, 17), (7, 12, 17, 22),
        (8, 12, 16, 20), (6, 12, 18, 24), (0, 6, 12, 18),(4, 8, 12, 16), (6, 7, 8, 9), (15, 16, 17, 18),(16, 17, 18, 19), (1, 6, 11, 16), (6, 11, 16, 21),
        (3, 8, 13, 18), (8, 13, 18, 23), (5, 6, 7, 8),(1, 7, 13, 19), (5, 11, 17, 23), (9, 13, 17, 21),(3, 7, 11, 15), (0, 1, 2, 3), (1, 2, 3, 4),
        (20, 21, 22, 23), (21, 22, 23, 24), (0, 5, 10, 15),(5, 10, 15, 20), (4, 9, 14, 19), (9, 14, 19, 24),

    ]
    for assign in Loc:
        Set_1 = [assign[0], assign[1], assign[2], assign[3]]
        FirstPlace, SecondPlace, ThirdPlace, FourthPlace = Set_1
        Satsfyloc = (Pos[FirstPlace], Pos[SecondPlace],
                     Pos[ThirdPlace], Pos[FourthPlace])

        if (Satsfyloc == (None, None, True, True)) or Satsfyloc == (None, True, None, True) or Satsfyloc == (None, True, True, None) or Satsfyloc == (True, None, None, True) or Satsfyloc == (True, None, True, None) or Satsfyloc == (True, True, None, None):
            if Pos[SecondPlace] != True:
                choiceSpace = SecondPlace
            elif Pos[ThirdPlace] != True:
                choiceSpace = ThirdPlace
            elif Pos[FirstPlace] != True:
                choiceSpace = FirstPlace
            elif Pos[FourthPlace] != True:
                choiceSpace = FourthPlace

            break

    return choiceSpace
