from src.handlers import hello_world_handler


def test_hello_world_handler():
    hello_world_handler({"hello": "world"}, None)
