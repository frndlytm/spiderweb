from typing import SupportsFloat

from fastapi import APIRouter
from .models import Tag

router = APIRouter(prefix="/vocab", tags=["vocab"])


@router.get("/{name}")
async def get_vocab_latest(name: str):
    key = f"{name}"


@router.get("/{name}:{version}")
async def get_vocab_by_version(name: str, version: int):
    key = f"{name}:{version}"


@router.post("/{name}")
async def set_vocab(name: str, terms: str, sep: str = "\n"):
    ...


@router.patch("/{name}")
async def extend_vocab(name: str, terms: str, sep: str = "\n"):
    ...


@router.post("/{name}/tags")
async def add_tag(name: str, tags: list[Tag]):
    ...
