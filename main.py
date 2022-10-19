from handlers import callback, client, extra, FSM_admin_mentors
from aiogram.utils import executor

from config import bot, dp
import logging
client.register_client_handler(dp)
callback.register_handler_callback(dp)
FSM_admin_mentors.register_handlers_fsm_anketa(dp)
extra.register_handlers_extra(dp)
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True)
