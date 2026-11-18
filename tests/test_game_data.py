from src.game_data import game_stats

def test_initial_stats():
    assert game_stats["wins"] == 0
    assert game_stats["losses"] == 0
    assert game_stats["ties"] == 0