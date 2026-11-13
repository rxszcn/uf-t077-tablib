class TablibException(Exception):
    """Tablib common exception."""


class InvalidDatasetType(TablibException, TypeError):
    """Only Datasets can be added to a Databook."""


class InvalidDimensions(TablibException, ValueError):
    """The size of the column or row doesn't fit the table dimensions."""


class InvalidDatasetIndex(TablibException, IndexError):
    """Outside of Dataset size."""


class HeadersNeeded(TablibException, AttributeError):
    """Header parameter must be given when appending a column to this Dataset."""


class DuplicateHeadersError(TablibException, ValueError):
    """Headers must be unique; one or more header names were repeated.

    The offending header values are available on the ``duplicates``
    attribute so callers can report or repair them programmatically.
    """

    def __init__(self, duplicates):
        self.duplicates = list(duplicates)
        super().__init__(
            "Duplicate column header(s) found: "
            + ", ".join(repr(d) for d in self.duplicates)
            + ". Headers must be unique so that columns can be addressed "
              "by name. Rename the duplicates, or pass "
              "deduplicate_headers=True to rename them automatically."
        )


class UnsupportedFormat(TablibException, NotImplementedError):
    """Format not supported."""
