import uuid


def new_name():
    return "lab-" + uuid.uuid4().hex[:12]


# A second user with a name that is already taken is refused with 400.
def test_username_already_taken(api):
    user = {"username": new_name(), "password": "Pizza-2026"}
    res = api.post("/api/users", json=user)          # first time: OK
    assert res.status_code == 201
    res = api.post("/api/users", json=user)          # same name again
    assert res.status_code == 400
    assert res.json() == {"error": "username already taken"}


# Logging in with a wrong password is refused with 401.
def test_login_with_wrong_password(api):
    user = {"username": new_name(), "password": "Pizza-2026"}
    res = api.post("/api/users", json=user)
    assert res.status_code == 201
    wrong = {"username": user["username"], "password": "Wrong-1234"}
    res = api.post("/api/users/token/login", json=wrong)
    assert res.status_code == 401
    assert res.json() == {"error": "authentication failed"}


# A user with an empty name is refused with 400.
def test_empty_username(api):
    user = {"username": "", "password": "Pizza-2026"}
    res = api.post("/api/users", json=user)
    assert res.status_code == 400
    assert res.json() == {"error": "username field is empty"}