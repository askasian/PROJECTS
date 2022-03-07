from datetime import datetime
from typing import NamedTuple


class _PdfContentRecord(NamedTuple):
    filename: str
    page: int
    cache: dict
    data: dict = None
    accessed: str = None


class PdfContentRecord(_PdfContentRecord):
    def __new__(cls, filename, page, cache, data=None, accessed=None):
        if data is None:
            data = {}
        if accessed is None:
            accessed = datetime.now().isoformat()
        return super().__new__(cls, filename, page, cache, data, accessed)
