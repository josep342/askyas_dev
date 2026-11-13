from  fastapi import Security,HTTPException,status
from fastapi.security.api_key import APIKeyHeader

API_KEY_NAME="ASKYAS-API-KEY"

API_KEY={
    'acdfe5f4d':'Junior',
    'dh5dfds3':'joseph'
}

api_key_header=APIKeyHeader(name=API_KEY_NAME,auto_error=False)

def verify_api(api_key: str=Security(api_key_header)):
    if api_key and api_key in API_KEY:

        return API_KEY[api_key]
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED, detail='user inconnu'
    )