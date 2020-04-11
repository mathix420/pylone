import regex

name_regex = regex.compile(r'^[a-zA-Z0-9-]+$')

questions = [
    {
        "type": "input",
        "name": "name",
        "validate": lambda x: bool(name_regex.match(x)),
        "message": "Function name"
    },
    {
        "type": "input",
        "name": "description",
        "message": "Description of the function"
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
        "message": "Function runtime"
    },
    {
        "type": "input",
        "name": "timeout",
        "validate": lambda x: x.isnumeric(),
        "filter": lambda x: int(x),
        "message": "Function timeout (sec)"
    },
    {
        "type": "input",
        "name": "handler",
        "validate": lambda x: '.' in x,
        "message": "Function handler"
    }
]
