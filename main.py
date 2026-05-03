from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def getPing():
    return {"message" : "This is a health check"}

