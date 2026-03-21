### Golang/Python Backend Coding Exercise: Cost-Effective GPU Reservation API

**Product Goal:**
Our product empowers users to find and reserve powerful GPU compute for specific time windows, making on-demand access to high-performance infrastructure simple and cost-effective.

![Product](./instructions.png)

**Your Task:**
Design and build a resilient RESTful API that queries AWS for machine learning capacity block reservations across multiple regions. The API should find and return the single most cost-effective option that meets the user's requirements.

**Interview Time: 1 hour**

---

### Requirements

#### 1. API Endpoint
Create a RESTful API with a single endpoint that accepts a search request. Using `POST` is recommended as it's better suited for complex query bodies.

*   **Endpoint:** `POST /reservations/find-cheapest`
*   **Request Body:**

    ```json
    {
      "instance_type": "p4d.24xlarge",
      "instance_count": 2,
      "regions": ["us-east-1", "us-west-2", "eu-central-1"],
      "start_date": "2025-11-10",
      "required_duration_hours": 72
    }
    ```

#### 2. Business Logic & Constraints
Your API must translate the user's request into a valid AWS query based on these rules:

*   **24-Hour Blocks:** AWS Capacity Blocks are offered only in **24-hour increments**. Your API must calculate the minimum number of 24-hour blocks needed to satisfy the `required_duration_hours`.
*   **Fixed Start Time:** Reservations always begin at **11:30 AM UTC** on the given `start_date`.
*   **Spin-Down Time:** The reservation requires a mandatory **1-hour spin-down period**.

#### 3. Core Logic
*   **Concurrent search with retries:** The service must query all specified `regions` **concurrently** to minimize response time.
*   **Resilience:** The system must gracefully handle partial failures. If an API call to one region fails or times out, the overall request must succeed using results from the healthy regions.
*   **Cost Optimization:** From all valid reservations found across all regions, identify and return the one with the lowest total price.

#### 4. Return Data Format
Design a clean and simple response. Do not just pass through the raw AWS response. The client should receive a single JSON object with only the essential information.

*   **Success Response Example (200 OK):**
    ```json
    {
      "capacityBlockOfferingId": "cb-0f7e8662751ff4036",
      "instanceType": "p5.48xlarge",
      "instanceCount": 1,
      "startDate": "2025-08-07T11:30:00Z",
      "endDate": "2025-08-08T10:30:00Z",
      "capacityBlockDurationHours": 24,
      "upfrontFee": 0,
      "currencyCode": "USD",
      "region": "us-east-1",
      "fee": 794.8799999999999,
      "providerFee": 0,
      region: "us-east-1",
    }
    ```
*   **Not Found Response (404 Not Found):** If no reservations matching the criteria are found, return a `404` with a clear error message.

#### 5. Error Handling
*   Handle AWS API errors in a way that supports the partial failure requirement.
*   Return `400 Bad Request` for invalid or missing parameters in the request body.
*   Return `404 Not Found` when no reservations are available.

#### 6. Testing
*   Write unit tests for your API and its components.
*   Tests should cover:
    *   The happy path (a cheapest reservation is successfully found).
    *   The business logic for calculating the correct number of 24-hour blocks.
    *   The partial failure case (one regional query fails, but the request succeeds).
    *   The failure case where no reservations are found across any region.

#### 7. Docker Container
*   Package the API into a Docker container for easy deployment.
*   The container should expose a port (e.g., `8080`) for incoming API requests.

#### 8. AWS Helpers:

Golang:

* Create the EC2 Client

```go
	regionConfig, err := config.LoadDefaultConfig(ctx, config.WithRegion("REGION"))
	if err != nil {
		fmt.Printf("couldn't make aws config: %v\n", err)
		os.Exit(1)
	}

	regionClient := ec2.NewFromConfig(regionConfig)
  ```

* Get capacity blocks: `ec2.DescribeCapacityBlockOfferings`
    *   Possible errors:
        * InvalidParameterValue
        * CapacityBlockDescribeLimitExceeded

Python:

* Create the EC2 Client

```python
try:
    ec2_client = boto3.client("ec2", region_name="REGION")
except Exception as e:
    print(f"Couldn't create EC2 client: {e}")
    exit(1)
```

* Get capacity blocks: `ec2_client.describe_capacity_block_offerings`
    *   Possible errors:
        * InvalidParameterValue
        * CapacityBlockDescribeLimitExceeded

