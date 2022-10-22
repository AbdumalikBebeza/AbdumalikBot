from handlers import callback, client, extra, FSM_admin_mentors, admin
from aiogram.utils import executor
from database.bot_db import sql_create
from config import bot, dp
import logging


async def on_startup(_):
    sql_create()


admin.register_message_admin(dp)
client.register_client_handler(dp)
callback.register_handler_callback(dp)
FSM_admin_mentors.register_handlers_fsm_anketa(dp)
extra.register_handlers_extra(dp)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup)
