import requests
import json


class SlackAPI:
    def __init__(self, SLACK_BOT_TOKEN, icon_emoji, icon_url, username, unfurl_media, unfurl_links):
        # WebClient instantiates a client that can call API methods
        # When using Bolt, you can use either `app.client` or the `client` passed to listeners.
        self.__token = SLACK_BOT_TOKEN
        if icon_url == '':
            self.__body = {
                "icon_emoji": icon_emoji,
                "username": username,
                "unfurl_media": eval(unfurl_media.capitalize()),
                "unfurl_links": eval(unfurl_links.capitalize())
            }
        else:
            self.__body = {
                "icon_url": icon_url,
                "username": username,
                "unfurl_media": eval(unfurl_media.capitalize()),
                "unfurl_links": eval(unfurl_links.capitalize())
            }

    def __make_call(self, path):
        url = f"https://slack.com/api/{path}"
        headers = {
            "Content-Type": "application/json;charset=utf-8",
            "Authorization": f"Bearer {self.__token}"
        }
        return requests.post(url=url, headers=headers, data=json.dumps(self.__body)).json()

    def __create_message(self, channel_id, message, attachments, blocks):
        self.__body["channel"] = channel_id
        if not (eval(attachments.capitalize())) and not (eval(blocks.capitalize())):
            self.__body["text"] = message
        elif eval(attachments.capitalize()):
            self.__body["attachments"] = json.loads(message)
        else:
            self.__body["blocks"] = message

    def post_message(self, channel_id, message, attachments, blocks):
        self.__create_message(channel_id, message, attachments, blocks)
        return self.__make_call(path="chat.postMessage")

    def post_emphemeral(self, channel_id, message):
        pass