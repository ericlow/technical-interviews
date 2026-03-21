# DoorDash — System Design: Food Item Review Website

## Type
System design (whiteboard/discussion)

## Problem

Design a review system that allows users to leave reviews for food items. Reviews cannot be edited after submission.

## Functional Requirements

- Users can leave a review for an item (rating + optional comment)
- Users can leave comments
- Aggregate reviews and show to other users
- When viewing a business: show items with their aggregate rating
- When clicking an item: see item details including comments and rating

## API

```
POST /v1/item/{id}/review
body: { rating, comment }

GET /v1/businesses/{id}/items
→ Partial<Item>[] + business details

GET /v1/items/{id}/detail?page={num}&sortType=...&filter={filter list}
→ Item details, aggregated rating, list of reviews (comment + rating)
```

## Entities

- **Users**: user_id, name, created_date
- **Business**: business_id, name
- **Items**: item_id, name, business_id, avg_rating, total_number_of_rating_points, total_number_of_reviews, date_of_last_aggregation
- **Reviews**: item_id, business_id, rating, comment, user_id, created_date

## Non-Functional Requirements

- Leaving/creating a review: latency < 0.5 sec, eventual consistency within 5 sec
- Leaving comments: latency < 0.5 sec, eventual consistency within 5 sec
- Aggregate reviews: latency < 0.2 sec, eventual consistency within hours
  - Reviews can wait hours to be consolidated into the aggregated rating
  - (Use Kafka / ESB / aggregation jobs)
