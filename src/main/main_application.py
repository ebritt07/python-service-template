import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.main.config.config import config
from src.main.controllers.controller1 import router as controller1
from src.main.controllers.controller2 import router as controller2
from src.main.util import server_util

app_name = config['backend']['name']
app_description = config['backend']['description'] + " (" + config['backend']['env'] + ")"

app = FastAPI(title=app_name, description=app_description)
app.include_router(controller1, prefix="/controller1")
app.include_router(controller2, prefix="/controller2")
app.add_middleware(
    CORSMiddleware,
    allow_origins=config['backend']['server']['allowedOrigins'],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

app_server = FastAPI()
server_path = config['backend']['server']['path']
app_server.mount(server_path, app)

if __name__ == "__main__":
    host = config['backend']['server']['host']
    port = config['backend']['server']['port']

    server_util.print_startup_message()

    uvicorn.run(app_server, host=host, port=port)
