import enum


class CardFormat(enum.Enum):
    JSON = 1
    CSV = 2


YELLOW_CLR_SYM = ['\033[93m', '\033[00m']
GREEN_CLR_SYM = ['\033[92m', '\033[00m']
RED_CLR_SYM = ['\033[91m', '\033[00m']
CYAN_CLR_SYM = ['\033[96m', '\033[00m']
