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

def player_list():
    team_list = []
    for location_data, team in game_dict().items():
        for players in team['players'].items():
            team_list.append(players[0])
    return team_list

def player_stats(player_name):
    for location_data, team in game_dict().items():
        for players in team['players'].items():
            if players[0] == player_name:
                return players[1]

###

def team_colors(team_name):
    for location_data, team in game_dict().items():
        if team['team_name'] == team_name: return team['colors']
        
print(team_colors("Brooklyn Nets"),"\n")

def team_names():
    team_list = []
    for location_data, team in game_dict().items():
        team_list.append(team['team_name'])
    return team_list
    
print(team_names(),"\n")

###

def player_numbers(player_name):
    return f"{player_name} wears #{player_stats(player_name)['number']}.\n"

print(player_numbers('Jason Terry'))

###

def shoe_size(player_name):
    return f"{player_name} wears a size {player_stats(player_name)['shoe']}.\n"

print(shoe_size('Brendan Haywood'))

###

def num_points_scored(player_name):
    return f"{player_name} scored {player_stats(player_name)['points']} points.\n"

print(num_points_scored('Reggie Evans'))

###

def big_shoe_rebounds(max_metric, stat):
    max_shoe_list = {}
    for player_name in player_list():
        max_shoe_list[player_name] = player_stats(player_name)[max_metric]
    max_shoe = max(zip(max_shoe_list.values(), max_shoe_list.keys()))
    return f"{max_shoe[1]} has a size {max_shoe[0]} shoe and had {player_stats(max_shoe[1])[stat]} rebounds.\n"
    
print(big_shoe_rebounds('shoe', 'rebounds'))

###

def most_points_scored(max_stat):
    max_stat_list = {}
    for player_name in player_list():
        max_stat_list[player_name] = player_stats(player_name)[max_stat]
    max_points = max(zip(max_stat_list.values(), max_stat_list.keys()))
    return f"{max_points[1]} scored the most points, with {max_points[0]}.\n"

print(most_points_scored('points'))