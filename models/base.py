'Easy interfacing with the moneybird'
import requests


class MoneybirdClient:
    'Client will connect to the moneybird api'
    def __init__(self, key):
        self.key = key

class Entity:
    def __init__(self, d=None):

        if d is not None:
            for key, value in d.items():
                setattr(self, key, value)


class Dao:

    entity = Entity
    ENDPOINT: str

    def __init__(self,  client: MoneybirdClient):
        self.client = client




    def get(self):

        args = {
            'Authorization': self.client.key,
            'Content-Type': 'application/json'
        }

        print(self.ENDPOINT)

        url = self.ENDPOINT

        data_list = []

        while url:

            response = requests.get(url=self.ENDPOINT, headers=args)
            data_list.append(response.json())
            link = response.headers.get("link")

            # Check for pages
            try:
                if link:
                    links = link.split(",")
                    print(links)

                    for link in links:
                        split = link.split(";")

                        if "next" in split[1]:
                            print("Detected another page")
                            url = split[2:-3]
                else:
                    url = None

            except Exception as e:
                url = None

        return_list = []

        for entry in data_list:
           return_list.append(self.entity(entry))

        return return_list






