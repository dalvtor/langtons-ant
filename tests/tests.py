import unittest
from src.game import LangtonsAnt
from src.direction import Direction


class TestLangtonsAnt(unittest.TestCase):

    def setUp(self):
        self.game = LangtonsAnt(
            [[False, False, False], [False, False, False], [False, False, False]],
            (1, 1)
        )

    def test_init(self):
        with self.assertRaises(TypeError):
            LangtonsAnt([[True, False], [False, False]], (2, 2))

        with self.assertRaises(TypeError):
            LangtonsAnt([[True, False], [False, False]], 2)

        with self.assertRaises(TypeError):
            LangtonsAnt([[True, False], [False, False]], ('x', '1'))

        game = LangtonsAnt([[True, False], [False, False]], (1, 1))
        self.assertEqual(game.state, [[True, False], [False, False]])

    def test_rotate_clockwise(self):
        self.assertEqual(Direction.get_direction(self.game.direction), Direction.LEFT)
        self.game.rotate_clockwise()
        self.assertEqual(Direction.get_direction(self.game.direction), Direction.UP)
        self.game.rotate_clockwise()
        self.assertEqual(Direction.get_direction(self.game.direction), Direction.RIGHT)
        self.game.rotate_clockwise()
        self.assertEqual(Direction.get_direction(self.game.direction), Direction.DOWN)
        self.game.rotate_clockwise()
        self.assertEqual(Direction.get_direction(self.game.direction), Direction.LEFT)

    def test_rotate_anticlockwise(self):
        self.assertEqual(Direction.get_direction(self.game.direction), Direction.LEFT)
        self.game.rotate_anticlockwise()
        self.assertEqual(Direction.get_direction(self.game.direction), Direction.DOWN)
        self.game.rotate_anticlockwise()
        self.assertEqual(Direction.get_direction(self.game.direction), Direction.RIGHT)
        self.game.rotate_anticlockwise()
        self.assertEqual(Direction.get_direction(self.game.direction), Direction.UP)
        self.game.rotate_anticlockwise()
        self.assertEqual(Direction.get_direction(self.game.direction), Direction.LEFT)

    def test_flip_color(self):
        self.assertFalse(self.game.state[1][1])
        self.game.flip_color(1, 1)
        self.assertTrue(self.game.state[1][1])
        self.game.flip_color(1, 1)
        self.assertFalse(self.game.state[1][1])

    def test_next(self):
        self.assertFalse(self.game.state[1][1])
        self.game.next()
        self.game.position['x'] = 0
        self.game.position['y'] = 1
        self.assertTrue(self.game.state[1][1])
        self.game.next()
        self.game.position['x'] = 0
        self.game.position['y'] = 2


if __name__ == '__main__':
    unittest.main()
