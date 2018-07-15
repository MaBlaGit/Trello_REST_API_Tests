import os, datetime

def create_test_results(path):
    if not os.path.exists("test_results"):
        os.mkdir(path + "/test_results")
    return path + "/test_results/" 

def report_output_filename():
    get_current_time = datetime.datetime.now().strftime("%y-%m-%d-%H-%M")
    report_output_file = "html_report_{0}.html".format(get_current_time)
    return report_output_file
