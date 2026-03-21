# Trailer Yard Invoicing: Part One

*For senior-level and higher candidates.*

Next let’s write a filter for the data. Here’s the same input file again:

[events.json](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/04f4b03d-a59d-4120-97e4-fe8de8505ac3/events.json)

## Backstory

Baton once owned several yards that have parking spaces for trailers. The yard operated 24/7 where trailers came in and out periodically. We had a system and process setup where any trailer that entered/exited our yard was recorded into our database.

We invoiced customers per facility per day based on their usage of that facility on that day.

## Instructions

The data we’re working with is for a single customer. Write a function that takes the trailer events, a date, and a facility ID, and returns all trailer events for trailers that were at the given facility on the given date.

As an example, if we filter for all trailer events for **January 18, 2022** at **facility 1**, such a function should return a collection of **18 events**.

## Time Target

We have up to the **30 minutes** mark to complete this.