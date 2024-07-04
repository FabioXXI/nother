from fastapi import APIRouter
from models.team import Team
from models.variable import Variable
from controller.crud.team import TeamCrud
from database.session import session
from schemas.team import CreateTeamModel, TeamModel, DeleteTeamModel, UpdateTeamModel

team_crud = TeamCrud()
router = APIRouter()

@router.get("/team")
async def get_teams():
    return await team_crud.get_all_teams(session)

@router.post("/team")
async def create_team(team: CreateTeamModel):
    team = Team(
        id=team.id,
        name=team.name
    )

    return await team_crud.create_team(session, team)

@router.put("/team")
async def update_team(team: UpdateTeamModel):
    team = dict(team)
    team['id'] = team['id']

    return await team_crud.update_team(session, team)

@router.delete("/team")
async def delete_team(team: DeleteTeamModel):
    return await team_crud.delete_team(session, team.id)