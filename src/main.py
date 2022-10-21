from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def hello():
    return {"message": "Hello, World!"}


@app.get("/bye")
def bye():
    return {"message": "Goodbye ma friend"}
