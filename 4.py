#функция хода
def hod(a, b):
        x1 = dict1.get(a[1])
        y1 = dict1.get(a[0])
        x2 = dict1.get(b[1])
        y2 = dict1.get(b[0])
        if deck[x2][y2]!='.':
                deck[x2][y2]='.'
        deck[x1][y1], deck[x2][y2] = deck[x2][y2], deck[x1][y1]
        for i in range(12):
                for j in range(12):
                        print(deck[i][j].ljust(3), end='')
                print()
        list2 = []
        for i in range(2, 11):
                for j in range(2, 11):
                        list2.append(deck[i][j])
        list_hod.append(list2)

# функция хода назад
def back_hod(c, list_hod):
        c = c+1
        list1 = list_hod[-c]
        a = 0
        for i in range(2, 11):
                for j in range(2, 11):
                                deck[i][j]=list1[a]
                                a+=1
        list_hod[:-c+1]
        print(list_hod)
        for d in deck:
            print(*d)

#функция подсказки хода
def hod_help(a):
        x1 = dict1.get(a[1])
        y1 = dict1.get(a[0])
        if deck[x1][y1]=='P':
                if x1==8:
                        for i in range(1, 3):
                                if deck[x1-i][y1]=='.' and 2<=x1-i<=9:
                                        deck[x1-i][y1]='*'
                                elif deck[x1-i][y1] in figuresl:
                                        deck[x1 - i][y1]='*'+deck[x1-i][y1]
                                        break
                                else:
                                        break
                elif deck[x1-1][y1]=='.' and 2<=x1-1<=9:
                                deck[x1-1][y1]='*'
                else:
                       if deck[x1 - 1][y1-1] in figuresl and deck[x1][y1] in figuresh:
                               deck[x1-1][y1-1]='*'+deck[x1-1][y1-1]
                       elif deck[x1 - 1][y1 + 1] in figuresl and deck[x1][y1] in figuresh:
                               deck[x1 - 1][y1 + 1] = '*' + deck[x1 - 1][y1 + 1]
                       if deck[x1 - 1][y1-1] in figuresh and deck[x1][y1] in figuresl:
                               deck[x1-1][y1-1]='*'+deck[x1-1][y1-1]
                       elif deck[x1 - 1][y1 + 1] in figuresh and deck[x1][y1] in figuresl:
                               deck[x1 - 1][y1 + 1] = '*' + deck[x1 - 1][y1 + 1]
        if deck[x1][y1]=='p':
                if x1 == 3:
                        for i in range(1, 3):
                                if deck[x1 + i][y1] == '.' and 2 <= x1 + i <= 9:
                                        deck[x1 + i][y1] = '*'
                                elif deck[x1-i][y1] in figuresh:
                                        deck[x1 - i][y1]='*'+deck[x1-i][y1]
                                        break
                                else:
                                        break
                elif deck[x1 + 1][y1] == '.' and 2 <= x1 + 1 <= 9:
                                deck[x1 + 1][y1] = '*'
                else:
                       if deck[x1 + 1][y1-1] in figuresl and deck[x1][y1] in figuresh:
                               deck[x1+1][y1-1]='*'+deck[x1+1][y1-1]
                       elif deck[x1 + 1][y1 + 1] in figuresl and deck[x1][y1] in figuresh:
                               deck[x1 - 1][y1 + 1] = '*' + deck[x1 + 1][y1 + 1]
                       if deck[x1 + 1][y1-1] in figuresh and deck[x1][y1] in figuresl:
                               deck[x1-1][y1-1]='*'+deck[x1+1][y1-1]
                       elif deck[x1 + 1][y1 + 1] in figuresh and deck[x1][y1] in figuresl:
                               deck[x1 + 1][y1 + 1] = '*' + deck[x1 + 1][y1 + 1]
        if deck[x1][y1]=='R' or deck[x1][y1]=='r':
                for i in range(1, 9):
                        try:
                                if deck[x1+i][y1]=='.' and 2<=x1+i<=9:
                                        deck[x1+i][y1]='*'
                                elif deck[x1][y1] in figuresl:
                                        if deck[x1 + i][y1] in figuresh and 2 <= x1 + i <= 9:
                                                deck[x1+i][y1]='*'+deck[x1+i][y1]
                                                break
                                elif deck[x1][y1] in figuresh:
                                        if deck[x1 + i][y1] in figuresl and 2 <= x1 + i <= 9:
                                                deck[x1 + i][y1] = '*' + deck[x1 + i][y1]
                                                break
                                else:
                                        break
                        except IndexError:
                                pass
                for i in range(1, 9):
                        try:
                                if deck[x1][y1+i]=='.' and 2<=y1+i<=9:
                                        deck[x1][y1+i]='*'
                                elif deck[x1][y1] in figuresl:
                                        if deck[x1][y1+i] in figuresh and 2 <= y1 + i <= 9:
                                                deck[x1+i][y1]='*'+deck[x1+i][y1]
                                                break
                                elif deck[x1][y1] in figuresh:
                                        if deck[x1][y1+i] in figuresl and 2 <= y1 + i <= 9:
                                                deck[x1][y1+i] = '*' + deck[x1][y1+i]
                                                break
                                else:
                                        break
                        except IndexError:
                                pass
                for i in range(1, 9):
                        try:
                                if deck[x1-i][y1]=='.' and 2<=x1-i<=9:
                                        deck[x1-i][y1]='*'
                                elif deck[x1][y1] in figuresl:
                                        if deck[x1 - i][y1] in figuresh and 2 <= x1 - i <= 9:
                                                deck[x1+i][y1]='*'+deck[x1+i][y1]
                                                break
                                elif deck[x1][y1] in figuresh:
                                        if deck[x1 - i][y1] in figuresl and 2 <= x1 - i <= 9:
                                                deck[x1 - i][y1] = '*' + deck[x1 - i][y1]
                                                break
                                else:
                                        break
                        except IndexError:
                                pass
                for i in range(1, 9):
                        try:
                                if deck[x1][y1-i]=='.' and 2<=y1-i<=9:
                                        deck[x1][y1-i]='*'
                                elif deck[x1][y1] in figuresl:
                                        if deck[x1][y1-i] in figuresh and 2 <= y1 - i <= 9:
                                                deck[x1][y1-i]='*'+deck[x1][y1-i]
                                                break
                                elif deck[x1][y1] in figuresh:
                                        if deck[x1][y1-i] in figuresl and 2 <= y1 - i <= 9:
                                                deck[x1][y1-i] = '*' + deck[x1][y1-i]
                                                break
                                else:
                                        break
                        except IndexError:
                                pass
        if deck[x1][y1]=='N' or deck[x1][y1]=='n':
                if 2<=x1-2<=9 and 2<=y1-1<=9 and deck[x1-2][y1-1]=='.':
                        deck[x1-2][y1-1]='*'
                elif 2<=x1-2<=9 and 2<=y1-1<=9 and deck[x1-2][y1-1] in figuresl:
                        if deck[x1][y1] in figuresh:
                                deck[x1-2][y1-1]='*'+deck[x1-2][y1-1]
                elif 2<=x1-2<=9 and 2<=y1-1<=9 and deck[x1-2][y1-1] in figuresh:
                        if deck[x1][y1] in figuresl:
                                deck[x1-2][y1-1]='*'+deck[x1-2][y1-1]
                if 2<=x1-2<=7 and 0<=y1+1<=9 and deck[x1-2][y1+1]=='.':
                        deck[x1-2][y1+1]='*'
                elif 2<=x1-2<=7 and 0<=y1+1<=9 and deck[x1-2][y1+1] in figuresl:
                        if deck[x1][y1] in figuresh:
                                deck[x1-2][y1+1]='*'+deck[x1-2][y1+1]
                elif 2<=x1-2<=7 and 0<=y1+1<=9 and deck[x1-2][y1+1] in figuresh:
                        if deck[x1][y1] in figuresl:
                                deck[x1-2][y1+1]='*'+deck[x1-2][y1+1]
                if 2<=x1-1<=7 and 0<=y1+2<=9 and deck[x1-1][y1+2]=='.':
                        deck[x1-1][y1+2]='*'
                elif 2<=x1-1<=7 and 0<=y1+2<=9 and deck[x1-1][y1+2] in figuresl:
                        if deck[x1][y1] in figuresh:
                                deck[x1-1][y1+2]='*'+deck[x1-1][y1+2]
                elif 2<=x1-1<=7 and 0<=y1+2<=9 and deck[x1-1][y1+2] in figuresh:
                        if deck[x1][y1] in figuresl:
                                deck[x1-1][y1+2]='*'+deck[x1-1][y1+2]
                if 2<=x1-1<= 7 and 0<=y1-2<=9 and deck[x1-1][y1-2]=='.':
                        deck[x1-1][y1-2]='*'
                elif 2<=x1-1<= 7 and 0<=y1-2<=9 and deck[x1-1][y1-2] in figuresl:
                        if deck[x1][y1] in figuresh:
                                deck[x1 - 1][y1 - 2]='*'+ deck[x1-1][y1-2]
                elif 2<=x1-1<= 7 and 0<=y1-2<=9 and deck[x1-1][y1-2] in figuresh:
                        if deck[x1][y1] in figuresl:
                                deck[x1 - 1][y1 - 2]='*'+ deck[x1-1][y1-2]
                if 2<=x1+2<=7 and 0<=y1+1<=9 and deck[x1+2][y1+1]=='.':
                        deck[x1+2][y1+1]='*'
                elif 2<=x1+2<=7 and 0<=y1+1<=9 and deck[x1+2][y1+1] in figuresl:
                        if deck[x1][y1] in figuresh:
                                deck[x1+2][y1+1]='*'+deck[x1+2][y1+1]
                elif 2<=x1+2<=7 and 0<=y1+1<=9 and deck[x1+2][y1+1] in figuresh:
                        if deck[x1][y1] in figuresl:
                                deck[x1+2][y1+1]='*'+deck[x1+2][y1+1]
                if 2<=x1+2<=7 and 0<=y1-1<=9 and deck[x1+2][y1-1]=='.':
                        deck[x1+2][y1-1]= '*'
                elif 2<=x1+2<=7 and 0<=y1-1<=9 and deck[x1+2][y1-1] in figuresl:
                        if deck[x1][y1] in figuresh:
                                deck[x1-2][y1-1]='*'+deck[x1-2][y1-1]
                elif 2<=x1+2<=7 and 0<=y1-1<=9 and deck[x1+2][y1-1] in figuresh:
                        if deck[x1][y1] in figuresl:
                                deck[x1 - 2][y1 - 1]='*'+deck[x1-2][y1-1]
                if 2<=x1+1<=7 and 0<=y1+2<=9 and deck[x1+1][y1+2]=='.':
                        deck[x1+1][y1+2]='*'
                elif 2<=x1+1<=7 and 0<=y1+2<=9 and deck[x1+1][y1+2] in figuresl:
                        if deck[x1][y1] in figuresh:
                                deck[x1 + 1][y1 + 2]='*'+deck[x1+1][y1+2]
                elif 2<=x1+1<=7 and 0<=y1+2<=9 and deck[x1+1][y1+2] in figuresh:
                        if deck[x1][y1] in figuresl:
                                deck[x1+1][y1+2]='*'+deck[x1+1][y1+2]
                if 2<=x1+1<=7 and 0<=y1-2<=9 and deck[x1+1][y1-2]=='.':
                        deck[x1+1][y1-2]='*'
                elif 2<=x1+1<=7 and 0<=y1-2<=9 and deck[x1+1][y1-2] in figuresl:
                        if deck[x1][y1] in figuresh:
                                deck[x1+1][y1-2]='*'+deck[x1+1][y1-2]
                elif 2<=x1+1<=7 and 0<=y1-2<=9 and deck[x1+1][y1-2] in figuresh:
                        if deck[x1][y1] in figuresl:
                                deck[x1+1][y1-2]='*'+deck[x1+1][y1-2]
        if deck[x1][y1]=='B' or deck[x1][y1]=='b':
                for i in range(1, 9):
                        if deck[x1+i][y1+i]=='.' and 2<=x1+i<=9 and 2<=y1+i<=9:
                                deck[x1+i][y1+i]='*'
                        elif deck[x1+i][y1+i] in figuresl and 2<=x1+i<=9 and 2<=y1+i<=9:
                                if deck[x1][y1] in figuresh:
                                        deck[x1+i][y1+i]='*'+deck[x1+i][y1+i]
                                        break
                        elif deck[x1+i][y1+i] in figuresh and 2<=x1+i<=9 and 2<=y1+i<=9:
                                if deck[x1][y1] in figuresl:
                                        deck[x1+i][y1+i]='*'+deck[x1+i][y1+i]
                                        break
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1-i][y1+i]=='.' and 2<=x1-i<=9 and 2<=y1+i<=9:
                                deck[x1-i][y1+i]='*'
                        elif deck[x1-i][y1+i] in figuresh and 2<=x1-i<=9 and 2<=y1+i<=9:
                                if deck[x1][y1] in figuresl:
                                        deck[x1 - i][y1 + i]='*'+deck[x1-i][y1+i]
                                        break
                        elif deck[x1-i][y1+i] in figuresl and 2<=x1-i<=9 and 2<=y1+i<=9:
                                if deck[x1][y1] in figuresh:
                                        deck[x1 - i][y1 + i]='*'+deck[x1-i][y1+i]
                                        break
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1+i][y1-i]=='.' and 2<=x1+i <= 9 and 2<=y1-i<=9:
                                deck[x1+i][y1-i]='*'
                        elif deck[x1+i][y1-i] in figuresl and 2<=x1+i <= 9 and 2<=y1-i<=9:
                                if deck[x1][y1] in figuresh:
                                        deck[x1+i][y1-i]='*'+ deck[x1+i][y1-i]
                                        break
                        elif deck[x1+i][y1-i] in figuresh and 2<=x1+i<= 9 and 2<=y1-i<=9:
                                if deck[x1][y1] in figuresl:
                                        deck[x1+i][y1-i]='*'+ deck[x1+i][y1-i]
                                        break
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1-i][y1-i]=='.' and 2<=x1-i<=9 and 2<=y1-i<=9:
                                deck[x1-i][y1-i]='*'
                        elif deck[x1-i][y1-i] in figuresl and 2<=x1-i<=9 and 2<=y1-i<=9:
                                if deck[x1][y1] in figuresh:
                                        deck[x1-i][y1-i]='*'+deck[x1-i][y1-i]
                                        break
                        elif deck[x1-i][y1-i] in figuresh and 2<=x1-i<=9 and 2<=y1-i<=9:
                                if deck[x1][y1] in figuresl:
                                        deck[x1-i][y1-i]='*'+deck[x1-i][y1-i]
                                        break
                        else:
                                break
        if deck[x1][y1]=='K' or deck[x1][y1]=='k':
                if deck[x1+1][y1+1]=='.' and 2<=x1+1<=9 and 2<=y1+1<=9:
                        deck[x1+1][y1+1]='*'
                elif deck[x1+1][y1+1] in figuresl and 2<=x1+1<=9 and 2<=y1+1<=9:
                        if deck[x1][y1] in figuresh:
                                deck[x1 + 1][y1 + 1]='*'+deck[x1+1][y1+1]
                elif deck[x1+1][y1+1] in figuresh and 2<=x1+1<=9 and 2<=y1+1<=9:
                        if deck[x1][y1] in figuresl:
                                deck[x1 + 1][y1 + 1]='*'+deck[x1+1][y1+1]
                if deck[x1-1][y1+1]=='.' and 2<=x1-1<=9 and 2<=y1+1<=9:
                        deck[x1-1][y1+1]='*'
                elif deck[x1-1][y1+1]=='.' and 2<=x1-1<=9 and 2<=y1+1<=9:
                        if deck[x1][y1] in figuresh:
                                deck[x1 - 1][y1 + 1]='*'+ deck[x1-1][y1+1]
                elif deck[x1-1][y1+1]=='.' and 2<=x1-1<=9 and 2<=y1+1<=9:
                        if deck[x1][y1] in figuresl:
                                deck[x1 - 1][y1 + 1]='*'+ deck[x1-1][y1+1]
                if deck[x1+1][y1-1]=='.' and 2<=x1+1<=9 and 2<=y1-1<=9:
                        deck[x1+1][y1-1]='*'
                elif deck[x1+1][y1-1]=='.' and 2<=x1+1<=9 and 2<=y1-1<=9:
                        if deck[x1][y1] in figuresh:
                               deck[x1+1][y1-1]='*'+deck[x1+1][y1-1]
                elif deck[x1+1][y1-1]=='.' and 2<=x1+1<=9 and 2<=y1-1<=9:
                        if deck[x1][y1] in figuresl:
                                deck[x1+1][y1-1]='*'+deck[x1+1][y1-1]
                if deck[x1-1][y1-1]=='.' and 2<=x1-1<=9 and 2<=y1-1<=9:
                        deck[x1-1][y1-1]='*'
                elif deck[x1-1][y1-1]=='.' and 2<=x1-1<=9 and 2<=y1-1<=9:
                        if deck[x1][y1] in figuresh:
                                deck[x1 - 1][y1 - 1]='*'+deck[x1-1][y1-1]
                elif deck[x1-1][y1-1]=='.' and 2<=x1-1<=9 and 2<=y1-1<=9:
                        if deck[x1][y1] in figuresl:
                                deck[x1-1][y1-1]='*'+deck[x1-1][y1-1]
                if deck[x1+1][y1]=='.' and 2<=x1+1<=9:
                        deck[x1+1][y1]='*'
                elif deck[x1+1][y1]=='.' and 2<=x1+1<=9:
                        if deck[x1][y1] in figuresh:
                                deck[x1 + 1][y1]='*'+deck[x1+1][y1]
                elif deck[x1+1][y1]=='.' and 2<=x1+1<=9:
                        if deck[x1][y1] in figuresl:
                                deck[x1 + 1][y1]='*'+ deck[x1+1][y1]
                if deck[x1-1][y1]=='.' and 2<=x1-1<=9:
                        deck[x1-1][y1]='*'
                elif deck[x1-1][y1]=='.' and 2<=x1-1<=9:
                        if deck[x1][y1] in figuresh:
                                deck[x1-1][y1]='*'+deck[x1-1][y1]
                elif deck[x1-1][y1]=='.' and 2<=x1-1<=9:
                        if deck[x1][y1] in figuresl:
                                deck[x1-1][y1]='*'+deck[x1-1][y1]
                if deck[x1][y1+1]=='.' and 2<=y1+1<=9:
                        deck[x1][y1+1]='*'
                elif deck[x1][y1+1]=='.' and 2<=y1+1<=9:
                        if deck[x1][y1] in figuresh:
                                deck[x1][y1+1]='*'+deck[x1][y1+1]
                elif deck[x1][y1+1]=='.' and 2<=y1+1<=9:
                        if deck[x1][y1] in figuresl:
                                deck[x1][y1+1]='*'+deck[x1][y1+1]
                if deck[x1][y1-1]=='.' and 2<=y1-1<=9:
                        deck[x1][y1-1]='*'
                elif deck[x1][y1-1]=='.' and 2<=y1-1<=9:
                        if deck[x1][y1] in figuresh:
                                deck[x1][y1-1]='*'+deck[x1][y1-1]
                elif deck[x1][y1-1]=='.' and 2<=y1-1<=9:
                        if deck[x1][y1] in figuresl:
                                deck[x1][y1-1]='*'+deck[x1][y1-1]
        if deck[x1][y1]=='Q' or deck[x1][y1]=='q':
                for i in range(1, 9):
                        if deck[x1+i][y1+i]=='.' and 2<=x1+i<=9 and 2<=y1+i<=9:
                                deck[x1+i][y1+i]='*'
                        elif deck[x1+i][y1+i] in figuresl:
                                if deck[x1][y1] in figuresh:
                                        deck[x1+i][y1+i]= '*' +deck[x1+i][y1+i]
                                        break
                        elif deck[x1+i][y1+i] in figuresh and 2<=x1+i<=9 and 2<=y1+i<=9:
                                if deck[x1][y1] in figuresl:
                                        deck[x1+i][y1+i]= '*' +deck[x1+i][y1+i]
                                        break
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1+i][y1-i]=='.' and 2<=x1+i<=9 and 2<=y1-i<=9:
                                deck[x1+i][y1-i]='*'
                        elif deck[x1+i][y1-i] in figuresl:
                                if deck[x1][y1] in figuresh:
                                        deck[x1+i][y1-i]= '*' +deck[x1+i][y1-i]
                                        break
                        elif deck[x1+i][y1-i] in figuresh:
                                if deck[x1][y1] in figuresl:
                                        deck[x1+i][y1-i]= '*' +deck[x1+i][y1-i]
                                        break
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1-i][y1+i]=='.' and 2<=x1-i<=9 and 2<=y1+i<=9:
                                deck[x1-i][y1+i]='*'
                        elif deck[x1-i][y1+i] in figuresl:
                                if deck[x1][y1] in figuresh:
                                        deck[x1-i][y1+i]= '*' +deck[x1-i][y1+i]
                                        break
                        elif deck[x1-i][y1+i] in figuresh:
                                if deck[x1][y1] in figuresl:
                                        deck[x1-i][y1+i]= '*' +deck[x1-i][y1+i]
                                        break
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1-i][y1-i]=='.' and 2<=x1-i<=9 and 2<=y1-i<=9:
                                deck[x1-i][y1-i]='*'
                        elif deck[x1-i][y1-i] in figuresl:
                                if deck[x1][y1] in figuresh:
                                        deck[x1-i][y1-i]= '*' +deck[x1-i][y1-i]
                                        break
                        elif deck[x1-i][y1-i] in figuresh:
                                if deck[x1][y1] in figuresl:
                                        deck[x1-i][y1-i]= '*' +deck[x1-i][y1-i]
                                        break
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1+i][y1]=='.' and 2<=x1+i<=9:
                                deck[x1+i][y1]='*'
                        elif deck[x1+i][y1] in figuresl:
                                if deck[x1][y1] in figuresh:
                                        deck[x1+i][y1]= '*' +deck[x1+i][y1]
                                        break
                        elif deck[x1+i][y1] in figuresh:
                                if deck[x1][y1] in figuresl:
                                        deck[x1+i][y1]= '*' +deck[x1+i][y1]
                                        break
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1-i][y1]=='.' and 2<=x1-i<=9:
                                deck[x1-i][y1]='*'
                        elif deck[x1-i][y1] in figuresl:
                                if deck[x1][y1] in figuresh:
                                        deck[x1-i][y1]= '*' +deck[x1-i][y1]
                                        break
                        elif deck[x1-i][y1] in figuresh:
                                if deck[x1][y1] in figuresl:
                                        deck[x1-i][y1]= '*' +deck[x1-i][y1]
                                        break
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1][y1-i]=='.' and 2<=y1-i<=9:
                                deck[x1][y1-i]='*'
                        elif deck[x1][y1-i] in figuresl:
                                if deck[x1][y1] in figuresh:
                                        deck[x1][y1-i]= '*' +deck[x1][y1-i]
                                        break
                        elif deck[x1][y1-i] in figuresh:
                                if deck[x1][y1] in figuresl:
                                        deck[x1][y1-i]= '*' +deck[x1][y1-i]
                                        break
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1][y1+i]=='.' and 2<=y1+i<=9:
                                deck[x1][y1+i]='*'
                        elif deck[x1][y1+i] in figuresl:
                                if deck[x1][y1] in figuresh:
                                        deck[x1][y1+i]= '*' +deck[x1][y1+i]
                                        break
                        elif deck[x1][y1+i] in figuresh:
                                if deck[x1][y1] in figuresl:
                                        deck[x1][y1 + i]= '*' +deck[x1][y1+i]
                                        break
                        else:
                                break
        print('Возможные ходы')
        for i in range(12):
                for j in range(12):
                        print(deck[i][j].ljust(3), end='')
                print()
        for i in range(12):
                for j in range(12):
                        if deck[i][j]=='*' and len(deck[i][j])==1:
                                deck[i][j]='.'
                        elif '*' in deck[i][j] and len(deck[i][j])>1:
                                deck[i][j] = deck[i][j][1:]
