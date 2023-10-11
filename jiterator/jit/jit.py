"""This is where the class for the context manager is."""
from collections.abc import Iterator, Any
from contextlib import contextmanager

class JitContextManager:
    """The class for the context manager."""

    def __init__(self, iterator: Iterator):
        """Initializer the context manager taking in an iterator as an argument."""
        self.iterator = iterator

    def __enter__(self):
        """Called as soon as the context manager is used."""
        # TODO: use subprocess.run() to use the jit compiler in pypy
    def __exit__(self, exception_type, execution_value, execution_traceback):
        """Called when the context manager's usage is done."""
        print(f"exited with type: {exception_type}, value: {execution_value}, and tb: {execution_traceback}")

### Possible alternative implementation below
@contextmanager
def jiterator(iterator: Iterator, operation: Callable[[Iterator],Any]) -> :
    """Sets a destination for exported files."""
    iterator = iterator
    try:
        subprocess.run("pypy --jit on")
        result = operation(iterator)
        yield # possibly yield result?
    finally:
        # print(f"exited with type: {exception_type}, value: {execution_value}, and tb: {execution_traceback}")
        subprocess.run("pypy --jit off")
