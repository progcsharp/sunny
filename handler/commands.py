from aiogram import types
# from aiogram.fsm.context import FSMContext
# from aiogram.types import InlineKeyboardMarkup
from aiogram.utils.keyboard import InlineKeyboardBuilder

# from State.form import Form
from config import ADMIN_ID
from db.handler.create import create_user
from db.handler.get import get_user_by_tg_id


async def cmd_start(message: types.Message):

    if await get_user_by_tg_id(message.from_user.id):
        await create_user(tg_id=message.from_user.id, nickname=message.from_user.username)

    web_app_info = types.WebAppInfo(
        url="https://sunny-flowers.bloommy.ru/")
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Открыть магазин",
        web_app=web_app_info)
    )

    await message.answer('''<b>👋 Приветствуем вас в нашем цветочном боте!</b>\n\n
Здесь каждый букет — это результат любви, заботы и свежести природы.
Мы поможем вам выбрать идеальную композицию: от утончённых роз до солнечных альстромерий.
<b>🎁 Готовы подарить радость вам и вашим близким?</b>\n
Выберите, что вам нужно, и мы всё оформим с душой!''', reply_markup=builder.as_markup(), parse_mode="HTML")


async def admin_cmd(message: types.Message):
    if not(message.from_user.id in ADMIN_ID):
        await message.answer("⛔ У вас нет прав администратора")
        return

    builder = InlineKeyboardBuilder()
    builder.add(
        types.InlineKeyboardButton(
            text="Изменить текста",
            callback_data="admin_edit_texts"
        ),
        types.InlineKeyboardButton(
            text="Провести рассылку",
            callback_data="admin_mailimg"
        )
    )
    builder.adjust(1)  # По одной кнопке в ряд

    await message.answer(
        "🛠️ <b>Административная панель</b>\n\n"
        "Выберите действие:",
        reply_markup=builder.as_markup(),
        parse_mode="HTML"
    )


