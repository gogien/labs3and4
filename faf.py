def print_field(green=None, red=None):
    green = [] if green is None else green
    red = [] if red is None else red
    print('  ', end=' ')
    for key in field.keys():
        print('\033[37m' + key + '\033[0m', end=' ')
    print()
    for number in range(8, 0, -1):
        print('\033[37m' + str(number) + '\033[0m', end='')
        print('\033[37m' + '|' + '\033[0m', end=' ')
        for key in field.keys():
            if key+str(number) in green:
                print('\033[32m' + field[key][str(number)] + '\033[0m', end=' ')
            elif key+str(number) in red:
                if field[key][str(number)] in 'Kk':
                    print('\033[35m' + field[key][str(number)] + '\033[0m', end=' ')
                else:
                    print('\033[31m' + field[key][str(number)] + '\033[0m', end=' ')
            else:
                print(field[key][str(number)], end=' ')
        print('\033[37m' + '|' + '\033[0m', end='')
        print('\033[37m' + str(number) + '\033[0m')
    print('  ', end=' ')
    for key in field.keys():
        print('\033[37m' + key + '\033[0m', end=' ')
    print()


def check_moves(current, color):
    figure = field[current[0]][current[-1]]
    possible_moves = []
    if figure in 'P':
        possible_moves += calculate_possible_moves_P(current)
    elif figure in 'p':
        possible_moves += calculate_possible_moves_p(current)
    elif figure in 'Rr':
        possible_moves += calculate_possible_moves_r(current, color)
    elif figure in 'Bb':
        possible_moves += calculate_possible_moves_b(current, color)
    elif figure in 'Nn':
        possible_moves += calculate_possible_moves_n(current, color)
    elif figure in 'Qq':
        possible_moves += calculate_possible_moves_r(current, color) + calculate_possible_moves_b(current, color)
    elif figure in 'Kk':
        possible_moves += calculate_possible_moves_k(current, color)
    return possible_moves


def calculate_possible_moves_k(current, color):
    possible_moves = []
    for first in range(-1, 2):
        for second in range(-1, 2):
            try:
                if field[alphabet[alphabet.index(current[0])+first]][str(int(current[-1])+second)] == ' ':
                    possible_moves.append(alphabet[alphabet.index(current[0])+first]+str(int(current[-1])+second))
                elif field[alphabet[alphabet.index(current[0])+first]][str(int(current[-1])+second)] in figures['All'] and field[alphabet[alphabet.index(current[0])+first]][str(int(current[-1])+second)] not in figures[color]:
                    possible_moves.append(alphabet[alphabet.index(current[0])+first]+str(int(current[-1])+second))
            except (KeyError, IndexError):
                pass
    possible_moves += check_castling(color)
    return possible_moves


def calculate_possible_moves_P(current):
    possible_moves = []
    try:
        if field[current[0]][str(int(current[-1])+1)] == ' ':
            possible_moves.append(current[0]+str(int(current[-1])+1))
    except (KeyError, IndexError):
        pass
    try:
        if field[alphabet[alphabet.index(current[0])-1]][str(int(current[-1])+1)] in figures['Black'] and alphabet.index(current[0])-1 >= 0:
            possible_moves.append(alphabet[alphabet.index(current[0])-1]+str(int(current[-1])+1))
    except (KeyError, IndexError):
        pass
    try:
        if field[alphabet[alphabet.index(current[0])+1]][str(int(current[-1])+1)] in figures['Black'] and alphabet.index(current[0])+1 <= 8:
            possible_moves.append(alphabet[alphabet.index(current[0])+1]+str(int(current[-1])+1))
    except (KeyError, IndexError):
        pass
    try:
        if current[-1] == '2' and field[current[0]][str(int(current[-1])+2)] == ' ' and field[current[0]][str(int(current[-1])+1)] == ' ':
            possible_moves.append(current[0]+str(int(current[-1])+2))
    except (KeyError, IndexError):
        pass
    return possible_moves


