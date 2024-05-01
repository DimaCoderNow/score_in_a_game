import json
import random
import unittest
from main import get_score, TIMESTAMPS_COUNT

COUNT_TESTS_FOR_EQUAL = 50000


def get_game_stamps_from_json():
    with open("game_stamps_for_test.json", "r") as file:
        return json.load(file)


class TestGetScoreMethods(unittest.TestCase):
    test_game_stamps = get_game_stamps_from_json()

    def _get_random_offset(self):
        return self.test_game_stamps[random.randint(0, TIMESTAMPS_COUNT)]

    def test_equal(self):
        for i in range(COUNT_TESTS_FOR_EQUAL):
            test_data = self._get_random_offset()
            self.assertEqual(
                get_score(
                    self.test_game_stamps,
                    test_data["offset"]
                ),
                (test_data["score"]["home"], test_data["score"]["away"])
            )

    def test_non_existent_offset(self):
        self.assertEqual(
            get_score(
                self.test_game_stamps,
                self.test_game_stamps[-1]["offset"] + 1
            ), (None, None)
        )


if __name__ == '__main__':
    unittest.main()
