from fastapi import FastAPI
import uvicorn

APP = FastAPI()

@APP.get("/")
async def root():
    return {"message": "Hello World"}


if __name__ == "__main__":
    uvicorn.run("service.__main__:APP", host="0.0.0.0", port=8080)