def calculate_possible_moves_p(current):
    possible_moves = []
    try:
        if field[current[0]][str(int(current[-1]) - 1)] == ' ':
            possible_moves.append(current[0] + str(int(current[-1]) - 1))
    except (KeyError,IndexError):
        pass
    try:
        if field[alphabet[alphabet.index(current[0]) - 1]][str(int(current[-1]) - 1)] in figures['White'] and alphabet.index(current[0]) - 1 >= 0:
            possible_moves.append(alphabet[alphabet.index(current[0]) - 1] + str(int(current[-1]) - 1))
    except (KeyError,IndexError):
        pass
    try:
        if field[alphabet[alphabet.index(current[0]) + 1]][str(int(current[-1]) - 1)] in figures['White'] and alphabet.index(current[0]) + 1 <= 8:
            possible_moves.append(alphabet[alphabet.index(current[0]) + 1] + str(int(current[-1]) - 1))
    except (KeyError,IndexError):
        pass
    try:
        if current[-1] == '7' and field[current[0]][str(int(current[-1]) - 2)] == ' ' and field[current[0]][str(int(current[-1]) - 1)] == ' ':
            possible_moves.append(current[0] + str(int(current[-1]) - 2))
    except (KeyError,IndexError):
        pass
    return possible_moves


def calculate_possible_moves_r(current, color):
    possible_moves = []
    for index in range(int(current[-1]) + 1, 9):
        if field[current[0]][str(index)] == ' ':
            possible_moves.append(current[0] + str(index))
        elif field[current[0]][str(index)] in figures['All'] and field[current[0]][str(index)] not in figures[color]:
            possible_moves.append(current[0] + str(index))
            break
        else:
            break
    for index in range(int(current[-1]) - 1, 0, -1):
        if field[current[0]][str(index)] == ' ':
            possible_moves.append(current[0] + str(index))
        elif field[current[0]][str(index)] in figures['All'] and field[current[0]][str(index)] not in figures[color]:
            possible_moves.append(current[0] + str(index))
            break
        else:
            break
    for index in range(alphabet.index(current[0]) + 1, 8):
        if field[alphabet[index]][current[-1]] == ' ':
            possible_moves.append(alphabet[index] + current[-1])
        elif field[alphabet[index]][current[-1]] in figures['All'] and field[alphabet[index]][current[-1]] not in figures[color]:
            possible_moves.append(alphabet[index] + current[-1])
            break
        else:
            break
    for index in range(alphabet.index(current[0]) - 1, -1, -1):
        if field[alphabet[index]][current[-1]] == ' ':
            possible_moves.append(alphabet[index] + current[-1])
        elif field[alphabet[index]][current[-1]] in figures['All'] and field[alphabet[index]][current[-1]] not in figures[color]:
            possible_moves.append(alphabet[index] + current[-1])
            break
        else:
            break
    return possible_moves


def calculate_possible_moves_b(current, color):
    possible_moves = []
    try:
        for pos in enumerate(alphabet[alphabet.index(current[0]) + 1:], int(current[-1]) + 1):
            if field[pos[-1]][str(pos[0])] == ' ':
                possible_moves.append(pos[-1] + str(pos[0]))
            elif field[pos[-1]][str(pos[0])] in figures['All'] and field[pos[-1]][str(pos[0])] not in figures[color]:
                possible_moves.append(pos[-1] + str(pos[0]))
                break
            else:
                break
    except (KeyError, IndexError):
        pass
    try:
        for pos in enumerate(alphabet[:alphabet.index(current[0])][::-1], int(current[-1]) + 1):
            if field[pos[-1]][str(pos[0])] == ' ':
                possible_moves.append(pos[-1] + str(pos[0]))
            elif field[pos[-1]][str(pos[0])] in figures['All'] and field[pos[-1]][str(pos[0])] not in figures[color]:
                possible_moves.append(pos[-1] + str(pos[0]))
                break
            else:
                break
    except (KeyError, IndexError):
        pass
    try:
        for pos in enumerate(alphabet[alphabet.index(current[0]) + 1:], int(current[-1]) - 1):
            number = pos[0]
            if number > int(current[-1]) - 1:
                number = (int(current[-1]) + int(int(current[-1]) - 2)) - pos[0]
            if field[pos[-1]][str(number)] == ' ':
                possible_moves.append(pos[-1] + str(number))
            elif field[pos[-1]][str(number)] in figures['All'] and field[pos[-1]][str(number)] not in figures[color]:
                possible_moves.append(pos[-1] + str(number))
                break
            else:
                break
    except (KeyError, IndexError):
        pass
    try:
        for pos in enumerate(alphabet[:alphabet.index(current[0])][::-1], int(current[-1]) - 1):
            number = pos[0]
            if number > int(current[-1]) - 1:
                number = (int(current[-1]) + int(int(current[-1]) - 2)) - pos[0]
            if field[pos[-1]][str(number)] == ' ':
                possible_moves.append(pos[-1] + str(number))
            elif field[pos[-1]][str(number)] in figures['All'] and field[pos[-1]][str(number)] not in figures[color]:
                possible_moves.append(pos[-1] + str(number))
                break
            else:
                break
    except (KeyError, IndexError):
        pass

    return possible_moves


