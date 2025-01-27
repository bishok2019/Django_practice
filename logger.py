def log_method_call(func):
    def wrapper(*args, **kwargs):
        print(f"Calling method: {func.__name__}")  # Log the method name
        result = func(*args, **kwargs)  # Call the original method
        print(f"Method: {func.__name__} executed successfully.")  # Log success
        return result
    return wrapper

# log_method_call()