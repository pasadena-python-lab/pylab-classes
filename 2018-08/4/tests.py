"""
Advanced Track

Pylab Pasadena

As we are working through the exercise, attempt to write everything as a small
function. Can you write a basic testcase for each one.

# TASK 1

Can you get these tests passing?
"""

import unittest

from classcode.exercise import *

class TheWorldIsSaneTestCase(unittest.TestCase):

    def test_world_is_sane(self):
        self.assertEqual(1 + 1, 2)

    def test_world_is_still_sane(self):
        self.assertNotEqual(1 + 2, 2)

    def test_world_is_not_perfectly_sane(self):
        self.assertEqual(1 + 1, 3)

class StarterTestCase(unittest.TestCase):

    def test_assert_types(self):
        # Task - how are these getting imported?
        self.assertIsInstance(url, str)
        self.assertIsInstance(filename, str)

    def test_callables(self):
        # Task -  what is a callable type in python?
        self.assertTrue(callable(file_downloader))

    def test_filename_is_txt(self):
        self.assertTrue('.csv' in  filename)


if __name__ == '__main__':
    unittest.main()
