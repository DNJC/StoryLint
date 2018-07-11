
from storyready import Story, has_gwt, has_asa, has_rightsize, has_size, has_description, rank
import unittest


class TestStoryReady(unittest.TestCase):

    def test_two_stories_one_without_gwts(self):
        stories = [Story(1,"a story with no gwts",0),
                   Story(2,"Given this When that Then the other etc.",0)]

        no_gwts = has_gwt(stories)
        self.assertEqual(1, len(no_gwts))

    def test_two_stories_one_without_asa(self):
        stories = [Story(1,"a story with no Story format",0),
                   Story(2,"As a frog I Want a pond So That I can swim",0)]

        no_asas = has_asa(stories)
        self.assertEqual(1, len(no_asas))

    def test_three_stories_with_two_without_size(self):
        stories = [Story(1,description="story one"),
                   Story(2,description="story two"),
                   Story(3,size=100)]

        not_sized = has_size(stories)
        self.assertEqual(2,len(not_sized))

    def test_three_stories_with_two_no_description(self):
        stories = [Story(1,size=30),
                   Story(2,size=10),
                   Story(3,description="story one")]

        no_description = has_description(stories)
        self.assertEqual(2,len(no_description))

    def test_three_stories_with_two_wrong_size(self):
        stories = [Story(1,size=30),
                   Story(2,size=10),
                   Story(3,size=100)]

        not_rightsized = has_rightsize(stories,200,0.3)
        self.assertEqual(1,len(not_rightsized))

    def test_rank(self):
        stories = [Story(1,description="As a I want So that ... Given this When that Then other ",size=10),
                   Story(2,description="rubbish description", size=10),
                   Story(3,size=100)]

        ranked = rank(stories, 200, 0.3)
        print(ranked)
        self.assertEqual(4,ranked[3]) # story 3 fails on everything except empty size
        self.assertEqual(2,ranked[2]) # story 2 fails on GWT and Story format
        self.assertEqual(False,1 in ranked) # story one is perfect
