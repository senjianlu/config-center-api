#!/usr/bin/env python
# -*- coding:UTF-8 -*-
#
# @AUTHOR: Rabbir
# @FILE: ~/Projects/sbeer/config-center/app/main.py
# @DATE: 2023/07/25 周二
# @TIME: 21:17:03
#
# @DESCRIPTION: todo...


from typing import Union

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordBearer
from pydantic import BaseModel

app = FastAPI()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


class User(BaseModel):
    """
    用户模型
    """
    username: str
    email: Union[str, None] = None
    full_name: Union[str, None] = None
    disabled: Union[bool, None] = None

def fake_decode_token(token):
    return User(
        username=token + "fakedecoded", email="john@example.com", full_name="John Doe"
    )

async def get_current_user(token: str = Depends(oauth2_scheme)):
    user = fake_decode_token(token)
    return user

@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_user)):
    return current_user

@app.get("/items/")
async def read_items(token: str = Depends(oauth2_scheme)):
    return {"token": token}


# 执行
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app='main:app', host="0.0.0.0", port=8000, reload=True)