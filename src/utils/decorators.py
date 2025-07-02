__all__ = ['run_every','event_listener']

def run_every(ms) -> None:
    """
    Decorator for scene methods to run approximately every `ms` milliseconds.

    This is typically used in game loops to throttle how often a method is called.
    Requires the object to have an `is_time(ms)` method.

    Args:
        ms (int): Millisecond interval at which the decorated method should run.
    """
    def decorator(method):
        def wrapper(self, *args, **kwargs):
            if self is None:
                raise ValueError("The decorator was applied to a function, not a method")
            if not hasattr(self, 'is_time'):
                raise ValueError("The decorator was applied to a method that lacks 'is_time'")
            if self.is_time(ms):
                return method(self, *args, **kwargs)
        return wrapper
    return decorator


def event_listener(event_name) -> None:
    """
    Decorator for scene methods to run when a specific event is triggered.

    Requires the object to implement an `is_custom_event(event_name)` method.

    Args:
        event_name (str): The name of the event to listen for.
    """
    def decorator(method):
        def wrapper(self=None, *args, **kwargs):
            if self is None:
                raise ValueError("The decorator was applied to a function, not a method")
            if not hasattr(self, 'is_custom_event'):
                raise ValueError("The decorator was applied to a method that lacks 'is_custom_event'")
            if self.is_custom_event(event_name):
                return method(self, *args, **kwargs)
        return wrapper
    return decorator
