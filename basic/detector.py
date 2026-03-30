import os

def detect_environment():
    if os.path.exists("/.dockerenv"):
        return "breeze"
    return "host"
