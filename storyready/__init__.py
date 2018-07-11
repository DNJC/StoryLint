from re import search, IGNORECASE, DOTALL


class Story():

    def __init__(self, description=None, size=None):
        self.description = description
        self.size = size


def has_gwt(issues):
    """ Return number of stories without Given, When, Thens in the Story description """

    no_gwts = 0
    for issue in issues:
        if search(r"^.*\bGiven\b.*When\b.*Then\b.*$",issue.description,IGNORECASE | DOTALL) is None:
            no_gwts += 1

    return no_gwts


def has_asa(issues):
    """ Return number of stories without As a, I want, So That in the Story description  """

    no_asa = 0
    for issue in issues:
        if search(r"^.*\bAs a\b.*I want\b.*So that\b.*$",issue.description,IGNORECASE | DOTALL) is None:
            no_asa += 1

    return no_asa


def has_rightsize(issues, velocity, pcnt_velocity=0.30):
    """ stories that are over velocity*pcnt_velocity """

    over = 0
    for issue in issues:
        if issue.size > velocity*pcnt_velocity:
            over += 1

    return over


def has_description(issues):
    """ stories that have no descriptions """

    blank = 0
    for issue in issues:
        if not issue.description:
            blank += 1

    return blank


def has_size(issues):
    """ stories that have no size """

    blank = 0
    for issue in issues:
        if not issue.size:
            blank += 1

    return blank