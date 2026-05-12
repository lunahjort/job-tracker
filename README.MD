# Job-Tracker
Ett enkel fullstack-webbapp för jobbansökningar.

## Funktioner
- Lägg till jobbansökningar
- Visa alla ansökningar
- Uppdatera status från Applied till Interview
- Ta bort jobb
- Data sparas i en databas (SQLite)

## Tech Stack
### Backend:
- Python
- FastAPI
- SQLAlchemy
- SQLite

### Frontend:
- HTML
- CSS
- JavaScript

## API Endpoints
- GET /jobs → Hämta alla jobb
- POST /jobs → Skapa nytt jobb
- PUT /jobs/{id} → Uppdatera jobb
- DELETE /jobs/{id} → Ta bort jobb