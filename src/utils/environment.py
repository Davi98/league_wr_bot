import os

debug = os.environ['DEBUG'] if 'DEBUG' in os.environ else False
region = os.environ['REGION'] if 'REGION' in os.environ else "Br"
