### Resources

Password - adminpassword

Wordlist - https://crackstation.net/files/crackstation-human-only.txt.gz
The list contains about 64 million passwords

### Performance Numbers

* The speed of the online password cracker (in guesses per second) - 521 guesses per second
* Total time is about 15,066.64 seconds -> 4hrs and 10min
* Number of guesses is 7,850,907 (the list was in alphabetical order so did not have to go through all 64 million)

### Website Improvements
The website can protect against such attacks by

* limiting number of attempts per username
* limiting number of requests per hardware address
* locking out accounts with higher than normal attempts from any IP address

### Notes on testing

We notice that trying to guess directly is significantly slower

* I noticed that running the server and the attack script on the same machine was probably bottlenecking somewhere since both the processess weren't using 100% CPU despite assigning them different CPUs using taskset
* Even if we assumed the bottleneck was on the network stack and double the bandwidth, this method is significantly slower than the 1.2 million guesses per second speed by bruteforcing passwords on our own machine, despite having to calculate the hashes by ourselves.
* Multithreading could possibly increase efficiency but we will still be bottlenecked by the server and network