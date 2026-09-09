from dataclasses import dataclass
from typing import List, Optional

@dataclass
class ExternalReference(Node):
    url: Optional[str]
    isbn: Optional[str]
    quotes: List[str]
    bookmarks: List[str]

