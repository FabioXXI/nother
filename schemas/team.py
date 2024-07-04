from pydantic import BaseModel, ConfigDict
from typing import Optional

class TeamModel(BaseModel):
    id: str
    name: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "uuid4",
                "name": "name of the team"
            }
        }
    )

class CreateTeamModel(TeamModel):
    pass

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "uuid4",
                "name": "name of the team"
            }
        }
    )

class UpdateTeamModel(TeamModel):
    name: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "id of the team",
                "name": "new name of the team [Optional]"
            }
        }
    )

class DeleteTeamModel(TeamModel):
    name: Optional[str] = None
    
    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "id of the team"
            }
        }
    )