from enum import Enum


class Transmission(str, Enum):
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"
    CVT = "CVT"
    SINGLE_SPEED = "Single Speed"
