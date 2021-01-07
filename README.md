# Password cracking

This repo contains program to break a given salted hash using a dictionary of words. The performance between breaking on the system vs breaking by trying passwords on a simple web application is compared.

We have the salt as well as the hashed password and the hash function used is sha256

### Components

* [pwcrack.py](src/pwcrack-scripts/pwcrack.py) contains code to break a given hash
* [pwcrack_online.py](src/pwcrack-scripts/pwcrack_online.py) contains code to try passwords on a site using post requests
* A simple Flask [web-app](src/web-app) was made to run the attacks on. It can be started by running `$ python app.py` on the terminal. The python version used is 3.8 and needs Flask installed.
* [pwcrack.md](report/pwcrack.md) contains the performance numbers for `pwcrack.py`
* [pwcrack_online.md](report/pwcrack_online.md) contains the performance numbers for `pwcrack_online.py`
* Wordlist can be found at [crackstation.net](https://crackstation.net/crackstation-wordlist-password-cracking-dictionary.htm) or use [this] (https://crackstation.net/files/crackstation-human-only.txt.gz) for direct download

#### Note
Make sure to download the `crackstation-human-only.txt` file and keep it in the ``src/pwcrack-scripts` folder before running the password crackers. I avoided adding that to the repo as it is over 650MB in size.

