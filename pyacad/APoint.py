import win32com.client
import pythoncom
import operator
from win32com.client import VARIANT


class APoint(VARIANT):
    """
    3D point with basic geometric operations and support for passing as a
    parameter for `AutoCAD` Automation functions.

    :ivar x: The X coordinate of the point.
    :vartype x: int, float, list of int, list of float, tuple of int, tuple of float
    :ivar y: The Y coordinate of the point.
    :vartype y: int, float, None
    :ivar z: The Z coordinate of the point.
    :vartype z: int, float, None
    """

    def __init__(self, x: float, y: float = 0, z: float = 0):
        """
        Initializes the Point3D with the given coordinates.

        :param x: The X coordinate of the point.
        :type x: int, float, list of int, list of float, tuple of int, tuple of float
        :param y: The Y coordinate of the point.
        :type y: int, float, None
        :param z: The Z coordinate of the point.
        :type z: int, float, None
        """
        super().__init__(vt=pythoncom.VT_ARRAY | pythoncom.VT_R8, value=(x, y, z))

        self._x = x
        self._y = y
        self._z = z

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, value):
        self._x = value
        self._set_value(newval=(self._x, self.y, self.z))

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, value):
        self._y = value
        self._set_value(newval=(self.x, self._y, self.z))

    @property
    def z(self):
        return self._z

    @z.setter
    def z(self, value):
        self._z = value
        self._set_value(newval=(self.x, self.y, self._z))

    def __call__(self):
        return self

    def __getitem__(self, item):
        return list(self)[item]

    def __iter__(self):
        return iter((self.x, self.y, self.z))

    def __eq__(self, other):
        if type(self) == type(other):
            if tuple(self) == tuple(other):
                return True
            else:
                return False
        else:
            return False

    def __add__(self, other):
        return self.__left_op(self, other, operator.add)

    def __sub__(self, other):
        return self.__left_op(self, other, operator.sub)

    def __mul__(self, other):
        return self.__left_op(self, other, operator.mul)

    def __truediv__(self, other):
        return self.__left_op(self, other, operator.truediv)

    def __floordiv__(self, other):
        return self.__left_op(self, other, operator.floordiv)

    def __iadd__(self, other):
        return self.__left_op(self, other, operator.iadd)

    def __isub__(self, other):
        return self.__left_op(self, other, operator.isub)

    def __imul__(self, other):
        return self.__left_op(self, other, operator.imul)

    def __idiv__(self, other):
        return self.__left_op(self, other, operator.idiv)

    def __neg__(self):
        return self.__left_op(self, -1, operator.mul)

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "APoint(%.2f, %.2f, %.2f)" % tuple(self)

    def __left_op(self, p1, p2, op):
        if isinstance(p2, (float, int)):
            return APoint(op(p1[0], p2), op(p1[1], p2), op(p1[2], p2))
        return APoint(op(p1[0], p2[0]), op(p1[1], p2[1]), op(p1[2], p2[2]))

    def distance_to(self, other):
        """
        Calculate the distance to another 3D point.

        :param other: The other Point3D object to calculate the distance to.
        :type other: Point3D
        :return: The distance between the two points.
        :rtype: float
        """
        return distance(self, other)


def distance(p1, p2):
    """
    Calculate the distance to another 3D point.

    :param p1: The other Point3D object to calculate the distance to.
    :type p1: Point3D
    :param p2: The other Point3D object to calculate the distance to.
    :type p2: Point3D
    :return: The distance between the two points.
    :rtype: float
    """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2 + (p1.z - p2.z) ** 2) ** 0.5
