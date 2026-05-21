import functools

def log_action(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"\n[SYSTEM LOG] Operation '{func.__name__}' is executing...")
        result = func(*args, **kwargs)
        print("[SYSTEM LOG] Operation completed successfully! ✅")
        return result
    return wrapper