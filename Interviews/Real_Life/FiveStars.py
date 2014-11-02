import datetime

yellow_player = None
black_player = None
black_player_score = 0
yellow_player_score = 0
goals = []
matches = []
players = {}


"""
players

{
    black_players
}


data
{
    request_type: register_player/goal,
    player_color: yellow/black,
    player_id: 12345,
}

"""

def handle_request(data):
    # validation(data) check for validation

    global yellow_player
    global black_player
    global black_player_score
    global yellow_player_score
    global goals
    global matches
    global players

    request_type = data["request_type"]

    if request_type == "register_player":
        # update the player as yellow/black
        if data["player_color"] == "yellow":
            yellow_player = data["player_id"]
        elif data["player_color"] == "black":
            black_player = data["player_id"]
        players[data['player_id']] = dict(wins=0,losses=0)

        # After registration, need to clean up all the goals/matches/player data

    if request_type == "goal":
        # Before goal, 1. need to check if players are registered.
        #              2. check if the game is finished

        # record the score
        if data["player_color"] == "yellow":
            yellow_player_score += 1
            goals.append((yellow_player, black_player, datetime.datetime.now()))

        elif data["player_color"] == "black":
            black_player_score += 1
            goals.append((black_player, yellow_player, datetime.datetime.now()))

        # check if the game is over
        if black_player_score == 5:
            # black wins
            matches.append((black_player, 5, yellow_player, yellow_player_score,
                datetime.datetime.now()))
            players[black_player]["wins"] += 1
            players[yellow_player]["losses"] += 1

        elif yellow_player_score == 5:
            # yellow wins
            matches.append((yellow_player, 5, black_player, black_player_score,
                datetime.datetime.now()))
            players[yellow_player]["wins"] += 1
            players[black_player]["losses"] += 1



if __name__ == "__main__":
    # write test code here
    handle_request(dict(request_type = 'register_player',
                        player_color = 'yellow',
                        player_id    = '00001',
        ))
    handle_request(dict(request_type = 'register_player',
                        player_color = 'black',
                        player_id    = '00002',
        ))
    handle_request(dict(request_type = 'goal',
                        player_color = 'yellow',
        ))
    handle_request(dict(request_type = 'goal',
                        player_color = 'yellow',
        ))
    handle_request(dict(request_type = 'goal',
                        player_color = 'yellow',
        ))
    handle_request(dict(request_type = 'goal',
                        player_color = 'yellow',
        ))
    handle_request(dict(request_type = 'goal',
                        player_color = 'yellow',
        ))

    print 'yellow_player = ', yellow_player
    print 'black_player = ', black_player
    print 'black_player_score = ', black_player_score
    print 'yellow_player_score = ', yellow_player_score
    print 'goals = ', goals
    print 'matches = ', matches
    print 'players = ', players

