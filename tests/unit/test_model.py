from api.models import Recipe
import pytest

def test_create_recipe():

    recipe = Recipe('Chicken and rice', 'Chicken, Salt, Pepper, Rice', 'Cut chicken, add salt and pepper, cook chicken, serve', 5, True)
    assert recipe.name == 'Chicken and rice'
    assert recipe.ingredients == 'Chicken, Salt, Pepper, Rice'
    assert recipe.steps == 'Cut chicken, add salt and pepper, cook chicken, serve'
    assert recipe.rating == 5
    assert recipe.favorite == True