import time
from hashlib import sha256

# method to print guesses per second and other metrics
def print_gps(start_time, guesses):
    total_time = time.time() - start_time
    gps = guesses / total_time
    print(f'gps is {gps}s, total time is {total_time} and number of guesses is {guesses}')

# setting start time to calculate performance metrics
start_time = time.time()

# setting the salt and the hash to be guessed
salt = '000000000000000000000000000078d2'.encode('utf-8')
t = '18821d89de11ab18488fdc0a01f1ddf4d290e198b0f80cd4974fc031dc2615a3'

with open('crackstation-human-only.txt', mode='r', encoding='ISO-8859-1') as f:
    i = 0
    for p in f:

        i += 1
        # removing new line characters
        p = p[:-1]

        # generating hash
        hasher = sha256()
        hasher.update(salt)
        hasher.update(p.encode('utf-8'))

        # checking if we broke the password
        if hasher.hexdigest() == t:
            print_gps(start_time, i)
            # printing plaintext value of broken password
            print(f'the password is {p}')
            break
