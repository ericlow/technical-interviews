# Backend Domain Quickfire — Microservice Chatter & Large-File Upload

- **Source:** Blue Shield
- **Date:** 2026-07-29
- **Stack:** Architecture / backend (language-agnostic, AWS context)
- **Type:** System Design

## Problem Statement

Two standalone backend design probes, asked verbally after the main system
design.

### Q1 — Reduce network communication between microservices

Imagine there are 6 microservices needed to perform an action. They are
containerized on AWS. For example a portfolio system, with operations like
`get`, `update`, `delete`.

If you want to reduce network communication, what do you do?

### Q2 — Resumable large-file upload

Imagine there is a 1 TB file and you need to upload it.

- How do you track the parts?
- You don't want to duplicate the uploads — what part do you restart?
- How do you divide the file?

## Constraints

- 6 microservices collaborate on a single action (fan-out chatter)
- Single 1 TB file; uploads may fail partway and must not be duplicated
