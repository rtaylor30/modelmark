from dataclasses import dataclass
from typing import List

from .node import Node

@dataclass
class Claim(Node):
    evidence: List[Evidence]
