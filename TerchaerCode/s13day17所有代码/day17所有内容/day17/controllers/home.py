# Author:Alex Li
import time
def index():
    f = open('views/index.html')
    data = f.read()
    data.replace('&&t&&',str(time.time()))
    return data

def login():
    return 'login'

def logout():
    return 'logout'
