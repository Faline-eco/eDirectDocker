# eDirect REST API

Docker image extending the `ncbi/edirect` image with a rest api allowing to translate a list of common animal names to scientific names

## Build

```
docker build -t species-rest-service .
```

## Run

```
docker run -p 5000:5000 species-rest-service
```

## Use

HTTP POST request to `http://localhost:5000/translate` with the following json body:

```json
{
    "common_names": [
        "thale cress", 
        "zebra"
    ]
}
```