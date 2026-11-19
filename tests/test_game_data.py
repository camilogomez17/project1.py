from src.game_data import game_stats
from src.game_data import total_games

def test_initial_stats():
    assert game_stats["wins"] == 0
    assert game_stats["losses"] == 0
    assert game_stats["ties"] == 0
    
def test_total_games():
    assert total_games == 0
    
def test_initial_game_stats():
    return None

def test_total_games():
    return None

def test_view_stats():
    return None

def test_win_rate():
    return None

def test_zero_games():
    return None

def test_stats_update():
    return None