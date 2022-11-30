from slack_API import SlackAPI

if __name__ == "__main__":
    slackAPI = SlackAPI(SLACK_BOT_TOKEN="")
    message = {
        "channel": "C04D5J9T3GR",
        "text": "I hope the tour went well",
        "icon_emoji": ":chart_with_upwards_trend:",
        "attachments": [{"pretext": "pre-hello", "text": "text-world"}],
        "blocks": [{"type": "section", "text": {"type": "plain_text", "text": "Hello world!!!"}}]
    }
    message2 = {
        "as_user": True,
        "username": "New Name",
        "channel": "C04D5J9T3GR",
        "attachments": [
            {
                "text": "List of all Stale Branches that were deleted",
                "fallback": "Please go over the list to see if your branch is there or not.",
                "color": "#3AA3E3",
                "actions": [
                    {
                        "name": "stale-branch",
                        "text": "Stale branches...",
                        "type": "select",
                        "options": [
                            {
                                "text": "Hearts",
                                "value": "hearts"
                            },
                            {
                                "text": "Bridge",
                                "value": "bridge"
                            },
                            {
                                "text": "Checkers",
                                "value": "checkers"
                            },
                            {
                                "text": "Chess",
                                "value": "chess"
                            },
                            {
                                "text": "Poker",
                                "value": "poker"
                            },
                            {
                                "text": "Falken's Maze",
                                "value": "maze"
                            },
                            {
                                "text": "Global Thermonuclear War",
                                "value": "war"
                            }
                        ]
                    }
                ]
            }
        ]
    }
    print(slackAPI.post_message(channel_id="C04D5J9T3GR", message=message2))