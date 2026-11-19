game_stats = {
    "wins": 0,
    "losses": 0,
    "ties": 0,
}


def total_games():
    return sum(game_stats.values())


def view_stats():
    games = total_games()

    if games == 0:
        print("\nPlease play a game.")
        return games

    win_rate = (game_stats["wins"] / games) * 100

    print(
        f"\nTotal games: {games}\n"
        f"Wins: {game_stats['wins']}\n"
        f"Ties: {game_stats['ties']}\n"
        f"Losses: {game_stats['losses']}\n"
        f"Win rate: {win_rate:.1f}%"
    )

    return games
