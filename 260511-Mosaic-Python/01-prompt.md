# Bookstore Inventory Management System

**Source:** Mosaic  
**Date:** 2026-05-11  
**Stack:** Python (or Ruby/Node), PostgreSQL  
**Type:** Full-stack

---

## Problem Statement

Build a web-based inventory management system for a bookstore. You may use AI tools as you would in real day-to-day work — autocomplete, debugging, lookups — but you must be able to explain every decision.

---

## Requirements

### Phase 1: Database Schema

Design a **`books`** table:

- `id` (primary key)
- `title`
- `isbn` (unique)
- `publication_time`
- `genre`
- `price`
- `quantity`
- `num_awards`

Design an **`authors`** table:

- `id` (primary key)
- `name`
- `num_total_awards` — sum of `num_awards` across all of this author's books

Rules:
- Each book has exactly one author; authors can have many books.
- You only need to implement CRUD for books. Author rows can be seeded via AI-generated SQL or a throwaway endpoint.

### Phase 2: RESTful API

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/books/:id` | Get a single book by ID |
| `GET` | `/books` | Get all books |
| `POST` | `/books` | Create a book |
| `PUT` | `/books/:id` | Update a book |
| `DELETE` | `/books/:id` | Delete a book |

### Phase 3: Concurrent Award Updates

Add an endpoint that increments a given book's `num_awards` by 1. When `num_awards` changes, the author's `num_total_awards` must update accordingly.

**Discussion:** Multiple concurrent requests may hit this endpoint simultaneously — for the same book, or for different books sharing an author. What could go wrong, and how do you design around it?

---

## Stretch Goals

- **Genre Aliasing** — "Science fiction" and "sci-fi" treated as the same genre; aliases normalized at read and/or write time.
- **Soft Deletes** — Deleted books recoverable within 30 days; permanently purged after.
- **Filtering, Pagination, Sorting** — Query params on `GET /books` for price range, publication time range, page/limit, and sort order.
- **Tests** — At least one test case for any endpoint or feature implemented.

---

## Constraints

- No prescribed language or framework — use what you know best.
- Relational database required (PostgreSQL preferred).
- Submit to a private GitHub repo; add `mosaicapp-interview` as a collaborator.
