import sys
import string
import itertools

def generate_names(length):
    chars = string.ascii_lowercase + string.digits # abcdefghijklmnopqrstuvwxyz0123456789
    names = []
    for item in itertools.product(chars, repeat=length):
        names.append(''.join(item))
    return names

def generate_tlds(length):
    tlds = []
    with open('tld.txt') as file:
        tld = file.read().splitlines()
    for ending in tld:
        if len(ending) <= length:
            tlds.append(ending)
    return tlds

def generate_domains(names, tlds):
    domains = []
    for name in names:
        for tld in tlds:
            domains.append('{0}.{1}'.format(name, tld))
    return domains

if len(sys.argv) == 3:
    max_domain_length = int(sys.argv[1])
    max_tld_length = int(sys.argv[2])

    names = generate_names(max_domain_length)
    print('Generated {0} names!'.format(len(names)))
    tlds = generate_tlds(max_tld_length)
    print('Generated {0} tlds!'.format(len(tlds)))

    domains = generate_domains(names, tlds)

    print('Generated {0} domains!'.format(len(domains)))

    with open('domains.txt', 'w') as file:
        for domain in domains:
            file.write("{0}\n".format(domain))
else:
    print('Usage: ./generate.py <max_domain_length> <max_tld_length>')