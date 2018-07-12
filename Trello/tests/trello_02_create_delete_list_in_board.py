import unittest, requests
from config import Credentials, BoardName, Endpoints
import pprint


class CreateDeleteListInBoard(unittest.TestCase):
    
    board_id = None
    list_id = None
    card_id = None
    comment_id = None

    def setUp(self): 
        self.create_board_endpoint = Endpoints.CREATE_BOARD
        self.delete_board_endpoint = Endpoints.DELETE_BOARD
        self.params_create_board = Endpoints.params_create_board
        self.params_delete = Endpoints.params_delete

        # list
        self.create_list_endpoint = Endpoints.CREATE_LIST
        self.params_create_list = Endpoints.params_create_list
        # card
        self.create_card_endpoint = Endpoints.CREATE_CARD
        self.comments_endpoint = Endpoints.CREATE_CARD_COMMENT
        self.params_create_card = Endpoints.params_create_card
        self.params_create_comment_in_the_card = Endpoints.params_create_comment_in_card


    def test_01_create_board(self):
        self.request = requests.post(self.create_board_endpoint, params=self.params_create_board())
        self.response = self.request.json()
        self.json = self.response.get("id")
        CreateDeleteListInBoard.board_id = self.json

        self.assertEqual(self.request.status_code, 200)
        self.assertEqual(self.params_create_board().get("name"), self.response.get("name"))

    def test_02_create_lists_within_board(self):
        parameters = self.params_create_list()
        parameters["idBoard"] = CreateDeleteListInBoard.board_id
        self.request = requests.post(self.create_list_endpoint, params=parameters)
        self.response = self.request.json()
        self.json = self.response.get("id")
        CreateDeleteListInBoard.list_id = self.json

        self.assertEqual(self.request.status_code, 200)
        self.assertEqual(self.params_create_list().get("name"), self.response.get("name"))

    def test_03_create_card_within_list(self):
        parameters = self.params_create_card()
        parameters["idList"] = CreateDeleteListInBoard.list_id
        self.request = requests.post(self.create_card_endpoint, params=parameters)
        self.response = self.request.json()
        CreateDeleteListInBoard.card_id = self.response.get("id")

        self.assertEqual(self.request.status_code, 200)
        self.assertEqual(self.params_create_card().get("name"), self.response.get("name"))

    def test_04_add_comment_to_the_card(self):
        parameters = self.params_create_comment_in_the_card()
        self.request = requests.post(self.create_card_endpoint + 
                                     CreateDeleteListInBoard.card_id + 
                                     self.comments_endpoint, 
                                     params=parameters
                                     )
        self.response = self.request.json()
        CreateDeleteListInBoard.comment_id = self.response.get("id")

        self.assertEqual(self.request.status_code, 200)
        self.assertEqual(self.params_create_comment_in_the_card().get("text"), 
                        self.response.get("data").get("text")
                        )

    def test_05_delete_comment_from_the_card(self):

        self.request = requests.delete(self.create_card_endpoint + 
                                       CreateDeleteListInBoard.card_id + 
                                       "/actions/" + 
                                       CreateDeleteListInBoard.comment_id + 
                                       "/comments",
                                       params=self.params_delete()
                                       )
        self.response = self.request.json()

        self.assertEqual(self.request.status_code, 200)
                                