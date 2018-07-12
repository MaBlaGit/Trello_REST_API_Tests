import unittest, requests
from config import Credentials, BoardName, Endpoints

class CreateBoardDeleteBoard(unittest.TestCase):

    board_id = None

    def setUp(self): 
        self.create_board_endpoint = Endpoints.CREATE_BOARD
        self.delete_board_endpoint = Endpoints.DELETE_BOARD
        self.params_create_board = Endpoints.params_create_board
        self.params_delete_board = Endpoints.params_delete_board

    def test_01_create_board(self):
        self.request = requests.post(self.create_board_endpoint, params=self.params_create_board())
        self.response = self.request.json()
        self.json = self.response.get("id")
        CreateBoardDeleteBoard.board_id = self.json

        self.assertEqual(self.request.status_code, 200)
        self.assertEqual(self.params_create_board().get("name"), self.response.get("name"))

    def test_02_delete_board(self):
        self.request = requests.delete(self.delete_board_endpoint + CreateBoardDeleteBoard.board_id, params=self.params_delete_board())

        self.assertEqual(self.request.status_code, 200)
        self.assertNotIn(CreateBoardDeleteBoard.board_id, self.request)

    def tearDown(self):
        self.board_id = None
