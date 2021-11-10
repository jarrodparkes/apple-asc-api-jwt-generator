import jwt
import time
import os
from dotenv import load_dotenv

# load .env variables
load_dotenv()
issuer_id = os.environ.get("ISSUER_ID")
key_id = os.environ.get("KEY_ID")
key_file = os.environ.get("KEY_FILE")

# read private key file
with open(key_file, 'r+b') as keyfile:
    secret = keyfile.read()

# generate an expiration time (20 minutes from now)
expir = round(time.time() + 20 * 60)

# sign the token with the iss, time, key, and kid with the correct alg
token = jwt.encode({'iss': issuer_id,
                    'iat': round(time.time()),
                    'exp': expir,
                    'aud': 'appstoreconnect-v1'},
                    secret, algorithm='ES256', 
                    headers={'alg': 'ES256', 'kid': key_id, 'typ': 'JWT'})

# print token
print(token)