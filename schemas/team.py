from pydantic import BaseModel

class TeamModel(BaseModel):
    id: str
    name: str
    data_access_token: str

class CreateTeamModel(BaseModel):
    name: str

class DeleteTeamModel(BaseModel):
    pass

class UpdateTeamModel(BaseModel):
    name: str