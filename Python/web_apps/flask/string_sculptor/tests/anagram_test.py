import unittest

from core import anagram


class AnagramTestCase(unittest.TestCase):
    """Tests for anagram.py"""

    def test_anagram_maker(self):
        """Test anagram_maker function."""
        n = None
        a = anagram.anagram_phrases("silent")
        while n != "listen".lower():
            n = next(a)
        self.assertIn("listen", n)