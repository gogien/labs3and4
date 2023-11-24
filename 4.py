#функция хода
def hod(a, b):
        x1 = dict1.get(a[1])
        y1 = dict1.get(a[0])
        x2 = dict1.get(b[1])
        y2 = dict1.get(b[0])
        if deck[x2][y2]!='.':
                deck[x2][y2]='.'
        deck[x1][y1], deck[x2][y2] = deck[x2][y2], deck[x1][y1]
        for d in deck:
                print(*d)
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
                                else:
                                        break
                else:
                        if deck[x1-1][y1]=='.' and 2<=x1-1<=9:
                                deck[x1-1][y1]='*'
        if deck[x1][y1]=='p':
                if x1 == 3:
                        for i in range(1, 3):
                                if deck[x1 + i][y1] == '.' and 2 <= x1 + i <= 9:
                                                        deck[x1 + i][y1] = '*'
                                else:
                                        break
                else:
                        if deck[x1 + 1][y1] == '.' and 2 <= x1 + 1 <= 9:
                                deck[x1 + 1][y1] = '*'
        if deck[x1][y1]=='R' or deck[x1][y1]=='r':
                for i in range(1, 9):
                        if deck[x1+i][y1]=='.' and 2<=x1+i<=9:
                                deck[x1+i][y1]='*'
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1][y1+i]=='.' and 2<=y1+i<=9:
                                deck[x1][y1+i]='*'
                        else:
                                break
        if deck[x1][y1]=='N' or deck[x1][y1]=='n':
                if 2<=x1-2<=9 and 2<=y1-1<=9 and deck[x1-2][y1-1]=='.':
                        deck[x1-2][y1-1]='*'
                if 2<=x1-2<=7 and 0<=y1+1<=9 and deck[x1-2][y1+1]=='.':
                        deck[x1-2][y1+1]='*'
                if 2<=x1-1<=7 and 0<=y1+2<=9 and deck[x1-1][y1+2]=='.':
                        deck[x1-1][y1+2]='*'
                if 2<=x1-1<= 7 and 0<=y1-2<=9 and deck[x1-1][y1-2]=='.':
                        deck[x1-1][y1-2]='*'
                if 2<=x1+2<=7 and 0<=y1+1<=9 and deck[x1+2][y1+1]=='.':
                        deck[x1+2][y1+1]='*'
                if 2<=x1+2<=7 and 0<=y1-1<=9 and deck[x1+2][y1-1]=='.':
                        deck[x1+2][y1-1]= '*'
                if 2<=x1+1<=7 and 0<=y1+2<=9 and deck[x1+1][y1+2]=='.':
                        deck[x1+1][y1+2]='*'
                if 2<=x1+1<=7 and 0<=y1-2<=9 and deck[x1+1][y1-2]=='.':
                        deck[x1+1][y1-2]='*'
        if deck[x1][y1]=='B' or deck[x1][y1]=='b':
                for i in range(1, 9):
                        if deck[x1+i][y1+i]=='.' and 2<=x1+i<=9 and 2<=y1+i<=9:
                                deck[x1+i][y1+1]='*'
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1-i][y1+i]=='.' and 2<=x1-i<=9 and 2<=y1+i<=9:
                                deck[x1-i][y1+i]='*'
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1+i][y1-i]=='.' and 2<=x1+i <= 9 and 2<=y1-i<=9:
                                deck[x1+i][y1-i]='*'
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1-i][y1-i]=='.' and 2<=x1-i<=9 and 2<=y1-i<=9:
                                deck[x1-i][y1-i]='*'
                        else:
                                break
        if deck[x1][y1]=='K' or deck[x1][y1]=='k':
                if deck[x1+1][y1+1]=='.' and 2<=x1+1<=9 and 2<=y1+1<=9:
                        deck[x1+1][y1+1]='*'
                if deck[x1-1][y1+1]=='.' and 2<=x1-1<=9 and 2<=y1+1<=9:
                        deck[x1-1][y1+1]='*'
                if deck[x1+1][y1-1]=='.' and 2<=x1+1<=9 and 2<=y1-1<=9:
                        deck[x1+1][y1-1]='*'
                if deck[x1-1][y1-1]=='.' and 2<=x1-1<=9 and 2<=y1-1<=9:
                        deck[x1-1][y1-1]='*'
                if deck[x1+1][y1]=='.' and 2<=x1+1<=9:
                        deck[x1+1][y1]='*'
                if deck[x1-1][y1]=='.' and 2<=x1-1<=9:
                        deck[x1-1][y1]='*'
                if deck[x1][y1+1]=='.' and 2<=y1+1<=9:
                        deck[x1][y1+1]='*'
                if deck[x1][y1-1]=='.' and 2<=y1-1<=9:
                        deck[x1][y1-1]='*'
        if deck[x1][y1]=='Q' or deck[x1][y1]=='q':
                for i in range(1, 9):
                        if deck[x1+i][y1+i]=='.' and 2<=x1+i<=9 and 2<=y1+i<=9:
                                deck[x1+i][y1+i]='*'
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1+i][y1-i]=='.' and 2<=x1+i<=9 and 2<=y1-i<=9:
                                deck[x1+i][y1-i]='*'
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1-i][y1+i]=='.' and 2<=x1-i<=9 and 2<=y1+i<=9:
                                deck[x1-i][y1+i]='*'
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1-i][y1-i]=='.' and 2<=x1-i<=9 and 2<=y1-i<=9:
                                deck[x1-i][y1-i]='*'
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1+i][y1]=='.' and 2<=x1+i<=9:
                                deck[x1+i][y1]='*'
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1-i][y1]=='.' and 2<=x1-i<=9:
                                deck[x1-i][y1]='*'
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1][y1-i]=='.' and 2<=y1-i<=9:
                                deck[x1][y1-i]='*'
                        else:
                                break
                for i in range(1, 9):
                        if deck[x1][y1+i]=='.' and 2<=y1+i<=9:
                                deck[x1][y1+i]='*'
                        else:
                                break
        print('Возможные ходы')
        for d in deck:
                print(*d)
        for i in range(12):
                for j in range(12):
                        if deck[i][j]=='*':
                                deck[i][j]='.'

#def mat():

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

#начало игры
for d in deck:
        print(*d)
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