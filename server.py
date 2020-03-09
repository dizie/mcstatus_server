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


def get_server(HOST, PORT):
    return mcs.MinecraftServer.lookup("{}:{}".format(HOST, PORT))

@app.route('/poll')
def poll_server():
    HOST = settings["host"]
    PORT = settings["port"]

    server = get_server(HOST, PORT)
    status = server.status()

    payload = {"online_players": status.players.online,
               "max_players": status.players.max,
               "server_version": status.version.name,
               "server_description": status.description["text"]}

    return payload


@app.route('/poll/<url>')
def poll_url(url):
    if ':' in url:
        HOST = url.split(':')[0]
        PORT = url.split(':')[1]
    else:
        HOST = url
        PORT = 25565

    server = get_server(HOST, PORT)
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
        print("Conf file does not exist, /poll will not work")


if __name__ == "__main__":
    main()
