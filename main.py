"""Main entrypoint for the app."""
import logging
import os

from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langchain.schema.runnable import RunnableLambda
from langserve import add_routes


app = FastAPI()
add_routes(app, ChatOpenAI(), path="/chat")
add_routes(app, RunnableLambda(lambda x: x), path="/lambda")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
