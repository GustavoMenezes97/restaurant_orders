from src.models.ingredient import Ingredient  # noqa: F401, E261, E501


# Req 1
def test_ingredient():
    alecrim = Ingredient("alecrim")

    assert alecrim.name == "alecrim"
    assert repr(alecrim) == "Ingredient('alecrim')"
    assert alecrim.__eq__(alecrim)
    assert hash(alecrim) == hash("alecrim")
    assert not alecrim.restrictions
