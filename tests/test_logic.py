import logic
from game_data import game_stats

def reset_stats(monkeypatch):
    monkeypatch.setitem(game_stats, "wins", 0)
    monkeypatch.setitem(game_stats, "losses", 0)
    monkeypatch.setitem(game_stats, "ties", 0)
    
def test_player_wins(monkeypatch):
    reset_stats(monkeypatch)
    
    inputs = iter(["rock", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(logic.random, "randrange", lambda _: 2)
    
    logic.rock_paper_scissors()
    
    assert game_stats["wins"] == 1
    
