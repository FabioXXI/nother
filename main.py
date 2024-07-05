from fastapi import FastAPI
import routers.group
import routers.team
import routers.variable
from src.objects.variable import VariableObj

app = FastAPI()

app.include_router(routers.team.router)
app.include_router(routers.variable.router)
app.include_router(routers.group.router)

@app.get("/")
def root():
    return "root"

v1 = VariableObj(
    {
        "type": "float",
        "value": "10"
    }
)

v2 = VariableObj(
    {
        "type": "float",
        "value": "20"
    }
)

print(v1 + v2)
print(v1 - v2)
print(v1 * v2)
print(v1 / v2)
print(v1 // v2)
print(v1 % v2)
print(v1 ** v2)