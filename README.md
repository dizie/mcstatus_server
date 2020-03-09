# mcstatus_server

mcstatus_server is a API to retrieve a minecraft server's status (players, description, version) using Dinnerbone's [mcstatus](https://github.com/Dinnerbone/mcstatus)

## Installation

Clone the repo

CD into dir
```bash
cd mcstatus_server
```

Create a venv
```bash
virtualenv mcstatus_server

# Mac OS / Linux
source mcstatus_server/bin/activate

# Windows
mcstatus_server\Scripts\activate

pip install -r requirements.txt
```

## Usage

```python
python3 server.py
```

With a config file
```
http://0.0.0.0:5000/poll
```

Without a config file
```
http://0.0.0.0:5000/poll/<ip:port>
```
