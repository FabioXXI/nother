from jose import jwt
from dotenv import load_dotenv
from os import getenv
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends
from typing import Annotated
from controller.errors.http.http_exceptions import unauthorized

load_dotenv()

SECRET_KEY = getenv('SECRET_KEY')
ALGORITHM = getenv('ALGORITHM')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='create/team')

def create_access_token(id: str, access_id: str = None):
    jwt_data = {"sub_id": id, "sub_access_id": access_id}
    encoded_jwt = jwt.encode(jwt_data, key=SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def decode_token(token: Annotated[str, Depends(oauth2_scheme)]) -> dict:
    try:
        payload = jwt.decode(token, key=SECRET_KEY, algorithms=ALGORITHM)
        id = payload.get('sub_id')
        access_id = payload.get('sub_access_id')
        return {'id': id, 'access_id': access_id}
    except Exception as error:
        return unauthorized(f"Token expired or invalid: {error!r}")