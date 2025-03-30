from datetime import datetime
import json

firstCall = True

def callFunctions(functions):
    if globals()['firstCall']:
        from GeminiCommunication import generate

    output = ""

    for f in functions:
        output += f"{f.name}:\n" + globals()[f.name](f.args)

    return generate(output)

def quit(args):
    quit()

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

def rememberIt(args):
    f = open('SystemInstructions','a')
    f.write(args.thingToremember)
    f.close()
    print("remembered")
    return ''