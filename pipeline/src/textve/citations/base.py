from typing import Protocol

from textve.models import Citation


class CitationExtractor(Protocol):
    def extract(self, text: str, own_document: str, own_chapter: str | None) -> list[Citation]: ...

    def is_bemyndigande(self, text: str) -> bool: ...
