import pika
from fastapi import FastAPI
from mangum import Mangum  # Amazon Lambda handler

from .routers import *

# connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
# channel = connection.channel()
#
# channel.queue_declare(queue='hello')
#
# channel.basic_publish(exchange='',
#                       routing_key='hello',  # the queue name
#                       body='Hello World!')
# print(" [x] Sent 'Hello World!'")
#
# connection.close()

app = FastAPI()

app.include_router(userrouter.router)
app.include_router(rolerouter.router)
app.include_router(authenticationrouter.router)

users = []


# Index route
@app.get("/u")
def read_root():
    return {"Eventor": "Welcome to USERS service"}


handler = Mangum(app=app)
# def check_user(data: UserLoginSchema):
#     for user in users:
#         if user.email == data.email and user.password == data.password:
#             return True
#         return False
#
#
# # User Login
# @app.post("/user/login", tags=["user"])
# def user_login(user: UserLoginSchema = Body(default=None)):
#     if check_user(user):
#         return sign_jwt(user.email)
#     else:
#         return {
#             "error": "Invalid login details!"
#         }
#
#
# # User Welcome page
# @app.get("/user/home", dependencies=[Depends(JWTBearer())], tags=["user"])
# def user_welcome():
#     return {'data': 'Successfully logged in'}

# # @app.get("/user")
# # def userslist(limit=10, logged: bool = True, sort: Optional[str] = None):
# #     if logged:
# #         return {'data': f'{limit} logged in users from the db'}
# #     else:
# #         return {'data': f'{limit} users from the db'}
# #
# #
# @app.get("/user/{id}", status_code=200, response_model=user.UserShow)
# def show(id: int, response: Response, db: Session = Depends(get_db)):
#     return {"data": id}

#
# @app.get("/user/{id}/subscriptions")
# def subscriptions(id, limit=10):
#     return {"data": {'data': {'1', '2'}}}
#
#
# class User(BaseModel):
#     name: str
#     logged: Optional[bool]
#
#
# @app.post('/user')
# def register_user(user: User):
#     # return user
#     return{'data': f"User is registered with name {user.name}"}
