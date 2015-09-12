import os


class build(object):
    def __init__(self, x, y):
        self.static_folder = 'reports'
        self.x = x
        self.y = y

    def foundation(self):

        return self.folderStructure()

    def folderStructure(self):

        report_folder = '/'.join([self.x, self.static_folder, self.y + ".txt"])

        if self.making_request_directory(report_folder):
            return str(report_folder)

        else:
            return str(report_folder)

    def making_request_directory(self, report_folder):

        trying_directory = os.path.dirname(report_folder)

        try:
            os.stat(trying_directory)
            return True

        except:
            os.mkdir(trying_directory)
            return False
