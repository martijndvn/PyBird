from models import base, administrations

with open('secrets') as f:
    key = f.read()

print("Creating Client")
client = base.MoneybirdClient(key)

print("Reading Administartions")
admins = administrations.Administrations(client)

admins.get()

print("Succes")
