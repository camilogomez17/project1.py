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
    
    
def test_computer_wins(monkeypatch):
    reset_stats(monkeypatch)
    
    inputs = iter(["rock", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(logic.random, "randrange", lambda _: 1)
    
    logic.rock_paper_scissor()
    
    assert game_stats["losses"] == 1
    
def test_draw(monkeypatch):
    reset_stats(monkeypatch)
    
    inputs = iter(["rock", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(logic.random, "randrange", lambda _: 0)
    
    logic.rock_paper_scissors()
    
    assert game_stats["ties"] == 1