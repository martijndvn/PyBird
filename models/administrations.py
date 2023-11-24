from models import base
import requests

from models.base import Entity, Dao, MoneybirdClient


class Administration(Entity):
    'Administration Class'

class Administrations(Dao):
    def __init__(self, client: MoneybirdClient):
        super().__init__(client)

    entity = Administration
    ENDPOINT = 'https://moneybird.com/api/v2/administrations.json'











