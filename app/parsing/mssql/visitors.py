import antlr4
from .grammar import TSqlParserVisitor


class JsonifyVisitor(TSqlParserVisitor):
    def handle_type_name(self, ctx: antlr4.ParserRuleContext) -> str:
        type_ = ctx.__class__.__name__
        type_ = type_.replace("Context", "")
        return type_.lower()

    def visit(self, ctx: antlr4.ParserRuleContext) -> dict:
        if not isinstance(ctx, antlr4.TerminalNode):
            return {
                "type": self.handle_type_name(ctx),
                "text": ctx.getText(),
                "children": self.visitChildren(ctx)
            }
    
    def visitChildren(self, ctx: antlr4.ParserRuleContext) -> list:
        return list(filter(bool, map(self.visit, ctx.getChildren())))
