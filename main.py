import requests
import base64
import json
import os
from dotenv import load_dotenv

USER_PROFILE_URL = "https://api.mojang.com/users/profiles/minecraft/"
USER_SKIN_URL = "https://sessionserver.mojang.com/session/minecraft/profile/"


class API():
    def __init__(self):
        load_dotenv()
        app_name = os.getenv("APP_NAME")
        self.headers = {"app_name": app_name}

    def do_request(self, url: str, extra: str):
        request = requests.get(url + extra, headers = self.headers)
        if request.status_code != 200:
            print(f"!!API connection issue: {request.status_code}")
            raise Exception("failed to retrieve information (double check username endtered is correct)")
        return request

    def get_uuid(self, name: str) -> str:
        request = self.do_request(USER_PROFILE_URL, name)
        response = request.json()
        uuid = response["id"]
        return uuid

    def get_skin_url(self, uuid: str) -> str:
        request = self.do_request(USER_SKIN_URL, uuid)
        response = request.json()
        value = response["properties"]
        value = value[0]
        value = value["value"]
        new_dict = json.loads(base64.b64decode(value))
        skin_url = new_dict["textures"]
        skin_url = skin_url["SKIN"]
        skin_url = skin_url["url"]
        return skin_url

"""
if __name__ == "__main__":
    api = API()
    uuid = api.get_uuid("your_account_name_here")
    print(uuid)
    url = api.get_skin_url(uuid)
    print(url)

"""
