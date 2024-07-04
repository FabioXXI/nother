from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker
from sqlalchemy import select
from models.variable import Variable
from controller.errors.error_handler import error_handler
from controller.errors.database_error import DatabaseError

class VariableCrud:
    async def get_all_variables(self, async_session: async_sessionmaker[AsyncSession]):
        async with async_session() as session:
            try:
                statement = select(Variable).order_by(Variable.id)
                variables = await session.execute(statement)
                return variables.scalars().all()
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)
    
    async def get_variable_by_id(self, async_session: async_sessionmaker[AsyncSession], variable_id: str):
        async with async_session() as session:
            try:
                statement = select(Variable).filter(Variable.id == variable_id)
                variable = await session.execute(statement)
                return variable.scalars().one()
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)

    async def get_variable_by_name(self, async_session: async_sessionmaker[AsyncSession], variable_name: str):
        async with async_session() as session:
            try:
                statement = select(Variable).filter(Variable.name == variable_name)
                variable = await session.execute(statement)
                return variable.scalars().one()
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)
    
    async def create_variable(self, async_session: async_sessionmaker[AsyncSession], variable: Variable):
        async with async_session() as session:
            try:
                session.add(variable)
                await session.commit()
                return variable
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)

    async def update_variable(self, async_session: async_sessionmaker[AsyncSession], new_variable: dict):
        async with async_session() as session:
            try:
                statement = select(Variable).filter(Variable.id == new_variable['id'])
                variable = await session.execute(statement)
                variable = variable.scalars().one()
                for key in new_variable:
                    match key:
                        case 'name':
                            variable.name = new_variable['name']
                        case 'type':
                            variable.type = new_variable['type']
                        case 'value':
                            variable.value = new_variable['value']
                        case 'group':
                            variable.group = new_variable['group']
                        case 'point_to':
                            variable.point_to = new_variable['point_to']
                await session.commit()
                return variable
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)
    
    async def delete_variable(self, async_session: async_sessionmaker[AsyncSession], variable_id: str):
        async with async_session() as session:
            try:
                statement = select(Variable).filter(Variable.id == variable_id)
                variable = await session.execute(statement)
                variable = variable.scalars().one()
                await session.delete(variable)
                await session.commit()
                return f"{variable} deleted!"
            except DatabaseError as database_error:
                await session.rollback()
                error_handler(database_error)