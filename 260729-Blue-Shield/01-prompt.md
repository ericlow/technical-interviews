# E-Commerce Platform — System Design

- **Source:** Blue Shield
- **Date:** 2026-07-29
- **Stack:** Architecture (language-agnostic); frontend React
- **Type:** System Design

## Problem Statement

Design an e-commerce website. It must support:

- Asynchronous notifications on order-status change
- Role-based authentication
- 100k concurrent users
- Secure, scalable, observable

The interview was conversational — the interviewer drilled into specific areas
rather than asking for a single diagram. Questions asked, verbatim where possible:

### Security / Auth
- How does security work? JWT?
- What are the details of the JWT?
- When the API gateway routes the request to the microservice, what happens
  then with security?
- How does the system break up the roles and permissions? Are there lookups
  that happen?

### Order Creation API
- Describe how this would work: validation, persistence, notifications.
- How does it scale?

### Front End
- How do you organize your React project?
- What router did you use?

### Ops / Deployment
- What's in your YAML?
- What are the deployment details? What do you deploy this system to?

## Constraints

- 100k concurrent users
- Must be secure, scalable, and observable
- Notifications on order-status change must be asynchronous
- Role-based access control is required

## What Makes This Hard

The prompt is broad, but the interviewer's follow-ups are narrow and concrete.
Success depends on being able to go deep on JWT internals, gateway-to-service
trust, RBAC lookup mechanics, and the end-to-end order flow — not on drawing
boxes.
