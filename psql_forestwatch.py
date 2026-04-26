import psycopg2
from psycopg2.extras import DictCursor

async def get_connect():
    return psycopg2.connect(
        database = "test_db", 
        user = "postgres",
        password = "diar2011",
        host = "127.0.0.1",
        port = 8000
    )

async def post_data(tree_s, fire_s, fire_c, time):
    query = "INSERT INTO forest_d(tree_spoted, fire_spotted, fire_chance, detected_at)VALUES(%s, %s, %s, CURRENT_TIMESTAMP)"
    with get_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (tree_s, fire_s, fire_c, time))
            conn.comit()

async def show_all():
    with get_connect() as conn:
        with conn.cursor(cursor_factory=DictCursor) as cursor:
            cursor.execute("SELECT * FROM forest_d")
            return cursor.fetchall() 

async def update_forest_status(tree_id, status: bool):
    query = "UPDATE forest_d SET tree_s =%s WHERE id =%s"
    with get_connect() as conn:
        with conn.cursor() as cursor:
            cursor.execute(query, (status, tree_id))
            conn.comit()