# API lab results

## Part 0
- Step 0.1, the number of pizza names: ___
- Step 0.3, status code of the request without a token: 401
- Step 0.4, the name of your pizza: ___
- Step 0.12, results of the three runs without a session (optional):
- Step 0.16, blocks of "how many of the three tools are excluded": 0, 1, 2, 3 tools excluded

## Defect report
- Title: Excluding all three tools returns 500 with an empty body
- Request: POST https://quickpizza.grafana.com/api/pizza with header `Authorization: token abcdef0123456789` and body `{"excludedTools": ["Knife", "Pizza cutter", "Scissors"]}`
- Expected result: Status 400 with a JSON error message explaining that no pizza can be made without any tool
- Actual result: Status 500 Internal Server Error with an empty body
- Severity: Medium. The server crashes instead of rejecting a request it cannot serve. An app that calls the API gets no message to show the user and cannot tell this case apart from a real server outage. It does not lose or expose data, so it is not high.

## Part A
- Step A4, status codes when the other user reads, changes and deletes:

## Part B
1.
2.
3.
4.
5.
6.
7.
8.