def calculate_possible_moves_n(current, color):
    possible_moves = []
    try:
        if field[alphabet[alphabet.index(current[0]) + 2]][str(int(current[-1]) + 1)] == ' ':
            possible_moves.append(alphabet[alphabet.index(current[0]) + 2] + str(int(current[-1]) + 1))
        elif field[alphabet[alphabet.index(current[0]) + 2]][str(int(current[-1]) + 1)] in figures['All'] and field[alphabet[alphabet.index(current[0]) + 2]][str(int(current[-1]) + 1)] not in figures[color]:
            possible_moves.append(alphabet[alphabet.index(current[0]) + 2] + str(int(current[-1]) + 1))
    except (KeyError, IndexError):
        pass
    try:
        if field[alphabet[alphabet.index(current[0]) + 2]][str(int(current[-1]) - 1)] == ' ':
            possible_moves.append(alphabet[alphabet.index(current[0]) + 2] + str(int(current[-1]) - 1))
        elif field[alphabet[alphabet.index(current[0]) + 2]][str(int(current[-1]) - 1)] in figures['All'] and field[alphabet[alphabet.index(current[0]) + 2]][str(int(current[-1]) - 1)] not in figures[color]:
            possible_moves.append(alphabet[alphabet.index(current[0]) + 2] + str(int(current[-1]) - 1))
    except (KeyError, IndexError):
        pass
    try:
        if field[alphabet[alphabet.index(current[0]) - 2]][str(int(current[-1]) + 1)] == ' ' and alphabet.index(current[0]) - 2 >= 0:
            possible_moves.append(alphabet[alphabet.index(current[0]) - 2] + str(int(current[-1]) + 1))
        elif field[alphabet[alphabet.index(current[0]) - 2]][str(int(current[-1]) + 1)] in figures['All'] and field[alphabet[alphabet.index(current[0]) - 2]][str(int(current[-1]) + 1)] not in figures[color] and alphabet.index(current[0]) - 2 >= 0:
            possible_moves.append(alphabet[alphabet.index(current[0]) - 2] + str(int(current[-1]) + 1))
    except (KeyError, IndexError):
        pass
    try:
        if field[alphabet[alphabet.index(current[0]) - 2]][str(int(current[-1]) - 1)] == ' ' and alphabet.index(current[0]) - 2 >= 0:
            possible_moves.append(alphabet[alphabet.index(current[0]) - 2] + str(int(current[-1]) - 1))
        elif field[alphabet[alphabet.index(current[0]) - 2]][str(int(current[-1]) - 1)] in figures['All'] and field[alphabet[alphabet.index(current[0]) - 2]][str(int(current[-1]) - 1)] not in figures[color] and alphabet.index(current[0]) - 2 >= 0:
            possible_moves.append(alphabet[alphabet.index(current[0]) - 2] + str(int(current[-1]) - 1))
    except (KeyError, IndexError):
        pass
    try:
        if field[alphabet[alphabet.index(current[0]) + 1]][str(int(current[-1]) + 2)] == ' ':
            possible_moves.append(alphabet[alphabet.index(current[0]) + 1] + str(int(current[-1]) + 2))
        elif field[alphabet[alphabet.index(current[0]) + 1]][str(int(current[-1]) + 2)] in figures['All'] and field[alphabet[alphabet.index(current[0]) + 1]][str(int(current[-1]) + 2)] not in figures[color]:
            possible_moves.append(alphabet[alphabet.index(current[0]) + 1] + str(int(current[-1]) + 2))
    except (KeyError, IndexError):
        pass
    try:
        if field[alphabet[alphabet.index(current[0]) - 1]][str(int(current[-1]) + 2)] == ' ' and alphabet.index(current[0]) - 1 >= 0:
            possible_moves.append(alphabet[alphabet.index(current[0]) - 1] + str(int(current[-1]) + 2))
        elif field[alphabet[alphabet.index(current[0]) - 1]][str(int(current[-1]) + 2)] in figures['All'] and field[alphabet[alphabet.index(current[0]) - 1]][str(int(current[-1]) + 2)] not in figures[color] and alphabet.index(current[0]) - 1 >= 0:
            possible_moves.append(alphabet[alphabet.index(current[0]) - 1] + str(int(current[-1]) + 2))
    except (KeyError, IndexError):
        pass
    try:
        if field[alphabet[alphabet.index(current[0]) + 1]][str(int(current[-1]) - 2)] == ' ':
            possible_moves.append(alphabet[alphabet.index(current[0]) + 1] + str(int(current[-1]) - 2))
        elif field[alphabet[alphabet.index(current[0]) + 1]][str(int(current[-1]) - 2)] in figures['All'] and field[alphabet[alphabet.index(current[0]) + 1]][str(int(current[-1]) - 2)] not in figures[color]:
            possible_moves.append(alphabet[alphabet.index(current[0]) + 1] + str(int(current[-1]) - 2))
    except (KeyError, IndexError):
        pass
    try:
        if field[alphabet[alphabet.index(current[0]) - 1]][str(int(current[-1]) - 2)] == ' ' and alphabet.index(current[0]) - 1 >= 0:
            possible_moves.append(alphabet[alphabet.index(current[0]) - 1] + str(int(current[-1]) - 2))
        elif field[alphabet[alphabet.index(current[0]) - 1]][str(int(current[-1]) - 2)] in figures['All'] and field[alphabet[alphabet.index(current[0]) - 1]][str(int(current[-1]) - 2)] not in figures[color] and alphabet.index(current[0]) - 1 >= 0:
            possible_moves.append(alphabet[alphabet.index(current[0]) - 1] + str(int(current[-1]) - 2))
    except (KeyError, IndexError):
        pass
    return possible_moves


