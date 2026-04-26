from fastapi import FastAPI
import psql_forestwatch

app = FastAPI()

@app.post("/resources")
async def add_d(tree_s: bool, fire_s: bool, fire_c: float):
    await psql_forestwatch.post_data(tree_s, fire_s, fire_c)
    return{"status": "Data saved to PostgreSQL!"}

@app.get("/resources")
async def get_resources():
    data = await psql_forestwatch.show_all()    
    return data
