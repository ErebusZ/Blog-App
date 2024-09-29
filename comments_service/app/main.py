from fastapi import FastAPI


from app.api import db

db.metadata.create_all(db.engine)

app = FastAPI()

@app.on_event("startup")
async def startup():
    await db.database.connect()

@app.on_event("shutdown")
async def shutdown():
    await db.database.disconnect()


