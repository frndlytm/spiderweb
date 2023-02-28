import antlr4
from .grammar import TSqlParserVisitor


class JsonifyVisitor(TSqlParserVisitor):
    def visitChildren(ctx: antlr4.RuleContext) -> dict:
        ...
