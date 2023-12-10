import pandas as pd
import plotly.graph_objs as go

# from plotly.grid_objs import Grid, Column
from plotly.offline import plot
import math
import copy

# pathval = sys.argv[1]


def makePlayerShapes(home, away, direction):
    dbs = []
    for i in range(len(home["x"])):
        if (
            home["text"][i] == "FS"
            or home["text"][i] == "SS"
            or home["text"][i] == "CB"
            or home["text"][i] == "S"
        ):
            dbs.append((home["x"][i], home["y"][i], home["text"][i]))
    for i in range(len(away["x"])):
        if (
            away["text"][i] == "FS"
            or away["text"][i] == "SS"
            or away["text"][i] == "CB"
            or away["text"][i] == "S"
        ):
            dbs.append((away["x"][i], away["y"][i], away["text"][i]))
    # print(dbs)

    recs = []
    newthing = sorted(dbs, key=lambda qqq: qqq[1])
    # print(thing)

    t = []
    for lel in newthing:
        to_add = True
        for lel2 in newthing:
            if abs(lel[1] - lel2[1]) < 7.5:
                if direction == "right":
                    if lel[0] < lel2[0]:
                        to_add = False
                else:
                    if lel[0] > lel2[0]:
                        to_add = False
        if to_add:
            t.append(lel)
    thing = sorted(t, key=lambda qqq: qqq[1])

    for i in range(len(thing)):
        if i == 0:
            tnow = thing[i]
            try:
                tnext = thing[i + 1]
            except:
                tnext = None

            if direction == "right":
                if tnext != None:
                    recs.append(
                        (tnow[0] - 2, 0, 120, (tnow[1] + tnext[1]) / 2, tnow[2])
                    )
                else:
                    recs.append((tnow[0] - 2, 0, 120, 54, tnow[2]))
            else:
                if tnext != None:
                    recs.append((tnow[0] + 2, 0, 0, (tnow[1] + tnext[1]) / 2, tnow[2]))
                else:
                    recs.append((tnow[0] - 2, 0, 0, 54, tnow[2]))
        elif i == len(thing) - 1:
            tnow = thing[i]
            tprev = thing[i - 1]
            if direction == "right":
                recs.append((tnow[0] - 2, (tnow[1] + tprev[1]) / 2, 120, 54, tnow[2]))
            else:
                recs.append((tnow[0] + 2, (tnow[1] + tprev[1]) / 2, 0, 54, tnow[2]))
        else:
            tnow = thing[i]
            tprev = thing[i - 1]
            tnext = thing[i + 1]
            if direction == "right":
                recs.append(
                    (
                        tnow[0] - 2,
                        (tnow[1] + tprev[1]) / 2,
                        120,
                        (tnow[1] + tnext[1]) / 2,
                        tnow[2],
                    )
                )
            else:
                recs.append(
                    (
                        tnow[0] + 2,
                        (tnow[1] + tprev[1]) / 2,
                        0,
                        (tnow[1] + tnext[1]) / 2,
                        tnow[2],
                    )
                )

    shapes = []
    for x in recs:
        # print(x[4])
        color = "rgb(127,187,34)" if "S" in x[4] else "rgb(187,34,127)"
        rect = {
            "type": "rect",
            "layer": "below",
            "x0": x[0],
            "y0": x[1],
            "x1": x[2],
            "y1": x[3],
            "line": {"color": "rgba(0,0,0,1)", "width": 1},
            "fillcolor": color,
        }
        shapes.append(rect)
    return shapes


