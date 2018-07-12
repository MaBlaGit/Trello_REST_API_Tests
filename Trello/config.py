import os

class Credentials:
    
    TRELLO_KEY = os.environ.get("TRELLO_KEY")
    TRELLO_TOKEN = os.environ.get("TRELLO_TOKEN")

class BoardName:
    BOARD_NAME = "Hello From Python Board"
    LIST_NAME = "Sample List Name"

class Endpoints:
    CREATE_BOARD = "https://api.trello.com/1/boards/"
    DELETE_BOARD = "https://api.trello.com/1/boards/"

    CREATE_LIST = "https://api.trello.com/1/lists/"
    DELETE_LIST = ""

    CREATE_CARD = ""
    DELETE_CARD = ""

    @staticmethod
    def params_create_board():
        params = {
            "name": BoardName.BOARD_NAME,
            "defaultLists": 0,
            "key": Credentials.TRELLO_KEY,
            "token": Credentials.TRELLO_TOKEN
        }
        return params

    @staticmethod
    def params_delete_board():
        params = {
            "key": Credentials.TRELLO_KEY,
            "token": Credentials.TRELLO_TOKEN,
        }
        return params

    @staticmethod
    def params_create_list():
        params = {
            "name": BoardName.LIST_NAME,
            "key": Credentials.TRELLO_KEY,
            "token": Credentials.TRELLO_TOKEN
        }
        return params
