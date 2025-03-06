import time
from set_log import init_logger
from config import *
import pyautogui as pg


logger = init_logger(__name__)


def open_feishu():
    feishu = pg.locateOnScreen(FEISHU_BUTTON_PATH, confidence=0.9)
    button_feishu = pg.center(feishu)
    pg.click(button_feishu)


def close_feishu():
    close = pg.locateOnScreen(CLOSE_BUTTON_PATH)
    button_close = pg.center(close)
    pg.click(button_close)


def execute_operation():
    fail_times = 0
    for _ in range(REPEAT_TIMES):
        try:
            open_feishu()
        except pg.ImageNotFoundException:
            continue
        time.sleep(60)
        try:
            close_feishu()
            time.sleep(5)
        except pg.ImageNotFoundException:
            logger.error("未找到关闭按钮")
            fail_times += 1
            continue
    logger.info(f"打开飞书次数：{REPEAT_TIMES}, 失败次数：{fail_times}")
