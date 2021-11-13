from functools import wraps, update_wrapper


class SimpleDecoratorClass:  # @SimpleDecoratorClass

    def __init__(self, function):
        self.function = function

    def __call__(self, *args, **kwargs):
        return self.function(*args, **kwargs)


class ComplexDecoratorClass:  # @ComplexDecoratorClass(*args, **kwargs)

    def __init__(self, *init_args, **init_kwargs):
        self.args = init_args
        self.kwargs = init_kwargs

    def __call__(self, function):
        @wraps(function)
        def wrapped(*args, **kwargs):
            return function(*args, **kwargs)
        return wrapped


class GeneralDecoratorClass:

    def __init__(self, *init_args, **init_kwargs):
        if len(init_args) == 1 and not init_kwargs:
            self._setup_simple(init_args[0])
        else:
            self._setup_complex(init_args, init_kwargs)

    def __call__(self, *args, **kwargs):
        return self._wrapper(*args, **kwargs)

    def _setup_simple(self, function):
        self._wrapper = lambda *args, **kwargs: function(*args, **kwargs)
        self.function = function
        update_wrapper(self, function)

    def _setup_complex(self, init_args, init_kwargs):
        def _wrapper(function):
            @wraps(function)
            def inner(*args, **kwargs):
                return function(*args, **kwargs)
            return inner
        self._wrapper = _wrapper
        self.args = init_args
        self.kwargs = init_kwargs
