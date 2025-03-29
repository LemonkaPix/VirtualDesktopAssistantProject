import base64
import os
from google import genai
from google.genai import types


def generate(prompt):
    client = genai.Client(
        api_key=os.environ.get("GEMINI_API_KEY"),
    )

    model = "gemini-2.0-flash"
    contents = [
        types.Content(
            role="user",
            parts=[
                types.Part.from_text(text=""f"{prompt}"""),
            ],
        ),
    ]
    tools = [
        types.Tool(
            function_declarations=[
                types.FunctionDeclaration(
                    name="getWeather",
                    description="gets the weather for a requested city",
                    parameters=genai.types.Schema(
                        type = genai.types.Type.OBJECT,
                        properties = {
                            "city": genai.types.Schema(
                                type = genai.types.Type.STRING,
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
            print(chunk.function_calls[0])
            return

    if isinstance(response, bytes):
        response = response.decode('utf-8')

    return response