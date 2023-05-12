from enum import Enum


class PostArticleStructureKind(str, Enum):
    PRODUCTION = "Production"
    STRUCTURE = "Structure"

    def __str__(self) -> str:
        return str(self.value)
