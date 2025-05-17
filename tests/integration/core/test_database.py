import pytest
from sqlmodel import create_engine, Session
from sqlalchemy import text
from app.core import database


@pytest.fixture(autouse=True, scope="module")
def patch_engine():
    test_engine = create_engine("sqlite:///:memory:")
    database._engine = test_engine
    yield


def test_session_works():
    """
    Test that a session can be created and used to execute a simple query.
    """
    with Session(database.get_engine()) as session:
        result = session.execute(text('SELECT 1+1')).scalar()
        assert result == 2
    gen = database.get_session()
    session2 = next(gen)
    assert isinstance(session2, Session)
    try:
        next(gen)
    except StopIteration:
        pass
