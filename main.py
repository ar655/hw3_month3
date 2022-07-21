from aiogram.utils import executor
from config import dp

import logging
from handlers import fsmAdminMenu

fsmAdminMenu.register_handlers_fsmAdminmenu(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp,skip_updates=True)