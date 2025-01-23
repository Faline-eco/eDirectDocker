# eDirect REST API

Docker image extending the [ncbi/edirect](https://hub.docker.com/r/ncbi/edirect/tags) image with a rest api allowing to translate a list of common animal names to scientific names using [Entrez Direct](https://www.ncbi.nlm.nih.gov/books/NBK179288/)

## Build

```
docker build -t species-rest-service .
```

## Run

```
docker run -p 5000:5000 species-rest-service
```

For best performance, obtain an [API Key from NCBI](https://account.ncbi.nlm.nih.gov/settings/), and provide it as environment variable:

```
docker run -p 5000:5000 -e NCBI_API_KEY=my_awesome_entrez_key species-rest-service
```

## Use

HTTP POST request to `http://localhost:5000/com2sci` with the following json body:

```json
{
    "common_names": [
        "thale cress", 
        "zebra"
    ]
}
```

Should return something like:

```json
{
    "thale cress": [
        "Arabidopsis thaliana"
    ],
    "zebra": []
}
```
