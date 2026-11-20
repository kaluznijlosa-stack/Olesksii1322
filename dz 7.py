import logging
from datetime import datetime

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s: %(message)s"
)

date = datetime.now().strftime("%Y-%m-%d")

logging.info(f"Сьогодні: {date}")
