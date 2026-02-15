# from fastapi import FastAPI
# from .routes import router
#
# app = FastAPI(title="Agent API")
# app.include_router(router)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
from fastapi import FastAPI
from .routes import router

app = FastAPI(title="Ahad's API")
app.include_router(router)