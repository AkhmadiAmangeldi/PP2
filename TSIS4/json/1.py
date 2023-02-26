import json

# Load the JSON data from file
with open('sample-data.json') as f:
    data = json.load(f)

# Print the table header
print("Interface Status")
print("=" * 80)
print("{:<50}{:<25}{:<8}{}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

# Loop through each interface in the data and print its details
for interface in data['imdata']:
    dn = interface['l1PhysIf']['attributes']['dn']
    description = interface['l1PhysIf']['attributes']['descr']
    speed = interface['l1PhysIf']['attributes']['speed']
    mtu = interface['l1PhysIf']['attributes']['mtu']
    print("{:<50}{:<25}{:<8}{}".format(dn, description, speed, mtu))