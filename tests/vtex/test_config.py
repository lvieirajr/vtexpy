from pytest import fail, mark, raises

from tests.unit import UnitTest
from vtex._config import Config
from vtex._constants import (
    ACCOUNT_NAME_ENV_VAR,
    APP_KEY_ENV_VAR,
    APP_TOKEN_ENV_VAR,
    RETRY_ATTEMPTS_ENV_VAR,
    TIMEOUT_ENV_VAR,
)
from vtex._utils import UNDEFINED, is_undefined


class TestConfig(UnitTest):
    # ACCOUNT NAME ---------------------------------------------------------------------
    @mark.parametrize("account_name", [UNDEFINED, "account_name"])
    def test_valid_value_to_parse_account_name(self, account_name):
        try:
            Config(account_name=account_name)
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("account_name", [UNDEFINED, "account_name"])
    def test_valid_env_var_to_parse_account_name(self, account_name, monkeypatch):
        if not is_undefined(account_name):
            monkeypatch.setenv(ACCOUNT_NAME_ENV_VAR, account_name)

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("account_name", ["", None])
    def test_invalid_value_to_parse_account_name(self, account_name):
        with raises(ValueError):
            Config(account_name=account_name)

    @mark.parametrize("account_name", [""])
    def test_invalid_env_var_to_parse_account_name(self, account_name, monkeypatch):
        if not is_undefined(account_name):
            monkeypatch.setenv(ACCOUNT_NAME_ENV_VAR, str(account_name))

        with raises(ValueError):
            Config()

    # APP KEY --------------------------------------------------------------------------
    @mark.parametrize("app_key", [UNDEFINED, "app_key"])
    def test_valid_value_to_parse_app_key(self, app_key):
        try:
            Config(app_key=app_key)
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("app_key", [UNDEFINED, "app_key"])
    def test_valid_env_var_to_parse_app_key(self, app_key, monkeypatch):
        if not is_undefined(app_key):
            monkeypatch.setenv(APP_KEY_ENV_VAR, app_key)

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("app_key", ["", None])
    def test_invalid_value_to_parse_app_key(self, app_key):
        with raises(ValueError):
            Config(app_key=app_key)

    @mark.parametrize("app_key", [""])
    def test_invalid_env_var_to_parse_app_key(self, app_key, monkeypatch):
        if not is_undefined(app_key):
            monkeypatch.setenv(APP_KEY_ENV_VAR, str(app_key))

        with raises(ValueError):
            Config()

    # APP TOKEN ------------------------------------------------------------------------
    @mark.parametrize("app_token", [UNDEFINED, "app_token"])
    def test_valid_value_to_parse_app_token(self, app_token):
        try:
            Config(app_token=app_token)
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("app_token", [UNDEFINED, "app_token"])
    def test_valid_env_var_to_parse_app_token(self, app_token, monkeypatch):
        if not is_undefined(app_token):
            monkeypatch.setenv(APP_TOKEN_ENV_VAR, app_token)

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("app_token", ["", None])
    def test_invalid_value_to_parse_app_token(self, app_token):
        with raises(ValueError):
            Config(app_token=app_token)

    @mark.parametrize("app_token", [""])
    def test_invalid_env_var_to_parse_app_token(self, app_token, monkeypatch):
        if not is_undefined(app_token):
            monkeypatch.setenv(APP_TOKEN_ENV_VAR, str(app_token))

        with raises(ValueError):
            Config()

    # TIMEOUT --------------------------------------------------------------------------
    @mark.parametrize("timeout", [UNDEFINED, 0.1, 1, 1.0, 2.1, None])
    def test_valid_value_to_parse_timeout(self, timeout):
        try:
            Config(timeout=timeout)
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("timeout", [UNDEFINED, "", "null", "0.1", "1", "1.0", "2.1"])
    def test_valid_env_var_to_parse_timeout(self, timeout, monkeypatch):
        if not is_undefined(timeout):
            monkeypatch.setenv(TIMEOUT_ENV_VAR, timeout)

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("timeout", ["", 0, 0.0, -1, -1.0])
    def test_invalid_value_to_parse_timeout(self, timeout):
        with raises(ValueError):
            Config(timeout=timeout)

    @mark.parametrize("timeout", ["0", "0.0", "-1", "-1.0"])
    def test_invalid_env_var_to_parse_timeout(self, timeout, monkeypatch):
        if not is_undefined(timeout):
            monkeypatch.setenv(TIMEOUT_ENV_VAR, str(timeout))

        with raises(ValueError):
            Config()

    # RETRY ATTEMPTS ---------------------------------------------------------------
    @mark.parametrize("retry_attempts", [UNDEFINED, 0, 1, 3])
    def test_valid_value_to_parse_retry_attempts(self, retry_attempts):
        try:
            Config(retry_attempts=retry_attempts)
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_attempts", [UNDEFINED, "0", "1", "3"])
    def test_valid_env_var_to_parse_retry_attempts(self, retry_attempts, monkeypatch):
        if not is_undefined(retry_attempts):
            monkeypatch.setenv(RETRY_ATTEMPTS_ENV_VAR, retry_attempts)

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_attempts", ["", 0.0, 0.1, -1, -1.1])
    def test_invalid_value_to_parse_retry_attempts(self, retry_attempts):
        with raises(ValueError):
            Config(retry_attempts=retry_attempts)

    @mark.parametrize("retry_attempts", ["", "0.0", "0.1", "-1", "-1.1"])
    def test_invalid_env_var_to_parse_retry_attempts(self, retry_attempts, monkeypatch):
        if not is_undefined(retry_attempts):
            monkeypatch.setenv(RETRY_ATTEMPTS_ENV_VAR, str(retry_attempts))

        with raises(ValueError):
            Config()