#функция определения мата
def mat(flagh, flagl):
        for i in range(2,10):
                for j in range(2,10):
                    if '!' in deck[i][j]:
                        a = deck[i][j][1:]
                    else:
                        a = deck[i][j]
                    if a in figuresh:
                        x1 = i
                        y1 = j
                        if a == 'P':
                            if x1 == 8:
                                for i in range(1, 3):
                                    if deck[x1 - i][y1] == '.' and 2 <= x1 - i <= 9:
                                        deck[x1 - i][y1] = '*'
                                    elif deck[x1 - i][y1] in figuresl:
                                        deck[x1 - i][y1] = '*' + deck[x1 - i][y1]
                                        break
                                    else:
                                        break
                            elif deck[x1 - 1][y1] == '.' and 2 <= x1 - 1 <= 9:
                                deck[x1 - 1][y1] = '*'
                            else:
                                if deck[x1 - 1][y1 + 1] in figuresh and a in figuresh:
                                    deck[x1 - 1][y1 + 1] = '!' + deck[x1 - 1][y1 + 1]
                                if deck[x1 - 1][y1 - 1] in figuresh and a in figuresl:
                                    deck[x1 - 1][y1 - 1] = '*' + deck[x1 - 1][y1 - 1]
                                elif deck[x1 - 1][y1 + 1] in figuresh and a in figuresl:
                                    deck[x1 - 1][y1 + 1] = '*' + deck[x1 - 1][y1 + 1]
                        if a == 'R':
                            for i in range(1, 9):
                                try:
                                    if deck[x1 + i][y1] == '.' and 2 <= x1 + i <= 9:
                                        deck[x1 + i][y1] = '*'
                                    elif a in figuresh:
                                        if deck[x1 + i][y1] in figuresh and 2 <= x1 + i <= 9:
                                            deck[x1 + i][y1] = '!' + deck[x1 + i][y1]
                                            break
                                    elif a in figuresh:
                                        if deck[x1 + i][y1] in figuresl and 2 <= x1 + i <= 9:
                                            deck[x1 + i][y1] = '*' + deck[x1 + i][y1]
                                            break
                                    else:
                                        break
                                except IndexError:
                                    pass
                            for i in range(1, 9):
                                try:
                                    if deck[x1][y1 + i] == '.' and 2 <= y1 + i <= 9:
                                        deck[x1][y1 + i] = '*'
                                    elif a in figuresh:
                                        if deck[x1][y1 + i] in figuresh and 2 <= y1 + i <= 9:
                                            deck[x1 + i][y1] = '!' + deck[x1 + i][y1]
                                            break
                                    elif a in figuresh:
                                        if deck[x1][y1 + i] in figuresl and 2 <= y1 + i <= 9:
                                            deck[x1][y1 + i] = '*' + deck[x1][y1 + i]
                                            break
                                    else:
                                        break
                                except IndexError:
                                    pass
                            for i in range(1, 9):
                                try:
                                    if deck[x1 - i][y1] == '.' and 2 <= x1 - i <= 9:
                                        deck[x1 - i][y1] = '*'
                                    elif a in figuresh:
                                        if deck[x1 - i][y1] in figuresh and 2 <= x1 - i <= 9:
                                            deck[x1 + i][y1] = '!' + deck[x1 + i][y1]
                                            break
                                    elif a in figuresh:
                                        if deck[x1 - i][y1] in figuresl and 2 <= x1 - i <= 9:
                                            deck[x1 - i][y1] = '*' + deck[x1 - i][y1]
                                            break
                                    else:
                                        break
                                except IndexError:
                                    pass
                            for i in range(1, 9):
                                try:
                                    if deck[x1][y1 - i] == '.' and 2 <= y1 - i <= 9:
                                        deck[x1][y1 - i] = '*'
                                    elif a in figuresh:
                                        if deck[x1][y1 - i] in figuresh and 2 <= y1 - i <= 9:
                                            deck[x1][y1 - i] = '!' + deck[x1][y1 - i]
                                            break
                                    elif a in figuresh:
                                        if deck[x1][y1 - i] in figuresl and 2 <= y1 - i <= 9:
                                            deck[x1][y1 - i] = '*' + deck[x1][y1 - i]
                                            break
                                    else:
                                        break
                                except IndexError:
                                    pass
                        if a == 'N':
                            if 2 <= x1 - 2 <= 9 and 2 <= y1 - 1 <= 9 and deck[x1 - 2][y1 - 1] == '.':
                                deck[x1 - 2][y1 - 1] = '*'
                            elif 2 <= x1 - 2 <= 9 and 2 <= y1 - 1 <= 9 and deck[x1 - 2][y1 - 1] in figuresh:
                                if a in figuresh:
                                    deck[x1 - 2][y1 - 1] = '!' + deck[x1 - 2][y1 - 1]
                            elif 2 <= x1 - 2 <= 9 and 2 <= y1 - 1 <= 9 and deck[x1 - 2][y1 - 1] in figuresl:
                                if a in figuresh:
                                    deck[x1 - 2][y1 - 1] = '*' + deck[x1 - 2][y1 - 1]
                            if 2 <= x1 - 2 <= 7 and 0 <= y1 + 1 <= 9 and deck[x1 - 2][y1 + 1] == '.':
                                deck[x1 - 2][y1 + 1] = '*'
                            elif 2 <= x1 - 2 <= 7 and 0 <= y1 + 1 <= 9 and deck[x1 - 2][y1 + 1] in figuresh:
                                if a in figuresh:
                                    deck[x1 - 2][y1 + 1] = '!' + deck[x1 - 2][y1 + 1]
                            elif 2 <= x1 - 2 <= 7 and 0 <= y1 + 1 <= 9 and deck[x1 - 2][y1 + 1] in figuresl:
                                if a in figuresh:
                                    deck[x1 - 2][y1 + 1] = '*' + deck[x1 - 2][y1 + 1]
                            if 2 <= x1 - 1 <= 7 and 0 <= y1 + 2 <= 9 and deck[x1 - 1][y1 + 2] == '.':
                                deck[x1 - 1][y1 + 2] = '*'
                            elif 2 <= x1 - 1 <= 7 and 0 <= y1 + 2 <= 9 and deck[x1 - 1][y1 + 2] in figuresh:
                                if a in figuresh:
                                    deck[x1 - 1][y1 + 2] = '!' + deck[x1 - 1][y1 + 2]
                            elif 2 <= x1 - 1 <= 7 and 0 <= y1 + 2 <= 9 and deck[x1 - 1][y1 + 2] in figuresl:
                                if a in figuresh:
                                    deck[x1 - 1][y1 + 2] = '*' + deck[x1 - 1][y1 + 2]
                            if 2 <= x1 - 1 <= 7 and 0 <= y1 - 2 <= 9 and deck[x1 - 1][y1 - 2] == '.':
                                deck[x1 - 1][y1 - 2] = '*'
                            elif 2 <= x1 - 1 <= 7 and 0 <= y1 - 2 <= 9 and deck[x1 - 1][y1 - 2] in figuresh:
                                if a in figuresh:
                                    deck[x1 - 1][y1 - 2] = '!' + deck[x1 - 1][y1 - 2]
                            elif 2 <= x1 - 1 <= 7 and 0 <= y1 - 2 <= 9 and deck[x1 - 1][y1 - 2] in figuresl:
                                if a in figuresh:
                                    deck[x1 - 1][y1 - 2] = '*' + deck[x1 - 1][y1 - 2]
                            if 2 <= x1 + 2 <= 7 and 0 <= y1 + 1 <= 9 and deck[x1 + 2][y1 + 1] == '.':
                                deck[x1 + 2][y1 + 1] = '*'
                            elif 2 <= x1 + 2 <= 7 and 0 <= y1 + 1 <= 9 and deck[x1 + 2][y1 + 1] in figuresh:
                                if a in figuresh:
                                    deck[x1 + 2][y1 + 1] = '!' + deck[x1 + 2][y1 + 1]
                            elif 2 <= x1 + 2 <= 7 and 0 <= y1 + 1 <= 9 and deck[x1 + 2][y1 + 1] in figuresl:
                                if a in figuresh:
                                    deck[x1 + 2][y1 + 1] = '*' + deck[x1 + 2][y1 + 1]
                            if 2 <= x1 + 2 <= 7 and 0 <= y1 - 1 <= 9 and deck[x1 + 2][y1 - 1] == '.':
                                deck[x1 + 2][y1 - 1] = '*'
                            elif 2 <= x1 + 2 <= 7 and 0 <= y1 - 1 <= 9 and deck[x1 + 2][y1 - 1] in figuresh:
                                if a in figuresh:
                                    deck[x1 - 2][y1 - 1] = '!' + deck[x1 - 2][y1 - 1]
                            elif 2 <= x1 + 2 <= 7 and 0 <= y1 - 1 <= 9 and deck[x1 + 2][y1 - 1] in figuresl:
                                if a in figuresh:
                                    deck[x1 - 2][y1 - 1] = '*' + deck[x1 - 2][y1 - 1]
                            if 2 <= x1 + 1 <= 7 and 0 <= y1 + 2 <= 9 and deck[x1 + 1][y1 + 2] == '.':
                                deck[x1 + 1][y1 + 2] = '*'
                            elif 2 <= x1 + 1 <= 7 and 0 <= y1 + 2 <= 9 and deck[x1 + 1][y1 + 2] in figuresh:
                                if a in figuresh:
                                    deck[x1 + 1][y1 + 2] = '!' + deck[x1 + 1][y1 + 2]
                            elif 2 <= x1 + 1 <= 7 and 0 <= y1 + 2 <= 9 and deck[x1 + 1][y1 + 2] in figuresl:
                                if a in figuresh:
                                    deck[x1 + 1][y1 + 2] = '*' + deck[x1 + 1][y1 + 2]
                            if 2 <= x1 + 1 <= 7 and 0 <= y1 - 2 <= 9 and deck[x1 + 1][y1 - 2] == '.':
                                deck[x1 + 1][y1 - 2] = '*'
                            elif 2 <= x1 + 1 <= 7 and 0 <= y1 - 2 <= 9 and deck[x1 + 1][y1 - 2] in figuresh:
                                if a in figuresh:
                                    deck[x1 + 1][y1 - 2] = '!' + deck[x1 + 1][y1 - 2]
                            elif 2 <= x1 + 1 <= 7 and 0 <= y1 - 2 <= 9 and deck[x1 + 1][y1 - 2] in figuresl:
                                if a in figuresh:
                                    deck[x1 + 1][y1 - 2] = '*' + deck[x1 + 1][y1 - 2]

                        if a == 'B':
                            for i in range(1, 9):
                                if deck[x1 + i][y1 + i] == '.' and 2 <= x1 + i <= 9 and 2 <= y1 + i <= 9:
                                    deck[x1 + i][y1 + i] = '*'
                                elif deck[x1 + i][y1 + i] in figuresh and 2 <= x1 + i <= 9 and 2<=y1+i<= 9:
                                    if a in figuresh:
                                        deck[x1 + i][y1 + i] = '!' + deck[x1 + i][y1 + i]
                                        break
                                elif deck[x1 + i][y1 + i] in figuresl and 2 <= x1 + i <= 9 and 2 <= y1 + i <= 9:
                                    if a in figuresh:
                                        deck[x1 + i][y1 + i] = '*' + deck[x1 + i][y1 + i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 - i][y1 + i] == '.' and 2 <= x1 - i <= 9 and 2 <= y1 + i <= 9:
                                    deck[x1 - i][y1 + i] = '*'
                                elif deck[x1 - i][y1 + i] in figuresh and 2 <= x1 - i <= 9 and 2 <= y1 + i <= 9:
                                    if a in figuresh:
                                        deck[x1 - i][y1 + i] = '!' + deck[x1 - i][y1 + i]
                                        break
                                elif deck[x1 - i][y1 + i] in figuresl and 2 <= x1 - i <= 9 and 2 <= y1 + i <= 9:
                                    if a in figuresh:
                                        deck[x1 - i][y1 + i] = '*' + deck[x1 - i][y1 + i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 + i][y1 - i] == '.' and 2 <= x1 + i <= 9 and 2 <= y1 - i <= 9:
                                    deck[x1 + i][y1 - i] = '*'
                                elif deck[x1 + i][y1 - i] in figuresh and 2 <= x1 + i <= 9 and 2 <= y1 - i <= 9:
                                    if a in figuresh:
                                        deck[x1 + i][y1 - i] = '!' + deck[x1 + i][y1 - i]
                                        break
                                elif deck[x1 + i][y1 - i] in figuresl and 2 <= x1 + i <= 9 and 2 <= y1 - i <= 9:
                                    if a in figuresh:
                                        deck[x1 + i][y1 - i] = '*' + deck[x1 + i][y1 - i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 - i][y1 - i] == '.' and 2 <= x1 - i <= 9 and 2 <= y1 - i <= 9:
                                    deck[x1 - i][y1 - i] = '*'
                                elif deck[x1 - i][y1 - i] in figuresh and 2 <= x1 - i <= 9 and 2 <= y1 - i <= 9:
                                    if a in figuresh:
                                        deck[x1 - i][y1 - i] = '!' + deck[x1 - i][y1 - i]
                                        break
                                elif deck[x1 - i][y1 - i] in figuresl and 2 <= x1 - i <= 9 and 2 <= y1 - i <= 9:
                                    if a in figuresh:
                                        deck[x1 - i][y1 - i] = '*' + deck[x1 - i][y1 - i]
                                        break
                                else:
                                    break
                        if deck[x1][y1] == 'Q' or deck[x1][y1] == 'q':
                            for i in range(1, 9):
                                if deck[x1 + i][y1 + i] == '.' and 2 <= x1 + i <= 9 and 2 <= y1 + i <= 9:
                                    deck[x1 + i][y1 + i] = '*'
                                elif deck[x1 + i][y1 + i] in figuresh:
                                    if a in figuresh:
                                        deck[x1 + i][y1 + i] = '!' + deck[x1 + i][y1 + i]
                                        break
                                elif deck[x1 + i][y1 + i] in figuresl and 2 <= x1 + i <= 9 and 2 <= y1 + i <= 9:
                                    if a in figuresh:
                                        deck[x1 + i][y1 + i] = '*' + deck[x1 + i][y1 + i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 + i][y1 - i] == '.' and 2 <= x1 + i <= 9 and 2 <= y1 - i <= 9:
                                    deck[x1 + i][y1 - i] = '*'
                                elif deck[x1 + i][y1 - i] in figuresh:
                                    if a in figuresh:
                                        deck[x1 + i][y1 - i] = '!' + deck[x1 + i][y1 - i]
                                        break
                                elif deck[x1 + i][y1 - i] in figuresl:
                                    if a in figuresh:
                                        deck[x1 + i][y1 - i] = '*' + deck[x1 + i][y1 - i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 - i][y1 + i] == '.' and 2 <= x1 - i <= 9 and 2 <= y1 + i <= 9:
                                    deck[x1 - i][y1 + i] = '*'
                                elif deck[x1 - i][y1 + i] in figuresh:
                                    if a in figuresh:
                                        deck[x1 - i][y1 + i] = '!' + deck[x1 - i][y1 + i]
                                        break
                                elif deck[x1 - i][y1 + i] in figuresl:
                                    if a in figuresh:
                                        deck[x1 - i][y1 + i] = '*' + deck[x1 - i][y1 + i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 - i][y1 - i] == '.' and 2 <= x1 - i <= 9 and 2 <= y1 - i <= 9:
                                    deck[x1 - i][y1 - i] = '*'
                                elif deck[x1 - i][y1 - i] in figuresh:
                                    if a in figuresh:
                                        deck[x1 - i][y1 - i] = '!' + deck[x1 - i][y1 - i]
                                        break
                                elif deck[x1 - i][y1 - i] in figuresl:
                                    if a in figuresh:
                                        deck[x1 - i][y1 - i] = '*' + deck[x1 - i][y1 - i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 + i][y1] == '.' and 2 <= x1 + i <= 9:
                                    deck[x1 + i][y1] = '*'
                                elif deck[x1 + i][y1] in figuresh:
                                    if a in figuresh:
                                        deck[x1 + i][y1] = '!' + deck[x1 + i][y1]
                                        break
                                elif deck[x1 + i][y1] in figuresl:
                                    if a in figuresh:
                                        deck[x1 + i][y1] = '*' + deck[x1 + i][y1]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 - i][y1] == '.' and 2 <= x1 - i <= 9:
                                    deck[x1 - i][y1] = '*'
                                elif deck[x1 - i][y1] in figuresh:
                                    if a in figuresh:
                                        deck[x1 - i][y1] = '!' + deck[x1 - i][y1]
                                        break
                                elif deck[x1 - i][y1] in figuresl:
                                    if a in figuresh:
                                        deck[x1 - i][y1] = '*' + deck[x1 - i][y1]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1][y1 - i] == '.' and 2 <= y1 - i <= 9:
                                    deck[x1][y1 - i] = '*'
                                elif deck[x1][y1 - i] in figuresh:
                                    if a in figuresh:
                                        deck[x1][y1 - i] = '!' + deck[x1][y1 - i]
                                        break
                                elif deck[x1][y1 - i] in figuresl:
                                    if a in figuresh:
                                        deck[x1][y1 - i] = '*' + deck[x1][y1 - i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1][y1 + i] == '.' and 2 <= y1 + i <= 9:
                                    deck[x1][y1 + i] = '*'
                                elif deck[x1][y1 + i] in figuresh:
                                    if a in figuresh:
                                        deck[x1][y1 + i] = '!' + deck[x1][y1 + i]
                                        break
                                elif deck[x1][y1 + i] in figuresl:
                                    if a in figuresh:
                                        deck[x1][y1 + i] = '*' + deck[x1][y1 + i]
                                        break
                                else:
                                    break
        counth = 0
        for i in range(2, 10):
                for j in range(2, 10):
                        if 'k' in deck[i][j]:
                                if '*' in deck[i][j]:
                                        if deck[i + 1][j + 1] == '*':
                                                counth += 1
                                        elif deck[i + 1][j + 1] in figuresh:
                                                if '!' in deck[i + 1][j + 1]:
                                                        counth += 1
                                        elif deck[i + 1][j + 1] == ' ':
                                                counth += 1
                                        if deck[i + 1][j - 1] == '*':
                                                counth += 1
                                        elif deck[i + 1][j - 1] in figuresh:
                                                if '!' in deck[i + 1][j - 1]:
                                                        counth += 1
                                        elif deck[i + 1][j - 1] == ' ':
                                                counth += 1
                                        if deck[i - 1][j - 1] == '*':
                                                counth += 1
                                        elif deck[i - 1][j - 1] in figuresh:
                                                if '!' in deck[i - 1][j - 1]:
                                                        counth += 1
                                        elif deck[i - 1][j - 1] == ' ':
                                                counth += 1
                                        if deck[i - 1][j + 1] == '*':
                                                counth += 1
                                        elif deck[i - 1][j + 1] in figuresh:
                                                if '!' in deck[i - 1][j + 1]:
                                                        counth += 1
                                        elif deck[i - 1][j + 1] == ' ':
                                                counth += 1
                                        if deck[i + 1][j] == '*':
                                                counth += 1
                                        elif deck[i + 1][j] in figuresh:
                                                if '!' in deck[i + 1][j]:
                                                        counth += 1
                                        elif deck[i + 1][j] == ' ':
                                                counth += 1
                                        if deck[i - 1][j] == '*':
                                                counth += 1
                                        elif deck[i - 1][j] in figuresh:
                                                if '!' in deck[i - 1][j]:
                                                        counth += 1
                                        elif deck[i - 1][j] == ' ':
                                                counth += 1
                                        if deck[i][j + 1] == '*':
                                                counth += 1
                                        elif deck[i][j + 1] in figuresh:
                                                if '!' in deck[i][j + 1]:
                                                        counth += 1
                                        elif deck[i][j + 1] == ' ':
                                                counth += 1
                                        if deck[i][j - 1] == '*':
                                                counth += 1
                                        elif deck[i][j - 1] in figuresh:
                                                if '!' in deck[i][j - 1]:
                                                        counth += 1
                                        elif deck[i][j - 1] == ' ':
                                                counth += 1
        if counth == 8:
                flagh = True
        for i in range(2, 10):
                for j in range(2, 10):
                        if deck[i][j]=='*':
                                deck[i][j]=='.'
                        elif '*' in deck[i][j]:
                                deck[i][j]=deck[i][j][1:]
                        elif '!' in deck[i][j]:
                                deck[i][j]=deck[i][j][1:]
        for i in range(2,10):
                for j in range(2,10):
                    if '!' in deck[i][j]:
                        a = deck[i][j][1:]
                    else:
                        a = deck[i][j]
                    if a in figuresl:
                        x1 = i
                        y1 = j
                        if a == 'p':
                            if x1 == 8:
                                for i in range(1, 3):
                                    if deck[x1 - i][y1] == '.' and 2 <= x1 - i <= 9:
                                        deck[x1 - i][y1] = '*'
                                    elif deck[x1 - i][y1] in figuresh:
                                        deck[x1 - i][y1] = '*' + deck[x1 - i][y1]
                                        break
                                    else:
                                        break
                            elif deck[x1 - 1][y1] == '.' and 2 <= x1 - 1 <= 9:
                                deck[x1 - 1][y1] = '*'
                            else:
                                if deck[x1 - 1][y1 + 1] in figuresl and a in figuresl:
                                    deck[x1 - 1][y1 + 1] = '!' + deck[x1 - 1][y1 + 1]
                                if deck[x1 - 1][y1 - 1] in figuresl and a in figuresh:
                                    deck[x1 - 1][y1 - 1] = '*' + deck[x1 - 1][y1 - 1]
                                elif deck[x1 - 1][y1 + 1] in figuresl and a in figuresh:
                                    deck[x1 - 1][y1 + 1] = '*' + deck[x1 - 1][y1 + 1]
                        if a == 'r':
                            for i in range(1, 9):
                                try:
                                    if deck[x1 + i][y1] == '.' and 2 <= x1 + i <= 9:
                                        deck[x1 + i][y1] = '*'
                                    elif a in figuresl:
                                        if deck[x1 + i][y1] in figuresl and 2 <= x1 + i <= 9:
                                            deck[x1 + i][y1] = '!' + deck[x1 + i][y1]
                                            break
                                    elif a in figuresl:
                                        if deck[x1 + i][y1] in figuresh and 2 <= x1 + i <= 9:
                                            deck[x1 + i][y1] = '*' + deck[x1 + i][y1]
                                            break
                                    else:
                                        break
                                except IndexError:
                                    pass
                            for i in range(1, 9):
                                try:
                                    if deck[x1][y1 + i] == '.' and 2 <= y1 + i <= 9:
                                        deck[x1][y1 + i] = '*'
                                    elif a in figuresl:
                                        if deck[x1][y1 + i] in figuresl and 2 <= y1 + i <= 9:
                                            deck[x1 + i][y1] = '!' + deck[x1 + i][y1]
                                            break
                                    elif a in figuresl:
                                        if deck[x1][y1 + i] in figuresh and 2 <= y1 + i <= 9:
                                            deck[x1][y1 + i] = '*' + deck[x1][y1 + i]
                                            break
                                    else:
                                        break
                                except IndexError:
                                    pass
                            for i in range(1, 9):
                                try:
                                    if deck[x1 - i][y1] == '.' and 2 <= x1 - i <= 9:
                                        deck[x1 - i][y1] = '*'
                                    elif a in figuresl:
                                        if deck[x1 - i][y1] in figuresl and 2 <= x1 - i <= 9:
                                            deck[x1 + i][y1] = '!' + deck[x1 + i][y1]
                                            break
                                    elif a in figuresl:
                                        if deck[x1 - i][y1] in figuresh and 2 <= x1 - i <= 9:
                                            deck[x1 - i][y1] = '*' + deck[x1 - i][y1]
                                            break
                                    else:
                                        break
                                except IndexError:
                                    pass
                            for i in range(1, 9):
                                try:
                                    if deck[x1][y1 - i] == '.' and 2 <= y1 - i <= 9:
                                        deck[x1][y1 - i] = '*'
                                    elif a in figuresl:
                                        if deck[x1][y1 - i] in figuresl and 2 <= y1 - i <= 9:
                                            deck[x1][y1 - i] = '!' + deck[x1][y1 - i]
                                            break
                                    elif a in figuresl:
                                        if deck[x1][y1 - i] in figuresh and 2 <= y1 - i <= 9:
                                            deck[x1][y1 - i] = '*' + deck[x1][y1 - i]
                                            break
                                    else:
                                        break
                                except IndexError:
                                    pass
                        if a == 'N':
                            if 2 <= x1 - 2 <= 9 and 2 <= y1 - 1 <= 9 and deck[x1 - 2][y1 - 1] == '.':
                                deck[x1 - 2][y1 - 1] = '*'
                            elif 2 <= x1 - 2 <= 9 and 2 <= y1 - 1 <= 9 and deck[x1 - 2][y1 - 1] in figuresl:
                                if a in figuresl:
                                    deck[x1 - 2][y1 - 1] = '!' + deck[x1 - 2][y1 - 1]
                            elif 2 <= x1 - 2 <= 9 and 2 <= y1 - 1 <= 9 and deck[x1 - 2][y1 - 1] in figuresh:
                                if a in figuresl:
                                    deck[x1 - 2][y1 - 1] = '*' + deck[x1 - 2][y1 - 1]
                            if 2 <= x1 - 2 <= 7 and 0 <= y1 + 1 <= 9 and deck[x1 - 2][y1 + 1] == '.':
                                deck[x1 - 2][y1 + 1] = '*'
                            elif 2 <= x1 - 2 <= 7 and 0 <= y1 + 1 <= 9 and deck[x1 - 2][y1 + 1] in figuresl:
                                if a in figuresl:
                                    deck[x1 - 2][y1 + 1] = '!' + deck[x1 - 2][y1 + 1]
                            elif 2 <= x1 - 2 <= 7 and 0 <= y1 + 1 <= 9 and deck[x1 - 2][y1 + 1] in figuresh:
                                if a in figuresl:
                                    deck[x1 - 2][y1 + 1] = '*' + deck[x1 - 2][y1 + 1]
                            if 2 <= x1 - 1 <= 7 and 0 <= y1 + 2 <= 9 and deck[x1 - 1][y1 + 2] == '.':
                                deck[x1 - 1][y1 + 2] = '*'
                            elif 2 <= x1 - 1 <= 7 and 0 <= y1 + 2 <= 9 and deck[x1 - 1][y1 + 2] in figuresl:
                                if a in figuresl:
                                    deck[x1 - 1][y1 + 2] = '!' + deck[x1 - 1][y1 + 2]
                            elif 2 <= x1 - 1 <= 7 and 0 <= y1 + 2 <= 9 and deck[x1 - 1][y1 + 2] in figuresh:
                                if a in figuresl:
                                    deck[x1 - 1][y1 + 2] = '*' + deck[x1 - 1][y1 + 2]
                            if 2 <= x1 - 1 <= 7 and 0 <= y1 - 2 <= 9 and deck[x1 - 1][y1 - 2] == '.':
                                deck[x1 - 1][y1 - 2] = '*'
                            elif 2 <= x1 - 1 <= 7 and 0 <= y1 - 2 <= 9 and deck[x1 - 1][y1 - 2] in figuresl:
                                if a in figuresl:
                                    deck[x1 - 1][y1 - 2] = '!' + deck[x1 - 1][y1 - 2]
                            elif 2 <= x1 - 1 <= 7 and 0 <= y1 - 2 <= 9 and deck[x1 - 1][y1 - 2] in figuresh:
                                if a in figuresl:
                                    deck[x1 - 1][y1 - 2] = '*' + deck[x1 - 1][y1 - 2]
                            if 2 <= x1 + 2 <= 7 and 0 <= y1 + 1 <= 9 and deck[x1 + 2][y1 + 1] == '.':
                                deck[x1 + 2][y1 + 1] = '*'
                            elif 2 <= x1 + 2 <= 7 and 0 <= y1 + 1 <= 9 and deck[x1 + 2][y1 + 1] in figuresl:
                                if a in figuresl:
                                    deck[x1 + 2][y1 + 1] = '!' + deck[x1 + 2][y1 + 1]
                            elif 2 <= x1 + 2 <= 7 and 0 <= y1 + 1 <= 9 and deck[x1 + 2][y1 + 1] in figuresh:
                                if a in figuresl:
                                    deck[x1 + 2][y1 + 1] = '*' + deck[x1 + 2][y1 + 1]
                            if 2 <= x1 + 2 <= 7 and 0 <= y1 - 1 <= 9 and deck[x1 + 2][y1 - 1] == '.':
                                deck[x1 + 2][y1 - 1] = '*'
                            elif 2 <= x1 + 2 <= 7 and 0 <= y1 - 1 <= 9 and deck[x1 + 2][y1 - 1] in figuresl:
                                if a in figuresl:
                                    deck[x1 - 2][y1 - 1] = '!' + deck[x1 - 2][y1 - 1]
                            elif 2 <= x1 + 2 <= 7 and 0 <= y1 - 1 <= 9 and deck[x1 + 2][y1 - 1] in figuresh:
                                if a in figuresl:
                                    deck[x1 - 2][y1 - 1] = '*' + deck[x1 - 2][y1 - 1]
                            if 2 <= x1 + 1 <= 7 and 0 <= y1 + 2 <= 9 and deck[x1 + 1][y1 + 2] == '.':
                                deck[x1 + 1][y1 + 2] = '*'
                            elif 2 <= x1 + 1 <= 7 and 0 <= y1 + 2 <= 9 and deck[x1 + 1][y1 + 2] in figuresl:
                                if a in figuresl:
                                    deck[x1 + 1][y1 + 2] = '!' + deck[x1 + 1][y1 + 2]
                            elif 2 <= x1 + 1 <= 7 and 0 <= y1 + 2 <= 9 and deck[x1 + 1][y1 + 2] in figuresh:
                                if a in figuresl:
                                    deck[x1 + 1][y1 + 2] = '*' + deck[x1 + 1][y1 + 2]
                            if 2 <= x1 + 1 <= 7 and 0 <= y1 - 2 <= 9 and deck[x1 + 1][y1 - 2] == '.':
                                deck[x1 + 1][y1 - 2] = '*'
                            elif 2 <= x1 + 1 <= 7 and 0 <= y1 - 2 <= 9 and deck[x1 + 1][y1 - 2] in figuresl:
                                if a in figuresl:
                                    deck[x1 + 1][y1 - 2] = '!' + deck[x1 + 1][y1 - 2]
                            elif 2 <= x1 + 1 <= 7 and 0 <= y1 - 2 <= 9 and deck[x1 + 1][y1 - 2] in figuresh:
                                if a in figuresl:
                                    deck[x1 + 1][y1 - 2] = '*' + deck[x1 + 1][y1 - 2]

                        if a == 'B':
                            for i in range(1, 9):
                                if deck[x1 + i][y1 + i] == '.' and 2 <= x1 + i <= 9 and 2 <= y1 + i <= 9:
                                    deck[x1 + i][y1 + i] = '*'
                                elif deck[x1 + i][y1 + i] in figuresl and 2 <= x1 + i <= 9 and 2<=y1+i<= 9:
                                    if a in figuresl:
                                        deck[x1 + i][y1 + i] = '!' + deck[x1 + i][y1 + i]
                                        break
                                elif deck[x1 + i][y1 + i] in figuresh and 2 <= x1 + i <= 9 and 2 <= y1 + i <= 9:
                                    if a in figuresl:
                                        deck[x1 + i][y1 + i] = '*' + deck[x1 + i][y1 + i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 - i][y1 + i] == '.' and 2 <= x1 - i <= 9 and 2 <= y1 + i <= 9:
                                    deck[x1 - i][y1 + i] = '*'
                                elif deck[x1 - i][y1 + i] in figuresl and 2 <= x1 - i <= 9 and 2 <= y1 + i <= 9:
                                    if a in figuresl:
                                        deck[x1 - i][y1 + i] = '!' + deck[x1 - i][y1 + i]
                                        break
                                elif deck[x1 - i][y1 + i] in figuresh and 2 <= x1 - i <= 9 and 2 <= y1 + i <= 9:
                                    if a in figuresl:
                                        deck[x1 - i][y1 + i] = '*' + deck[x1 - i][y1 + i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 + i][y1 - i] == '.' and 2 <= x1 + i <= 9 and 2 <= y1 - i <= 9:
                                    deck[x1 + i][y1 - i] = '*'
                                elif deck[x1 + i][y1 - i] in figuresl and 2 <= x1 + i <= 9 and 2 <= y1 - i <= 9:
                                    if a in figuresl:
                                        deck[x1 + i][y1 - i] = '!' + deck[x1 + i][y1 - i]
                                        break
                                elif deck[x1 + i][y1 - i] in figuresh and 2 <= x1 + i <= 9 and 2 <= y1 - i <= 9:
                                    if a in figuresl:
                                        deck[x1 + i][y1 - i] = '*' + deck[x1 + i][y1 - i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 - i][y1 - i] == '.' and 2 <= x1 - i <= 9 and 2 <= y1 - i <= 9:
                                    deck[x1 - i][y1 - i] = '*'
                                elif deck[x1 - i][y1 - i] in figuresl and 2 <= x1 - i <= 9 and 2 <= y1 - i <= 9:
                                    if a in figuresl:
                                        deck[x1 - i][y1 - i] = '!' + deck[x1 - i][y1 - i]
                                        break
                                elif deck[x1 - i][y1 - i] in figuresh and 2 <= x1 - i <= 9 and 2 <= y1 - i <= 9:
                                    if a in figuresl:
                                        deck[x1 - i][y1 - i] = '*' + deck[x1 - i][y1 - i]
                                        break
                                else:
                                    break
                        if deck[x1][y1] == 'Q' or deck[x1][y1] == 'q':
                            for i in range(1, 9):
                                if deck[x1 + i][y1 + i] == '.' and 2 <= x1 + i <= 9 and 2 <= y1 + i <= 9:
                                    deck[x1 + i][y1 + i] = '*'
                                elif deck[x1 + i][y1 + i] in figuresl:
                                    if a in figuresl:
                                        deck[x1 + i][y1 + i] = '!' + deck[x1 + i][y1 + i]
                                        break
                                elif deck[x1 + i][y1 + i] in figuresh and 2 <= x1 + i <= 9 and 2 <= y1 + i <= 9:
                                    if a in figuresl:
                                        deck[x1 + i][y1 + i] = '*' + deck[x1 + i][y1 + i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 + i][y1 - i] == '.' and 2 <= x1 + i <= 9 and 2 <= y1 - i <= 9:
                                    deck[x1 + i][y1 - i] = '*'
                                elif deck[x1 + i][y1 - i] in figuresl:
                                    if a in figuresl:
                                        deck[x1 + i][y1 - i] = '!' + deck[x1 + i][y1 - i]
                                        break
                                elif deck[x1 + i][y1 - i] in figuresh:
                                    if a in figuresl:
                                        deck[x1 + i][y1 - i] = '*' + deck[x1 + i][y1 - i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 - i][y1 + i] == '.' and 2 <= x1 - i <= 9 and 2 <= y1 + i <= 9:
                                    deck[x1 - i][y1 + i] = '*'
                                elif deck[x1 - i][y1 + i] in figuresl:
                                    if a in figuresl:
                                        deck[x1 - i][y1 + i] = '!' + deck[x1 - i][y1 + i]
                                        break
                                elif deck[x1 - i][y1 + i] in figuresh:
                                    if a in figuresl:
                                        deck[x1 - i][y1 + i] = '*' + deck[x1 - i][y1 + i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 - i][y1 - i] == '.' and 2 <= x1 - i <= 9 and 2 <= y1 - i <= 9:
                                    deck[x1 - i][y1 - i] = '*'
                                elif deck[x1 - i][y1 - i] in figuresl:
                                    if a in figuresl:
                                        deck[x1 - i][y1 - i] = '!' + deck[x1 - i][y1 - i]
                                        break
                                elif deck[x1 - i][y1 - i] in figuresh:
                                    if a in figuresl:
                                        deck[x1 - i][y1 - i] = '*' + deck[x1 - i][y1 - i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 + i][y1] == '.' and 2 <= x1 + i <= 9:
                                    deck[x1 + i][y1] = '*'
                                elif deck[x1 + i][y1] in figuresl:
                                    if a in figuresl:
                                        deck[x1 + i][y1] = '!' + deck[x1 + i][y1]
                                        break
                                elif deck[x1 + i][y1] in figuresh:
                                    if a in figuresl:
                                        deck[x1 + i][y1] = '*' + deck[x1 + i][y1]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1 - i][y1] == '.' and 2 <= x1 - i <= 9:
                                    deck[x1 - i][y1] = '*'
                                elif deck[x1 - i][y1] in figuresl:
                                    if a in figuresl:
                                        deck[x1 - i][y1] = '!' + deck[x1 - i][y1]
                                        break
                                elif deck[x1 - i][y1] in figuresh:
                                    if a in figuresl:
                                        deck[x1 - i][y1] = '*' + deck[x1 - i][y1]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1][y1 - i] == '.' and 2 <= y1 - i <= 9:
                                    deck[x1][y1 - i] = '*'
                                elif deck[x1][y1 - i] in figuresl:
                                    if a in figuresl:
                                        deck[x1][y1 - i] = '!' + deck[x1][y1 - i]
                                        break
                                elif deck[x1][y1 - i] in figuresh:
                                    if a in figuresl:
                                        deck[x1][y1 - i] = '*' + deck[x1][y1 - i]
                                        break
                                else:
                                    break
                            for i in range(1, 9):
                                if deck[x1][y1 + i] == '.' and 2 <= y1 + i <= 9:
                                    deck[x1][y1 + i] = '*'
                                elif deck[x1][y1 + i] in figuresl:
                                    if a in figuresl:
                                        deck[x1][y1 + i] = '!' + deck[x1][y1 + i]
                                        break
                                elif deck[x1][y1 + i] in figuresh:
                                    if a in figuresl:
                                        deck[x1][y1 + i] = '*' + deck[x1][y1 + i]
                                        break
                                else:
                                    break
        countl = 0
        for i in range(2, 10):
            for j in range(2, 10):
                if 'k' in deck[i][j]:
                    if '*' in deck[i][j]:
                        if deck[i+1][j+1]=='*':
                            countl+=1
                        elif deck[i+1][j+1] in figuresl:
                                if '!' in deck[i+1][j+1]:
                                    countl+=1
                        elif deck[i+1][j+1]==' ':
                            countl+=1
                        if deck[i + 1][j - 1] == '*':
                            countl+=1
                        elif deck[i + 1][j - 1] in figuresl:
                            if '!' in deck[i + 1][j - 1]:
                                countl+=1
                        elif deck[i + 1][j - 1] == ' ':
                            countl+=1
                        if deck[i - 1][j - 1] == '*':
                            countl+=1
                        elif deck[i - 1][j - 1] in figuresl:
                            if '!' in deck[i - 1][j - 1]:
                                countl+=1
                        elif deck[i - 1][j - 1] == ' ':
                            countl+=1
                        if deck[i - 1][j + 1] == '*':
                            countl+=1
                        elif deck[i - 1][j + 1] in figuresl:
                            if '!' in deck[i - 1][j + 1]:
                                countl+=1
                        elif deck[i - 1][j + 1] == ' ':
                            countl+=1
                        if deck[i + 1][j] == '*':
                            countl+=1
                        elif deck[i + 1][j] in figuresl:
                            if '!' in deck[i + 1][j]:
                                countl += 1
                        elif deck[i + 1][j] == ' ':
                            countl+=1
                        if deck[i - 1][j] == '*':
                            countl+=1
                        elif deck[i - 1][j] in figuresl:
                            if '!' in deck[i - 1][j]:
                                countl+=1
                        elif deck[i - 1][j] == ' ':
                            countl += 1
                        if deck[i][j + 1] == '*':
                            countl+=1
                        elif deck[i][j + 1] in figuresl:
                            if '!' in deck[i][j + 1]:
                                countl+=1
                        elif deck[i][j + 1] == ' ':
                            countl+=1
                        if deck[i][j - 1] == '*':
                            countl+=1
                        elif deck[i][j - 1] in figuresl:
                            if '!' in deck[i][j - 1]:
                                countl+=1
                        elif deck[i][j - 1] == ' ':
                            countl+=1
                if countl==8:
                        flagl = True
        for i in range(2, 10):
                for j in range(2, 10):
                        if deck[i][j]=='*':
                                deck[i][j]=='.'
                        elif '*' in deck[i][j]:
                                deck[i][j]=deck[i][j][1:]
                        elif '!' in deck[i][j]:
                                deck[i][j]=deck[i][j][1:]

        return flagh, flagl

