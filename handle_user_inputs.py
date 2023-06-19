import re


def character_aliases(user_character: str) -> str:
    character_name_dict = {
        "Ehonda": "E.Honda",
        "Honda": "E.Honda",
        "Chun": "Chun-Li",
        "Chunli": "Chun-Li",
        "Li": "Chun-Li",
        "Dj": "Dee_Jay",
        "Deejay": "Dee_Jay",
        "Dhal": "Dhalsim",
        "Sim": "Dhalsim",
        "Jp": "JP",
        "Gief": "Zangief",
        "Zan": "Zangief",
        "Kim": "Kimberly"
    }
    if user_character in character_name_dict:
        return character_name_dict[user_character]
    return user_character


def replace_input(input_string: str) -> str:
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

    # Ignore the leading 'J' if present
    if input_string.count("J") > 1:
        input_string = input_string.lstrip('J')
        j = "J"
    else:
        j = ""

    # Remove '5'
    input_string = "".join(letter for letter in input_string if letter != "5")

    # Sort the keys in descending order of length
    sorted_keys = sorted(replacements.keys(), key=len, reverse=True)

    # Find and replace the keys with their values
    pattern = re.compile('|'.join(re.escape(key) for key in sorted_keys))
    result = pattern.sub(lambda x: replacements[x.group()], input_string)

    return j + result


def rearrange_input(input_string: str) -> str:
    # Match the 'j' in the string
    j_match = re.search(r'J', input_string)
    j = j_match.group() if j_match else ''

    # Remove 'j' from the input string
    processed_string = input_string.replace('J', '')

    # Extract the numbers and letters using regex
    numbers_match = re.findall(r'\d+', processed_string)
    letters_match = re.findall(r'[A-Za-z]+', processed_string)

    # Concatenate the 'j', numbers, and letters in the desired order
    rearranged_string = j + ''.join(numbers_match) + ''.join(letters_match)
    return rearranged_string
