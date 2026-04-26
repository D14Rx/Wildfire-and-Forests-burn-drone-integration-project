from fastapi import FastAPI
import psql_forestwatch

app = FastAPI()

@app.post("/resources")
async def add_d(tree_s: bool, fire_s: bool, fire_c: float):
    psql_forestwatch.post_data()
    return{"status": "received"}

@app.get("/resources")
def get_resources():
    data = psql_forestwatch.show_all()    
    return data