from typing import Protocol

from textve.models import LegalDocument


class Source(Protocol):
    name: str

    def list_ids(self) -> list[str]: ...

    def fetch(self, item_id: str) -> None: ...

    def parse(self, item_id: str) -> LegalDocument: ...
