from fastapi import Request
from controller.auth import jwt

async def verify_team_access_token(request: Request) -> dict:
    access_token = request.headers.get("Authorization")
    team = jwt.decode_token(access_token)
    return team

async def verify_data_access_token(request: Request) -> str:
    data_access_token = request.headers.get('Authorization')
    team = jwt.decode_token(data_access_token)
    return team['id']