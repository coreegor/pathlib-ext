from socket import gethostname
from pathlib_ext.ssh import SSHSession

def test_ssh_session(ssh_session):
    assert ssh_session.exec('hostname') == gethostname()
