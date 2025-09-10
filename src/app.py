def greet(name="world"):
    return f"hello, {name}!"

def lambda_handler(event, context):
    # If name is passed via API Gateway or test event, fetch it
    name = event.get("name", "world")
    message = greet(name)
    return {
        "statusCode": 200,
        "body": message
    }