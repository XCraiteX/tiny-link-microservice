import random
import string
import re

async def generate_key():
    symbols = string.ascii_letters + string.digits
    
    key = ''.join(random.choice(symbols) for _ in range(6))

    return key

async def valid_link(link):
    reg = '(http|ftp|https):\/\/([\w_-]+(?:(?:\.[\w_-]+)+))([\w.,@?^=%&:\/~+#-]*[\w@?^=%&\/~+#-])'

    res = re.match(reg, link)
    if res:
        return True
            
    return False