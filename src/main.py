from fastapi import FastAPI
from platform_manager.router import router as router_hivecore
# from docker.router import router as router_docker
from aredis_om import Migrator

app = FastAPI()

app.include_router(router_hivecore)


@app.get('/')
async def home():
    return 'home'


@app.on_event("startup")
async def startup():
    await Migrator().run()
