import logging
from datetime import datetime

# Налаштовуємо logging
logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

# Отримуємо поточну дату
date = datetime.now().strftime("%Y-%m-%d")

# Записуємо дату в повідомлення INFO
logging.info(f"Сьогодні: {date}")
