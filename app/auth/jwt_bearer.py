# Verification of the routes
# This file checks whether the request is authorized or not

from fastapi import Request,HTTPException
from fastapi.security import HTTPBearer,HTTPAuthorizationCredentials
from .jwt_handler import decodeJWT

class JWTBearer(HTTPBearer):
    def __init__(self,auto_Error:bool=True):
        super(JWTBearer,self).__init__(auto_error=auto_Error)

    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials =await super(JWTBearer,self).__call__(request)
        if credentials:
            if not credentials.scheme=="Bearer":
                raise HTTPException(status_code=403,detail="Invalid or Expired Token")
            return credentials.credentials 
        else:
            raise HTTPException(status_code=403,detail="Invalid or Expired Token")
        
# to post any post user has to verify first
    def verify_jwt(self,jwt_token:str):
        isValidToken:bool=False 
        payload=decodeJWT(jwt_token)
        if payload:
            isValidToken=True

        return isValidToken       

