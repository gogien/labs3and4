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
for d in deck:
    print(*d)
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
        list2 = [x1, y1, x2, y2]
        list_hod.append(list2)

list_hod = []
def back_hod(list_hod):
        print('На сколько ходов вы хотите вернуться назад?')
        c = int(input())
        for i in range(1, c+1):
            x1 = list_hod[-i][0]
            y1 = list_hod[-i][1]
            x2 = list_hod[-i][2]
            y2 = list_hod[-i][3]
            deck[x1][y1], deck[x2][y2] = deck[x2][y2], deck[x1][y1]
        count-=c
        for d in deck:
            print(*d)

count = 0
while True:
        print('Введите позицию фигуры, которой будет сделан ход')
        a = str(input())
        if a=='мат' or a=='ничья':
                print(count)
                break
        elif a == 'вернуться назад':
                back_hod(list_hod)
        else:
                print('Введите позицию для перемещения фигуры')
                b = str(input())
                hod(a, b)
                count+=1