from .grammar import TSqlParser, TSqlParserListener


class ExtractIdentifiers(TSqlParserListener):
    def __init__(self):
        self.ids = []

    def enterId_(self, ctx: TSqlParser.Id_Context):
        self.ids.append(ctx.getText())
