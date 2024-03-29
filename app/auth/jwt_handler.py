# This file is responsible for encoding,decoding and returning JWTs

import time 
import jwt
from decouple import config

JWT_SECRET=config("secret")
JWT_ALGORITHM=config("algorithm")

# returns generated tokens(JWTs)
def token_response(token:str):
    return {"access token":token}

#signing the JWT string 
def signJWT(userid:str):
    payload={
        "userid":userid,
        "expiry":time.time() + 600
    }    
    token=jwt.encode(payload,JWT_SECRET,algorithm=JWT_ALGORITHM)
    return token_response(token)


# returns the decoded JWT 
def decodeJWT(token:str):
    try:
      decode_token=jwt.decode(token,JWT_SECRET,algorithms=JWT_ALGORITHM)
      return decode_token if decode_token['expires'] >=time.time() else None
    except:
        return {}
