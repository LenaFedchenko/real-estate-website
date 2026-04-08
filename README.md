# Real Estate Website

![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Backend-Flask-000000?logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57?logo=sqlite&logoColor=white)
![Type](https://img.shields.io/badge/App-Server--Rendered%20Web-1F2937)

Real Estate Website is a Flask-based property listing platform for publishing, browsing, and managing residential real estate offers. It includes email-verified registration, property publishing with images, a paginated catalog, property detail pages, and an admin-only inventory screen.

## Overview

This project addresses the core flow of a listing marketplace: attract visitors with featured properties, let authenticated users publish new offers, and provide a catalog/detail experience for browsing available listings.

The implementation is server-rendered and database-backed, making it a good portfolio example of full-stack CRUD fundamentals with authentication and media uploads.

## Features

- Public landing page with featured property cards
- User registration with email verification
- Login and profile pages
- Property publishing form with:
  - city, district, and address
  - floor, area, price, room count
  - property type and deal type
  - owner contact information
  - free-text description
  - multiple uploaded images
- Paginated property catalog
- Property detail page with contact block
- User profile page showing the current user's listings
- Admin page for creating and deleting listings when `User.isAdmin=True`

## Tech Stack

- Python
- Flask
- Flask-Login
- Flask-Mail
- Flask-SQLAlchemy
- Flask-Migrate
- SQLite
- Jinja2 templates
- Vanilla JavaScript
- `python-dotenv`

## Architecture / Project Structure

The active application code lives under the `Project/` directory.

```text
real-estate-website/
├── README.md
├── Project/
│   ├── manage.py
│   ├── Project/
│   │   ├── __init__.py
│   │   ├── config_page.py
│   │   ├── db.py
│   │   ├── loadenv.py
│   │   ├── loginmanager.py
│   │   ├── settings.py
│   │   ├── templates/base.html
│   │   └── migrations/
│   ├── home/
│   ├── publish/
│   └── catalog/
└── docs/
```

### Module Responsibilities

- `Project/Project/`: app bootstrap, configuration, database, login manager, route registration
- `Project/home/`: landing page, registration, login, verification, profile
- `Project/publish/`: property creation flow and media upload handling
- `Project/catalog/`: listing catalog, detail pages, admin create/delete screen

## Getting Started

### Prerequisites

- Python 3.10 or newer
- `pip`
- SMTP credentials for the registration verification email flow

### Installation

This repository does not include a dependency lockfile, so dependencies need to be installed from the imported packages used by the app.

```bash
python -m venv .venv
source .venv/bin/activate
pip install Flask Flask-Login Flask-Mail Flask-SQLAlchemy Flask-Migrate python-dotenv
```

### Environment Variables

Create a `.env` file in the repository root:

```env
MAIL=your-email@gmail.com
PASSWORD=your-app-password
DB_INIT=flask --app Project:project db init
DB_MIGRATE=flask --app Project:project db migrate -m "Initial migration"
DB_UPGRADE=flask --app Project:project db upgrade
```

| Variable | Required | Purpose |
| --- | --- | --- |
| `MAIL` | Yes | Sender email used by Flask-Mail |
| `PASSWORD` | Yes | SMTP password or app password |
| `DB_INIT` | Optional | First-time migration initialization command |
| `DB_MIGRATE` | Optional | Migration generation command run by `execute()` |
| `DB_UPGRADE` | Optional | Database upgrade command run by `execute()` |

### Running Locally

Use the application entry point inside `Project/`:

```bash
cd Project
python manage.py
```

The app runs on:

```text
http://127.0.0.1:8000/
```

## Database

- Engine: SQLite
- Default database file: `Project/Project/instance/data.db`
- ORM: Flask-SQLAlchemy
- Migrations: Flask-Migrate / Alembic

The project currently stores at least:

- users
- published flats/properties

## Main Routes

| Route | Purpose |
| --- | --- |
| `/` | Home page with featured listings |
| `/publish` | Publish a new property |
| `/catalog/` | Browse paginated listings |
| `/catalog/<id>/` | Property details |
| `/register/` | Registration page |
| `/verify/` | Email code verification |
| `/login/` | Login page |
| `/profile/` | Current user's profile and listings |
| `/admin/` | Admin-only listing management |
| `/delete/?id=<id>` | Admin-only listing deletion |

## Future Improvements

- Wire the landing-page search selectors to real filtering logic
- Add edit/update flows for published listings
- Hash and validate passwords properly
- Improve role management for admin creation
- Add automated tests for registration, publishing, and catalog flows
- Add Docker and production deployment configuration
