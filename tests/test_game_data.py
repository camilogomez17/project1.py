from game_data import game_stats, total_games, view_stats


def test_initial_stats():
    assert game_stats == {"wins": 0, "losses": 0, "ties": 0}


def test_total_games(monkeypatch):
    monkeypatch.setitem(game_stats, "wins", 3)
    monkeypatch.setitem(game_stats, "losses", 2)
    monkeypatch.setitem(game_stats, "ties", 1)

    assert total_games() == 6


def test_view_stats(monkeypatch, capsys):
    monkeypatch.setitem(game_stats, "wins", 3)
    monkeypatch.setitem(game_stats, "losses", 2)
    monkeypatch.setitem(game_stats, "ties", 1)

    view_stats()

    output = capsys.readouterr().out

    assert "Total games: 6" in output
    assert "Wins: 3" in output
    assert "Ties: 1" in output
    assert "Losses: 2" in output


def test_win_rate(monkeypatch, capsys):
    monkeypatch.setitem(game_stats, "wins", 3)
    monkeypatch.setitem(game_stats, "losses", 2)
    monkeypatch.setitem(game_stats, "ties", 1)

    view_stats()

    assert "Win rate: 50.0%" in capsys.readouterr().out


def test_zero_games(monkeypatch, capsys):
    monkeypatch.setitem(game_stats, "wins", 0)
    monkeypatch.setitem(game_stats, "losses", 0)
    monkeypatch.setitem(game_stats, "ties", 0)

    view_stats()

    assert "Please play a game." in capsys.readouterr().out


def test_stats_update(monkeypatch, capsys):
    monkeypatch.setitem(game_stats, "wins", 2)
    monkeypatch.setitem(game_stats, "losses", 1)
    monkeypatch.setitem(game_stats, "ties", 0)

    view_stats()

    output = capsys.readouterr().out

    assert "Total games: 3" in output
    assert "Wins: 2" in output
