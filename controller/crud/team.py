from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select
from models.team import Team
from models.variable import Variable
from controller.errors.error_handler import error_handler
from controller.errors.database_error import DatabaseError

class TeamCrud:
    async def get_all_teams(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            try:
                statement = select(Team).order_by(Team.id)
                teams = await session.execute(statement)
                return teams.scalars().all()
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)

    async def get_team_by_id(self, async_session: async_sessionmaker[AsyncSession], team_id: str):
        async with async_session() as session:
            try:
                statement = select(Team).filter(Team.id == team_id)
                team = await session.execute(statement)
                return team.scalars().one()
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)
        
    async def create_team(self, async_session: async_sessionmaker[AsyncSession], team: Team):
        async with async_session() as session:
            try:
                session.add(team)
                await session.commit()
                return team
            except DatabaseError as database_error:
                await session.rollback()

    async def update_team(self, async_session: async_sessionmaker[AsyncSession], new_team: dict):
        async with async_session() as session:
            try:
                statement = select(Team).filter(Team.id == new_team['id'])
                team = await session.execute(statement)
                team = team.scalars().one()
                for key in new_team.keys():
                    match key:
                        case 'name':
                            team.name = new_team['name']
                await session.commit()
                return team
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)
    
    async def delete_team(self, async_session: async_sessionmaker[AsyncSession], team_id: str):
        async with async_session() as session:
            try:
                statement = select(Team).filter(Team.id == team_id)
                team = await session.execute(statement)
                team = team.scalars().one()
                await session.delete(team)
                await session.commit()
                return f"{team} deleted!"
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)