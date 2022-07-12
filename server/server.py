from fastapi import FastAPI

app = FastAPI()


@app.get("/api/cases")
async def get_cases():
    return {"message": "Hello World"}
