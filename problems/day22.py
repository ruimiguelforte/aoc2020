from problems.common import get_input_of_day


def process_input(input_list):
    players = []
    current_player = []
    for line in input_list:
        if line.strip() == '':
            if len(current_player) > 0:
                players.append(current_player)
                current_player = []
        elif line.startswith('P'):
            continue
        else:
            current_player.append(int(line.strip()))
    if len(current_player) > 0:
        players.append(current_player)
    return players[0], players[1]


def get_score(winner):
    return sum([winner[i] * (len(winner) - i) for i in range(len(winner))])


def get_game_state(player1, player2):
    return ','.join(map(str, player1)) + '#' + ','.join(map(str, player2))


def recursive_combat(player1, player2):
    game_states = set()
    while (len(player1) > 0) and (len(player2) > 0):
        current_state = get_game_state(player1, player2)
        if current_state in game_states:
            return player1, player2, True
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if (len(player1) >= card1) and (len(player2) >= card2):
            subp1, subp2, p1autowon = recursive_combat(player1.copy()[0:card1], player2.copy()[0:card2])
            if p1autowon or (len(subp2) == 0):
                player1.append(card1)
                player1.append(card2)
            else:
                player2.append(card2)
                player2.append(card1)
        elif card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)
        game_states.add(current_state)
    return player1, player2, False


def solve_part1(input_list):
    player1, player2 = process_input(input_list)
    while (len(player1) > 0) and (len(player2) > 0):
        card1 = player1.pop(0)
        card2 = player2.pop(0)
        if card1 > card2:
            player1.append(card1)
            player1.append(card2)
        else:
            player2.append(card2)
            player2.append(card1)
    winner = player1 if len(player2) == 0 else player2
    return get_score(winner)


def solve_part2(input_list):
    player1, player2 = process_input(input_list)
    subp1, subp2, p1autowon = recursive_combat(player1, player2)
    winner = subp1 if len(subp2) == 0 or p1autowon else subp2
    return get_score(winner)


if __name__ != 'main':
    print(solve_part1(get_input_of_day(22)))
    print(solve_part2(get_input_of_day(22)))
