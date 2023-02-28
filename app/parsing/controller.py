import antlr4
from fastapi import APIRouter

from .mssql.grammar import TSqlLexer, TSqlParser
from .mssql.listeners import ExtractIdentifiers
from .mssql.visitors import JsonifyVisitor

router = APIRouter(prefix="/parse", tags=["parsing"])


@router.post("/mssql")
async def parse_sql_to_tree(body: str):
    # Construct an AST using antlr
    lexer = TSqlLexer(antlr4.FileStream(body))
    stream = antlr4.CommonTokenStream(lexer)
    parser = TSqlParser(stream)

    # Jsonify
    return JsonifyVisitor().visit(parser.tsql_file())


@router.post("/mssql/vocab")
async def parse_sql_to_vocab(body: str):
    # Construct an AST using antlr
    lexer = TSqlLexer(antlr4.FileStream(body))
    stream = antlr4.CommonTokenStream(lexer)
    parser = TSqlParser(stream)

    # Listen for IDs
    listener = ExtractIdentifiers()
    antlr4.ParseTreeWalker(parser.tsql_file(), listener)
    return listener.ids


@router.post("/question")
async def parse_question_to_tree(body: str):
    ...


@router.post("/question/vocab")
async def parse_question_to_vocab(body: str):
    ...