def move(current, expected, color):
    figure = field[current[0]][current[-1]]
    action = '-'
    if figure == ' ':
        print('\033[31m' + 'На введёной клетке нет фигуры' + '\033[0m')
        return '', color
    if color == 'White' and figure not in figures['White']:
        print('\033[31m' + 'Сейчас ход белых, введите ход заново' + '\033[0m')
        return '', color
    if color == 'Black' and figure not in figures['Black']:
        print('\033[31m' + 'Сейчас ход чёрных, введите ход заново'+ '\033[0m')
        return '', color
    temp = ''
    eaten_temp = ''
    if field[current[0]][current[-1]] in 'Kk' and expected in ['C8', 'C1', 'G8', 'G1'] and ('0-0' in calculate_possible_moves_k(current,color) or '0-0-0' in calculate_possible_moves_k(current,color)):
        if expected == 'C8':
            field['C']['8'] = 'k'
            field['D']['8'] = 'r'
            field['A']['8'] = ' '
            field['E']['8'] = ' '
            color = 'Black' if color == 'White' else 'White'
            return '0-0-0', color
        if expected == 'C1':
            field['C']['1'] = 'K'
            field['D']['1'] = 'R'
            field['A']['1'] = ' '
            field['E']['1'] = ' '
            color = 'Black' if color == 'White' else 'White'
            return '0-0-0', color
        if expected == 'G8':
            field['G']['8'] = 'k'
            field['F']['8'] = 'r'
            field['H']['8'] = ' '
            field['E']['8'] = ' '
            color = 'Black' if color == 'White' else 'White'
            return '0-0', color
        if expected == 'G1':
            field['G']['1'] = 'K'
            field['F']['1'] = 'R'
            field['H']['1'] = ' '
            field['E']['1'] = ' '
            color = 'Black' if color == 'White' else 'White'
            return '0-0', color
    else:
        if field[current[0]][current[-1]] not in 'Pp':
            temp = figure
        if field[expected[0]][expected[-1]] == ' ':
            field[current[0]][current[-1]], field[expected[0]][expected[-1]] = field[expected[0]][expected[-1]], field[current[0]][current[-1]]
        else:
            if field[expected[0]][expected[-1]] not in 'Pp':
                eaten_temp = field[expected[0]][expected[-1]]
            field[expected[0]][expected[-1]] = field[current[0]][current[-1]]
            field[current[0]][current[-1]] = ' '
            action = ':'
    color = 'Black' if color == 'White' else 'White'
    return temp + current + action + eaten_temp + expected, color


