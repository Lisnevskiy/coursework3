import pytest

from coursework2_source.app import app

keys = {"poster_name",
        "poster_avatar",
        "pic",
        "content",
        "views_count",
        "likes_count",
        "pk",
        }


def test_get_api_posts_json():
    response = app.test_client().get('/api/posts')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == list
    assert set(api_response[0].keys()) == keys


def test_get_api_post_json():
    response = app.test_client().get('/api/posts/1')
    assert response.status_code == 200
    api_response = response.json
    assert type(api_response) == dict
    assert set(api_response[0].keys()) == keys
