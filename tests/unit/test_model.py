from api.models import Recipe
import pytest

def test_create_recipe():
    """
    GIVEN a Recipe model
    WHEN a new Recipe is created
    THEN check the name, ingredients, steps, rating and favorite fields are defined correctly
    """
    recipe = Recipe('Egg Omelete', 'Large Eggs, Salt, Pepper, Butter', 'Crack eggs, pour eggs, cook eggs, serve', 5, True)
    assert recipe.name == 'Egg Omelete'
    assert recipe.ingredients == 'Large Eggs, Salt, Pepper, Butter'
    assert recipe.steps == 'Crack eggs, pour eggs, cook eggs, serve'
    assert recipe.rating == 5
    assert recipe.favorite == True