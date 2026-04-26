import asyncpg

async def post_data(tree_s, fire_s, fire_c):
    conn = await asyncpg.connect(
        database = "test_db", 
        user = "postgres",
        password = "diar2011",
        host = "127.0.0.1",
        port = 8000
    )

    query = """INSERT INTO forest_d(tree_spoted, fire_spotted, fire_chance, detected_at)
                VALUES($1, $2, $3, CURRENT_TIMESTAMP)"""
    
    await conn.execute(query, tree_s, fire_s, fire_c)
    await conn.close()

async def show_all():
    conn = await asyncpg.connect(
        database="test_db", user="postgres", password="diar2011", host="127.0.0.1", port=8000
    )
    #rows - A horizonal interaction in PSQL tables like with lists function 
    rows = await conn.fetch("SELECT * FROM forest_d") #fetch() returning data in dict looking format
    await conn.close()
    return rows
