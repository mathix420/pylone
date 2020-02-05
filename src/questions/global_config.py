import regex

name_regex = regex.compile(r'^[a-zA-Z0-9-]+$')

questions = [
    {
        "type": "input",
        "name": "name",
        "validate": lambda x: bool(name_regex.match(x)),
        "message": "Project name"
    },
    {
        "type": "list",
        "name": "region",
        "choices": [
            "us-east-2",
            "us-east-1",
            "us-west-1",
            "us-west-2",
            "eu-central-1",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "eu-north-1",
            "ap-east-1",
            "ap-south-1",
            "ap-northeast-3",
            "ap-northeast-2",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-northeast-1",
            "ca-central-1",
            "cn-north-1",
            "cn-northwest-1",
            "me-south-1",
            "sa-east-1",
            "us-gov-east-1",
            "us-gov-west-1"
        ],
        "message": "Project region"
    },
    {
        "type": "list",
        "name": "cloud",
        "choices": ["aws"],
        "message": "Cloud provider"
    }
]