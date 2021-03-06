import os


class Credentials:
    
    TRELLO_KEY = os.environ.get("TRELLO_KEY")
    TRELLO_TOKEN = os.environ.get("TRELLO_TOKEN")


class BoardName:
    BOARD_NAME = "Hello From Python Board"
    LIST_NAME = "Sample List Name"
    CARD_NAME = "Sample Card Name"
    CARD_DESCRIPTION = "Card description"
    CARD_COMMENT = "This Is a Comment"


class Endpoints:
    CREATE_BOARD = "https://api.trello.com/1/boards/"
    DELETE_BOARD = "https://api.trello.com/1/boards/"

    CREATE_LIST = "https://api.trello.com/1/lists/"
    DELETE_LIST = ""

    CREATE_CARD = "https://api.trello.com/1/cards/"
    CREATE_CARD_COMMENT = "/actions/comments"
    DELETE_CARD = "https://api.trello.com/1/cards/"

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
    def params_delete():
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

    @staticmethod
    def params_create_card():
        params = {
            "name": BoardName.CARD_NAME,
            "desc": BoardName.CARD_DESCRIPTION,
            "key": Credentials.TRELLO_KEY,
            "token": Credentials.TRELLO_TOKEN
        }
        return params
    
    @staticmethod
    def params_create_comment_in_card():
        params = {
            "text": BoardName.CARD_COMMENT,
            "key": Credentials.TRELLO_KEY,
            "token": Credentials.TRELLO_TOKEN
        }
        return params
