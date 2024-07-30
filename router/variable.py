from fastapi import APIRouter, status, Depends
from router.authorization import verify_data_access_token, verify_team_access_token
from controller.crud.variable import VariableCrud
from database.session import session
from schemas.variable import CreateVariableModel, GetVariableInfoModel, UpdateVariableModel
from models.variable import Variable
from uuid import uuid4
from controller.src.variable import encode_variable_name, decode_variable_name
from controller.crud.team import TeamCrud
from controller.validators.variable import VariableValidator
from schemas.variable import DeleteVariableModel

router = APIRouter()
variable_crud = VariableCrud()
team_crud = TeamCrud()
@router.post('/variable/info', status_code=status.HTTP_200_OK, dependencies=[Depends(verify_data_access_token)])
async def get_variable_info(variable: GetVariableInfoModel, team_access_id: str = Depends(verify_data_access_token)):
    variable = await variable_crud.get_variable_by_name(session, encode_variable_name(variable.name, team_access_id))
    return {'name': decode_variable_name(variable.name), 'type': variable.type, 'value': variable.value}

@router.post('/variable/create', status_code=status.HTTP_201_CREATED, dependencies=[Depends(verify_team_access_token)])
async def create_variable(variable_data: CreateVariableModel, team: dict = Depends(verify_team_access_token)):
    variable = Variable()
    VariableValidator(dict(variable_data))
    variable.id = str(uuid4())
    variable.name = encode_variable_name(variable_data.name, team['access_id'])
    variable.type = variable_data.type
    variable.value = variable_data.value
    variable.team_access_id = team['access_id']
    variable = await variable_crud.create_variable(session, variable)
    return {'name': decode_variable_name(variable.name), 'type': variable.type, 'value': variable.value}

@router.put('/variable/update/{variable_name}', status_code=status.HTTP_200_OK, dependencies=[Depends(verify_team_access_token)])
async def update_variable(variable_name: str, variable_data: UpdateVariableModel, team: dict = Depends(verify_team_access_token)):
    variable_data = dict(variable_data)
    VariableValidator(variable_data)
    variable = await variable_crud.get_variable_by_name(session, encode_variable_name(variable_name, team['access_id']))
    variable_data['id'] = variable.id
    variable_data['name'] = encode_variable_name(variable_data['name'], team['access_id'])
    variable = await variable_crud.update_variable(session, variable_data)
    variable.name = decode_variable_name(variable.name)
    return variable

@router.delete('/variable/delete', status_code=status.HTTP_200_OK, dependencies=[Depends(verify_team_access_token)])
async def delete_variable(variable: DeleteVariableModel, team: dict = Depends(verify_team_access_token)):
    variable_name = encode_variable_name(variable.name, team['access_id'])
    variable = await variable_crud.get_variable_by_name(session, variable_name)
    return await variable_crud.delete_variable(session, variable)