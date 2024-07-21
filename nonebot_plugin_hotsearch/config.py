from nonebot import get_driver
from nonebot.log import logger


class Config:

    plugin_config = get_driver().config

    def __init__(self) -> None:
        try:
            self.hotsearch_cnt = self.plugin_config.hotsearch_cnt
        except:
            self.hotsearch_cnt: int = 10
            logger.error("未找到hotsearch_cnt配置项,使用默认值10")


plugin_config = Config()
