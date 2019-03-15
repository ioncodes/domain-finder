import thread
from threading import Lock

lock = Lock()

with open('domains.txt') as file:
    domains = file.read().splitlines()

with open('words_alpha.txt') as file:
    words = file.read().splitlines()

def check_domain(domain):
    for word in words:
        if domain.replace('.', '') == word:
            lock.acquire()
            print(domain)
            lock.release()

for domain in domains:
    thread.start_new_thread(check_domain, (domain,))
    