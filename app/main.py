from fastapi import FastAPI
from starlette.responses import RedirectResponse

from app import parsing, vocab

api = FastAPI(
    title="spiderweb",
    version="1.0",
    description="Locally hosted RDF store for exploring the Spider Text-to-SQL dataset.",
    license_info={"name": "The MIT License (MIT)"},
    contact={
        "name": "Christian DiMare-Baits",
        "url": "https://frndlytm.github.io/contact",
        "email": "frndlytm@gmail.com",
    },
    openapi_tags=[
        {
            "name": "parser",
            "description": "Operations to recognize and extract entities and relations."
        },
        {
            "name": "vocab",
            "description": "Operations to create, edit, and read vocabularies."
        },
    ]
)

api.include_router(parsing.router)
api.include_router(vocab.router)


@api.get("/", include_in_schema=False, response_class=RedirectResponse)
def docs_redirect():
    return "/docs"


if __name__ == '__main__':
    import uvicorn
    uvicorn.run(api, host='0.0.0.0', port=8080, log_level='info')
