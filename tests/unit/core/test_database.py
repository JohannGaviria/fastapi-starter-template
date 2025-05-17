import pytest
from sqlmodel import create_engine
from app.core import database


@pytest.fixture(autouse=True, scope="module")
def patch_engine():
    test_engine = create_engine("sqlite:///:memory:")
    database._engine = test_engine
    yield


def test_engine_is_created():
    """
    Test that the SQLAlchemy engine is created and has the correct URL.
    """
    engine = database.get_engine()
    assert engine is not None
    assert hasattr(engine, 'connect')


def test_get_session_yields_session():
    """
    Test that get_session yields a session object.
    """
    gen = database.get_session()
    session = next(gen)
    assert hasattr(session, 'close')
    try:
        next(gen)
    except StopIteration:
        pass
