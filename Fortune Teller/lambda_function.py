import json
import random

def random_int():
    opts=[1,2,3]
    return random.choice(opts)
    
def lambda_handler(events, context):
    opts=random_int()
    if opts==1:
        value="Yes,Your future looks bright and successful!"
        if opts==2:
            value="NO, I don't Think you can go with that. "
    else:
        value="MAY BE, I am Not Sure "
        
    message=f"{value} "
    return {
        "statusCode":200,
        "body": json.dumps(message)
    }