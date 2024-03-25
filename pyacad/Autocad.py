import win32com.client
# from pywintypes import com_error # Not in use.


class Autocad:
    """Main class of AutoCAD app."""

    def __init__(self):
        self._app = None

    @property
    def app(self):
        """Creates/gets and returns AutoCAD Application."""
        try:
            self._app = win32com.client.GetActiveObject("AutoCAD.Application")
        except:
            self._app = win32com.client.Dispatch("AutoCAD.Application")
        return self._app

    @property
    def doc(self):
        """Returns active document."""
        return self.app.ActiveDocument

    @property
    def model(self):
        """Returns active model space of curring document."""
        return self.doc.ModelSpace

    def iter_objects(self, block=None, filter_for=None, limit=None):
        """Iters the objects in 'block'.

        Parameters
        ----------
        block : win32com.client.CDispatch, None
            COM object returned from AutoCAD application. If None is specified Active Layout is used.
             (Default value = None)
        filter_for : {list of str, tuple of str, None}
             (Default value = None)
        limit : {int, None}
             (Default value = None)

        Yield
        -------
        generator
            Generator of objects in layout specified (default Active Layout).
        """
        if block is None:
            block = self.doc.ActiveLayout.Block
        if limit is None:
            limit = block.Count
        if filter_for is not None:
            for n in range(limit):
                if block.Item(n).ObjectName in filter_for:
                    yield block.Item(n)
        else:
            for n in range(limit):
                yield block.Item(n)

    def iter_layouts(self, document=None, skip_model=False):
        """Iters layouts from the document passed.

        Parameters
        ----------
        document : win32com.client.CDispatch, None
            COM object returned from AutoCAD application. If None is specified Active Document is used.
             (Default value = None)
        skip_model : bool
             (Default value = False)

        Yield
        -------
        generator
            Generator of layouts in document passed.

        """
        if not document:
            document = self.doc
        for layout in sorted(document.Layouts, key=lambda x: x.TabOrder):
            if skip_model and not layout.TabOrder:
                continue
            yield layout

    def iter_layers(self, document=None):
        """Iters layers from the document passed.

        Parameters
        ----------
        document : win32com.client.CDispatch, None
            COM object returned from AutoCAD application. If None is specified Active Document is used.
             (Default value = None)

        Yield
        -------
        generator
            Generator of layers in document passed.
        """
        if not document:
            document = self.doc
        for layer in sorted(document.Layers, key=lambda x: x.Name):
            yield layer

    def iter_blocks(self, document=None):
        """Iters existing blocks definitions from the document passed.

        Parameters
        ----------
        document : win32com.client.CDispatch, None
            COM object returned from AutoCAD application. If None is specified Active Document is used.
             (Default value = None)

        Yield
        -------
        generator
            Generator of blocks definitions in the document passed.
        """
        if not document:
            document = self.doc
        for block in sorted(document.Blocks, key=lambda x: x.Name):
            yield block

    def iter_dim_styles(self, document=None):
        """Iters existing dimensions styles from the document passed.

        Parameters
        ----------
        document : {win32com.client.CDispatch, None}
            COM object returned from AutoCAD application. If None is specified Active Document is used.
             (Default value = None)

        Yield
        -------
        generator
            Generator of dim styles in document passed.
        """
        pass

    def iter_text_styles(self, document=None):
        """Iters existing texts styles from the document passed.

        Parameters
        ----------
        document : win32com.client.CDispatch, None
            COM object returned from AutoCAD application. If None is specified Active Document is used.
             (Default value = None)

        Yield
        -------
        generator
            Generator of text styles in document passed.
        """
        pass
