import win32com.client

def aDouble(xyz):
    """
    Packs list of floats into an array for passing to AutoCAD.

    Parameters
    ----------
    xyz: list
    Tuple or list of floats.

    Returns
    -------
    Array variant.
    """
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, xyz)


def aInt(xyz):
    """
    Packs list of floats into an array for passing to AutoCAD (same as aDouble).
    """
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_R8, xyz)


def aDispatch(vObject):
    """
    Packs a win32 objecto into Variant Array.
    """
    return win32com.client.VARIANT(pythoncom.VT_ARRAY | pythoncom.VT_DISPATCH, vObject)
