from dataclasses import dataclass, field
from uuid import UUID, uuid7

@dataclass
class Node:
    id: UUID = field(default_factory=lambda: uuid7())
    slug: str
    $content: str
