from socket import gethostname

def test_ssh_session(ssh_session):
    assert ssh_session.exec('hostname') == gethostname()
