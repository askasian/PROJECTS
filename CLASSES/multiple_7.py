import dataclasses


@dataclasses.dataclass
class PdfFileRecord:
    name: str
    type: str
    cache: dict
    data: dict = dataclasses.field(default_factory=dict)
    accessed: str = dataclasses.field(default_factory=lambda: datetime.now().isoformat())
