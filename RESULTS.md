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
- Step A4, status codes when the other user reads, changes and deletes: read [___], change [___], delete [___]

## Part B
1. Two failures that only tests against the real server can find: (a) problems between the parts of the system, for example the server crashing with 500 when all tools are excluded, or the database and the API not agreeing; (b) problems in the infrastructure, for example the load balancer sending a login to a server that has never seen the user. A unit test with stubs replaces those parts, so it cannot see these failures. Unit tests with stubs are still worth writing because they are fast, they do not depend on the network, and when one fails it points at one function, so the cause is easy to find.

2. Ratings made with the public token are shared by everyone, so another student could change or delete them while my test runs, and my tests could damage other people's data. A new user with a random name gives every test its own clean data, so the tests are independent and can run in any order. In Project 2, each test (or fixture) will create its own customer account, cart or booking with a unique name, and delete it afterwards, and never touch the data of other groups.

3. QuickPizza runs on several servers behind a load balancer, and each server keeps its own users. The AWSALB cookie tells the load balancer which server to use. A Session keeps that cookie, so every request in the run reaches the same server, and the login finds the user that was just created. Without a session the login can go to another server and fail with 401, which makes the test flaky. [If you did Step 0.12, add your three results here; otherwise say you skipped it.]

4. The block "all three tools excluded" revealed the defect. A 500 with an empty body is worse than a 400 with a message, because the app gets no explanation to show the user, it cannot tell its own bad request apart from a real server crash, and it may retry a request that will never work. The test stays as xfail because it documents the defect and keeps it visible in every run; with strict=True it will fail as soon as QuickPizza fixes the bug, so we know to remove the mark. Deleting it would hide the defect.

5. The model has characteristics with 3, 4, 2 and 3 blocks. Base choice needs 1 base test plus one test for each non-base block: 1 + (3−1) + (4−1) + (2−1) + (3−1) = 1 + 2 + 3 + 1 + 2 = 9 tests. All combinations coverage needs 3 × 4 × 2 × 3 = 72 tests.

6. The other user got [___] for read, [___] for change and [___] for delete. [Answer depends on your codes:
   - If all were 404: I would expect 403 Forbidden, because the rating exists but belongs to someone else. 404 is not a defect, though: it hides whether the rating exists at all, so a stranger cannot even learn which ids are in use. That is a common and safer design.
   - If they were different from each other: the API is inconsistent, and a code that reveals the rating exists can leak information.
   The important result is that the rating stayed unchanged in all three cases, so there is no security defect.]

7. [Write the status code and body you got.] [If it was 200: This is a defect. QuickPizza accepted a token it never issued, so it seems to check only the length of the token, not whether it is real. On a real system a stranger could invent a token and read, change or delete other users' data without logging in. If it was 401: QuickPizza correctly refused a token it never issued.]

8. An API test checks the exact data better: the status codes, every field of the JSON, error messages and refused requests, which the web page may hide or never send. Only a test through the web pages can check what the user actually sees and does: the layout, buttons, forms and how the page shows an error.