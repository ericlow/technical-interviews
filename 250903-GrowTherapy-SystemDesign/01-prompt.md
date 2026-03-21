# Grow Therapy — System Design: Therapist Finder & Booking

## Type
System design (whiteboard/discussion)

## Problem

Design a system that lists therapists for prospective patients to book near them ("Therapists near me"). Focus on web architecture to serve city/local searches in a fast and reliable way.

## Functional Requirements

- Search for providers by location (city/specialty)
- View provider profile and availability
- Book an appointment with a provider
- Query provider calendars via a third-party calendar provider
- Providers enter their address or virtual place of business on onboarding

## Routes (at least 4 surface areas)

- `GET /search?location={location}&page={pageId}` → list of partial provider info
- `GET /provider/{id}` → full provider profile
- `POST /provider` → create provider (onboarding)
- `GET /provider/{id}/availability?pageId=...&dateStart=...&dateEnd=...` → list of appointment slots
- `POST /book` → book a provider

## Non-Functional Requirements

- **Provider calendars**: up-to-date information from third-party system
- **Provider info**: strongly consistent, low latency (< 0.5 sec)
- **Fault tolerant**
- **Consistency over availability**
