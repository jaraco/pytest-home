import platform

import pytest


@pytest.fixture
def alt_home(monkeypatch, tmp_path_factory):
    """
    >>> home = getfixture('alt_home')
    >>> list(home.iterdir())
    []
    >>> import pathlib
    >>> pathlib.Path('~').expanduser() == home
    True
    """
    var = 'USERPROFILE' if platform.system() == 'Windows' else 'HOME'
    home = tmp_path_factory.mktemp('home')
    monkeypatch.setenv(var, str(home))
    return home