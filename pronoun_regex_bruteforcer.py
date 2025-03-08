import sys, re

from pronoun_reference import pronouns



def get_pronouns_from_regex(pronoun_regex):
    pronoun_types = pronouns["nominative"].keys()

    pronoun_list = []
    for _type in pronoun_types:
        buffer = ""
        for i, case in enumerate(["nominative", "accusative", "possessive"]):
            pronoun = pronouns[case][_type]

            if re.fullmatch(pronoun_regex, pronoun.lower(), re.IGNORECASE) != None:
                if i != 0: buffer += "/"
                buffer += pronoun
                
        if buffer != "":
            pronoun_list.append(buffer)

    return pronoun_list



if __name__ == "__main__":
    if len(sys.argv) < 2: sys.exit("No pronouns regex provided")

    possible_pronouns = get_pronouns_from_regex(sys.argv[1])

    print("Possible pronouns:")
    for pronoun in possible_pronouns:
        print(f"- {pronoun}")