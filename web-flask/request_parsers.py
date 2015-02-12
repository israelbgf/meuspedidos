def safe_int(value, fallback=None):
    try:
        return int(value)
    except:
        return fallback