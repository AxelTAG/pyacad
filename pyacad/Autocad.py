import win32com.client
# from pywintypes import com_error # Not in use.


class Autocad:
    """
    Main class of AutoCAD app.
    """

    def __init__(self, create_if_not_exist: bool = True, visible: bool = True):
        self._app = None
        self._create_if_not_exist = create_if_not_exist
        self._visible = True

    @property
    def app(self):
        """Creates/gets and returns AutoCAD Application."""
        try:
            self._app = win32com.client.GetActiveObject("AutoCAD.Application")
        except:
            if self._create_if_not_exist:
                self._app = win32com.client.Dispatch("AutoCAD.Application")
                self._app.Visible = self._visible
            else:
                return None
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
        """
        Iterate over the objects in a specified 'block'.

        :param block: COM object returned from the AutoCAD application. If `None` is specified,
                      the active layout is used.
        :type block: win32com.client.CDispatch, None
        :param filter_for: A filter for specific object types. Can be a list or tuple of strings.
                           If `None`, no filtering is applied.
        :type filter_for: list of str, tuple of str, None
        :param limit: The maximum number of objects to iterate over. If `None`, no limit is applied.
        :type limit: int, None
        :yield: Generator of objects in the specified layout or active layout if none is specified.
        :rtype: generator
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
        """
        Iterate over the layouts in the specified document.

        :param document: COM object returned from the AutoCAD application. If `None` is specified,
                         the active document is used.
        :type document: win32com.client.CDispatch, None
        :param skip_model: Whether to skip the model layout. Defaults to `False`.
        :type skip_model: bool
        :yield: Generator of layouts in the specified document.
        :rtype: generator
        """
        if not document:
            document = self.doc
        for layout in sorted(document.Layouts, key=lambda x: x.TabOrder):
            if skip_model and not layout.TabOrder:
                continue
            yield layout

    def iter_layers(self, document=None):
        """
        Iterate over the layers in the specified document.

        :param document: COM object returned from the AutoCAD application. If `None` is specified,
                         the active document is used.
        :type document: win32com.client.CDispatch, None
        :yield: Generator of layers in the specified document.
        :rtype: generator
        """
        if not document:
            document = self.doc
        for layer in sorted(document.Layers, key=lambda x: x.Name):
            yield layer

    def iter_blocks(self, document=None):
        """
        Iterate over the existing block definitions in the specified document.

        :param document: COM object returned from the AutoCAD application. If `None` is specified,
                         the active document is used.
        :type document: win32com.client.CDispatch, None
        :yield: Generator of block definitions in the specified document.
        :rtype: generator
        """
        if not document:
            document = self.doc
        for block in sorted(document.Blocks, key=lambda x: x.Name):
            yield block

    def iter_dim_styles(self, document=None):
        """
        Iterate over the existing dimension styles in the specified document.

        :param document: COM object returned from the AutoCAD application. If `None` is specified,
                         the active document is used.
        :type document: win32com.client.CDispatch, None
        :yield: Generator of dimension styles in the specified document.
        :rtype: generator
        """
        if not document:
            document = self.doc
        for dim_style in sorted(document.DimStyles, key=lambda x: x.Name):
            yield dim_style

    def iter_text_styles(self, document=None):
        """
        Iterate over the existing text styles in the specified document.

        :param document: COM object returned from the AutoCAD application. If `None` is specified,
                         the active document is used.
        :type document: win32com.client.CDispatch, None
        :yield: Generator of text styles in the specified document.
        :rtype: generator
        """
        if not document:
            document = self.doc
        for text_styles in sorted(document.TextStyles, key=lambda x: x.Name):
            yield text_styles

    def iter_documents(self):
        """
        Iterate over all the open documents.

        :yield: Generator of documents.
        :rtype: generator
        """
        for document in self.app.Documents:
            yield document
