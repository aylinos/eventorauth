# This file is responsible for checking out if the request is authorized or not [Verification of the protected route]

from fastapi import HTTPException, Request
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

from .jwt_handler import decode_jwt


# this class is a sub class of the fastapi's HTTPBearer, this will be used to persist authentication on the routes
class JWTBearer(HTTPBearer):
    def __init__(self, auto_Error: bool = True):
        super(JWTBearer, self).__init__(auto_error=auto_Error)

    # Check if there is a Bearer token in the request
    async def __call__(self, request: Request):
        credentials: HTTPAuthorizationCredentials = await super(JWTBearer, self).__call__(request)
        if credentials:
            # If the credentials' scheme is not a bearer scheme, raise an exception
            if not credentials.scheme == "Bearer":
                raise HTTPException(status_code=403, details="Invalid or Expired Token!")
            return credentials.credentials
        else:
            raise HTTPException(status_code=403, details="Invalid or Expired Token!")

    # Verify the JWT
    def verify_jwt(self, jwtoken: str):
        isTokenValid: bool = False  # A false flag
        payload = decode_jwt(jwtoken)  # Decode whatever jwt token is being passed here
        if payload:
            isTokenValid = True
        return isTokenValid
