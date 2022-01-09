from pathlib import _NormalAccessor

from pathlib_ext.base import AbstractPath, AbstractPathAccessor

class NormalAccessor(_NormalAccessor, AbstractPathAccessor):
    pass

class LocalPath(AbstractPath):
    __slots__ = ()
    accessor_class = NormalAccessor

    def new(self, path: AbstractPath) -> AbstractPath:
        return path
