import logging
import sys
import src.utils.environment as env


logging.basicConfig(
        format="{\"logger\":\"%(name)s\",\"timestamp\": \"%(asctime)s\" , \"level\": \"%(levelname)s\", \"message\": \"%(message)s\"}",
        datefmt="%Y-%m-%dT%H:%M:%SZ",
        stream=sys.stdout,
        level=logging.INFO)
logging.getLogger().setLevel(logging.INFO)



if str(env.debug).lower() in ['1', 'true', 'yes']:
    logging.getLogger().setLevel(logging.DEBUG)
else:
    logging.getLogger().setLevel(logging.INFO)

def log():
    return logging
