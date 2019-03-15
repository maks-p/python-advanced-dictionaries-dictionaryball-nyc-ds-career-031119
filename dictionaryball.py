def game_dict():
    game_dictionary = {'home':
                            {'team_name': 'Brooklyn Nets',
                            'colors': ['Black', 'White'],
                            'players':
                                {'Alan Anderson': {'number': 0,'shoe': 16,'points': 22,'rebounds': 12,'assists': 12,'steals': 3,'blocks': 1,'slam_dunks': 1},
                                'Reggie Evans': {'number': 30,'shoe': 14,'points': 12,'rebounds': 12,'assists': 12,'steals': 12,'blocks': 12,'slam_dunks': 7},
                                'Brook Lopez': {'number': 11,'shoe': 17,'points': 17,'rebounds': 19,'assists': 10,'steals': 3,'blocks': 1,'slam_dunks': 15},
                                'Mason Plumlee': {'number': 1,'shoe': 19,'points': 26,'rebounds': 12,'assists': 6,'steals': 3,'blocks': 8,'slam_dunks': 5},
                                'Jason Terry': {'number': 31,'shoe': 15,'points': 19,'rebounds': 2,'assists': 2,'steals': 4,'blocks': 11,'slam_dunks': 11}
                                }
                            }, 
                        'away':
                            {'team_name': 'Charlotte Hornets',
                            'colors': ['Turquoise', 'Purple'],
                            'players':
                                {'Jeff Adrien': {'number': 4, 'shoe': 18, 'points': 10, 'rebounds': 1, 'assists': 1, 'steals': 2, 'blocks': 7, 'slam_dunks': 2},
                                'Bismack Biyombo': {'number': 0, 'shoe': 16, 'points': 12, 'rebounds': 4, 'assists': 7, 'steals': 7, 'blocks': 15, 'slam_dunks': 10},
                                'DeSagna Diop': {'number': 2, 'shoe': 14, 'points': 24, 'rebounds': 12, 'assists': 12, 'steals': 4, 'blocks': 5, 'slam_dunks': 5},
                                'Ben Gordon': {'number': 8, 'shoe': 15, 'points': 33, 'rebounds': 3, 'assists': 2, 'steals': 1, 'blocks': 1, 'slam_dunks': 0},
                                'Brendan Haywood': {'number': 33, 'shoe': 15, 'points': 6, 'rebounds': 12, 'assists': 12, 'steals': 22, 'blocks': 5, 'slam_dunks': 12}
                                }
                            }
                        }

    return game_dictionary

###

"""HELPER FUNCTIONS"""

team_1 = game_dict()['home']['team_name'] #Brooklyn Nets
team_2 = game_dict()['away']['team_name'] #Charlotte Hornets

def player_list():
    team_list = []
    for location_data, team in game_dict().items():
        for players in team['players'].items():
            team_list.append(players[0])
    return team_list

print(player_list())

def player_stats(player_name):
    for location_data, team in game_dict().items():
        for players in team['players'].items():
            if players[0] == player_name:
                return players[1]

print(player_stats('Brook Lopez'))

def which_team(team_var):
    player_list = []
    for location_data, team in game_dict().items():
        for players in team['players'].items():
            if team['team_name'] == team_var:
                player_list.append(players[0])
    return player_list

team_1_players = which_team(team_1)
team_2_players = which_team(team_2)

###

def team_colors(team_name):
    for location_data, team in game_dict().items():
        if team['team_name'] == team_name: return team['colors']
    return team_colors

team_colors(team_1)

def team_names():
    team_list = []
    for location_data, team in game_dict().items():
        team_list.append(team['team_name'])
    return team_list
    
team_names()

###

def player_numbers(team_name):
    return [player_stats(player)['number'] for player in which_team(team_name)]
    # return f"{player_name} wears #{player_stats(player_name)['number']}.\n"

print(player_numbers('Brooklyn Nets'))

###

def shoe_size(player_name):
    return player_stats(player_name)['shoe']
    # return f"{player_name} wears a size {player_stats(player_name)['shoe']}.\n"

shoe_size('Brendan Haywood')

###

def num_points_scored(player_name):
    return player_stats(player_name)['points']
    # return f"{player_name} scored {player_stats(player_name)['points']} points.\n"

num_points_scored('Reggie Evans')

###

def big_shoe_rebounds(max_metric, stat):
    max_shoe_list = {}
    for player_name in player_list():
        max_shoe_list[player_name] = player_stats(player_name)[max_metric]
    max_shoe = max(zip(max_shoe_list.values(), max_shoe_list.keys()))
    return player_stats(max_shoe[1])[stat]
    # return f"{max_shoe[1]} has a size {max_shoe[0]} shoe and had {player_stats(max_shoe[1])[stat]} rebounds.\n"
    
big_shoe_rebounds('shoe', 'rebounds')

###

def most_points_scored(max_stat):
    max_stat_list = {}
    for player_name in player_list():
        max_stat_list[player_name] = player_stats(player_name)[max_stat]
    max_points = max(zip(max_stat_list.values(), max_stat_list.keys()))
    return max_points[0]
    # return f"{max_points[1]} scored the most points, with {max_points[0]}.\n"

most_points_scored('points')

###

def winning_team(team1, team2):
    team_1_score = sum([player_stats(player_name)['points'] for player_name in player_list() if player_name in which_team(team_1)])
    team_2_score = sum([player_stats(player_name)['points'] for player_name in player_list() if player_name in which_team(team_2)])
    if team_1_score > team_2_score:
        return team_1
    else:
        return team_2

winning_team(team_1, team_2)

###

def player_with_longest_name(players):
    longest_name, longest_name_count = (None, 0)
    for player in players:
        if len(player) > longest_name_count:
            longest_name, longest_name_count = player, len(player)
    return longest_name

player_with_longest_name(player_list())

###
