from datetime import datetime

from users.models import MemberUser, LeaderUser, AdminUser


# To do:
#   1.  test the log function, once others are done with the module.
#   2.  add a function to parse each line of a given log file and
#       render them into a HTML structure for use in a view.

def log(level, username, content, **kwargs):
    """
    Log function.
    Call from any function or context with the required parameters to
    write to the appropriate log file. Can use threading for pseudo
    non-blocking IO but due to some constraints have reasoned otherwise.

    :param level: either: INFO, WARNING or SUCCESS
    :param username: Username of user who called a function with log.
    :param content: the path to the log
    :param kwargs: random kwargs to add to the log message.
    Will add implementation only if needed.
    :return: None
    """
    # the content attribute of the project has the entire
    # path from BASE_DIR(mentioned in settings.py).
    l = MemberUser.objects.get(username__contains=username)
    # print(l.username)

    data = datetime.now().strftime('%A, %d. %B %Y %I:%M%p') + ' '
    # data += content

    logfile = l.project.activitylog.content

    if logfile is '':
        raise ValueError('Empty path to log file.')
    else:
        print('[{}] [{}] [{}] [{}] [{}]'.format(level, l.username, l.project.name, data, content), file=open(logfile, 'w+'))
