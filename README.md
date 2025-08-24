# Dockerized Flask Starter 🚀

A zero-to-ship Flask web app that's fully Dockerized. Perfect for beginners who want a clean project to push on GitHub.

## What you get
- Simple Flask app with a home page + JSON API
- Dockerfile (Python 3.12 slim)
- Optional Docker Compose
- Clean `.gitignore` and `.dockerignore`
- Step-by-step run + GitHub push guide

---

## Prereqs
- [Docker Desktop](https://www.docker.com/products/docker-desktop/)
- [Git](https://git-scm.com/downloads)

---

## Run locally with Docker
```bash
# 1) Build the image (rename tag if you like)
docker build -t sobi/flask-hello:1.0 .

# 2) Run the container
docker run -p 5000:5000 sobi/flask-hello:1.0

# Open: http://localhost:5000
```

### Or use Docker Compose
```bash
docker compose up --build
```

Stop with `Ctrl+C`, then `docker compose down` if using Compose.

---

## Project structure
```text
sobi-docker-starter/
├─ app/
│  ├─ app.py
│  ├─ templates/
│  │  └─ index.html
│  └─ static/
│     └─ style.css
├─ requirements.txt
├─ Dockerfile
├─ docker-compose.yml
├─ .dockerignore
├─ .gitignore
└─ README.md
```

---

## Push this to GitHub (quick guide)
1. Create a **new empty repo** on GitHub (no README). Copy its URL.
2. In this folder, run:
   ```bash
   git init
   git branch -M main
   git add .
   git commit -m "Docker Flask starter 🚀"
   git remote add origin https://github.com/<your-username>/<repo-name>.git
   git push -u origin main
   ```

### Update later
```bash
git add .
git commit -m "feat: update UI / docs"
git push
```

---

## API quick test
```bash
curl http://localhost:5000/api/health
curl http://localhost:5000/api/ping
```

---

## Troubleshooting
- **Port in use**: Change `5000:5000` to `5050:5000` (for example) in `docker run` or `docker-compose.yml`.
- **Slow build on first try**: It's downloading Python layers — normal.
- **Windows PowerShell path issues**: Wrap paths in quotes, e.g., `"C:\Users\you\project"`.

MIT License.
