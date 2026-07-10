import logging
from pathlib import Path
from datetime import datetime

# Create logs directory
LOG_DIR = Path.cwd() / "logs"
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Create log file
LOG_FILE = LOG_DIR / f"{datetime.now().strftime('%Y_%m_%d_%H_%M_%S')}.log"

# Configure logging
logging.basicConfig(
    filename=str(LOG_FILE),
    format="[%(asctime)s] %(levelname)s - %(message)s",
    level=logging.INFO,
    force=True
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    logger.info("Logger initialized successfully.")
    print(f"Log file created at: {LOG_FILE}")