import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.main.config.config import config
from src.main.controllers.policy_controller import router as policy_router
from src.main.controllers.admin_controller import router as admin_router
from src.main.util import server_util

app_name = config['backend']['name']
app_description = config['backend']['description'] + " (" + config['backend']['env'] + ")"

app = FastAPI(title=app_name, description=app_description)
app.include_router(admin_router)
app.include_router(policy_router, prefix="/mock-carrier")
app.add_middleware(
    CORSMiddleware,
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
