from fastapi import FastAPI
import routers.group
import routers.team
import routers.variable

app = FastAPI()

app.include_router(routers.team.router)
app.include_router(routers.variable.router)
app.include_router(routers.group.router)

@app.get("/")
def root():
    return "root"