from fastapi import APIRouter
from models.variable import Variable
from controller.crud.variable import VariableCrud
from database.session import session
from schemas.variable import VariableModel, DeleteVariableModel, CreateVariableModel, UpdateVariableModel

router = APIRouter()
variable_crud = VariableCrud()

@router.get("/variables")
async def get_all_variables():
    return await variable_crud.get_all_variables(session)

@router.post("/variables")
async def create_variable(variable: CreateVariableModel):
    variable = Variable(
        id="1",
        name=variable.name,
        type=variable.type,
        value=variable.value,
        team_id=variable.team_id,
        group=variable.group,
        point_to=variable.point_to
    )
    return await variable_crud.create_variable(session, variable)

@router.put("/variables")
async def update_variable(new_variable: UpdateVariableModel):
    new_variable = dict(new_variable)

    return await variable_crud.update_variable(session, new_variable)

@router.delete("/variables")
async def delete_variable(variable: DeleteVariableModel):
    return await variable_crud.delete_variable(session, variable.id)