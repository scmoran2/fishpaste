import hashlib 

def make_hash( url ):
    return hashlib.sha224( url ).hexdigest()

