from pydantic import BaseModel, ConfigDict
from typing import Optional

class GroupModel(BaseModel):
    id: str
    name: str
    team_id: str

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "Id of the group",
                "name": "Name of the group",
                "team_id": "Team of the group"
            }
        }
    )

class CreateGroupModel(GroupModel):
    id: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "name": "Name of the group",
                "team_id": "Team of the group"
            }
        }
    )

class UpdateGroupModel(GroupModel):
    name: Optional[str] = None
    team_id: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "Id of the group",
                "name": "New name of the group [Optional]"
            }
        }
    )

class DeleteGroupModel(GroupModel):
    name: Optional[str] = None
    team_id: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "Id of the group"
            }
        }
    )