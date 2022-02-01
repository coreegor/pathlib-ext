from _pytest.fixtures import fixture
import pytest
from pathliberty import ssh_config
from pathliberty.ssh import SSHSession

def pytest_addoption(parser):
    parser.addoption("--host", action="store", help="host name", default='localhost')
    parser.addoption("--port", action="store", help="port num", default=ssh_config.DEFAULT_PORT, type=int)
    parser.addoption("--password", action="store", help="password", default=None)


@pytest.fixture(scope='package', autouse=True)
def setup_port(request):
    ssh_config.DEFAULT_PORT = request.config.getoption('--port')
    
@pytest.fixture
def ssh_session(request):
    ssh_config.DEFAULT_CONNECTION_TIMEOUT = 1.0
    ssh = SSHSession(
        request.config.getoption('--host'),
        password=request.config.getoption('--password'),
    )
    yield ssh