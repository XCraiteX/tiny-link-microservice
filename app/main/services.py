import requests
import random
import string


async def generate_key():
    symbols = string.ascii_letters + string.digits
    
    key = ''.join(random.choice(symbols) for _ in range(6))

    return key

async def valid_link(link):
    try:
        response = requests.get(link)

        if response.status_code == 200:
            return True
        return False
    except: return False

