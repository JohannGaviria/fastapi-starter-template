from app.core.config import settings


def test_app_metadata_settings():
    """
    Test that application metadata settings are loaded and not empty.
    """
    assert isinstance(settings.app_name, str)
    assert settings.app_name
    assert isinstance(settings.app_summary, str)
    assert settings.app_summary
    assert isinstance(settings.app_description, str)
    assert settings.app_description
    assert isinstance(settings.app_version, str)
    assert settings.app_version


def test_secret_key_and_algorithm():
    """
    Test that secret_key and algorithm are set.
    """
    assert isinstance(settings.secret_key, str)
    assert settings.secret_key
    assert isinstance(settings.algorithm, str)
    assert settings.algorithm


def test_access_token_expire_minutes():
    """
    Test that access_token_expire_minutes is an integer and positive.
    """
    assert isinstance(settings.access_token_expire_minutes, int)
    assert settings.access_token_expire_minutes > 0


def test_database_url():
    """
    Test that database_url is set and is a string.
    """
    assert isinstance(settings.database_url, str)
    assert settings.database_url


def test_cors_settings():
    """
    Test CORS settings types.
    """
    assert isinstance(settings.cors_allow_origins, str) or settings.cors_allow_origins is None
    assert isinstance(settings.cors_allow_credentials, bool)
    assert isinstance(settings.cors_allow_methods, str) or settings.cors_allow_methods is None
    assert isinstance(settings.cors_allow_headers, str) or settings.cors_allow_headers is None
    