def just_check(current):
    try:
        len(field[current[0]][current[-1]])
        return True
    except KeyError:
        print('\033[31m' + 'Введена несуществующая клетка! Введите заново' + '\033[0m')
        return False


def can_move(possible_moves, expected, color):
    if color =='White':
        possible_moves = (' '.join(possible_moves).replace('0-0-0', 'C1').replace('0-0', 'G1')).split(' ')
    else:
        possible_moves = (' '.join(possible_moves).replace('0-0-0', 'C8').replace('0-0', 'G8')).split(' ')
    if expected in possible_moves:
        return True
    return False


def tips(possible_moves, color):
    green = []
    for step in possible_moves:
        if step == '0-0':
            if color =='White':
                field['G']['1'] = '*'
            else:
                field['G']['8'] = '*'
        elif step == '0-0-0':
            if color =='White':
                field['C']['1'] = '*'
            else:
                field['C']['8'] = '*'
        else:
            if field[step[0]][step[-1]] == ' ':
                field[step[0]][step[-1]] = '*'
            else:
                green.append(step)
    print_field(green, under_fire(color))
    clear_tips()


def clear_tips():
    for key in field.keys():
        for number in field[key].keys():
            if field[key][number] == '*':
                field[key][number] = ' '


def under_fire(color):
    enemy_color = 'Black' if color == 'White' else 'White'
    under_fire_figures = []
    for ally_key in field.keys():
        for ally_number in field[ally_key].keys():
            if field[ally_key][ally_number] in figures[color]:
                for key in field.keys():
                    for number in field[key].keys():
                        if field[key][number] in figures[enemy_color] and (ally_key + ally_number) in check_moves(key+number, enemy_color):
                            under_fire_figures.append(ally_key + ally_number)
    return under_fire_figures


def check_check(color):
    pos_king = find_king(color)
    if pos_king in under_fire(color):
        return True
    return False


def find_king(color):
    figure = 'K' if color == 'White' else 'k'
    pos_king = ''
    for key in field.keys():
        for number in field[key].keys():
            if field[key][number] == figure:
                pos_king = key+number
    return pos_king


