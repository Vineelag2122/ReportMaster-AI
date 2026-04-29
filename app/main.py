from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import os

app = FastAPI()

# Try safe mounting
if os.path.exists("app/frontend/static"):
    app.mount("/static", StaticFiles(directory="app/frontend/static"), name="static")

if os.path.exists("app/frontend"):
    app.mount("/", StaticFiles(directory="app/frontend", html=True), name="frontend")
