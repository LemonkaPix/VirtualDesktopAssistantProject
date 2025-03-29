from datetime import datetime
import json



def callFunctions(functions):
    from GeminiCommunication import generate

    for f in functions:
        return globals()[f.name](f.args)

def getWeather(args):
    return f"pogoda w {args['city']} jest słoneczna"

def getDateTime(args):
    now = datetime.now()

    data = {
        "year": now.year,
        "month": now.month,
        "day": now.day,
        "hour": now.hour,
        "minute": now.minute,
    }

    json_string = json.dumps(data, indent=4)
    return json_string