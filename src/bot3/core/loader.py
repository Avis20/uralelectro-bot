from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.fsm.storage.base import DefaultKeyBuilder
from aiogram.fsm.storage.redis import RedisStorage
from aiohttp import web
from redis.asyncio import ConnectionPool, Redis

from bot3.settings import Settings

settings = Settings()

app = web.Application()

token = settings.bot.token

bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

redis_client = Redis(
    connection_pool=ConnectionPool(
        host=settings.cache.REDIS_HOST,
        port=settings.cache.REDIS_PORT,
        password=settings.cache.REDIS_PASS,
        db=0,
    ),
)

storage = RedisStorage(
    redis=redis_client,
    key_builder=DefaultKeyBuilder(with_bot_id=True),
)

dp = Dispatcher(storage=storage)

DEBUG = settings.DEBUG
