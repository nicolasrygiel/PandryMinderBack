from dotenv import load_dotenv
load_dotenv()

from fastapi import FastAPI
import uvicorn

from api import api_app


def start_app():
    app = FastAPI()
    app.mount('/api', api_app)

    @app.get("/")
    async def root():
        return {"message": "Hello World"}
    
    return app

app = start_app()

if __name__ == "__main__":
    # uvicorn.run(app, port=8080, reload=True)
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True)