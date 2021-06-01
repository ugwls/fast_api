from fastapi import FastAPI, Body, Request, File, UploadFile, Form, Depends
from pydantic import BaseModel
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm, oauth2
app = FastAPI()

list_of_username = []
templates = Jinja2Templates(directory='templates')

oauth_scheme = OAuth2PasswordBearer(tokenUrl="token")


class NameValue(BaseModel):
    name: str = None
    country: str
    age: int
    base_salary: float


@app.post("/token")
async def token_generate(from_data: OAuth2PasswordRequestForm = Depends()):
    print(from_data)
    return {
        "access token": from_data.username,
        "token_type": "bearer"
    }


@app.get("/users/profilepic")
async def profilepic(token: str = Depends(oauth_scheme)):
    print(token)
    return {
        "user": "Ujjwal",
        "profilepic": "my_face"
    }


@app.get("/home/{user_name}", response_class=HTMLResponse)
def write_home(request: Request, user_name: str):
    return templates.TemplateResponse('home.html', {"request": request, "username": user_name})


@app.post("/submitform")
async def handle_form(assigment: str = Form(...), assigment_file: UploadFile = File(...)):
    print(assigment)
    print(assigment_file.filename)
    content_assignment = await assigment_file.read()
    print(content_assignment)


@app.post('/postData')
def post_data(namevalue: NameValue, spousal_status: str = Body(...)):
    print(NameValue)
    return {
        "name": namevalue.name,
        "spousal status": spousal_status
    }
