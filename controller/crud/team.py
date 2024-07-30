from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from models.team import Team
from models.variable import Variable
from controller.errors.http.http_exceptions import internal_server_error, not_found

class TeamCrud:
    async def get_team_by_name(self, async_session: async_sessionmaker[AsyncSession], team_name: str):
        async with async_session() as session:
            try:
                statement = select(Team).filter(Team.name == team_name)
                team = await session.execute(statement)
                return team.scalars().one()
            except Exception as error:
                await session.rollback()
                raise not_found(f"Team not found: {error!r}")
    async def get_team_by_id(self, async_session: async_sessionmaker[AsyncSession], team_id: str):
        async with async_session() as session:
            try:
                statement = select(Team).filter(Team.id == team_id)
                team = await session.execute(statement)
                return team.scalars().one()
            except Exception as error:
                await session.rollback()
                raise not_found(f"Team not found: {error!r}")

    async def create_team(self, async_session: async_sessionmaker[AsyncSession], team: Team):
        async with async_session() as session:
            try:
                session.add(team)
                await session.commit()
                return team
            except Exception as error:
                await session.rollback()
                raise internal_server_error(f"CRUD error: {error!r}")

    async def update_team(self, async_session: async_sessionmaker[AsyncSession], team_data: dict):
        async with async_session() as session:
            try:
                statement = select(Team).filter(Team.id == team_data['id'])
                team = await session.execute(statement)
                team = team.scalars().one()
                for key in team_data.keys():
                    match key:
                        case "name":
                            team.name = team_data['name']
                await session.commit()
                return team
            except Exception as error:
                await session.rollback()
                raise internal_server_error(f"CRUD error: {error!r}")

    async def delete_team(self, async_session: async_sessionmaker[AsyncSession], team: Team):
        async with async_session() as session:
            try:
                await session.delete(team)
                await session.commit()
                return f"{team!r} deleted"
            except Exception as error:
                await session.rollback()
                raise internal_server_error(f"CRUD error: {error!r}")

    async def delete_team_by_id(self, async_session: async_sessionmaker[AsyncSession], team_id: str):
        async with async_session() as session:
            try:
                statement = select(Team).filter(Team.id == team_id)
                team = await session.execute(statement)
                team = team.scalars().one()
                await session.delete(team)
                await session.commit()
                return f"{team!r} deleted"
            except Exception as error:
                await session.rollback()
                raise internal_server_error(f"CRUD error: {error!r}")

    async def delete_team_by_name(self, async_session: async_sessionmaker[AsyncSession], team_name: str):
        async with async_session() as session:
            try:
                statement = select(Team).filter(Team.name == team_name)
                team = await session.execute(statement)
                team = team.scalars().one()
                await session.delete(team)
                await session.commit()
                return f"{team!r} deleted"
            except Exception as error:
                await session.rollback()
                raise internal_server_error(f"CRUD error: {error!r}")