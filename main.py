from fastapi import FastAPI
import router.team
import router.variable

app = FastAPI()
app.include_router(router.team.router)
app.include_router(router.variable.router)