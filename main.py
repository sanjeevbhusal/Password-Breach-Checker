import requests
import hashlib

class InvalidQueryException(Exception):
    pass

def get_breach_count(hash_to_check, hashes_list):
    hashes_list = (hash.split(":") for hash in hashes_list)
    breached_count = 0
    for current_hash, count in hashes_list:
        if current_hash == hash_to_check:
            breached_count = count
            break 
    return breached_count


def call_api(query_char):
    url = f"https://api.pwnedpasswords.com/range/{query_char}"
    r = requests.get(url)
    if r.status_code != 200:
        raise InvalidQueryException(f"Opps!. Seems like the quetu_character {query_char} is invalid")
    return r

def hash_string(string):
    return hashlib.sha1(string.encode("utf-8")).hexdigest().upper()
    
