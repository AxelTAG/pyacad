Usage
=====

For the following examples, we will use :class:`Autocad` and :class:`APoint`.

.. code:: python

   from pyacad import Autocad

Initializing the AutoCAD API:
-----------------------------

.. code:: python

    acad = Autocad()

Retrieving active document name
-------------------------------

.. code:: python

    # Only the document name.
    acad.doc.Name

    # For the document path.
    acad.doc.FullName

Adding objects to the active document
-------------------------------------

Points
^^^^^^

.. code:: python

    p0 = APoint(2, 1)
    point = acad.model.AddPoint(p0())

Lines
^^^^^^

.. code:: python

    p0, p1 = APoint(1, 1), APoint(2, 1)
    line = acad.model.AddLine(p0(), p1())

Polylines
^^^^^^^^^
For drawing polylines we need to use aDouble.

.. code:: python

    from pyacad import aDouble
    points = aDouble([0, 0, 1, 0, 1, 1, 0, 1, 0, 0])
    polyline = acad.model.AddLightweightPolyline(points)

Circles
^^^^^^^

.. code:: python

    p0 = APoint(3, 1)
    radius = .5
    circle = acad.model.AddCircle(p0(), radius)

Text
^^^^

.. code:: python

    p0 = APoint(0, 3)
    height = 1
    textstring = "Hello World!"
    text = acad.model.AddText(textstring, p0(), height)

MultiLineText
^^^^^^^^^^^^^

.. code:: python

    p0 = APoint(0, 4)
    width = 1
    textstring = "This is a MText."
    mtext = acad.model.AddMText(p0(), width, textstring)

Hatch
^^^^^

For drawing hatchs we need to use aDispatch.

.. code:: python

    # Defining boundary.
    outer_boundary = []
    outer_boundary.append(acad.model.AddCircle(APoint(0, 0)(), 1))
    outer_boundary_dispatch = aDispatch(outer_boundary)

    # Creating hatch and adding boundary.
    hatch = acad.model.AddHatch(0, "ANSI31", True)
    hatch.AppendOuterLoop(outer_boundary_dispatch)
    hatch.Evaluate()

Aligned Dimension
^^^^^^^^^^^^^^^^^

.. code:: python

    p0, p1, p2 = APoint(0, 4), APoint(4, 4), APoint(2, 4.5)
    acad.model.AddDimAligned(p0(), p1(), p3())

Further information about objects
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

For more information on creating objects, I recommend visiting the official Autodesk site on ActiveX Automation for your corresponding version of AutoCAD.

* `AutoCAD 2024 <https://help.autodesk.com/view/OARX/2024/ENU/?guid=GUID-36BF58F3-537D-4B59-BEFE-2D0FEF5A4443>`_
* `AutoCAD 2023 <https://help.autodesk.com/view/OARX/2023/ENU/?guid=GUID-36BF58F3-537D-4B59-BEFE-2D0FEF5A4443>`_

Retrieving over documents, layouts, layer, objects and more.
------------------------------------------------------------

Retrieving documents from the AutoCAD API
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    acad.iter_documents()

Retrieving blocks from the document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    blocks = acad.iter_blocks()

Alternatively, you can pass a specific document using the document parameter, which should be of the type returned by the app.iter_documents() function.

.. code:: python

    docs = [*acad.iter_documents()]
    doc_selected = docs[0]  # 0 if you want select first document of list.
    blocks = acad.iter_blocks(document=doc_selected)

Retrieving dimension styles from the document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    dim_styles = acad.iter_dim_styles()

You can also do it in the same way as shown in iter_blocks().

Retrieving layers from the document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    layers = acad.iter_layers()

You can also do it in the same way as shown in iter_blocks().

Retrieving layouts from the document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

    layouts = acad.iter_layouts()

You can also do it in the same way as shown in iter_blocks().

Retrieving objects from the document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

You can iterate over the objects in a drawing.

.. code:: python

    objects = acad.iter_objects()

Also you can filter for a concrete obejct type.

.. code:: python

    text_obejects = acad.iter_objects("Text")

Retrieving text styles from the document
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. code:: python

  text_styles = acad.iter_text_styles()

You can also do it in the same way as shown in iter_blocks().
