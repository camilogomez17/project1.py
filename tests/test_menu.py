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
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    calls = []
    monkeypatch.setattr(
        menu,
        "view_stats",
        lambda: calls.append("viewed")
    )
    
    menu.show_menu()
    
    assert calls == ["viewed"]

def test_exit(monkeypatch):
    inputs = iter(["3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    menu.show_menu()

def test_invalid_menu_option(monkeypatch, capsys):
    inputs = iter(["invalid", "3"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    
    menu.show_menu()
    
    output = capsys.readouterr().out
    
    assert "Invalid choice" in output

def test_menu_persistence():
    return None