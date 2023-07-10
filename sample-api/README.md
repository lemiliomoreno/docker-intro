Commands:

Docker processes:

```bash
docker ps
```

1. Database:

```bash
cd database
docker build -t academia-database .
docker run -p 27017:27017 -d academia-database
```

2. API

Get the Database IP with `docker inspect <CONTAINER_ID>`.

Change the connection string in `utils/database.py`.

```bash
cd api
docker build -t academia-api .
docker run -p 8000:8000 -d academia-api
```
