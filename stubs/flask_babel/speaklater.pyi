from flask_babel._compat import text_type as text_type
from typing import Any

class LazyString:
    def __init__(self, func: Any, *args: Any, **kwargs: Any) -> None: ...
    def __getattr__(self, attr: Any): ...
    def __len__(self): ...
    def __getitem__(self, key: Any): ...
    def __iter__(self) -> Any: ...
    def __contains__(self, item: Any): ...
    def __add__(self, other: Any): ...
    def __radd__(self, other: Any): ...
    def __mul__(self, other: Any): ...
    def __rmul__(self, other: Any): ...
    def __lt__(self, other: Any) -> Any: ...
    def __le__(self, other: Any) -> Any: ...
    def __eq__(self, other: Any) -> Any: ...
    def __ne__(self, other: Any) -> Any: ...
    def __gt__(self, other: Any) -> Any: ...
    def __ge__(self, other: Any) -> Any: ...
    def __html__(self): ...
    def __hash__(self) -> Any: ...
    def __mod__(self, other: Any): ...
    def __rmod__(self, other: Any): ...
