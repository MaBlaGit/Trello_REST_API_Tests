import unittest
import HTMLTestRunner
import os
import datetime
from tests.trello_01_create_delete_board import CreateBoardDeleteBoard
from tests.trello_02_create_delete_list_in_board import CreateDeleteListInBoard
from utilities import helper


create_board_delete_board_tests = unittest.TestLoader().loadTestsFromTestCase(CreateBoardDeleteBoard)
create_delete_list_in_board_tests = unittest.TestLoader().loadTestsFromTestCase(CreateDeleteListInBoard)

create_test_suite = unittest.TestSuite([create_board_delete_board_tests, 
                                        create_delete_list_in_board_tests])

reporter_path = helper.create_test_results(os.getcwd())
html_report = helper.report_output_filename()

report_output = open(reporter_path + html_report, "wb")


if __name__ == '__main__':
    runner = HTMLTestRunner.HTMLTestRunner(stream=report_output,
                                           title='Trello_REST_API_Tests_Report',
                                           description='REST_API_testing_for_createng_deleting_board_card_list_comments'
                                           )
    runner.run(create_test_suite)
