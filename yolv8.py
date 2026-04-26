from ultralytics import YOLO
from fastapi import FastAPI
import os
from pathlib import Path
import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from datetime import datetime
from watchdog import observers
from watchdog.events import FileSystemEventHandler

engine = create_async_engine('postgresql+asyncpg://postgres:diar2011@localhost:8000/test_db')

new_session = async_sessionmaker(engine, expire_on_commit=False)

async def get_session():
    async with new_session() as session:
        yield session

class Base(DeclarativeBase):
    pass

class TreeModel(Base):
    __tablename__ = "trees"

    id: Mapped[int] = mapped_column(primary_key=True)
    tree_spoted: Mapped[bool]
    fire_spoted: Mapped[bool]
    fire_chance: Mapped[float]
    detected_at: Mapped[datetime]

async def setup_database():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


model = YOLO("yolov8n.pt")
app = FastAPI()

@app.post("/resources")
async def add_d():

    path = Path("../yolo8/runs/detect/predict*/labels/test_tree.txt")
    all_files = list(Path("../yolo8/runs/detect/").glob("predict*/labels/test_tree.txt"))

    if all_files:
        print(all_files[-1].read_text())

        lines = all_files[-1].read_text().splitlines()

        tree_found = False
        fire_found = False
        chance = 0.0

        for line in lines:
            num_id = line.split()[0]
            print(num_id)

            if num_id == "0":
                tree_found = True
            if num_id == "1":
                fire_found = True

        for line in lines:
            num_c = line.split()[5]
            chance = float(num_c)
            print(f"chance: {chance:.2f}")

        if tree_found:
            print("Tree spotted")
        if fire_found:
            print(f"Fire detected, Fire percentage: {chance:.2f}")
        else:
            print("No detections")

    else:
        print("No files")

async def main():
    print("Preparing data base...")
    await setup_database()

    print("Analyzing")
    await add_d()

if __name__ == "__main__":
    asyncio.run(main())  