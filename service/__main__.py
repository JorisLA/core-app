from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from service.layers.api.player_api import router as player_router
from service.layers.api.team_api import router as team_router
from service.layers.api.fine_api import router as fine_router

APP = FastAPI()

@APP.get("/")
async def root():
    return {"message": "Hello World"}

# Include routers
APP.include_router(player_router, prefix="/players", tags=["players"])
APP.include_router(team_router, prefix="/teams", tags=["teams"])
APP.include_router(fine_router, prefix="/fines", tags=["fines"])

origins = [
    "http://localhost:*",
]

APP.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

if __name__ == "__main__":
    uvicorn.run("service.__main__:APP", host="0.0.0.0", port=8888, reload=True)
