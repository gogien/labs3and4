def print_field():
    print(' ', end=' ')
    for key in field.keys():
        print(key, end=' ')
    print()
    for number in range(8, 0, -1):
        print(number, end=' ')
        for key in field.keys():
            print(field[key][str(number)], end=' ')
        print(number)
    print(' ', end=' ')
    for key in field.keys():
        print(key, end=' ')
    print()


def check_moves(current, color):
    figure = field[current[0]][current[-1]]
    possible_moves = []
    if figure in 'P':
        if field[current[0]][str(int(current[-1])+1)] == ' ':
            possible_moves.append(current[0]+str(int(current[-1])+1))
        if field[alphabet[alphabet.index(current[0])-1]][str(int(current[-1])+1)] in figures['Black'] and alphabet.index(current[0])-1 >= 0:
            possible_moves.append(alphabet[alphabet.index(current[0])-1]+str(int(current[-1])+1))
        if field[alphabet[alphabet.index(current[0])+1]][str(int(current[-1])+1)] in figures['Black'] and alphabet.index(current[0])+1 <= 8:
            possible_moves.append(alphabet[alphabet.index(current[0])+1]+str(int(current[-1])+1))
        if current[-1] == '2' and field[current[0]][str(int(current[-1])+2)] == ' ' and field[current[0]][str(int(current[-1])+1)] == ' ':
            possible_moves.append(current[0]+str(int(current[-1])+2))
    elif figure in 'p':
        if field[current[0]][str(int(current[-1])-1)] == ' ':
            possible_moves.append(current[0]+str(int(current[-1])-1))
        if field[alphabet[alphabet.index(current[0])-1]][str(int(current[-1])-1)] in figures['White'] and alphabet.index(current[0])-1 >= 0:
            possible_moves.append(alphabet[alphabet.index(current[0])-1]+str(int(current[-1])-1))
        if field[alphabet[alphabet.index(current[0])+1]][str(int(current[-1])-1)] in figures['White'] and alphabet.index(current[0])+1 <= 8:
            possible_moves.append(alphabet[alphabet.index(current[0])+1]+str(int(current[-1])-1))
        if current[-1] == '7' and field[current[0]][str(int(current[-1])-2)] == ' ' and field[current[0]][str(int(current[-1])-1)] == ' ':
            possible_moves.append(current[0]+str(int(current[-1])-2))
    elif figure in 'Rr':
        for index in range(int(current[-1])+1, 9):
            if field[current[0]][str(index)] == ' ':
                possible_moves.append(current[0]+str(index))
            elif field[current[0]][str(index)] in figures['All'] and field[current[0]][str(index)] not in figures[color]:
                possible_moves.append(current[0] + str(index))
                break
            else:
                break
        for index in range(int(current[-1])-1, 0, -1):
            if field[current[0]][str(index)] == ' ':
                possible_moves.append(current[0] + str(index))
            elif field[current[0]][str(index)] in figures['All'] and field[current[0]][str(index)] not in figures[color]:
                possible_moves.append(current[0] + str(index))
                break
            else:
                break
        for index in range(alphabet.index(current[0])+1, 8):
            if field[alphabet[index]][current[-1]] == ' ':
                possible_moves.append(alphabet[index]+current[-1])
            elif field[alphabet[index]][current[-1]] in figures['All'] and field[alphabet[index]][current[-1]] not in figures[color]:
                possible_moves.append(alphabet[index]+current[-1])
                break
            else:
                break
        for index in range(alphabet.index(current[0])-1, -1, -1):
            if field[alphabet[index]][current[-1]] == ' ':
                possible_moves.append(alphabet[index]+current[-1])
            elif field[alphabet[index]][current[-1]] in figures['All'] and field[alphabet[index]][current[-1]] not in figures[color]:
                possible_moves.append(alphabet[index] + current[-1])
                break
            else:
                break
    elif figure in 'Bb':
        try:
            for pos in enumerate(alphabet[alphabet.index(current[0])+1:], int(current[-1])+1):
                if field[pos[-1]][str(pos[0])] == ' ' :
                    possible_moves.append(pos[-1]+str(pos[0]))
                elif field[pos[-1]][str(pos[0])] in figures['All'] and field[pos[-1]][str(pos[0])] not in figures[color]:
                    possible_moves.append(pos[-1] + str(pos[0]))
                    break
                else:
                    break
        except KeyError or IndexError:
            pass
        try:
            for pos in enumerate(alphabet[:alphabet.index(current[0])][::-1], int(current[-1])+1):
                if field[pos[-1]][str(pos[0])] == ' ':
                    possible_moves.append(pos[-1] + str(pos[0]))
                elif field[pos[-1]][str(pos[0])] in figures['All'] and field[pos[-1]][str(pos[0])] not in figures[color]:
                    possible_moves.append(pos[-1] + str(pos[0]))
                    break
                else:
                    break
        except KeyError or IndexError:
            pass
        try:
            for pos in enumerate(alphabet[alphabet.index(current[0])+1:], int(current[-1])-1):
                number = pos[0]
                if number > int(current[-1])-1:
                    number = (int(current[-1])+int(int(current[-1])-2))-pos[0]
                if field[pos[-1]][str(number)] == ' ':
                    possible_moves.append(pos[-1] + str(number))
                elif field[pos[-1]][str(number)] in figures['All'] and field[pos[-1]][str(number)] not in figures[color]:
                    possible_moves.append(pos[-1] + str(number))
                    break
                else:
                    break
        except KeyError or IndexError:
            pass
        try:
            for pos in enumerate(alphabet[:alphabet.index(current[0])][::-1], int(current[-1])-1):
                number = pos[0]
                if number > int(current[-1])-1:
                    number = (int(current[-1])+int(int(current[-1])-2)) - pos[0]
                if field[pos[-1]][str(number)] == ' ':
                    possible_moves.append(pos[-1] + str(number))
                elif field[pos[-1]][str(number)] in figures['All'] and field[pos[-1]][str(number)] not in figures[color]:
                    possible_moves.append(pos[-1] + str(number))
                    break
                else:
                    break
        except KeyError or IndexError:
            pass
    elif figure in 'Nn':
        pass
    elif figure in 'Qq':
        pass
    elif figure in 'Kk':
        pass
    return possible_moves


