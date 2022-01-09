
from pathlib_ext import LocalPath

def test_local():
    path = LocalPath('/foo/bar')
    assert (path / 'baz').parent == LocalPath('/foo/bar')

