import telebot
from environs import Env
from telebot.handler_backends import State, StatesGroup
from telebot.storage import StateMemoryStorage
from telebot.types import BotCommand

from bot.todo.keybords import languages_inline_btn, share_phone_btn
from bot.todo.messages import messages
from bot.todo.task import Chat
from bot.utils import write_row_to_csv, get_fullname

env = Env()
env.read_env("../.env")

BOT_TOKEN = env("BOT_TOKEN")

state_storage = StateMemoryStorage()

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="html", state_storage=state_storage)


# States
class StudentRegistrationForm(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    age = State()
    language = State()
    course = State()


# /start
@bot.message_handler(commands=["start"])
def welcome_message(message):
    chat_id = message.chat.id
    user = message.from_user
    fullname = get_fullname(user.first_name, user.last_name)
    bot.send_message(chat_id, f"Assalomu alaykum, {fullname}", reply_markup=languages_inline_btn)
    # bot.register_next_step_handler(message, set_language_handler)


# def set_language_handler(message):
#     chat = message.chat
#     new_chat = Chat(
#         chat.id,
#         get_fullname(chat.first_name, chat.last_name),
#         LANGUAGES.get(message.text)
#     )
#     write_row_to_csv(
#         "chats.csv",
#         list(new_chat.get_attrs_as_dict().keys()),
#         new_chat.get_attrs_as_dict()
#     )
#     bot.send_message(chat.id, messages[LANGUAGES.get(message.text)].get("add_task"), reply_markup=ReplyKeyboardRemove())


@bot.callback_query_handler(lambda call: call.data.startswith("language_"))
def set_language_query_handler(call):
    message = call.message
    lang_code = call.data.split("_")[1]
    chat = message.chat
    new_chat = Chat(
        chat.id,
        get_fullname(chat.first_name, chat.last_name),
        lang_code
    )
    write_row_to_csv(
        "chats.csv",
        list(new_chat.get_attrs_as_dict().keys()),
        new_chat.get_attrs_as_dict()
    )
    bot.delete_message(chat.id, message.id - 1)
    bot.delete_message(chat.id, message.id)
    bot.send_message(chat.id, messages[lang_code].get("add_task"))


@bot.message_handler(commands=["register"])
def register_student_handler(message):
    bot.send_message(message.chat.id, "Ismingizni kiriting:")
    bot.set_state(message.from_user.id, StudentRegistrationForm.first_name, message.chat.id)


@bot.message_handler(state=StudentRegistrationForm.first_name)
def first_name_get(message):
    print(message)
    bot.send_message(message.chat.id, 'Familyangizni kiriting:')
    bot.set_state(message.from_user.id, StudentRegistrationForm.last_name, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['first_name'] = message.text


@bot.message_handler(state=StudentRegistrationForm.last_name)
def last_name_get(message):
    bot.send_message(message.chat.id, 'Telefon raqaminingizni yuboring:', reply_markup=share_phone_btn)
    bot.set_state(message.from_user.id, StudentRegistrationForm.phone, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        data['last_name'] = message.text


@bot.message_handler(state=StudentRegistrationForm.phone)
def phone_get(message):
    bot.send_message(message.chat.id, 'Yoshingizni kiriting:')
    bot.set_state(message.from_user.id, StudentRegistrationForm.age, message.chat.id)
    with bot.retrieve_data(message.from_user.id, message.chat.id) as data:
        print(data)
        data['phone'] = message.text

    bot.delete_state(message.from_user.id, message.chat.id)


#
# # /add
# @bot.message_handler(commands=["add"])
# def add_task_handler(message):
#     chat_id = message.chat.id
#     lang_code = get_language_code_by_chat_id(chat_id, "chats.csv")
#     msg = messages[lang_code].get("send_task")
#     bot.send_message(message.chat.id, msg)
#
#     bot.register_next_step_handler(message, get_task_handler)
#
#
# @bot.message_handler(content_types=["text"])
# def get_task_handler(message):
#     chat_id = message.chat.id
#     if message.content_type != "text":
#         bot.send_message(chat_id, "Invalid format.")
#
#     new_task = Task(chat_id, message.text, datetime.now())
#     write_row_to_csv(
#         "tasks.csv",
#         list(new_task.get_attrs_as_dict().keys()),
#         new_task.get_attrs_as_dict()
#     )
#
#     bot.send_message(chat_id, "Add successfully.")


def my_commands():
    return [
        BotCommand("/start", "Start bot"),
        BotCommand("/add", "Add new task"),
        BotCommand("/register", "Register student")
    ]


if __name__ == "__main__":
    print("Started...")
    bot.set_my_commands(commands=my_commands())
    bot.infinity_polling()
