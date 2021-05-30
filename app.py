from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

list_of_username = []


@app.get("/home/{user_name}")
def write_home(user_name: str, query):
    return {
        "Name": user_name,
        "Age": 18,
        "Query": query
    }


@app.put('/username/{user_name}')
def put_data(user_name: str):
    print(user_name)
    list_of_username.append(user_name)
    return {
        "username": user_name
    }


@app.post('/postData')
def post_data(user_name: str):
    list_of_username.append(user_name)
    return {
        "username": list_of_username
    }


@app.delete("/deletedata/{user_name}")
def delete_data(user_name: str):
    list_of_username.remove(user_name)
    return {
        "username": list_of_username
    }


@app.api_route('/homedata', methods=['GET', 'POST', 'PUT', 'DELETE'])
def handle_homedata(user_name: str):
    print(user_name)
    return {
        "username": user_name
    }
