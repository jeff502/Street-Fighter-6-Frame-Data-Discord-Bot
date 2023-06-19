import pytest
from handle_user_inputs import rearrange_input, replace_input, character_aliases

replacements = {
    "QCF": "236",
    "QCB": "214",
    "HCF": "41236",
    "HCB": "63214",
    "DP": "623",
    "BDP": "412",
    "DU": "28",
    "BF": "46",
    "63214789": "360",
    "6321478963214789": "720",
    "BFBF": "4646",
    "JAB": "LP",
    "AB": "LP",
    "STRONG": "MP",
    "FIERCE": "HP",
    "SHORT": "LK",
    "FORWARD": "MK",
    "ROUNDHOUSE": "HK",
    "KICKS": "KKK",
    "PUNCHES": "PPP",
    "ALL": "PPPKKKK",
    "TAUNT": "PPPKKKK",
    "THROW": "LPLK"
}


def test_replace_input():
    for key, value in replacements.items():
        assert replace_input(key) == value


def test_replace_input_input_equals_value():
    for _, value in replacements.items():
        assert replace_input(value) == value


def test_replace_input_no_matches():
    testing_strings = ["abc", "123", "xyz", "Jbanana"]
    for random_string in testing_strings:
        assert replace_input(random_string) == random_string


def test_replace_input_jab_and_j():
    testing_two_j = "JQCFJAB"
    testing_one_j = "JQCFLK"
    testing_zero_j = "QCFLP"
    assert replace_input(testing_two_j) == "J236LP"
    assert replace_input(testing_one_j) == "J236LK"
    assert replace_input(testing_zero_j) == "236LP"


def test_rearrange_input():
    input_string = "123JQCF456BF789"
    expected_output = "J123456789QCFBF"
    input_throw = "THROW8"
    expected_output_input_throw = "8THROW"
    assert rearrange_input(input_string) == expected_output
    assert rearrange_input(input_throw) == expected_output_input_throw


def test_rearrange_input_with_j():
    input_string = "QCFJ123BF456"
    expected_output = "J123456QCFBF"
    assert rearrange_input(input_string) == expected_output


def test_character_aliases():
    assert character_aliases("Ehonda") == "E.Honda"
    assert character_aliases("Honda") == "E.Honda"
    assert character_aliases("Chun") == "Chun-Li"
    assert character_aliases("Chunli") == "Chun-Li"
    assert character_aliases("Li") == "Chun-Li"
    assert character_aliases("Dj") == "Dee_Jay"
    assert character_aliases("Deejay") == "Dee_Jay"
    assert character_aliases("Dhal") == "Dhalsim"
    assert character_aliases("Sim") == "Dhalsim"
    assert character_aliases("Jp") == "JP"
    assert character_aliases("Gief") == "Zangief"
    assert character_aliases("Zan") == "Zangief"
    assert character_aliases("Kim") == "Kimberly"
    assert character_aliases("Ryu") == "Ryu"
    assert character_aliases("Cat") == "Cat"


if __name__ == '__main__':
    pytest.main()

