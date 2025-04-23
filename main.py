import asyncio

from aiogram import Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from config import bot
from keyboards.set_commands import set_commands
from register_handler.reg_callback import register_handlers_callback
from register_handler.reg_commands import register_handlers_commands
from register_handler.reg_message import register_handlers_message


async def main():
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)

    await set_commands(bot)

    await register_handlers_commands(dp)
    await register_handlers_callback(dp)
    await register_handlers_message(dp)

    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())



# import asyncio
# from contextlib import asynccontextmanager
#
# import uvicorn
# from aiogram.types import Update
# # from aiogram import Dispatcher
# # from aiogram.fsm.storage.memory import MemoryStorage
# from fastapi import FastAPI
# from fastapi.requests import Request
#
# from config import bot, dp
# from keyboards.set_commands import set_commands
# # from keyboards.set_commands import set_commands
# from register_handler.reg_callback import register_handlers_callback
# from register_handler.reg_commands import register_handlers_commands
# # from register_handler.reg_message import register_handlers_message
#
#
# # async def main():
# #     # storage = MemoryStorage()
# #     # dp = Dispatcher(storage=storage)
# #
# #     # await set_commands(bot)
# #
# #     await register_handlers_commands(dp)
# #     await register_handlers_callback(dp)
# #     await register_handlers_message(dp)
#
#     # await dp.start_polling(bot)
#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await set_commands(bot)
#
#     await bot.set_webhook(url="https://428a-85-91-213-213.ngrok-free.app/webhook",
#                           allowed_updates=[
#                               "message", "callback_query", "message_reaction"
#                           ],
#     drop_pending_updates=True)
#     yield
#     await bot.delete_webhook()
#
# app = FastAPI(lifespan=lifespan)
#
# @app.post("/webhook")
# async def webhook(request: Request) -> None:
#     j = await request.json()
#     print(await request.json())
#     await register_handlers_commands(dp)
#     await register_handlers_callback(dp)
#     # await register_handlers_message(dp)
#     update = Update.model_validate(await request.json(), context={"bot": bot})
#     await dp.feed_update(bot, update)
#
#
# if __name__ == "__main__":
#     uvicorn.run(app, port=8080)

# if __name__ == '__main__':
#     asyncio.run(main())
#
# import logging
# from aiogram.client.default import DefaultBotProperties
# from aiogram import Bot, Dispatcher, F
# from aiogram.types import Message, Update
# from aiogram.filters import CommandStart
# from aiogram.enums import ParseMode
# from fastapi import FastAPI
# from fastapi.responses import HTMLResponse
# from fastapi.staticfiles import StaticFiles
# from fastapi.templating import Jinja2Templates
# from fastapi.requests import Request
# import uvicorn
# from contextlib import asynccontextmanager
#
# from sqlalchemy.util import await_only
#
# from register_handler.reg_callback import register_handlers_callback
# from register_handler.reg_commands import register_handlers_commands
# from register_handler.reg_message import register_handlers_message
#
# bot = Bot(token='5488557457:AAF-ugjhaQ_NbJSP9eYF3Z6mBvgVZOz4YaU',
#           default=DefaultBotProperties(parse_mode=ParseMode.HTML))
# dp = Dispatcher()
#
#
# @asynccontextmanager
# async def lifespan(app: FastAPI):
#     await bot.set_webhook(url="https://4be2-89-110-117-85.ngrok-free.app/webhook",
#                           allowed_updates=[
#                               "message", "callback_query", "message_reaction"
#                           ],
#     drop_pending_updates=True)
#     yield
#     await bot.delete_webhook()
#
#
# app = FastAPI(lifespan=lifespan)
#
#
# # @dp.message(CommandStart())
# # async def start(message: Message) -> None:
# #     await message.answer('Привет!')
# #
#
# @app.get("/", response_class=HTMLResponse)
# async def read_root(request: Request):
#     return HTMLResponse('<h1>Hello, world!</h1>')
#
#
# @app.post("/webhook")
# async def webhook(request: Request) -> None:
#     j = await request.json()
#     print(await request.json())
#     await register_handlers_commands(dp)
#     await register_handlers_callback(dp)
#     await register_handlers_message(dp)
#     update = Update.model_validate(await request.json(), context={"bot": bot})
#     await dp.feed_update(bot, update)
#
#
# if __name__ == "__main__":
#     uvicorn.run(app, port=8080)