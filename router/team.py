from fastapi import APIRouter, status, Depends
from schemas.team import CreateTeamModel, UpdateTeamModel
from router.authorization import verify_team_access_token
from database.session import session
from controller.crud.team import TeamCrud
from models.team import Team
from uuid import uuid4
from controller.auth import jwt

router = APIRouter()
team_crud = TeamCrud()
@router.post('/team/create', status_code=status.HTTP_201_CREATED)
async def create_team(team_data: CreateTeamModel):
    team = Team(
        id = str(uuid4()),
        name = team_data.name,
        access_id = str(uuid4())
    )
    team.data_access_token = jwt.create_access_token(team.access_id)
    access_token = jwt.create_access_token(team.id, team.access_id)
    team = await team_crud.create_team(session, team)
    return {"name": team.name, "data_access_token": team.data_access_token, "access_token": access_token}

@router.get('/team/info', status_code=status.HTTP_200_OK, dependencies=[Depends(verify_team_access_token)])
async def get_team_info(team: dict = Depends(verify_team_access_token)):
    team = await team_crud.get_team_by_id(session, team['id'])
    return {'name': team.name, "data_access_token": team.data_access_token}

@router.put('/team/update', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(verify_team_access_token)])
async def update_team(team_data: UpdateTeamModel, team: dict = Depends(verify_team_access_token)):
    team_data = dict(team_data)
    team_data['id'] = team['id']
    team = await team_crud.update_team(session, team_data)
    return {'name': team.name}
@router.delete('/team/delete', status_code=status.HTTP_204_NO_CONTENT, dependencies=[Depends(verify_team_access_token)])
async def delete_team(team: dict = Depends(verify_team_access_token)):
    return await team_crud.delete_team_by_id(session, team['id'])