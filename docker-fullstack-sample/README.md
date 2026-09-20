# Docker Full Stack Demo

Sample frontend + Python Flask backend using Docker Compose.

## Structure

- `frontend/` - Nginx + HTML frontend
- `backend/` - Python Flask API
- `docker-compose.yml` - Runs both containers

## Run

```bash
docker compose build
docker compose up -d
docker compose ps
```

Open:

http://localhost:8080

Test API:

http://localhost:8080/api/hello

Stop:

```bash
docker compose down
```

## Hostinger VPS

Clone the project and run:

```bash
cd docker-fullstack
docker compose up -d --build
docker compose ps
```

Then open:

`http://YOUR_VPS_IP:8080`
