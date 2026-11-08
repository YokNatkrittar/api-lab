# Another user cannot read the rating, and the rating stays unchanged.
def test_other_user_cannot_read(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.get(path, headers=other_auth)
    print("other user READ:", res.status_code, res.text)
    assert 400 <= res.status_code <= 499

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


# Another user cannot change the stars, and the rating stays unchanged.
def test_other_user_cannot_update(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": 5}, headers=other_auth)
    print("other user UPDATE:", res.status_code, res.text)
    assert 400 <= res.status_code <= 499

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating


# Another user cannot delete the rating, and the rating still exists.
def test_other_user_cannot_delete(api, auth, other_auth, rating):
    path = f"/api/ratings/{rating['id']}"
    res = api.delete(path, headers=other_auth)
    print("other user DELETE:", res.status_code, res.text)
    assert 400 <= res.status_code <= 499

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    assert res.json() == rating