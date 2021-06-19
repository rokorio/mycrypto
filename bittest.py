import fieldelement
import point


class point_Test(TestCase):
    def on_the_curve(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)

        valid_points = ((192, 105), (17, 56), (1, 193))
        invalid_points = ((200, 119), (42, 99))
        for x_raw, y_raw in valid_points:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            Point(x, y, a, b)

        for x_raw, y_raw in invalid_points:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            with self.assertRaises(ValueError):
                Point(x, y, a, b)

    def test_add(self):
        prime = 223
        a = FieldElement(0, prime)
        b = FieldElement(7, prime)

        p1 = (170, 142)
        p2 = (60, 139)
        invalid_points = ((200, 119), (42, 99))
        for x_raw, y_raw in p1:
            x = FieldElement(x_raw, prime)
            y = FieldElement(y_raw, prime)
            p1 = Point(x, y, a, b)
            for x_raw1, y_raw1 in p2:
                x1 = FieldElement(x_raw1, prime)
                y1 = FieldElement(y_raw1, prime)
                p2 = Point(x1, y1, a, b)
            return p1 + p2
        