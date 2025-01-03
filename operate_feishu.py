import time
from set_log import init_logger
from config import settings
import pyautogui as pg


logger = init_logger(__name__)


def open_feishu():
    feishu = pg.locateOnScreen(settings['feishu_button_path'], confidence=0.9)
    button_feishu = pg.center(feishu)
    pg.click(button_feishu)


def close_feishu():
    close = pg.locateOnScreen(settings['close_button_path'])
    button_close = pg.center(close)
    pg.click(button_close)


def execute_operation():
    fail_times = 0
    for _ in range(settings['execution_times']):
        open_feishu()
        time.sleep(30)
        try:
            close_feishu()
            time.sleep(1)
        except pg.ImageNotFoundException:
            logger.error("未找到关闭按钮")
            fail_times += 1
            continue
    logger.info(f"打开飞书次数：{settings['execution_times']}, 失败次数：{fail_times}")
