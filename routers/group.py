from fastapi import APIRouter
from models.group import Group
from controller.crud.group import GroupCrud
from database.session import session
from schemas.group import GroupModel, CreateGroupModel, DeleteGroupModel, UpdateGroupModel

router = APIRouter()
group_crud = GroupCrud()

@router.get("/groups")
async def get_all_groups():
    return await group_crud.get_all_groups(session)

@router.post("/groups")
async def create_group(group: CreateGroupModel):
    group = Group(
        id="1",
        name=group.name,
        team_id=group.team_id
    )
    return await group_crud.create_group(session, group)

@router.put("/groups")
async def update_group(group: UpdateGroupModel):
    group = dict(group)

    return await group_crud.update_group(session, group)

@router.delete("/groups")
async def delete_group(group: DeleteGroupModel):
    return await group_crud.delete_group(session, group.id)