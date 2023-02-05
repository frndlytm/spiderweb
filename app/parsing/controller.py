from fastapi import APIRouter

router = APIRouter(prefix="/parse", tags=["parsing"])


@router.post("/mssql")
async def parse_sql_to_tree(body: str):
    ...


@router.post("/mssql/vocab")
async def parse_sql_to_vocab(body: str):
    ...


@router.post("/question")
async def parse_question_to_tree(body: str):
    ...


@router.post("/question/vocab")
async def parse_question_to_vocab(body: str):
    ...
