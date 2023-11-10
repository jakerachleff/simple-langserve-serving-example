"""Main entrypoint for the app."""
from fastapi import FastAPI
from langchain.chat_models import ChatOpenAI
from langserve import add_routes


app = FastAPI()
add_routes(app, ChatOpenAI(), path="/chat")

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)