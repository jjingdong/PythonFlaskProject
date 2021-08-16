from unittest import TestCase

from main import app
from match import match


class MatchTestCase(TestCase):

    def test_empty_match(self):
        self.assertTrue(match('', ''))


class AppTestCase(TestCase):

    def setUp(self) -> None:
        self.client = app.test_client()