def move(current, expected, color):
    try:
        figure = field[current[0]][current[-1]]
        action = '-'
        if figure == ' ':
            print('На введёной клетке нет фигуры')
            return '', color
        if color == 'White' and figure not in figures['White']:
            print('Сейчас ход белых, введите ход заново')
            return '', color
        if color == 'Black' and figure not in figures['Black']:
            print('Сейчас ход чёрных, введите ход заново')
            return '', color
        temp = ''
        if field[current[0]][current[-1]] not in 'Pp':
            temp = figure
        if field[expected[0]][expected[-1]] == ' ':
            field[current[0]][current[-1]], field[expected[0]][expected[-1]] = field[expected[0]][expected[-1]], field[current[0]][current[-1]]
        elif field[expected[0]][expected[-1]] in figures[color]:
            print('Нельзя съесть свою же фигуру! Введите ход заново')
            return '', color
        else:
            field[expected[0]][expected[-1]] = field[current[0]][current[-1]]
            field[current[0]][current[-1]] = ' '
            action = ':'
        if color == 'White':
            color = 'Black'
        else:
            color = 'White'
        return temp + current + action + expected, color
    except KeyError:
        print('Введена несуществующая клетка! Введите заново')
        return '', color


field = {
    'A': {
        '1': 'R',
        '2': 'P',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': 'p',
        '8': 'r',
    },
    'B': {
        '1': 'N',
        '2': 'P',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': 'p',
        '8': 'n',
    },
    'C': {
        '1': 'B',
        '2': 'P',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': 'p',
        '8': 'b',
    },
    'D': {
        '1': 'Q',
        '2': 'P',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': 'p',
        '8': 'q',
    },
    'E': {
        '1': 'K',
        '2': 'P',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': 'p',
        '8': 'k',
    },
    'F': {
        '1': 'B',
        '2': 'P',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': 'p',
        '8': 'b',
    },
    'G': {
        '1': 'N',
        '2': 'P',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': 'p',
        '8': 'n',
    },
    'H': {
        '1': 'R',
        '2': 'P',
        '3': ' ',
        '4': ' ',
        '5': ' ',
        '6': ' ',
        '7': 'p',
        '8': 'r',
    },
}

moves = []
figures = {
    'White': 'RNBQKP',
    'Black': 'rnbqkp',
    'All': 'RNBQKPrnbqkp',
}
alphabet = "ABCDEFGH"


def main():
    global moves
    flag = 'White'
    while True:
        print_field()
        if flag == 'White':
            print('Ход белых')
        else:
            print('Ход чёрных')
        operand = input('Введите позицию фигуры, которой будет сделан ход: ').upper()
        print(check_moves(operand, flag))
        step = input('Введите позицию для перемещения фигуры: ').upper()
        notation, flag = move(operand, step, flag)
        moves.append(notation)
        moves = list(filter(lambda x: x != '', moves))


if __name__ == '__main__':
    main()