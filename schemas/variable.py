from pydantic import BaseModel, ConfigDict
from typing import Optional

class VariableModel(BaseModel):
    id: str
    name: str
    team_id: str
    type: str
    value: str
    group: Optional[str] = None
    point_to: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "Id of the variable",
                "name": "Name of the variable",
                "team_id": "Team of the variable",
                "type": "Type of the variable [String | Float]",
                "value": "Value of the type of the variable",
                "group": "Group of the variable",
                "point_to": "Relational variable of the variable"
            }
        }
    )

class CreateVariableModel(VariableModel):
    id: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "name": "Name of the variable",
                "team_id": "Team of the variable",
                "type": "Type of the variable [String | Float]",
                "value": "Value of the type of the variable",
                "group": "Group of the variable [Optional]",
                "point_to": "Relational variable of the variable [Optional]"
            }
        }
    )

class UpdateVariableModel(VariableModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    team_id: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "Id of the variable",
                "name": "Name of the variable [Optional]",
                "type": "Type of the variable [String | Float] [Optional]",
                "value": "Value of the type of the variable [Optional]",
                "group": "Group of the variable [Optional]",
                "point_to": "Relational variable of the variable [Optional]"
            }
        }
    )

class DeleteVariableModel(VariableModel):
    name: Optional[str] = None
    type: Optional[str] = None
    value: Optional[str] = None
    team_id: Optional[str] = None

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "id": "Id of the variable"
            }
        }
    )