import requests
import json


class SlackAPI:
    def __init__(self, SLACK_BOT_TOKEN):
        # WebClient instantiates a client that can call API methods
        # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
        self.__token = SLACK_BOT_TOKEN

    def __make_call(self, method, path, body):
        url = f"https://slack.com/api/{path}"
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.__token}"
        }
        if method == "post":
            return requests.post(url=url, headers=headers, data=json.dumps(body)).json()

    def post_message(self, channel_id, message):
        return self.__make_call(method="post", path="chat.postMessage", body=message)