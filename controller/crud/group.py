from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select
from models.variable import Variable
from controller.errors.error_handler import error_handler
from controller.errors.database_error import DatabaseError
from models.group import Group

class GroupCrud:
    async def get_all_groups(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            try:
                statement = select(Group).order_by(Group.id)
                groups = await session.execute(statement)
                return groups.scalars().all()
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)

    async def get_group_by_id(self, async_session: async_sessionmaker[AsyncSession], group_id: str):
        async with async_session() as session:
            try:
                statement = select(Group).filter(Group.id == group_id)
                group = await session.execute(statement)
                return group.scalars().one()
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)

    async def get_group_by_name(self, async_session: async_sessionmaker[AsyncSession], group_name: str):
        async with async_session() as session:
            try:
                statement = select(Group).filter(Group.name == group_name)
                group = await session.execute(statement)
                return group.scalars().all()
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)

    async def create_group(self, async_session: async_sessionmaker[AsyncSession], group: Group):
        async with async_session() as session:
            try:
                session.add(group)
                await session.commit()
                return group
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)

    async def update_group(self, async_session: async_sessionmaker[AsyncSession], new_group: dict):
        async with async_session() as session:
            try:
                statement = select(Group).filter(Group.id == new_group['id'])
                group = await session.execute(statement)
                group = group.scalars().one()
                for key in new_group.keys():
                    match key:
                        case 'name':
                            group.name = new_group['name']
                await session.commit()
                return group
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)

    async def delete_group(self, async_session: async_sessionmaker[AsyncSession], group_id: str):
        async with async_session() as session:
            try:
                statement = select(Group).filter(Group.id == group_id)
                group = await session.execute(statement)
                group = group.scalars().one()
                await session.delete(group)
                await session.commit()
                return f"{group} deleted!"
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)