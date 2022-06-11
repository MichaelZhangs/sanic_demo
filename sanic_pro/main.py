from init import app
from config.configs import server_host, server_port


if __name__ == '__main__':
    app.run(host=server_host, port=server_port, debug=True)