def return_steps(count, color):
    steps = moves[::-1]
    if count > len(moves):
        print('\033[31m' + 'Такого кол-ва ходов не было разыграно' + '\033[0m')
        return color
    for step in range(count):
        if steps[step] == '0-0':
            if color == 'Black':
                field['G']['1'] = ' '
                field['F']['1'] = ' '
                field['H']['1'] = 'R'
                field['E']['1'] = 'K'
            else:
                field['G']['8'] = ' '
                field['F']['8'] = ' '
                field['H']['8'] = 'r'
                field['E']['8'] = 'k'
        elif steps[step] == '0-0-0':
            if color == 'Black':
                field['C']['1'] = ' '
                field['D']['1'] = ' '
                field['A']['1'] = 'R'
                field['E']['1'] = 'K'
            else:
                field['C']['8'] = ' '
                field['D']['8'] = ' '
                field['A']['8'] = 'r'
                field['E']['8'] = 'k'
        else:
            if '-' in steps[step]:
                current, expected = steps[step].split('-')
                field[current[-2]][current[-1]], field[expected[-2]][expected[-1]] = field[expected[-2]][expected[-1]], field[current[-2]][current[-1]]
            elif ':' in steps[step]:
                current, expected = steps[step].split(':')
                if len(expected) == 2:
                    field[expected[0]][expected[-1]] = 'p' if color == 'Black' else 'P'
                else:
                    field[expected[1]][expected[-1]] = expected[0]
                if len(current) == 2:
                    field[current[0]][current[-1]] = 'p' if color == 'White' else 'P'
                else:
                    field[current[1]][current[-1]] = current[0]
        color = 'Black' if color == 'White' else 'White'
        moves.pop(-1)
    return color


def check_mate(color):
    flag = True
    for key in field.keys():
        for number in field[key].keys():
            if field[key][number] in figures[color]:
                for possible_move in check_moves(key + number, color):
                    notation = move(key + number, possible_move, color)
                    moves.append(notation[0])
                    if not check_check(color):
                        flag = False
                        return_steps(1, color)
                        break
                    else:
                        return_steps(1, color)
            if not flag:
                break
        if not flag:
            break
    for possible_move_king in check_moves(find_king(color), color):
        notation = move(find_king(color), possible_move_king, color)
        moves.append(notation[0])
        if not check_check(color):
            flag = False
            return_steps(1, color)
            break
        else:
            return_steps(1, color)
    return flag


def check_castling(color):
    possible_castling = []
    if color == 'White':
        if field['F']['1'] == field['G']['1'] == ' ' and not check_in_moves('RH1') and not check_in_moves('KE1'):
            possible_castling.append('0-0')
        if field['B']['1'] == field['C']['1'] == ' ' and not check_in_moves('RA1') and not check_in_moves('KE1'):
            possible_castling.append('0-0-0')
    elif color == 'Black':
        if field['F']['8'] == field['G']['8'] == ' ' and not check_in_moves('rH8') and not check_in_moves('kE8'):
            possible_castling.append('0-0')
        if field['B']['8'] == field['C']['8'] == ' ' and not check_in_moves('rA8') and not check_in_moves('kE8'):
            possible_castling.append('0-0-0')
    return possible_castling


def check_in_moves(position):
    flag = False
    for step in moves:
        if position in step:
            flag = True
            break
    return flag


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
    game_over = False
    while not game_over:
        print_field(green=None, red=under_fire(flag))
        if flag == 'White':
            print('Ход белых')
        else:
            print('Ход чёрных')
        if check_check(flag) and check_mate(flag):
            game_over = True
            previous_color = 'чёрных' if flag == 'White' else 'белых'
            print(f'Игра окончена! Мат! Победа {previous_color}')
            continue
        operand = input('Введите позицию фигуры, которой будет сделан ход: ').upper()
        if operand == '<-':
            count = int(input('Введите количество ходов для отмены:'))
            flag = return_steps(count, flag)
        else:
            if just_check(operand):
                possible_moves = check_moves(operand, flag)
                tips(possible_moves, flag)
                step = input('Введите позицию для перемещения фигуры: ').upper()
                if just_check(step):
                    if can_move(possible_moves, step, flag):
                        notation, flag = move(operand, step, flag)
                        moves.append(notation)
                    else:
                        print('\033[31m' + 'Эта фигура не может сходить сюда!' + '\033[0m')
                previous_color = 'Black' if flag == 'White' else 'White'
                if check_check(previous_color):
                    print('\033[31m' + f'Шах {previous_color}!Введите ход заново' + '\033[0m')
                    flag = return_steps(1, flag)
        moves = list(filter(lambda x: x != '', moves))


if __name__ == '__main__':
    main()
