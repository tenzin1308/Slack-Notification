import sys
from slack_API import SlackAPI

if __name__ == "__main__":
    bot_token = sys.argv[1] if len(sys.argv) > 1 else ''
    channel_id = sys.argv[2] if len(sys.argv) > 1 else 'C04D3JMQFL5'
    text = sys.argv[3] if len(sys.argv) > 1 else '[{"type": "section", "text": {"type": "plain_text", "text": "Hello world"}}]'
    attachments = sys.argv[4] if len(sys.argv) > 1 else 'false'
    blocks = sys.argv[5] if len(sys.argv) > 1 else 'true'
    icon_emoji = sys.argv[6] if len(sys.argv) > 1 else ':bell:'
    icon_url = sys.argv[7] if len(sys.argv) > 1 else ''
    thread_ts = sys.argv[8] if len(sys.argv) > 1 else ''
    unfurl_media = sys.argv[9] if len(sys.argv) > 1 else 'false'
    unfurl_links = sys.argv[10] if len(sys.argv) > 1 else 'false'
    username = sys.argv[11] if len(sys.argv) > 1 else 'Mr. Awesome Bot'

    slackAPI = SlackAPI(SLACK_BOT_TOKEN=bot_token, icon_emoji=icon_emoji, icon_url=icon_url, username=username, unfurl_media=unfurl_media, unfurl_links=unfurl_links)
    print(slackAPI.post_message(channel_id=channel_id, message=text, attachments=attachments, blocks=blocks))