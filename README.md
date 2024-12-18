# pyacad

A package aimed to simplfy coding of Activex Automation Module of AutoCAD, based on pywin32 library.


## Features

- Uses of COM (Componnent Object Model of Microsoft) for manipulate AutoCAD application with Python.
- Python Autocad class for manipulate.

## Usage

```
from pyacad import Autocad, APoint

# Create a line in the active document model space.
acad = Autocad()
p0 = APoint(1, 1)
p1 = APoint(2, 3)
acad.model.AddLine(p0(), p1())

# Zoom the line by extents.
acad.app.ZoomExtents()
```


## Links

- Documentation at: [ReadTheDocs](https://pyacad.readthedocs.io/en/latest/)
- Source code and issue tracking at: [GitHub](https://pypi.org/project/pyacad/)

## Support me:

- If you want to pay me for a beer, coffee, or something else: [C|_|] (https://www.paypal.com/paypalme/KevinAxelTagliaferri)