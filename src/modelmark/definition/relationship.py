from dataclasses import dataclass

@dataclass
class Relationship:
    id: UUID = field(default_factory=lambda: uuid7())
    slug: str
    from_id: UUID
    to_id: UUID
    $content: str
