import antlr4
from fastapi import APIRouter
from pydantic import BaseModel

from .mssql.grammar import TSqlLexer, TSqlParser
from .mssql.listeners import ExtractIdentifiers
from .mssql.visitors import JsonifyVisitor

router = APIRouter(prefix="/parse", tags=["parsing"])


class QueryBody(BaseModel):
    text: str


@router.post("/mssql")
async def parse_sql_to_tree(body: QueryBody):
    # Construct an AST using antlr
    lexer = TSqlLexer(antlr4.InputStream(body.text))
    stream = antlr4.CommonTokenStream(lexer)
    parser = TSqlParser(stream)

    # Jsonify
    return JsonifyVisitor().visit(parser.tsql_file())


@router.post("/mssql/vocab")
async def parse_sql_to_vocab(body: QueryBody):
    # Construct an AST using 
    lexer = TSqlLexer(antlr4.InputStream(body.text))
    stream = antlr4.CommonTokenStream(lexer)
    parser = TSqlParser(stream)

    # Listen for IDs
    listener = ExtractIdentifiers()
    antlr4.ParseTreeWalker().walk(listener, parser.tsql_file())

    return {
        "text": body.body,
        "vocab": listener.ids
    }


@router.post("/question")
async def parse_question_to_tree(body: str):
    ...


@router.post("/question/vocab")
async def parse_question_to_vocab(body: str):
    ...
