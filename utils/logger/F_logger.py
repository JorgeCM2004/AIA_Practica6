import logging
import os
from logging.handlers import RotatingFileHandler

os.makedirs("logs", exist_ok=True)

logger = logging.getLogger("Medical_Copilot")
logger.setLevel(logging.INFO)

formato = logging.Formatter(
	"%(asctime)s - %(levelname)s - %(message)s", datefmt="%Y-%m-%d %H:%M:%S"
)

file_handler = RotatingFileHandler("logs/backend.log", maxBytes=5000000, backupCount=10)
file_handler.setFormatter(formato)

console_handler = logging.StreamHandler()
console_handler.setFormatter(formato)

if not logger.handlers:
	logger.addHandler(file_handler)
	logger.addHandler(console_handler)
