import re

name_regex = re.compile(r'^[a-zA-Z0-9-]+$')

questions = [
    {
        "type": "input",
        "name": "name",
        "validate": lambda x: bool(name_regex.match(x)),
        "message": "Layer name"
    },
    {
        "type": "input",
        "name": "description",
        "message": "Layer description"
    },
    {
        "type": "list",
        "name": "runtime",
        "choices": [
            "nodejs20.x","nodejs18.x",
            "python3.12", "python3.11", "python3.10", "python3.9",
            "ruby3.3", "ruby3.2",
            "java21", "java17", "java11", "java8.al2",
            "dotnet8",
            "provided.al2023", "provided.al2"
        ],
        "message": "Runtime of the layer"
    }
]
