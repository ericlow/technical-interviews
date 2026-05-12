# BE Dev — Bookstore Inventory Management System

## Instructions

### Before You Start

You're welcome to use AI tools and online resources (Google, GPT, Copilot, etc.) the way you'd use them in your actual day-to-day work. Look things up, autocomplete boilerplate, debug errors. That's all fair game.

What we **don't** want is vibe coding. Don't paste the entire problem into a chat window and submit whatever comes back. We're evaluating your understanding of the code, your design decisions, and your ability to talk through tradeoffs. If you can't explain what your code does or why you made a choice, that's going to be obvious.

If anything is unclear, just ask. We're happy to clarify requirements or help you get unstuck on environmental issues.

Please keep your camera on and use a single screen.

### Setup

1. Create a private GitHub repository. Initialize your project and push all skeleton code.
2. Add `mosaicapp-interview` as a collaborator with read access so we can review your code.
3. If you run into issues with GitHub, you can zip your code and email it to `dev-interviews@mosaicapp.com`.
4. Submit whatever you have to the repository when the interview ends.

### Tech Stack

- **Back-End:** Ruby on Rails, Python, Node.js, or whatever you're most comfortable with.
- **Database:** PostgreSQL or any relational database you're comfortable with.

---

## Objective

Build a web-based inventory management system for a bookstore.

---

## Core Requirements

### Database

Design a **`books`** table with the following fields:

| Field | Notes |
|---|---|
| `id` | primary key |
| `title` | |
| `isbn` | unique identifier |
| `publication_time` | |
| `genre` | |
| `price` | |
| `quantity` | |
| `num_awards` | |

Design an **`authors`** table with the following fields:

| Field | Notes |
|---|---|
| `id` | primary key |
| `name` | |
| `num_total_awards` | sum of `num_awards` for every book they authored |

**Additional rules:**

- Books should be uniquely identified by ISBN.
- Each book has exactly one author. Authors can have many books.

> **Note on authors:** You only need to implement CRUD for books. Once you've finalized the schema with your interviewer, you can use AI to seed author rows however you like — a raw SQL migration/seed script, or a throwaway `POST /authors` endpoint. Either is fine; we don't want you spending core time on author boilerplate.

### RESTful API

Implement the following endpoints:

| Method | Endpoint | Description |
|---|---|---|
| `GET` | `/books/:id` | Get a single book by ID |
| `GET` | `/books` | Get all books |
| `POST` | `/books` | Create a book |
| `PUT` | `/books/:id` | Update a book |
| `DELETE` | `/books/:id` | Delete a book by ID |

### Concurrent Award Updates

Using the `books` and `authors` tables defined above:

- Add an endpoint that increments a given book's `num_awards` by 1.
- When `num_awards` is incremented, the book's author's `num_total_awards` should update accordingly.

**Discussion prompt:** Now imagine multiple concurrent requests hitting this endpoint at the same time — possibly for the same book, possibly for different books that share an author. What could go wrong, and how would you design around it?

---

## Stretch Goals

### Genre Aliasing

Different people refer to the same genre differently. "Science fiction" and "sci-fi" should be treated as equivalent. The same applies across languages (e.g., English and Spanish).

Update your code and database design so that genre lookups treat aliases as the same genre. This should be reflected in the `GET` endpoint, and depending on the implementation, may require changes to `POST` and `PUT` as well.

### Soft Deletes with 30-Day Recovery

Assume we want to be able to recover deleted books within 30 days. After 30 days, they should be permanently removed.

### Filtering, Pagination, and Sorting

- **Filtering** — Add optional query parameters to filter the book list by price range, publication time range, or any other column of your choice.
- **Pagination** — Add pagination support to the "Get all books" endpoint.
- **Sorting** — Add sorting support to the "Get all books" endpoint.

### Tests

Add at least one test case for any endpoint or feature you've implemented (e.g., a test that creates a book with valid inputs and asserts the response).
