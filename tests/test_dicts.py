import pytest

from utils import dicts

@pytest.fixture
def data_fixture():
    return {"vcs": "mercurial"}


def test_get_val(data_fixture):
    assert dicts.get_val(data_fixture, "vcs", 'git') == "mercurial"
    assert dicts.get_val(data_fixture, "vcs") == "mercurial"
    assert dicts.get_val({}, "vcs", 'git') == "git"
    assert dicts.get_val({}, "vcs", 'bazaar') == "bazaar"
    assert dicts.get_val(data_fixture, "git", 'bazaar') == "bazaar"