def g(plays_df, games_df, player_info, game_df, gameId, playId):
    midpoint_trace = go.Scatter(x=[60], y=[53.3 / 2])
    outer_shape = {
        "type": "rect",
        "layer": "below",
        "x0": 0,
        "y0": 0,
        "x1": 120,
        "y1": 53.3,
        "line": {"color": "rgba(0,0,0,1)", "width": 1},
        "fillcolor": "rgb(61,204,132)",
    }

    left_goal = {
        "type": "rect",
        "layer": "below",
        "x0": 0,
        "y0": 0,
        "x1": 10,
        "y1": 53.3,
        "line": {"color": "rgba(0,0,0,1)", "width": 1},
        "fillcolor": "rgb(0,0,127)",
    }

    right_goal = {
        "type": "rect",
        "layer": "below",
        "x0": 110,
        "y0": 0,
        "x1": 120,
        "y1": 53.3,
        "line": {"color": "rgba(0,0,0,1)", "width": 1},
        "fillcolor": "rgb(0,0,127)",
    }

    _shapes = [
        outer_shape,
        left_goal,
        right_goal,
    ]

    for x in range(1, 13):
        temp_shape = {
            "type": "rect",
            "layer": "below",
            "x0": x * 10,
            "y0": 0,
            "x1": x * 10,
            "y1": 53.3,
            "line": {"color": "rgba(0,0,0,1)", "width": 1},
        }
        _shapes.append(temp_shape)

    layout = go.Layout(
        title="Football Field",
        shapes=_shapes,
    )
    xs = []
    ys = []
    ts = []
    for i in range(1, 10):
        x = (i + 1) * 10 - 1
        xs.append(x)
        y = 10
        ys.append(y)
        tt = i if i < 5 else 10 - i
        ts.append(tt)

        x = (i + 1) * 10 + 1
        xs.append(x)
        y = 10
        ys.append(y)
        ts.append(0)

    yardlabels = go.Scatter(
        x=xs,
        y=ys,
        mode="text",
        name="Lines, Markers and Text",
        text=ts,
    )

    # play = plays_df.iloc[int(PLAYVAL)]
    # kk1 = int(input("Enter gameId \n"))
    # kk2 = int(input("Enter playId \n"))
    play = plays_df[
        (plays_df["gameId"] == gameId) & (plays_df["playId"] == playId)
    ].iloc[0]
    # print(play)

    # playId = play['playId']
    # gameId = play['gameId']
    # bigLos = play['LOS']
    gameInfo = games_df.query("gameId == %s" % gameId)
    trackingfilename = (
        "data/tracking_week_1.parquet"  #'tracking_gameId_' + str(gameId) + '.csv'
    )

    game_df = pd.read_parquet(trackingfilename)
    game_play_df = game_df.query("(playId == @playId) & (gameId == @gameId)")
    direction = game_play_df["playDirection"].iloc[0]  #'GOING RIGHT'
    print(game_play_df["event"].unique())

    sett = set()

    play_info = {}
    lastname = ""
    playlengthframes = game_play_df["frameId"].max()

    game_play_df["frameId"].value_counts()

    home_team = gameInfo["homeTeamAbbr"].iloc[0]
    away_team = gameInfo["visitorTeamAbbr"].iloc[0]

    layout = {
        "xaxis": {
            "range": [0, 120],
            "autorange": False,
            "showgrid": False,
            "showticklabels": False,
        },
        "yaxis": {
            "range": [0, 53.3],
            "autorange": False,
            "showgrid": False,
            "showticklabels": False,
        },
        "title": "GameID "
        + str(gameId)
        + ", PlayID "
        + str(playId)
        + "\n"
        + play["playDescription"],
        #'shapes': _shapes,
        "updatemenus": [
            {
                "type": "buttons",
                "buttons": [
                    {
                        "label": "Play",
                        "method": "animate",
                        "args": [
                            None,
                            {
                                "frame": {"redraw": True, "duration": 100},
                                "fromcurrent": True,
                            },
                        ],
                    },
                    {
                        "args": [
                            [None],
                            {
                                "frame": {"duration": 75, "redraw": True},
                                "mode": "immediate",
                                "transition": {"duration": 0},
                            },
                        ],
                        "label": "Pause",
                        "method": "animate",
                    },
                ],
            }
        ],
    }

    for x in range(len(game_play_df)):
        try:
            playerInfo = player_info[
                player_info["nflId"] == game_play_df.iloc[x]["nflId"]
            ].iloc[0]
        except:
            playerInfo = player_info[
                player_info["nflId"] == game_play_df.iloc[0]["nflId"]
            ].iloc[0]

        currname = game_play_df.iloc[x]["displayName"]
        # print(game_play_df.iloc[x]['team'])
        if currname == lastname:
            play_info[currname].append(
                (
                    game_play_df.iloc[x]["x"],
                    game_play_df.iloc[x]["y"],
                    game_play_df.iloc[x]["club"],
                    game_play_df.iloc[x]["jerseyNumber"],
                    game_play_df.iloc[x]["event"],
                    playerInfo["position"],
                )
            )
        else:
            # if(lastname != ''):
            #   playlengthframes = len(play_info[lastname])
            play_info[currname] = [
                (
                    game_play_df.iloc[x]["x"],
                    game_play_df.iloc[x]["y"],
                    game_play_df.iloc[x]["club"],
                    game_play_df.iloc[x]["jerseyNumber"],
                    game_play_df.iloc[x]["event"],
                    playerInfo["position"],
                )
            ]

        lastname = currname

    los = None
    frames = []
    ball_thrown = False

    # print(len(play_info["A'Shawn Robinson"]))

    for c in range(playlengthframes):
        frame = {"data": [], "name": c}
        home = {"x": [], "y": [], "text": []}
        away = {"x": [], "y": [], "text": []}
        ball = {"x": [], "y": [], "text": []}
        frameInfo = {"x": [], "y": [], "text": []}
        checkevent = False
        player_shapes = []

        for p in sorted(play_info):
            if checkevent == False:
                try:
                    b = math.isnan(play_info[f"{p}"][c][4])
                except:
                    b = False
                if b:
                    frameInfo["x"].append(85)
                    frameInfo["y"].append(8)
                    frameInfo["text"].append("Frame %s" % c)
                    frameInfo["mode"] = "text"
                    frameInfo["name"] = "frameInfo"
                    frameInfo["textfont"] = dict(size=15, color="#ffffff")
                else:
                    if play_info[p][c][4] == "pass_forward":
                        print("BALL THROWN")
                        ball_thrown = True
                    frameInfo["x"].append(85)
                    frameInfo["y"].append(8)
                    frameInfo["text"].append(play_info[p][c][4])
                    frameInfo["mode"] = "text"
                    frameInfo["textfont"] = dict(size=10, color="#ffffff")
                checkEvent = True
            if play_info[p][c][2] == home_team:
                home["x"].append(play_info[p][c][0])
                home["y"].append(play_info[p][c][1])
                home["text"].append(int(play_info[p][c][3]))
                home["mode"] = "markers+text"
                home["marker"] = {"color": "blue", "size": 20}
                home["name"] = home_team
                home["textfont"] = dict(size=10, color="#ffffff")
            elif play_info[p][c][2] == away_team:
                away["x"].append(play_info[p][c][0])
                away["y"].append(play_info[p][c][1])
                away["text"].append(int(play_info[p][c][3]))
                away["mode"] = "markers+text"
                away["name"] = away_team
                away["marker"] = {"color": "red", "size": 20}
                away["textfont"] = dict(size=10, color="#ffffff")

            else:
                if los == None:
                    los = (play_info[p][c][0], play_info[p][c][1])
                ball["x"].append(play_info[p][c][0])
                ball["y"].append(play_info[p][c][1])
                ball["mode"] = "markers"
                ball["marker"] = {"color": "brown", "size": 10}
                ball["name"] = "Ball"

        ball_thrown = True
        if not ball_thrown:
            player_shapes = makePlayerShapes(home, away, direction)
        else:
            player_shapes = []

        # defense_Zones = makeDefenseZones(bigLos, direction,4,4)
        tempshapes = copy.deepcopy(_shapes)
        tempshapes.extend(player_shapes)
        # tempshapes.extend(defense_Zones)
        # layout['shapes'] = tempshapes
        frame = {"data": [home, away, ball], "layout": {"shapes": tempshapes}}
        frames.append(frame)

    # print(los)

    figure = {
        "layout": layout,
        "frames": frames,
        "data": [
            {"x": [1], "y": [1]},
            {"x": [1], "y": [1]},
            {"x": [1], "y": [1]},
            yardlabels,
        ]
        #'data' : [yardlabels]
    }

    # plot(figure)
    return figure


if __name__ == "__main__":
    plays_df = pd.read_csv("plays.csv")
    games_df = pd.read_csv("games.csv")
    player_info = pd.read_csv("players.csv")
    game_df = pd.read_parquet("tracking_week_1.parquet")

    opts = [x for x in range(len(plays_df))]
    fig = g(plays_df, games_df, player_info, game_df)
    print(plot(fig, include_plotlyjs=False, output_type="div"))
