table = ['#', '#', '#', '#', '#', '#', '#', '#', '#', '#']

def show_table(table):
    emptyTable = '''
_________________________
|       |       |       |
|   1   |   2   |   3   |
|       |       |       |
|_______|_______|_______|
|       |       |       |
|   4   |   5   |   6   |
|       |       |       |
|_______|_______|_______|
|       |       |       |
|   7   |   8   |   9   |
|       |       |       |
|_______|_______|_______|

'''
    for i in range(1, 10):
        if table[i] == 'O' or table[i] == 'X':
            emptyTable = emptyTable.replace(str(i), table[i])
        else:
            emptyTable = emptyTable.replace(str(i), ' ')
    print(emptyTable)

def place_marker(table, marker, position):
    table[position] = marker
    return table


def check_space(table, position):
    return table[position] == '#'

def full_table_check(table):
    # for x in table:
    #     if x == '#' and len([x for x in table]) == 1:
    #         return True
    #     else:
    #         return False
    return len([x for x in table if x == '#']) == 1


def check_win(table, mark):
    if table[1] == table[2] == table[3] == mark:
        return True
    if table[4] == table[5] == table[6] == mark:
        return True
    if table[7] == table[8] == table[9] == mark:
        return True
    if table[1] == table[4] == table[7] == mark:
        return True
    if table[1] == table[5] == table[9] == mark:
        return True
    if table[2] == table[5] == table[8] == mark:
        return True
    if table[3] == table[6] == table[9] == mark:
        return True
    if table[3] == table[5] == table[7] == mark:
        return True
    else:
        return False


def rematch():
    re_play = input("Are you up for another game? Answer yes or no: ")
    if re_play.lower() == 'yes':
        return True
    if re_play.lower() == 'no':
        return False