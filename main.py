import requests
import hashlib
import sys

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
    
    
def check_password_breach(password):
    hashed_pw = hash_string(password)
    query_char = hashed_pw[:5]
    tail = hashed_pw[5:]
    
    response = call_api(query_char)
    hashes_list = response.text.splitlines()
    
    breached_count = get_breach_count(tail, hashes_list)
    return int(breached_count)        
 
        
    