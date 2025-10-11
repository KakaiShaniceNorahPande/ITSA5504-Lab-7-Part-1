import json
from handler import handler

event = {
    "httpMethod": "GET",
    "path": "/lambda/hello",
    "queryStringParameters": {"name": "Tester"}
}

print("Event:", json.dumps(event))
response = handler(event, None)
print("Response:", json.dumps(response, indent=2))
