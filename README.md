# spiderweb

Locally hosted RDF store for exploring the Spider Text-to-SQL dataset

## Run Locally

### Using Docker Compose

First, install Docker Desktop by following the instructions for your OS.

```shell
docker compose run make-dataset
```

Then, the following command will connect your terminal to a running instance
of the API, with Redis as the database.

```shell
docker compose up app 
```

Open your browser to http://localhost:8000/docs to view the OpenAPI docs.
