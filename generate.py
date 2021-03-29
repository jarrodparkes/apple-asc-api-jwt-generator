import jwt
import time

issuer_id = '[ISSUER_ID]'
key_id = '[KEY_ID]'
private_key = 'AuthKey_[KEY_ID].p8'

# read private key
with open(private_key, 'r+b') as keyfile:
    secret = keyfile.read()

# generate an expiration time
expir = round(time.time() + 20 * 60)

# sign the token with the iss, time, key, and kid with the correct alg
token = jwt.encode({'iss': issuer_id, 
                    'exp': expir, 
                    'aud': 'appstoreconnect-v1'},
                    secret, algorithm='ES256', 
                    headers={'alg': 'ES256', 'kid': key_id, 'typ': 'JWT'})

# print token
print(token)