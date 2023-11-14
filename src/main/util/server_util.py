from src.main.config.config import config


def print_startup_message():
    dashes = "".join(["-" for i in range(60)])

    app_name = config['backend']['name']
    host = config['backend']['server']['host']
    port = config['backend']['server']['port']
    server_path = config['backend']['server']['path']

    if host == "0.0.0.0":
        host = "localhost"

    msg = "\n".join([
        "\n",
        dashes,
        "RONNY BROS. LLC",
        dashes,
        "Welcome to '" + app_name + "'",
        dashes,
        "Check out the Swagger UI at http://{0}:{1}{2}/docs".format(host, port, server_path),
        dashes,
        "Check out the ReDoc at http://{0}:{1}{2}/redoc".format(host, port, server_path),
        dashes,
        "\n"
    ])

    print(msg)
