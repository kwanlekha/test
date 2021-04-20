from typing import Optional
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/curlmyip")
def read_curlmyip():
    return RedirectResponse(url='http://curlmyip.org')