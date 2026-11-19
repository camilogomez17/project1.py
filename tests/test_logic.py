import logic
from game_data import game_stats, total_games


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

    logic.rock_paper_scissors()

    assert game_stats["losses"] == 1


def test_draw(monkeypatch):
    reset_stats(monkeypatch)

    inputs = iter(["rock", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(logic.random, "randrange", lambda _: 0)

    logic.rock_paper_scissors()

    assert game_stats["ties"] == 1


def test_random_pc_choice(monkeypatch, capsys):
    reset_stats(monkeypatch)

    inputs = iter(["rock", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    def fake_random(stop):
        assert stop == 3
        return 2

    monkeypatch.setattr(logic.random, "randrange", fake_random)

    logic.rock_paper_scissors()

    assert "Computer chose scissors" in capsys.readouterr().out


def test_invalid_player_input(monkeypatch, capsys):
    reset_stats(monkeypatch)

    inputs = iter(["lizard", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    logic.rock_paper_scissors()

    assert "move is invalid" in capsys.readouterr().out
    assert total_games() == 0


def test_case_insensitive_input(monkeypatch):
    reset_stats(monkeypatch)

    inputs = iter(["ROCK", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(logic.random, "randrange", lambda _: 2)

    logic.rock_paper_scissors()

    assert game_stats["wins"] == 1


def test_whitespace_handling(monkeypatch):
    reset_stats(monkeypatch)

    inputs = iter([" rock ", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(logic.random, "randrange", lambda _: 2)

    logic.rock_paper_scissors()

    assert game_stats["wins"] == 1


def test_quit_command(monkeypatch):
    reset_stats(monkeypatch)

    inputs = iter(["quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    def unexpected_random_call(stop):
        raise AssertionError("Random selection should not happen")

    monkeypatch.setattr(logic.random, "randrange", unexpected_random_call)

    logic.rock_paper_scissors()

    assert total_games() == 0


def test_statistics_update(monkeypatch):
    reset_stats(monkeypatch)

    inputs = iter(["rock", "quit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))
    monkeypatch.setattr(logic.random, "randrange", lambda _: 2)

    logic.rock_paper_scissors()

    assert game_stats["wins"] == 1
