import schedule
import time
from set_log import init_logger
from config import settings
from connect_to_campus_web import AutoConnect
from operate_feishu import execute_operation

logger = init_logger(__name__)


# 设置每天早上的任务
def morning_task():
    logger.info("开始执行早间任务...")
    auto_connect = AutoConnect(settings['student_id'], settings['student_pwd'])  # 请根据实际需要替换ID和密码
    auto_connect.connect()
    execute_operation()
    logger.info("早间任务执行完成。")


# 设置每天晚上的任务
def evening_task():
    logger.info("开始执行晚间任务...")
    execute_operation()
    logger.info("晚间任务执行完成。")


# 安排任务
def schedule_weekday_tasks():
    if settings['pattern'] == 'only_morning':
        # 安排早间任务
        for day in [schedule.every().monday, schedule.every().tuesday, schedule.every().wednesday,
                    schedule.every().thursday, schedule.every().friday]:
            day.at(settings['morning_time']).do(morning_task)
    if settings['pattern'] == 'only_evening':
        # 安排晚间任务
        for day in [schedule.every().monday, schedule.every().tuesday, schedule.every().wednesday,
                    schedule.every().thursday, schedule.every().friday]:
            day.at(settings['evening_time']).do(evening_task)
    if settings['pattern'] == 'both':
        # 安排早间和晚间任务
        for day in [schedule.every().monday, schedule.every().tuesday, schedule.every().wednesday,
                    schedule.every().thursday, schedule.every().friday]:
            day.at(settings['morning_time']).do(morning_task)
        for day in [schedule.every().monday, schedule.every().tuesday, schedule.every().wednesday,
                    schedule.every().thursday, schedule.every().friday]:
            day.at(settings['evening_time']).do(evening_task)


# 安排任务
schedule_weekday_tasks()

# 启动任务调度
logger.info("任务调度已启动...")
while True:
    schedule.run_pending()
    time.sleep(1)
