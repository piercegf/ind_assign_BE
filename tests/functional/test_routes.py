from api import app
import pytest

def test_dummy_wrong_path():

    with app.test_client() as client:
        response = client.get('/wrong_path')
        assert response.status_code == 404

def test_dummy_wrong_method():

    with app.test_client() as client:
        response = client.post('/')
        assert response.status_code == 400

def test_get_recipes(testing_client):

    response = testing_client.get('/')
    assert response.status_code == 200

def test_create_recipe(testing_client):

    response = testing_client.post('/', json={'name': 'recipe', 'ingredients': 'ingredient', 'steps': 'step', 'rating': 1, 'favorite': False})
    assert response.status_code == 200

def test_create_recipe_invalid_rating(testing_client):

    response = testing_client.post('/', json={'name': 'recipe', 'ingredients': 'ingredient', 'steps': 'step', 'rating': 7, 'favorite': False})
    assert response.status_code == 200


def test_get_recipe(testing_client):

    response = testing_client.get('/1')
    assert response.status_code == 200

def test_update_recipe(testing_client):

    response = testing_client.put('/1', json={'name': 'recipe', 'ingredients': 'ingredient', 'steps': 'step', 'rating': 1, 'favorite': False})
    assert response.status_code == 200

def test_delete_recipe(testing_client):

    response = testing_client.delete('/1')
    assert response.status_code == 200

