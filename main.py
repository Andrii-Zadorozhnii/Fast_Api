from sys import prefix
from typing import Annotated

from fastapi import FastAPI, Body, Path

from pydantic import EmailStr, BaseModel

import uvicorn
from imp import reload

from items_views import router as items_router
from users.views import router as user_router


app = FastAPI()
app.include_router(items_router)
app.include_router(user_router)




@app.get('/')
def hello_index():
    return {
        'message': 'hello index!',
    }


@app.get('/hello/')
def hello(name: str="World"):
    name = name.strip().title()
    return {
        'message': f'Hello {name}'
    }



@app.get('/calc/add/')
def add(a: int, b:int):
    return {
        'a': a,
        "b": b,
        'result': a + b,
    }






if __name__ == '__main__':
    uvicorn.run("main:app", reload=True)