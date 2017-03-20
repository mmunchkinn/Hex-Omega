# import schedule
# import time
# from .utils import start_schedule_thread
#
# seed = 0
#
# print('starting scheduler within __init__....')
# schedule.every().day.at('09:00').do(start_schedule_thread)
#
#
# while len(schedule.jobs) > 0:
#     schedule.run_pending()
