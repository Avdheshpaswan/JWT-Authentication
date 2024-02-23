from pydantic import BaseModel,Field,EmailStr

class PostSchema(BaseModel):
    id:int=Field(default=None)
    title:str=Field(default=None)
    content:str=Field(default=None)

    class config:
        extra_schema={
            "demo_post":{
                "title":"Title related to post",
                "content":"Content related to post"
            }
        }

class UserSchema(BaseModel):
    fullname:str=Field(default=None)
    email:str=Field(default=None)
    password:str=Field(default=None)


    class config:
        user_schema={
            "user_dummy":{
                "fullname":"abc",
                "email":"abc@gmail.com",
                "password":"123@hello"   
            }
        }


class UserLoginSchema(BaseModel):
    email:str=Field(default=None)
    password:str=Field(default=None)

    class config:
        user_schema={
            "user_dummy":{
                "email":"abc@gmail.com",
                "password":"123@hello"   
            }
        }        