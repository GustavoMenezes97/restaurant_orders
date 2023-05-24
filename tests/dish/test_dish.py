from src.models.dish import Dish  # noqa: F401, E261, E501
from src.models.ingredient import Ingredient
import pytest


# Req 2
def test_dish():
    parmegiana = Dish("parmegiana de frango", 32.00)

    assert parmegiana.name == "parmegiana de frango"

    assert hash(parmegiana) == hash(Dish("parmegiana de frango", 32.00))
    assert hash(parmegiana) != hash(Dish("parmegiana de carne", 39.00))

    assert parmegiana.__eq__(Dish("parmegiana de frango", 32.00)) is True
    assert parmegiana.__eq__(Dish("parmegiana de carne", 39.00)) is False

    assert repr(parmegiana) == "Dish('parmegiana de frango', R$32.00)"

    assert not parmegiana.get_restrictions()

    with pytest.raises(TypeError, match="Dish price must be float."):
        Dish("parmegiana de frango", "32.00")

    with pytest.raises(
        ValueError, match="Dish price must be greater then zero."
    ):
        Dish("parmegiana de frango", 0.00)

    parmegiana.add_ingredient_dependency(Ingredient("molho de tomate"), 1)

    assert parmegiana.get_ingredients() == {Ingredient("molho de tomate")}
