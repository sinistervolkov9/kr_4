import os
from pathlib import Path

HH_API_KEY: str = os.getenv("HH_API_KEY")
SUPERJOB_API_KEY: str = os.environ.get("SUPERJOB_API_KEY")

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath("data", "vacancies.json")
