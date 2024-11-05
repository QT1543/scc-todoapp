from fastapi import FastAPI
import sqlite3

app = FastAPI()


@app.get('/get_tasks') #where we define the url

def get_tasks():
    with sqlite3.connect("./todos.db") as conn:
        query = conn.execute("SELECT * FROM todos;")
        result = query.fetchall

        response = []
        for todo in result:
            todo_json = {
                'id': todo[0],
                'todo': todo[1]
            }
            response.append(todo_json)
        return response

#cd backend
#sqlite3 todos.db
#sqlite> CREATE TABLE todos (id INTEGER PRIMARY KEY AUTOINCREMENT, todo TEXT NOT NULL);
#sqlite> INSERT INTO todos (todo) VALUES ("Learn FastAPI");
#sqlite> SELECT * FROM todos;
#uvicorn main:app --reload