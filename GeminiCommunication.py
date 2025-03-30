import base64
import os
from google import genai
from google.genai import types

from FunctionCalling import callFunctions
from SpeechAndSpeaking import SpeakText

contents = []

def generate(prompt):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash"

    globals()['contents'].append(
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=""f"{prompt}"""),
            ],
        )
    )

    tools = [
        types.Tool(
            function_declarations=[
                types.FunctionDeclaration(
                    name="getDateTime",
                    description="gets the current date and time, don't respond to me when you want to call this function",
                    parameters=None,
                ),
                types.FunctionDeclaration(
                    name="quit",
                    description="when I say goodbye to you, answer me and then call this function",
                    parameters=None,
                ),
                types.FunctionDeclaration(
                    name="rememberIt",
                    description="remembers a given thing",
                    parameters=genai.types.Schema(
                        type=genai.types.Type.OBJECT,
                        required=["thingToremember"],
                        properties={
                            "thingToremember": genai.types.Schema(
                                type=genai.types.Type.STRING,
                            ),
                        },
                    ),
                ),

            ])
    ]

    systemInstructions = open('SystemInstructions', 'r', encoding='utf-8')
    generate_content_config = types.GenerateContentConfig(
        temperature=2,
        tools=tools,
        response_mime_type="text/plain",
        system_instruction=[
            types.Part.from_text(text=""f"{systemInstructions.read()}"""),
        ],
    )
    systemInstructions.close()

    response = ""
    for chunk in client.models.generate_content_stream(
        model=model,
        contents=contents,
        config=generate_content_config,
    ):
        # print(chunk.text if not chunk.function_calls else chunk.function_calls[0], end="")
        if not chunk.function_calls:
            response += chunk.text
        else:
            if response != "":
                SpeakText(response)
            return callFunctions(chunk.function_calls)


    if isinstance(response, bytes):
        response = response.decode('utf-8')

    globals()['contents'].append(
        types.Content(
            role="model",
            parts=[
                types.Part.from_text(text=""f"{response}"""),
            ],
        )
    )

    return response