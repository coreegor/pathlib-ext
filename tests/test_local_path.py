from getpass import getuser
import os
from pathliberty import LocalPath

def test_local():
    path = LocalPath('/foo/bar')
    assert (path / 'baz').parent == LocalPath('/foo/bar')

def test_chown(tmp_path):
    path = LocalPath(tmp_path)
    path.chown(os.getuid(), os.getgid())

