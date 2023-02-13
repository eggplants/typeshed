from typing_extensions import Callable, Iterable, ParamSpec, TypeVar

P = ParamSpec('P')
R = TypeVar('R')

__all__ = ["thread_map", "process_map"]

def thread_map(fn: Callable[P, R], *iterables: Iterable[P.args], **tqdm_kwargs) -> list[R]: ...
def process_map(fn: Callable[P, R], *iterables: Iterable[P.args], **tqdm_kwargs) -> list[R]: ...
