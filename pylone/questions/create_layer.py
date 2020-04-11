import regex

name_regex = regex.compile(r'^[a-zA-Z0-9-]+$')

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
            "nodejs12.x", "nodejs10.x",
            "python3.8", "python3.7", "python3.6", "python2.7",
            "ruby2.5",
            "java11", "java8",
            "dotnetcore2.1",
            "go1.x"
        ],
        "message": "Runtime of the layer"
    }
]
