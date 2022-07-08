import requests
import hashlib

class InvalidQueryException(Exception):
    pass

def call_api(query_char):
    url = f"https://api.pwnedpasswords.com/range/{query_char}"
    r = requests.get(url)
    if r.status_code != 200:
        raise InvalidQueryException(f"Opps!. Seems like the quetu_character {query_char} is invalid")
    return r

def hash_string(string):
    return hashlib.sha1(string.encode("utf-8")).hexdigest().upper()
    
