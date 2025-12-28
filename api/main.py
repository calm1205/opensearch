from fastapi import FastAPI

from routes.root import router as root_router
from routes.opensearch import router as opensearch_router

app = FastAPI()

app.include_router(root_router)
app.include_router(opensearch_router)
