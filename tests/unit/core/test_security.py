from app.core import security


def test_hash_password_returns_different_hashes():
    """
    Test that hashing the same password twice returns different hashes (due to salt).
    """
    password = "mysecretpassword"
    hash1 = security.hash_password(password)
    hash2 = security.hash_password(password)
    assert hash1 != hash2
    assert hash1.startswith("$2b$") or hash1.startswith("$2a$")
    assert hash2.startswith("$2b$") or hash2.startswith("$2a$")


def test_verify_password_success():
    """
    Test that verify_password returns True for correct password.
    """
    password = "mysecretpassword"
    hashed = security.hash_password(password)
    assert security.verify_password(password, hashed)


def test_verify_password_failure():
    """
    Test that verify_password returns False for incorrect password.
    """
    password = "mysecretpassword"
    hashed = security.hash_password(password)
    assert not security.verify_password("wrongpassword", hashed)
