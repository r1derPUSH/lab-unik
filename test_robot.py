import unittest
from robot import robot_route


class TestRobotRoute(unittest.TestCase):

    def test_5x5(self):
        matrix = [
            [1, 2, 3, 4, 5],
            [6, 7, 8, 9, 10],
            [11, 12, 13, 14, 15],
            [16, 17, 18, 19, 20],
            [21, 22, 23, 24, 25]
        ]
        expected = [
            1, 2, 3, 4, 5,
            10, 9, 8, 7, 6,
            11, 12, 13, 14, 15,
            20, 19, 18, 17, 16,
            21, 22, 23, 24, 25
        ]
        self.assertEqual(robot_route(matrix), expected)

    def test_2x4(self):
        matrix = [
            [1, 2, 3, 4],
            [5, 6, 7, 8]
        ]
        expected = [1, 2, 3, 4, 8, 7, 6, 5]
        self.assertEqual(robot_route(matrix), expected)

    def test_n_equals_1(self):
        matrix = [
            [1],
            [2],
            [3],
            [4]
        ]
        expected = [1, 2, 3, 4]
        self.assertEqual(robot_route(matrix), expected)

    def test_m_equals_6(self):
        matrix = [
            [1, 2],
            [3, 4],
            [5, 6],
            [7, 8],
            [9, 10],
            [11, 12]
        ]
        expected = [
            1, 2,
            4, 3,
            5, 6,
            8, 7,
            9, 10,
            12, 11
        ]
        self.assertEqual(robot_route(matrix), expected)


if __name__ == "__main__":
    unittest.main()