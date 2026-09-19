# M.AI — Task Management System (CodeSignal)

**Date:** 2026-06-11  
**Company:** M.AI  
**Platform:** CodeSignal — Progressive Filesystem with Unit Tests  
**Duration:** 90 minutes  
**Stack:** React, TypeScript, Vite  
**Levels:** 4 progressive levels (unlock by passing all tests at current level)

---

## Overview

Implement UI features for a task management system. The problem is presented as 4 locked levels; each unlocks once the previous level's tests all pass. You always have access to starter files and data from all previous levels.

**Important notes:**
- Use the provided CSS class names exactly — tests access elements via CSS selectors
- Templates are given as plain HTML; convert to JSX/TSX syntax
- All test files except `sample.test.js` are read-only
- `uuid` library is pre-installed (`import { v4 as uuidv4 } from 'uuid'`)

---

## Starter File Structure

```
src/
  App.tsx           — board layout; renders 3 TaskColumn components
  index.tsx         — React root, read-only
  index.scss        — styles, read-only
  TaskCard.tsx      — empty card component (stub with comment)
  TaskColumn.tsx    — column component (title prop; empty column__cards div)
  taskData.json     — local task data (used in Levels 1–2)
test/
  level1.test.js    — read-only
  level2.test.js    — read-only
  level3.test.js    — read-only
  level4.test.js    — read-only
  sample.test.js    — writable for debugging
```

---

## Level 1 — Display tasks from local JSON (250 pts)

Show a Kanban board with 3 columns populated from `taskData.json`.

**`taskData.json` shape:**
```json
{
  "tasks": {
    "todoItems":       [{ "id": "...", "title": "...", "description": "..." }],
    "inProgressItems": [{ "id": "...", "title": "...", "description": "...", "assignedUser": "..." }],
    "doneItems":       [{ "id": "...", "title": "...", "description": "...", "assignedUser": "..." }]
  }
}
```

**Required HTML template for a task card:**
```html
<div class="card">
  <h3 class="card__title">Fix CSS</h3>
  <p class="card__description">Homepage footer uses an inline style — should use a class</p>
</div>
```

**Acceptance criteria:**
- All To Do tasks displayed in the To Do column
- All In Progress tasks displayed in the In Progress column
- All Done tasks displayed in the Done column

---

## Level 2 — Create task via form (500 pts)

Add a form above the board that allows creating new tasks.

**Required HTML template for the form:**
```html
<div class="create-task-form">
  <h2 class="create-task-form__title">Create task</h2>
  <form>
    <input name="title" placeholder="Title" />
    <textarea name="description" placeholder="Description"></textarea>
    <input type="submit" value="Add new task" />
  </form>
</div>
```

**Acceptance criteria:**
- Submitting with both Title and Description filled → new task added to To Do column; form fields cleared
- Submitting with either field empty → form not submitted; fields not cleared; task not added

---

## Level 3 — Load tasks from API + show assigned users (750 pts)

Replace hardcoded `taskData.json` with live API data. Tasks now have a flat `status` field. Some tasks have an `assignedUser` ID; fetch the user's name and display it.

**Tasks API:** `GET https://api-regional.codesignalcontent.com:443/task-management-system/tasks`

Response shape:
```json
[
  { "id": "...", "title": "Task 1", "description": "Some description", "status": "TO_DO" },
  { "id": "...", "title": "Task 2", "description": "Another description", "assignedUser": "5f10478b-...", "status": "IN_PROGRESS" }
]
```
Status values: `"TO_DO"`, `"IN_PROGRESS"`, `"DONE"`

**Users API:** `GET https://api-regional.codesignalcontent.com:443/task-management-system/users/{userId}`
- Returns 200 with user info, or 404 if user not found
- Fetch users one at a time (no bulk endpoint)

**Updated HTML template for a task card with assigned user:**
```html
<div class="card">
  <h3 class="card__title">Fix CSS</h3>
  <span class="card__owner">Assigned user: Lisa Lake</span>  <!-- omit if no user -->
  <p class="card__description">Homepage footer uses an inline style — should use a class</p>
</div>
```

**Acceptance criteria:**
- Tasks rendered in correct column based on `status` field
- Task with `assignedUser` + successful Users API response → show `card__owner` span
- Task without `assignedUser` → no `card__owner` span
- Task with `assignedUser` but Users API returns 404 → no `card__owner` span

---

## Level 4 — Update task status (1000 pts)

Support dragging/moving tasks between columns (status update). Full details not captured — inferred as drag-and-drop or click-based status transitions updating the board state.
