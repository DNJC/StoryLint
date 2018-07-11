
from storyready import Story, gwts,asa
import unittest


class testStoryready(unittest.TestCase):


    def test_two_stories_one_without_gwts(self):
        stories = [Story("a story with no gwts"),
                   Story("Given this When that Then the other etc.")]

        self.assertEqual(1, gwts(stories))


    def test_two_stories_one_without_asa(self):
        stories = [Story("a story with no Story format"),
                   Story("As a frog I Want a pond So That I can swim")]

        self.assertEqual(1, asa(stories))
