# ResFrac ResApps — Take-Home Mini Project (React/Node)

## Type
Take-home full-stack project

## Stack
- TypeScript / JavaScript
- React (or Angular 2+ / Vue)
- Electron (preferred) or Express (for desktop or local web)
- State management (NgRx / Redux)
- SQLite (or other SQL)
- OAuth2 (Google or Microsoft)
- Axios (or equivalent) for API calls

## Requirements

### Home Screen
- Title bar: app name (left), settings + login buttons (right), window controls (min/max/close)
- Body: welcome message with instructions to log in and select a city for weather

### Settings Screen
- Show and allow editing of settings (weather API URL, API key, etc.)
- Settings persisted to SQLite

### Login Screen
- Google OAuth2 login (or Microsoft)
- On successful login: check `users` table in SQLite; if not found, insert record with first name, last name, email from ID token
- After login: home page shows location input (text box or dropdown) + button to fetch weather

### Weather
- Fetch weather for selected city via external API (e.g. Weatherstack)
- Display in appropriate format

### Logout
- Allow user to log out

## Evaluation Criteria
- Frontend framework (React/Angular/Vue)
- State management
- TypeScript/JavaScript quality
- Electron or Express integration
- Unit tests
- SQLite integration
- OAuth2 + REST API usage

## Deliverables
- Working app (GitHub/BitBucket link or zip)
- README
- Architecture diagram
- Logging
- Unit test cases

## Clarifying Questions Asked
- What date range / precision level for weather (hourly, daily)?
- What counts as "appropriate format" for weather display?
- How many cities to support?
- Should stored user info be used for anything beyond storage?
- Is NgRx a hard requirement or is any state management (e.g. Redux) acceptable?
- Any performance expectations?
