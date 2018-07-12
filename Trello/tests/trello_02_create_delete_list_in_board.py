import unittest, requests
from config import Credentials, BoardName, Endpoints


class CreateDeleteListInBoard(unittest.TestCase):
    
    board_id = None
    list_id = None

    def setUp(self): 
        self.create_board_endpoint = Endpoints.CREATE_BOARD
        self.delete_board_endpoint = Endpoints.DELETE_BOARD
        self.params_create_board = Endpoints.params_create_board
        self.params_delete_board = Endpoints.params_delete_board

        # list
        self.create_list_endpoint = Endpoints.CREATE_LIST
        self.params_create_list = Endpoints.params_create_list
        # card
        self.create_card_endpoint = Endpoints.CREATE_CARD
        self.params_create_card = Endpoints.params_create_card


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
        
        self.assertEqual(self.request.status_code, 200)
        self.assertEqual(self.params_create_card().get("name"), self.response.get("name"))
