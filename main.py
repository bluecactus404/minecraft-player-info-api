import requests
import base64
import json

#add custom header to let mojang know origin of requests

USER_PROFILE_URL = "https://api.mojang.com/users/profiles/minecraft/"
USER_SKIN_URL = "https://sessionserver.mojang.com/session/minecraft/profile/"


class API():
    def __init__(self):
        #set headder here later
        pass

    def get_uuid(self, name: str) -> str:

        request = requests.get(USER_PROFILE_URL + name)
        response = request.json()
        uuid = response["id"]
        return uuid

    def get_skin_url(self, uuid: str) -> str:
        request = requests.get(USER_SKIN_URL + uuid)
        response = request.json()
        value = response["properties"]
        value = value[0]
        value = value["value"]
        new_dict = json.loads(base64.b64decode(value))
        skin_url = new_dict["textures"]
        skin_url = skin_url["SKIN"]
        skin_url = skin_url["url"]
        return skin_url


if __name__ == "__main__":
    api = API()
    uuid = api.get_uuid("namehere")
    print(uuid)
    api.get_skin_url(uuid)






