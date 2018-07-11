
from storyready import Story, has_gwt, has_asa, has_rightsize, has_size, has_description
import unittest


class TestStoryReady(unittest.TestCase):

    def test_two_stories_one_without_gwts(self):
        stories = [Story("a story with no gwts",0),
                   Story("Given this When that Then the other etc.",0)]

        self.assertEqual(1, has_gwt(stories))

    def test_two_stories_one_without_asa(self):
        stories = [Story("a story with no Story format",0),
                   Story("As a frog I Want a pond So That I can swim",0)]

        self.assertEqual(1, has_asa(stories))

    def test_three_stories_with_two_without_size(self):
        stories = [Story(description="story one"),
                   Story(description="story two"),
                   Story(size=100)]

        self.assertEqual(2,has_size(stories))

    def test_three_stories_with_two_no_description(self):
        stories = [Story(size=30),
                   Story(size=10),
                   Story(description="story one")]

        self.assertEqual(2,has_description(stories))

    def test_three_stories_with_two_wrong_size(self):
        stories = [Story(size=30),
                   Story(size=10),
                   Story(size=100)]

        self.assertEqual(1,has_rightsize(stories,200,0.3))