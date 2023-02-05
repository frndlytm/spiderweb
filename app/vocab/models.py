from enum import Enum

from pydantic import BaseModel, Field


class Tag(BaseModel):
    type_: str = Field(..., alias="type")
    tag: str = Field(...)
    description: str = Field(...)


class DiffType(Enum):
    ADD = 1
    NOOP = 0
    REMOVE = -1

    # fmt:off
    def __str__(self):
        if self.value < 0:    return "- "
        elif self.value == 0: return ""
        else:                 return "+ "
    # fmt:on


class Diff(BaseModel):
    type_: DiffType = Field(..., alias="type")
    term: str = Field(...)

    def __str__(self):
        return f"{str(self.type_)}{self.term}"


class Vocab(BaseModel):
    name: str = Field(...)
    version: str = Field(0)
    tags: list[Tag] = Field(default_factory=list)
    terms: list[str] = Field(default_factory=list)

    def __key__(self):
        return f"{self.name}:{self.version}"


class VocabDiffs(BaseModel):
    success: bool
    vocab: Vocab
    diffs: list[Diff]
