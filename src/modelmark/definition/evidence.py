from dataclasses import dataclass, field
from typing import List

from .node import Node

@dataclass
class Evidence(Node):
    citations: List[ExternalReference] = field(default_factory=lambda: [])

