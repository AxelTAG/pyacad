import win32com.client
import pythoncom

def aDouble(xyz):
    """
    Packs a list or tuple of floats into an array for passing to AutoCAD.

    :param xyz: A tuple or list of floats to be packed into an array.
    :type xyz: list of float, tuple of float
    :return: An array variant suitable for AutoCAD.
    :rtype: VARIANT
    """
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, xyz)


def aInt(xyz):
    """
    Packs list of floats into an array for passing to AutoCAD (same as aDouble).

    :param xyz: List of floats or integers.
    :type xyz: list of float, tuple of float
    :return: An array variant suitable for AutoCAD.
    :rtype: VARIANT
    """
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, xyz)


def aDispatch(object):
    """
    Packs a win32 object into Variant Array.

    :param object: Win32 object.
    :return: An array variant suitable for AutoCAD.
    :rtype: VARIANT
    """
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, object)
