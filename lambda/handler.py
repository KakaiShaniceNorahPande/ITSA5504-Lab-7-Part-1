import json

def handler(event, context):
    # Expect an API Gateway-style event but handle missing keys safely
    qsp = (event or {}).get("queryStringParameters") or {}
    name = qsp.get("name", "Cloud")
    return {
        "statusCode": 200,
        "headers": {"Content-Type": "application/json"},
        "body": json.dumps({"message": f"Hello {name} from Lambda!"})
    }

if __name__ == "__main__":
    # Simple local simulation
    sample_event = {
        "httpMethod": "GET",
        "path": "/lambda/hello",
        "queryStringParameters": {"name": "Pritesh"}
    }
    print("Invoking handler() with:", json.dumps(sample_event))
    print(handler(sample_event, None))
