from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from os import path
import mcstatus as mcs
import json

settings = {
    'host': 'sample.com',
    'port': 25565
}

app = Flask(__name__)
api = Api(app)
CORS(app)


@app.route('/poll')
def poll_server():
    print(settings)
    HOST = settings["host"]
    print(HOST)
    PORT = settings["port"]
    print(PORT)

    server = mcs.MinecraftServer.lookup("{}:{}".format(HOST, PORT))
    status = server.status()

    payload = {"online_players": status.players.online,
               "max_players": status.players.max,
               "server_version": status.version.name,
               "server_description": status.description["text"]}

    return payload


def main():

    if path.exists("conf.json"):
        global settings
        with open("conf.json", "r") as s:
            settings = json.loads(s.read())
        app.run(host='0.0.0.0', port='5000')
    else:
        print("Conf file does not exist, exiting")
        exit(1)


if __name__ == "__main__":
    main()
