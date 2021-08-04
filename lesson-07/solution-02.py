from collections import defaultdict
from sys import stdin

# Define the dictionary for clients to get the data from lambda function
clients = defaultdict(lambda: defaultdict(int))


# The cycle to get the data and parsing the string by arguments
for line in stdin.readlines():
    client, thing, value = line.split()
    clients[client][thing] += int(value)

# Sort clients and goods in ascending order
for client in sorted(clients):
    print(client + ":")
    for thing in sorted(clients[client]):
        print(thing, clients[client][thing])