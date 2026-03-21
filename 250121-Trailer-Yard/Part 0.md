# Trailer Yard Invoicing: Part Zero

*For senior-level and higher candidates.*

We’ll do a warmup to get started.

Take a look at this JSON file:

[events.json](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/04f4b03d-a59d-4120-97e4-fe8de8505ac3/events.json)

The objects in here have the following structure:

```json
{
  "id": <number>,
  "trailer_id": <number>,
  "facility_id": <number>,
  "entrance_time": <string>,
  "exit_time": <string> | null
}
```

## Instructions

Write a function that parses the input JSON file and deserializes the date-time strings (`entrance_time` and `exit_time`) to an appropriate object (e.g. `Date` in Javascript or `datetime` in Python) in your language of choice. The function should return the whole dataset with these values deserialized.

Print the result returned from the function so we can verify it has been successfully parsed.

## Time Target

We have up to the **15 minutes** mark to complete this.