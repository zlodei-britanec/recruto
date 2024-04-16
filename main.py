from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def testovoe(recruto: str, message: str):
    return {"message": f"Hello {recruto}! {message}!"}