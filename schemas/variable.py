from pydantic import BaseModel

class VariableModel(BaseModel):
    id: str
    name: str
    type: str
    value: str

class CreateVariableModel(BaseModel):
    name: str
    type: str
    value: str

class UpdateVariableModel(BaseModel):
    name: str = None
    type: str
    value: str

class DeleteVariableModel(BaseModel):
    name: str

class GetVariableInfoModel(BaseModel):
    name: str