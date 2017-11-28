import json


def hello(event, context):
    try:
        return dict(
            statusCode=200,
            body="Simple hello"
        )
    except Exception as e:
        return dict(
            statusCode=500,
            body=str(e)
        )
