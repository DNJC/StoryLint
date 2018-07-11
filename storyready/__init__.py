from re import search, IGNORECASE, DOTALL


class Story():

    def __init__(self, description):
        self.description = description


"""
Look for Given, When, Thens in the Story description field
"""


def gwts(issues):
    no_gwts = 0
    for issue in issues:
        if search(r"^.*\bGiven\b.*When\b.*Then\b.*$",issue.description,IGNORECASE | DOTALL) is None:
            no_gwts += 1

    return no_gwts


def asa(issues):
    no_asa = 0
    for issue in issues:
        if search(r"^.*\bAs a\b.*I want\b.*So that\b.*$",issue.description,IGNORECASE | DOTALL) is None:
            no_asa += 1

    return no_asa
