import time
from fastapi import FastAPI
from pydantic import BaseModel
import mysql.connector


app = FastAPI() # -> inisialiserer FastAPI


class Post(BaseModel): # -> bruker pydantic for å lage en Basemodel som innholder variablene mine 
    title: str
    content: str

#hvordan koble til mysql:
while True:
    try:
        conn = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="######",
        database= "webapi")
        cursor = conn.cursor()
        print("\n*Database connection was succesfull!*\n")
        break
    except Exception as error:
        print("connecting to databse failed")
        print("Error: ", error)
        time.sleep(2)

    


# GET routing
@app.get("/")
def root():
    return {"message":"Welcome to my page Note"}

@app.get("/posts")
def get_posts():
    cursor.execute(""" SELECT * FROM posts""")
    posts = cursor.fetchall()

    return {"data": posts}

@app.get("/posts/{id}")
def get_one_post(id: int):
    return {"data": f" {id} is fetched"}


#POST routing
@app.post("/posts")
def create_posts(post: Post):
    return {"message": f" the message is created : {post}"}


#DELETE routing
@app.delete("/posts/{id}")
def delete_post(id = int):
    return {"message": f" post with id: {id}, is succ deleted"}


#PUT routing
@app.put("/posts/{id}")
def update_post(id : int, post : Post):
    return {"message": f"{id} is succesfully updated to {post.title}  {post.content}"}















