import unittest


class Clock:

    @staticmethod
    def get_hour_pointer_degrees(hours, minutes):
        return 30 * hours + 0.5 * minutes

    @staticmethod
    def get_minute_pointer_degrees(minutes):
        return 6 * minutes

    @classmethod
    def min_angle_between_pointers(cls, hours=0, minutes=0):
        hours_pointer_angle = cls.get_hour_pointer_degrees(hours, minutes)
        minutes_pointer_angle = cls.get_minute_pointer_degrees(minutes)

        first_angle = abs(hours_pointer_angle - minutes_pointer_angle)
        second_angle = 360 - first_angle

        return min(first_angle, second_angle)


class TestClock(unittest.TestCase):

    def test_same_angle_between_pointers(self):
        self.assertEqual(Clock.min_angle_between_pointers(12, 0), 0)
        self.assertEqual(Clock.min_angle_between_pointers(0, 0), 0)
        self.assertEqual(Clock.min_angle_between_pointers(6, 30), 15)

    def test_opposite_angle_between_pointers(self):
        self.assertEqual(Clock.min_angle_between_pointers(12, 30), 165)
        self.assertEqual(Clock.min_angle_between_pointers(3, 45), 157.5)

    def test_hour_pointer_before_min_pointer(self):
        self.assertEqual(Clock.min_angle_between_pointers(7, 45), 37.5)
        self.assertEqual(Clock.min_angle_between_pointers(3, 30), 75)

    def test_min_pointer_before_hour_pointer(self):
        self.assertEqual(Clock.min_angle_between_pointers(10, 0), 60)
        self.assertEqual(Clock.min_angle_between_pointers(9, 30), 105)


if __name__ == '__main__':
    unittest.main()