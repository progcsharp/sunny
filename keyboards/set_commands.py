from aiogram.types import BotCommand, WebAppInfo, MenuButtonWebApp


async def set_commands(bot):
    # commands = [
    #     BotCommand(command="open", description="Открыть WebApp",
    #                web_app=WebAppInfo(url="https://ar-test.ru/?action=wptelegram_login_webapp&confirm_login=0&redirect_to=https://ar-test.ru/"))
    # ]
    # await bot.set_my_commands(commands)
    menu_button = MenuButtonWebApp(
        text="Открыть",
        web_app=WebAppInfo(url="https://sunny-flowers.bloommy.ru/?action=wptelegram_login_webapp&confirm_login=0&redirect_to=https://sunny-flowers.bloommy.ru/")
    )

    await bot.set_chat_menu_button(menu_button=menu_button)

