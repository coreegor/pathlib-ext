
import os
import pwd
import string
import pytest
import inspect
from getpass import getuser
from socket import gethostname
from pathliberty import SSHPath
from datetime import date, datetime

host = 'localhost'
parent = f'/home/{getuser()}'

def get_func_name():
    return inspect.stack()[1][3]

@pytest.fixture
def ssh_path(ssh_session):
    root = SSHPath(f'{parent}/{gethostname()}', ssh=ssh_session)
    root.mkdir(exist_ok=True)
    assert root.is_dir()
    yield root
    root.rmdir(recursive=True)

@pytest.fixture
def test_path(ssh_path, request):
    test_path = ssh_path / request.function.__name__
    test_path.mkdir(exist_ok=True)
    yield test_path

@pytest.fixture
def test_files(test_path):
    num = 10
    files = [(test_path / f'{char}.txt') for char in string.ascii_uppercase[:num]]
    for file in files:
        file.touch()
    yield test_path, files

def test_base(ssh_path):
    new = ssh_path / f'../../{getuser()}'

    assert new.resolve() == SSHPath(parent, host=host)
    assert ssh_path.is_dir()
    assert ssh_path.host == host
    assert ssh_path.parent == SSHPath(parent, host=host)
    assert ssh_path.getsize() > 0
    today = datetime.today()
    assert ssh_path.getmtime(dt=True).date() == today.date()
    assert ssh_path.getatime(dt=True).date() == today.date()

def test_chown(ssh_path):
    ssh_path.chown(os.getuid(), os.getgid())

def test_touch(test_path):
    with pytest.raises(OSError):
        test_path.mkdir()

    (test_path / 'A.txt').touch()
    with pytest.raises(OSError):
        (test_path / 'A.txt').touch(exist_ok=False)

def test_iterdir(test_files):
    path, files = test_files

    iterdir = path.iterdir()
    assert len(list(iterdir)) == len(files)

    for p in iterdir:
        assert isinstance(p, SSHPath)

def test_glob(test_files):
    path, files = test_files

    assert len(list(path.glob('*.txt'))) == len(files)
    assert len(list(path.parent.rglob('*.txt'))) == len(files)

def test_stat(test_path):
    stat = test_path.stat()
    pwd_db = pwd.getpwnam(getuser())
    assert stat.st_uid == pwd_db.pw_uid
    assert stat.st_gid == pwd_db.pw_gid
