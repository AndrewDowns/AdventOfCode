def init_game():
    """
    A function to initialise the game by loading in the player's starting hands

    :return players: list
    """
    fh = open("Input.txt")
    players = []
    for player in fh.read().split("\n\n"):
        hand = []
        for line in player.split("\n"):
            if not line.startswith("Player"):
                hand.append(int(line))
        players.append(hand)
    return players


def winner(players):
    """
    A function to check if either player is the winner.
    The winner is determined to be the player who has all of the available cards.

    -------------------
    players:
    A list of lists that represent each played hand of cards

    -------------------

    :parameter players:list
    :return boolean
    """
    for player in players:
        if len(player) == 0:
            return True
    return False


def play_round(players):
    """
    A function to simulate one round of combat.
    Before either player deals a card, if there was a previous round in this game that had exactly
    the same cards in the same order in the same players' decks, the game instantly ends in a win for player 1.
    Previous rounds from other games are not considered. (This prevents infinite games of Recursive Combat,
    which everyone agrees is a bad idea.)
    Otherwise, this round's cards must be in a new configuration; the players begin the round by each drawing the
    top card of their deck as normal.

    If both players have at least as many cards remaining in their deck as the value of the card they just drew,
    the winner of the round is determined by playing a new game of Recursive Combat (see below).

    Otherwise, at least one player must not have enough cards left in their deck to recurse; the winner
    of the round is the player with the higher-value card.

    As in regular Combat, the winner of the round (even if they won the round by winning a sub-game) takes
    the two cards dealt at the beginning of the round and places them on the bottom of their own deck
    (again so that the winner's card is above the other card). Note that the winner's card might be the lower-valued of
    the two cards if they won the round due to winning a sub-game. If collecting cards by winning the round causes
    a player to have all of the cards, they win, and the game ends.

    -------------------
    players:
    A list of lists that represent each played hand of cards

    -------------------

    :parameter players:list
    :return players:list
    """
    cards_in_play = []
    for i, player in enumerate(players):
        card = player.pop(0)
        print("Player", i+1, "plays:", card)
        cards_in_play.append(card)

    if cards_in_play[0] <= len(players[0]) and cards_in_play[1] <= len(players[1]):
        print("Playing a sub-game to determine the winner...")
        new_players = [players[0][:cards_in_play[0]], players[1][:cards_in_play[1]]]
        round_winner = start_game(new_players)
        if round_winner == 0:
            players[round_winner].append(cards_in_play[0])
            players[round_winner].append(cards_in_play[1])
        else:
            players[round_winner].append(cards_in_play[1])
            players[round_winner].append(cards_in_play[0])

    else:
        if cards_in_play[0] > cards_in_play[1]:
            round_winner = 0
        else:
            round_winner = 1
        cards_in_play.sort(reverse=True)
        for card in cards_in_play:
            players[round_winner].append(card)

    print("Player", round_winner+1, "wins the round")
    return players


def instant_end_game(players, game):
    """
    A function to handle the instant win rule of Recursive Combat.
    Similar to end_game this function shows the results of the current game.
    If the game is the main game and not a sub-game then it will finish the game.
    If an instant win occurs Player 1 autmatically gets the win.

    -------------------
    players:
    A list of lists that represent each played hand of cards

    game:
    An integer determining which game is currentling being played.

    -------------------

    :parameter players:list
    :parameter game:integer
    :return integer
    """
    if game == 1:
        print("== Post-game results ==")
        for j, player in enumerate(players):
            print("Player", j + 1, "hand:", player)

        print("Player 1 wins the game")
        print("Win by INSTANT WIN")
        winner = 0

        winning_score = 0
        for i, card in enumerate(players[winner]):
            winning_score += card * (len(players[winner])-i)
        print("Winning Score:", winning_score)
    else:
        print("Player 1 wins game", game)
        return 0


def end_game(players, game):
    """
    A function to process the end of the game and show the results.
    This function also handles then end of game scenario for sub-games
    started during recursive combat.

    -------------------
    players:
    A list of lists that represent each played hand of cards

    game:
    An integer representing the current game. Game 1 will always be the main game.

    -------------------

    :parameter integer
    """
    if game == 1:
        print("== Post-game results ==")
        for j, player in enumerate(players):
            print("Player", j + 1, "hand:", player)

        if len(players[0]) == 0:
            print("Player 2 wins game", game)
            winner = 1
        else:
            print("Player 1 wins game", game)
            winner = 0

        winning_score = 0
        for i, card in enumerate(players[winner]):
            winning_score += card * (len(players[winner])-i)
        print("Winning Score:", winning_score)
    else:
        if len(players[0]) == 0:
            print("Player 2 wins game", game)
            return 1
        else:
            print("Player 1 wins game", game)
            return 0


def check_instant_win(players, game):
    """
    A function to check if the current hand of each player has been played in this exact order before
    during this game and therefore determine if this game should instantly end awarding Player 1 the win.

    -------------------
    players:
    A list of lists that represent each played hand of cards

    game:
    An integer representing the current game.

    -------------------

    :parameter players:list
    :parameter game:integer
    :return boolean

    """
    if players in round_record[str(game)]:
        return True
    else:
        return False


def start_game(players):
    """
    A function to start a game of combat and continue playing rounds until a winner is decided

    -------------------
    players:
    A list of lists that represent each played hand of cards

    -------------------

    :parameter players:list
    """
    round = 1
    if len(round_record) == 0:
        game = 1
    else:
        game = len(round_record)+1
    instant_win = False
    round_record[str(game)] = []
    print()
    print("=== Game",game,"===")
    print()
    while not winner(players) and not instant_win:
        print("--Round", round, "Game",game, "--")
        for j, player in enumerate(players):
            print("Player", j+1,"hand:", player )

        if not check_instant_win(players, game):
            new_players = []
            for i, player in enumerate(players):
                new_player = []
                for item in player:
                    new_player.append(item)
                new_players.append(new_player)
            round_record[str(game)].append(new_players)
            players = play_round(players)
            print()
            round += 1
        else:
            print()
            instant_win = True
            break

    if instant_win:
        return instant_end_game(players, game)
    else:
        return end_game(players, game)


players = init_game()
round_record = dict()
start_game(players)
