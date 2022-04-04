from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def read_root():
    return {"Eventor": "Welcome to Eventor website"}
