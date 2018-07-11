Story Ready
===========

Story Ready is a very simple Python library that takes a list of stories and performs a number of common readniess checks:

- Acceptance Criteria: Given, When, Thens
- User Story format: As a, I want, So that
- Story size over percentage of velocity
- Rank a bunch of stories by all criteria

A simple example
----------------

..code-block:: python

  from storyready import Story, has_gwt
  
  stories = [Story(1,"a story with no gwts",0),
             Story(2,"Given this When that Then the other etc.",0)]

        no_gwts = has_gwt(stories)

        print("%{0} stories don't have GWTs".format(len(no_gwts))
        
