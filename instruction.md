There is an access log in the working directory.

Analyze the traffic and determine:

1. Total number of requests.
2. Number of unique client IP addresses.
3. Most requested page.

Save the results as a JSON file at:

/app/report.json

The JSON object must contain exactly these keys:

- "total_requests"
- "unique_ips"
- "top_path"