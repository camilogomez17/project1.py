import menu

def test_play_option(monkeypatch):
    inputs = iter(["1", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    calls = []
    monkeypatch.setattr(
        menu,
        "rock_paper_scissors",
        lambda: calls.append("played")
    )
    
    menu.show_menu()
    
    assert calls == ["played"]

def test_view_stats(monkeypatch):
    inputs = iter(["2", "3"])
    

def test_exit():
    return None

def test_invalid_menu_option():
    return None

def test_menu_persistence():
    return None