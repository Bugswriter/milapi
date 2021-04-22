from fastapi import FastAPI
from databases import Database

app = FastAPI()

database = Database("sqlite:///site.db")

@app.on_event("startup")
async def database_connect():
  await database.connect()


@app.on_event("shutdown")
async def database_disconnect():
  await database.disconnect()

@app.get("/")
async def root(id: int):
  query = "SELECT * FROM data WHERE ID={}".format(str(id))
  results = await database.fetch_all(query=query)
  return  results

