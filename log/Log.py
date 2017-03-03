from datetime import datetime

from HexOmega.settings import BASE_DIR

import os


class Log(object):
    def __init__(self, name, project_id):
        self.name = name
        self.project_id = project_id
        self.log_name = self.name + '_' + str(self.project_id)

    def log(self, level, content, **kwargs):
        data = datetime.now().strftime('%A, %d. %B %Y %I:%M%p')
        data += content

        outfile = os.path.join(BASE_DIR, os.path.join('projects', self.log_name))

        print('[{}] {}'.format(level, data), file=outfile)
