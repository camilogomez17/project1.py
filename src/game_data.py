game_stats = {
    "wins": 0,
    "losses": 0,
    "ties": 0,
}

total_games = game_stats[0 + 1 + 2]

win_rate = (game_stats[0] / total_games) * 100

def view_stats():
    print(game_stats)