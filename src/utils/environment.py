import os

debug = os.environ['DEBUG'] if 'DEBUG' in os.environ else False
tor_port = os.environ['TOR_PORT'] if 'TOR_PORT' in os.environ else '9050'