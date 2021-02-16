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
        if len(player)==0:
            return True
    return False


def play_round(players):
    """
    A function to simulate one round of combat.
    Both players draw their top card, and the player with the higher-valued
    card wins the round. The winner keeps both cards, placing them on the bottom of
    their own deck so that the winner's card is above the other card.

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

    if cards_in_play[0] > cards_in_play[1]:
        round_winner = 0
    else:
        round_winner = 1

    print("Player", round_winner+1, "wins the round")
    cards_in_play.sort(reverse=True)
    for card in cards_in_play:
        players[round_winner].append(card)

    return players


def end_game(players):
    """
    A function to process the end of the game and show the results

    -------------------
    players:
    A list of lists that represent each played hand of cards

    -------------------

    :parameter players:list
    """
    print("== Post-game results ==")
    for j, player in enumerate(players):
        print("Player", j + 1, "hand:", player)

    if len(players[0]) == 0:
        print("Player 2 wins the game")
        winner = 1
    else:
        print("Player 1 wins the game")
        winner = 0

    winning_score = 0
    for i, card in enumerate(players[winner]):
        winning_score += card * (len(players[winner])-i)
    print("Winning Score:", winning_score)


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
    while not winner(players):
        print("--Round", round,"--")
        for j, player in enumerate(players):
            print("Player", j+1,"hand:", player )
        players = play_round(players)
        print()
        round += 1

    end_game(players)


players = init_game()
start_game(players)
