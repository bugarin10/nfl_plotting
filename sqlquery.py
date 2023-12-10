def sqlQuery(c, tab, gameId, playId):

    query = f'SELECT * FROM {tab} gameId = {gameId} AND playId = {playId}'
    
    c.execute(query)
    results = c.fetchall()
    return results