# from fastapi import FastAPI
# from .routes import router
#
# app = FastAPI(title="Agent API")
# app.include_router(router)

# XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
from fastapi import FastAPI
from .routes import router

app = FastAPI(title="API Practice")
app.include_router(router)