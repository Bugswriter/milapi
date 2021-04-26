from fastapi import FastAPI
from databases import Database
from typing import Optional

app = FastAPI()

database = Database("sqlite:///site.db")

@app.on_event("startup")
async def database_connect():
  await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
  await database.disconnect()


@app.get("/data/{data_id}")
async def read_data(data_id):
  q = "SELECT * FROM data WHERE id={}".format(int(data_id))
  res = await database.fetch_all(query=q)
  return res


@app.get("/data")
async def read_data_from_code(code: str):
  q = "SELECT * FROM data WHERE code='{}'".format(str(code))
  res = await database.fetch_all(query=q)
  return res 

