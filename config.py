from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

TOKEN="7689561730:AAE-dc4V7Jn-Z5CCbkFKr0vEOsW8GoxDPZ0"
BD="sqlite:///db.db"
ADMIN_ID=[1028962949]

storage = MemoryStorage()
dp = Dispatcher(storage=storage)
bot = Bot(token=TOKEN)
