import pytest


# Updating the stars accepts 1 and 5, refuses 0 and 6, and a refused update changes nothing.
@pytest.mark.parametrize("stars, expected", [(0, 400), (1, 200), (5, 200), (6, 400)])
def test_update_stars_boundaries(api, auth, rating, stars, expected):
    path = f"/api/ratings/{rating['id']}"
    res = api.put(path, json={"stars": stars}, headers=auth)
    assert res.status_code == expected

    res = api.get(path, headers=auth)
    assert res.status_code == 200
    if expected == 200:
        assert res.json()["stars"] == stars
    else:
        assert res.json()["stars"] == rating["stars"]