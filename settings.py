import os
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

SUPERJOB_API_KEY: str = os.getenv("SUPERJOB_API_KEY")
SUPERJOB_API_KEY = SUPERJOB_API_KEY.replace(" ", "").replace("\t", "").replace("\n", "").replace("\r", "")

ROOT_PATH = Path(__file__).parent
DATA_PATH = ROOT_PATH.joinpath("data", "vacancies.json")
DATA_PATH_HH = ROOT_PATH.joinpath("data", "vacancies_hh.json")
DATA_PATH_SJ = ROOT_PATH.joinpath("data", "vacancies_sj.json")