#поле и глобальные листы
deck = [[' ', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ' ', ' '],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        ['8', ' ', 'r', 'n', 'b', 'q', 'k', 'b', 'n', 'r', ' ', '8'],
        ['7', ' ', 'p', 'p', 'p', 'p', 'p', 'p', 'p', 'p', ' ', '7'],
        ['6', ' ', '.', '.', '.', '.', '.', '.', '.', '.', ' ', '6'],
        ['5', ' ', '.', '.', '.', '.', '.', '.', '.', '.', ' ', '5'],
        ['4', ' ', '.', '.', '.', '.', '.', '.', '.', '.', ' ', '4'],
        ['3', ' ', '.', '.', '.', '.', '.', '.', '.', '.', ' ', '3'],
        ['2', ' ', 'P', 'P', 'P', 'P', 'P', 'P', 'P', 'P', ' ', '2'],
        ['1', ' ', 'R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R', ' ', '1'],
        [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
        [' ', ' ', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', ' ', '']]
dict1 = {'a': 2, 'b': 3, 'c': 4, 'd': 5, 'e': 6, 'f': 7, 'g': 8, 'h': 9, '1': 9, '2': 8, '3': 7, '4': 6, '5': 5, '6': 4, '7': 3, '8': 2}
list_hod = []
count = 0
figuresh = 'PRNBQK'
figuresl = 'prnbqk'
flagh = False
flagl = False

#начало игры
print('большие буквы - белые')
print('маленькие буквы - черные')
for i in range(12):
        for j in range(12):
                print(deck[i][j].ljust(3), end='')
        print()
list_deck=[]
for i in range(2,11):
        for j in range(2,11):
                list_deck.append(deck[i][j])
list_hod.append(list_deck)


#основная часть игры
while True:
        print('Введите позицию фигуры, которой будет сделан ход')
        a = str(input())
        if a=='мат' or a=='ничья':
                print(count)
                break
        elif a == 'вернуться назад':
                print('На сколько ходов вы хотите вернуться назад?')
                c = int(input())
                back_hod(c, list_hod)
                count-=c
        else:
                hod_help(a)
                print('Введите позицию для перемещения фигуры')
                b = str(input())
                hod(a, b)
                count+=1
                mat(flagh,flagl)
                if flagh==True or flagl==True:
                        print('мат')
                        break