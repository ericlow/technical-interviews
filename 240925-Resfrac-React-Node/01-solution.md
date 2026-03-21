# Solution — ResFrac ResApps Mini Project

## Architecture

```
Electron shell
└── React frontend (TypeScript)
    ├── Redux (state management)
    ├── Axios (API calls)
    └── SQLite (via better-sqlite3 or electron-store)
        ├── users table
        └── settings table
```

## Key Components

### Auth (Google OAuth2)
- Use Google's OAuth2 PKCE flow (suitable for Electron/desktop — no client secret needed)
- On success: decode ID token, upsert user into SQLite `users` table
- Store access token in Redux state (not persisted to disk)

### Settings
- SQLite table: `settings(key TEXT PRIMARY KEY, value TEXT)`
- Settings screen reads/writes via IPC (Electron main process) or direct SQLite in renderer
- Keys: `weatherApiUrl`, `weatherApiKey`

### Weather
- Fetch from Weatherstack (or OpenWeatherMap)
- `GET http://api.weatherstack.com/current?access_key={key}&query={city}`
- Display: current temp, description, humidity, wind speed
- Redux slice: `{ city, weather, loading, error }`

### SQLite Schema

```sql
CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  email TEXT UNIQUE,
  first_name TEXT,
  last_name TEXT,
  created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE settings (
  key TEXT PRIMARY KEY,
  value TEXT
);
```

## State Management (Redux)

```
store
├── auth: { user, isLoggedIn, token }
├── weather: { city, data, loading, error }
└── settings: { weatherApiUrl, weatherApiKey }
```

## File Structure

```
src/
├── main/          # Electron main process
│   ├── index.ts
│   └── db.ts      # SQLite access
├── renderer/      # React app
│   ├── App.tsx
│   ├── screens/
│   │   ├── HomeScreen.tsx
│   │   ├── LoginScreen.tsx
│   │   └── SettingsScreen.tsx
│   ├── store/
│   │   ├── authSlice.ts
│   │   ├── weatherSlice.ts
│   │   └── settingsSlice.ts
│   └── services/
│       ├── weatherApi.ts
│       └── googleAuth.ts
└── shared/        # Types shared between main/renderer
```

## Testing
- Unit tests with Jest + React Testing Library
- Test: weather fetch (mock Axios), Redux reducers, SQLite upsert logic
