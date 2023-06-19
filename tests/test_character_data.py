import pytest
from character_data import get_move_data


def test_get_move_data():
    expected_string = "Startup: 16 |  Active: 4 |  Recovery: 20 |  Cancel: sp* |  Damage: 800 |  Guard: LH |  On Hit: +2 |  On Block: -4 | "
    assert get_move_data("Ryu", "6HK") == expected_string


def test_get_move_data_move_not_found():
    assert get_move_data("Ryu", "Banana") is False


def test_get_move_data_character_not_found():
    assert get_move_data("Cat", "Banana") is False


def test_get_move_data_all_characters():
    character_names = [
        "Blanka", "Cammy", "Chun-Li", "Dee_Jay", "Dhalsim", "E.Honda", "Guile", "Jamie", "JP", "Juri", "Ken",
        "Kimberly",
        "Lily", "Luke", "Manon", "Marisa", "Ryu", "Zangief"]
    for character in character_names:
        assert get_move_data(character, "LP") is not False
        assert get_move_data(character, "JLP") is not False


if __name__ == '__main__':
    pytest.main()
