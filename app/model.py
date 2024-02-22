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
