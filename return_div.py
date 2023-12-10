import sys
import pandas as pd
from sqlconn import sqlConnect, sqlQuery
from animate_vals import g
from plotly.offline import plot


def return_div(playId):
    gameId = 2022090800

    playId = int(playId)

    cursor, status = sqlConnect()

    if status != "Success":
        print("Error Occurred. Check error_log.txt.")
        sys.exit()
    else:
        print("Success")

    all_plays = sqlQuery(cursor, "nfl_la_vs_buf_2023", str(gameId))
    column_names = [desc[0] for desc in cursor.description]
    all_plays_df = pd.DataFrame(all_plays, columns=column_names)

    # Map user input to play ID - return None if not a valid input
    play_list = [play for play in all_plays_df["playId"].unique()]
    user_input = [i for i in range(1, len(play_list) + 1)]
    mapped_input = dict(zip(user_input, play_list))
    if int(playId) in mapped_input.keys():
        playId = mapped_input[int(playId)]
    else:
        return None

    game_play = sqlQuery(cursor, "nfl_la_vs_buf_2023", str(gameId), str(playId))
    column_names = [desc[0] for desc in cursor.description]
    game_play_df = pd.DataFrame(game_play, columns=column_names)

    games = sqlQuery(cursor, "nfl_games_2023", gameId)
    column_names = [desc[0] for desc in cursor.description]
    games_df = pd.DataFrame(games, columns=column_names)

    plays = sqlQuery(cursor, "nflplays", gameId, playId)
    column_names = [desc[0] for desc in cursor.description]
    plays_df = pd.DataFrame(plays, columns=column_names)

    player_info = sqlQuery(cursor, "nfl_players_2023")
    column_names = [desc[0] for desc in cursor.description]
    player_info_df = pd.DataFrame(player_info, columns=column_names)

    # Comment this out when connection to databricks is secured
    # plays_df = pd.read_csv("data/plays.csv")

    # games_df = pd.read_csv("data/games.csv")

    # player_info_df = pd.read_csv("data/players.csv")

    # game_play_df = pd.read_parquet("data/tracking_week_1.parquet")

    fig = g(plays_df, games_df, player_info_df, game_play_df, gameId, playId)

    return plot(fig, include_plotlyjs=False, output_type="div")


if __name__ == "__main__":
    print(return_div(1))
