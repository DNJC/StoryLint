"""A little collection  of methods that check user stories for certain properties.

It supports checks for measuable things that are typically included in a Definition of Ready.

"""
from re import search, IGNORECASE, DOTALL
from collections import Counter


class Story():

    def __init__(self, id,description=None, size=None, parent=None):
        self.description = description
        self.size = size
        self.parent = parent
        self.id = id


def has_gwt(issues):
    """ Return number of stories without Given, When, Thens in the Story description """

    no_gwts = []
    for issue in issues:
        if issue.description is None or search(r"^.*\bGiven\b.*When\b.*Then\b.*$",issue.description,IGNORECASE | DOTALL) is None :
            no_gwts.append(issue.id)

    return no_gwts


def has_asa(issues):
    """ Return number of stories without As a, I want, So That in the Story description  """

    no_asa = []
    for issue in issues:
        if issue.description is None or search(r"^.*\bAs a\b.*I want\b.*So that\b.*$",issue.description,IGNORECASE | DOTALL) is None:
            no_asa.append(issue.id)

    return no_asa


def has_rightsize(issues, velocity, pcnt_velocity=0.30):
    """ stories that are over velocity*pcnt_velocity """

    over = []
    for issue in issues:
        if issue.size is None or issue.size > velocity*pcnt_velocity:
            over.append(issue.id)

    return over


def has_description(issues):
    """ stories that have no descriptions """

    blank = []
    for issue in issues:
        if not issue.description:
            blank.append(issue.id)

    return blank


def has_size(issues):
    """ stories that have no size """

    blank = []
    for issue in issues:
        if not issue.size:
            blank.append(issue.id)

    return blank


def rank(issues, velocity, pcnt_velocity=0.30):
    """ run all checks and assign a 1..5 rank
    5 = fails all checks
    1 = fails 1 check
    Return a dict of id : rank
    """

    no_gwts = has_gwt(issues)
    no_asaa = has_asa(issues)
    not_rightsized = has_rightsize(issues,velocity,pcnt_velocity)
    no_descriptions = has_description(issues)
    no_size = has_size(issues)

    return Counter(no_gwts+no_asaa+not_rightsized+no_descriptions+no_size)
