# This file is responsible for signing, encoding, decoding and returning JWTs.
import time

import jwt
# helps to organize settings so that parameters can be changed without having to redeploy the application
from decouple import config

# pointing towards the secret & the algorithm in the .env file
JWT_SECRET = config("secret")  # used for encoding and decoding jwt string
JWT_ALGORITHM = config("algorithm")  # type of algorithm used in the encoding process


# returns the generated JWT token
def token_response(token: str):
    return {
        "access_token": token
    }


# signs the JWT string
def sign_jwt(userId: int):
    payload = {
        "userId": userId,
        "expiry": time.time() + 600
    }
    token = jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)
    return token_response(token)


def decode_jwt(token: str):
    try:
        decode_token = jwt.decode(token, JWT_SECRET, algorithm=JWT_ALGORITHM)
        return decode_token if decode_token['expires'] >= time.time() else None
    except:
        return {}
