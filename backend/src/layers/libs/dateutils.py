from datetime import datetime

def get_current_timestamp():
    return datetime.now().timestamp()

def to_unix_timestamp(timestamp: float):
    return timestamp * 1000
