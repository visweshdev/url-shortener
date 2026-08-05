# URL Shortener

[![CI](https://github.com/smtchahal/url-shortener/actions/workflows/ci.yml/badge.svg)](https://github.com/smtchahal/url-shortener/actions/workflows/ci.yml)
[![codecov](https://codecov.io/gh/smtchahal/url-shortener/branch/master/graph/badge.svg)](https://codecov.io/gh/smtchahal/url-shortener)

A simple, modern Django-based URL shortening web application.

<img src="docs/uiscreenshot.png" alt="URL Shortener Screenshot" />

## Architecture Highlights
- **Framework**: Django 
- **Styling**: Bootstrap 5 (via CDN for a lightweight frontend)
- **Database**: SQLite (local) / PostgreSQL (production)
- **Static Files**: Served efficiently via WhiteNoise
- **App Structure**: 
  - `links/`: Core URL shortening logic, models, and views.
  - `shorty/`: Project URL routing and WSGI application.
  - `settings/`: Multi-environment settings (`base.py`, `local.py`, `production.py`).

## Running Locally with Docker (Recommended)

**Prerequisites:** Docker with the Compose plugin (`docker compose version`).

### 1. Configure Environment
```bash
cp .env.example .env
```
Edit `.env` and set at minimum:

| Variable | Description |
|---|---|
| `SECRET_KEY` | Long random string (Django secret key) |
| `DB_PASSWORD` | Password for the Postgres container |
| `ALLOWED_HOSTS` | Comma-separated hostnames, e.g. `localhost,127.0.0.1` |

*(The other variables in `.env.example` can be left as-is for local development.)*

### 2. Start the App
```bash
docker compose up --build
```
The application will be available at <http://localhost:8000>. Database migrations and static file collection run automatically on startup.

### 3. Stop the App
```bash
docker compose down
```
To also remove the database volume:
> [!CAUTION]
> `docker compose down -v` permanently deletes all database data.

---

## Running Locally (Without Docker)

1. **Set up a virtual environment** and activate it.
2. **Install dependencies**:
   ```bash
   pip install -r requirements.txt -r requirements-dev.txt
   ```
3. **Configure environment**:
   ```bash
   cp .env.example .env
   # Edit .env and set SECRET_KEY
   ```
4. **Run migrations and start the server**:
   ```bash
   python manage.py migrate
   python manage.py runserver
   ```

---

## Running Tests

The `test` build target runs linting (`flake8`), the test suite, and prints a coverage report inside an isolated container:

```bash
docker build --target test -t url-shortener-test .
docker run --rm url-shortener-test
```
