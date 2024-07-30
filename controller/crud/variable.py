from sqlalchemy import select
from models.variable import Variable
from sqlalchemy.ext.asyncio import async_sessionmaker, AsyncSession
from controller.errors.http.http_exceptions import internal_server_error, not_found

class VariableCrud:

    async def get_variable_by_id(self, async_session: async_sessionmaker[AsyncSession], variable_id: str):
        async with async_session() as session:
            try:
                statement = select(Variable).filter(Variable.id == variable_id)
                variable = await session.execute(statement)
                return variable.scalars().one()
            except Exception as error:
                await session.rollback()
                raise not_found(f"Variable not found: {error!r}")

    async def get_variable_by_name(self, async_session: async_sessionmaker[AsyncSession], variable_name: str):
        async with async_session() as session:
            try:
                statement = select(Variable).filter(Variable.name == variable_name)
                variable = await session.execute(statement)
                return variable.scalars().one()
            except Exception as error:
                await session.rollback()
                raise not_found(f"Variable not found: {error!r}")

    async def create_variable(self, async_session: async_sessionmaker[AsyncSession], variable: Variable):
        async with async_session() as session:
            try:
                session.add(variable)
                await session.commit()
                return variable
            except Exception as error:
                await session.rollback()
                raise internal_server_error(f"CRUD error: {error!r}")

    async def update_variable(self, async_session: async_sessionmaker[AsyncSession], variable_data: dict):
        async with async_session() as session:
            try:
                variable = None
                if variable_data.get('id'):
                    statement = select(Variable).filter(Variable.id == variable_data['id'])
                    variable = await session.execute(statement)
                    variable = variable.scalars().one()
                else:
                    statement = select(Variable).filter(Variable.name == variable_data['name'])
                    variable = await session.execute(statement)
                    variable = variable.scalars().one()
                for key in variable_data.keys():
                    match key:
                        case "name":
                            variable.name = variable_data['name']
                        case "type":
                            variable.type = variable_data['type']
                        case "value":
                            variable.value = variable_data['value']
                await session.commit()
                return variable
            except Exception as error:
                await session.rollback()
                raise internal_server_error(f"CRUD error: {error!r}")

    async def delete_variable(self, async_session: async_sessionmaker[AsyncSession], variable: Variable):
        async with async_session() as session:
            try:
                await session.delete(variable)
                await session.commit()
                return f"{variable!r} deleted"
            except Exception as error:
                await session.rollback()
                raise internal_server_error(f"CRUD error: {error!r}")

    async def delete_variable_by_id(self, async_session: async_sessionmaker[AsyncSession], variable_id: str):
        async with async_session() as session:
            try:
                statement = select(Variable).filter(Variable.id == variable_id)
                variable = await session.execute(statement)
                variable = variable.scalars().one()
                await session.delete(variable)
                await session.commit()
                return f"{variable!r} deleted"
            except Exception as error:
                await session.rollback()
                raise internal_server_error(f"CRUD error: {error!r}")

    async def delete_variable_by_name(self, async_session: async_sessionmaker[AsyncSession], variable_name: str):
        async with async_session() as session:
            try:
                statement = select(Variable).filter(Variable.name == variable_name)
                variable = await session.execute(statement)
                variable = variable.scalars().one()
                await session.delete(variable)
                return f"{variable!r} deleted"
            except Exception as error:
                await session.rollback()
                raise internal_server_error(f"CRUD error: {error!r}")