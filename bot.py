import config
import logging

from aiogram import Bot, Dispatcher, executor, types

from filters import IsAdminFilter

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.TOKEN)
dp = Dispatcher(bot)


dp.filters_factory.bind(IsAdminFilter)


@dp.message_handler(is_admin=True, commands=["ban"], commands_prefix="!/")
async def cmd_ban(message: types.Message):
    if not message.reply_to_message:
        await message.reply("Этой командой надо отвечать на сообщения хохлов!")
        return

    await message.bot.kick_chat_member(chat_id=config.GROUP_ID, user_id=message.reply_to_message.from_user.id)

    await message.reply_to_message.reply("Пользователь ебаный хохол!\nИ он пошел нахуй.")


@dp.message_handler(content_types=["new_chat_members"])
async def on_user_joined(message: types.Message):
    await message.delete()

@dp.message_handler()
async def filter_messages(message: types.Message):
    if "Слава Украине" in message.text:
        await message.reply("Слава России!")
        await message.delete()
    elif "слава украине" in message.text:
        await message.reply("Слава России!")
        await message.delete()
    elif "Слава Україні" in message.text:
        await message.reply("За Россию!")
        await message.delete()
    elif "За Украину" in message.text:
        await message.reply("За Россию!")
        await message.delete()
    elif "за украину" in message.text:
        await message.reply("За Россию!")
        await message.delete()
    elif "За Україну" in message.text:
        await message.reply("За Россию!")
        await message.delete()
    elif "Россия напала на Украину" in message.text:
        await message.reply("Слава России")
        await message.delete()
    elif "Путин хуйло" in message.text:
        await message.reply("Аххааххаха пошел нахуй ущемленный хохол жди пока в дом прилетит фаерболл! Слава России!!!!")
        await message.delete()

    elif "ПУТИН ХУЙЛО" in message.text:
        await message.reply("Аххааххаха пошел нахуй ущемленный хохол жди пока в дом прилетит фаерболл! Слава России!!!!")
        await message.delete()

    elif "путин хуйло" in message.text:
        await message.reply("Аххааххаха пошел нахуй ущемленный хохол жди пока в дом прилетит фаерболл! Слава России!!!!")
        await message.delete()
    elif "Андрей не лох" in message.text:
        await message.reply("Андрей лох!")
        await message.delete()
    elif "Миша лох" in message.text:
        await message.reply("Миша не лох, Мишок лучший")
        await message.delete()
    elif "Roblox топ" in message.text:
        await message.reply("Roblox помойка")
        await message.delete()
    elif "бот пидр" in message.text:
        await message.reply("Пошел нахуй этот бот ахуителен!Кст Слава России!!!")
        await message.delete()
    elif "Бот пидр" in message.text:
        await message.reply("Пошел нахуй этот бот ахуителен!Кст Слава России!!!")
        await message.delete()
    elif "Бот пидор" in message.text:
        await message.reply("Пошел нахуй этот бот ахуителен!Кст Слава России!!!")
        await message.delete()
    elif "бот пидор" in message.text:
        await message.reply("Пошел нахуй этот бот ахуителен!Кст Слава России!!!")
    elif "БОТ ПИДР" in message.text:
        await message.reply("Пошел нахуй этот бот ахуителен!Кст Слава России!!!")
        await message.delete()
    elif "БОТ ПИДОР" in message.text:
        await message.reply("Пошел нахуй этот бот ахуителен!Кст Слава России!!!")
        await message.delete()
    elif "bot pidr" in message.text:
        await message.reply("Пошел нахуй этот бот ахуителен!Кст Слава России!!!")
        await message.delete()
    elif "Bot pidr" in message.text:
        await message.reply("Пошел нахуй этот бот ахуителен!Кст Слава России!!!")
        await message.delete()
    elif "bot pidor" in message.text:
        await message.reply("Пошел нахуй этот бот ахуителен!Кст Слава России!!!")
        await message.delete()
    elif "Bot pidor" in message.text:
        await message.reply("Пошел нахуй этот бот ахуителен!Кст Слава России!!!")
        await message.delete()
    elif "BOT PIDR" in message.text:
        await message.reply("Пошел нахуй этот бот ахуителен!Кст Слава России!!!")
        await message.delete()
    elif "BOT PIDOR" in message.text:
        await message.reply("Пошел нахуй этот бот ахуителен!Кст Слава России!!!")
        await message.delete()


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)