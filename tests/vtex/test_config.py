from pytest import fail, mark, raises

from tests.unit import UnitTest
from vtex._config import Config
from vtex._constants import (
    ACCOUNT_NAME_ENV_VAR,
    APP_KEY_ENV_VAR,
    APP_TOKEN_ENV_VAR,
    RAISE_FOR_STATUS_ENV_VAR,
    RETRY_ATTEMPTS_ENV_VAR,
    RETRY_BACKOFF_EXPONENTIAL_ENV_VAR,
    RETRY_BACKOFF_MAX_ENV_VAR,
    RETRY_BACKOFF_MIN_ENV_VAR,
    RETRY_LOGS_ENV_VAR,
    RETRY_STATUSES_ENV_VAR,
    TIMEOUT_ENV_VAR,
)
from vtex._utils import UNDEFINED, is_undefined


class TestInit(UnitTest):
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
            monkeypatch.setenv(ACCOUNT_NAME_ENV_VAR, str(account_name))

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("account_name", [None, ""])
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
            monkeypatch.setenv(APP_KEY_ENV_VAR, str(app_key))

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("app_key", [None, ""])
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
            monkeypatch.setenv(APP_TOKEN_ENV_VAR, str(app_token))

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("app_token", [None, ""])
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
            monkeypatch.setenv(TIMEOUT_ENV_VAR, str(timeout))

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

    # RETRY ATTEMPTS -------------------------------------------------------------------
    @mark.parametrize("retry_attempts", [UNDEFINED, 0, 1, 3])
    def test_valid_value_to_parse_retry_attempts(self, retry_attempts):
        try:
            Config(retry_attempts=retry_attempts)
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_attempts", [UNDEFINED, "0", "1", "3"])
    def test_valid_env_var_to_parse_retry_attempts(self, retry_attempts, monkeypatch):
        if not is_undefined(retry_attempts):
            monkeypatch.setenv(RETRY_ATTEMPTS_ENV_VAR, str(retry_attempts))

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_attempts", [None, "", 0.0, 0.1, 0.9, -1, -1.1])
    def test_invalid_value_to_parse_retry_attempts(self, retry_attempts):
        with raises(ValueError):
            Config(retry_attempts=retry_attempts)

    @mark.parametrize("retry_attempts", ["", "0.0", "0.1", "0.9", "-1", "-1.1"])
    def test_invalid_env_var_to_parse_retry_attempts(self, retry_attempts, monkeypatch):
        if not is_undefined(retry_attempts):
            monkeypatch.setenv(RETRY_ATTEMPTS_ENV_VAR, str(retry_attempts))

        with raises(ValueError):
            Config()

    # RETRY BACKOFF MIN ----------------------------------------------------------------
    @mark.parametrize("retry_backoff_min", [UNDEFINED, 0.1, 1, 1.0, 1.1])
    def test_valid_value_to_parse_retry_backoff_min(self, retry_backoff_min):
        try:
            Config(retry_backoff_min=retry_backoff_min)
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_backoff_min", [UNDEFINED, "0.1", "1", "1.0", "1.1"])
    def test_valid_env_var_to_parse_retry_backoff_min(
        self,
        retry_backoff_min,
        monkeypatch,
    ):
        if not is_undefined(retry_backoff_min):
            monkeypatch.setenv(RETRY_BACKOFF_MIN_ENV_VAR, str(retry_backoff_min))

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_backoff_min", [None, "", 0, 0.0, -1, -1.1])
    def test_invalid_value_to_parse_retry_backoff_min(self, retry_backoff_min):
        with raises(ValueError):
            Config(retry_backoff_min=retry_backoff_min)

    @mark.parametrize("retry_backoff_min", ["", "0", "0.0", "-1", "-1.1"])
    def test_invalid_env_var_to_parse_retry_backoff_min(self, retry_backoff_min, monkeypatch):
        if not is_undefined(retry_backoff_min):
            monkeypatch.setenv(RETRY_BACKOFF_MIN_ENV_VAR, str(retry_backoff_min))

        with raises(ValueError):
            Config()

    # RETRY BACKOFF MAX ----------------------------------------------------------------
    @mark.parametrize("retry_backoff_max", [UNDEFINED, 0.1, 1, 1.0, 1.1])
    def test_valid_value_to_parse_retry_backoff_max(self, retry_backoff_max):
        try:
            Config(retry_backoff_max=retry_backoff_max)
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_backoff_max", [UNDEFINED, "0.1", "1", "1.0", "1.1"])
    def test_valid_env_var_to_parse_retry_backoff_max(
        self,
        retry_backoff_max,
        monkeypatch,
    ):
        if not is_undefined(retry_backoff_max):
            monkeypatch.setenv(RETRY_BACKOFF_MAX_ENV_VAR, str(retry_backoff_max))

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_backoff_max", [None, "", 0, 0.0, -1, -1.1])
    def test_invalid_value_to_parse_retry_backoff_max(self, retry_backoff_max):
        with raises(ValueError):
            Config(retry_backoff_max=retry_backoff_max)

    @mark.parametrize("retry_backoff_max", ["", "0", "0.0", "-1", "-1.1"])
    def test_invalid_env_var_to_parse_retry_backoff_max(self, retry_backoff_max, monkeypatch):
        if not is_undefined(retry_backoff_max):
            monkeypatch.setenv(RETRY_BACKOFF_MAX_ENV_VAR, str(retry_backoff_max))

        with raises(ValueError):
            Config()

    # RETRY BACKOFF EXPONENTIAL --------------------------------------------------------
    @mark.parametrize("retry_backoff_exponential", [UNDEFINED, 1, 1.0, 1.1])
    def test_valid_value_to_parse_retry_backoff_exponential(
        self,
        retry_backoff_exponential,
    ):
        try:
            Config(retry_backoff_exponential=retry_backoff_exponential)
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_backoff_exponential", [UNDEFINED, "1", "1.0", "1.1"])
    def test_valid_env_var_to_parse_retry_backoff_exponential(
        self,
        retry_backoff_exponential,
        monkeypatch,
    ):
        if not is_undefined(retry_backoff_exponential):
            monkeypatch.setenv(
                RETRY_BACKOFF_EXPONENTIAL_ENV_VAR,
                str(retry_backoff_exponential),
            )

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_backoff_exponential", [None, "", 0, 0.0, 0.9, -1, -1.1])
    def test_invalid_value_to_parse_retry_backoff_exponential(
        self,
        retry_backoff_exponential,
    ):
        with raises(ValueError):
            Config(retry_backoff_exponential=retry_backoff_exponential)

    @mark.parametrize("retry_backoff_exponential", ["", "0.0", "0.9" "-1", "-1.1"])
    def test_invalid_env_var_to_parse_retry_backoff_exponential(
        self,
        retry_backoff_exponential,
        monkeypatch,
    ):
        if not is_undefined(retry_backoff_exponential):
            monkeypatch.setenv(
                RETRY_BACKOFF_EXPONENTIAL_ENV_VAR,
                str(retry_backoff_exponential),
            )

        with raises(ValueError):
            Config()

    # RETRY STATUSES -------------------------------------------------------------------
    @mark.parametrize("retry_statuses", [UNDEFINED, [], [408], [408, 429]])
    def test_valid_value_to_parse_retry_statuses(self, retry_statuses):
        try:
            Config(retry_statuses=retry_statuses)
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_statuses", [UNDEFINED, "", "408", "408,429"])
    def test_valid_env_var_to_parse_retry_statuses(self, retry_statuses, monkeypatch):
        if not is_undefined(retry_statuses):
            monkeypatch.setenv(RETRY_STATUSES_ENV_VAR, str(retry_statuses))

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_statuses", [None, "", [""], ["test"], "408", 408])
    def test_invalid_value_to_parse_retry_statuses(self, retry_statuses):
        with raises(ValueError):
            Config(retry_statuses=retry_statuses)

    @mark.parametrize("retry_statuses", ["status1", "status1,status2" "", "99,7"])
    def test_invalid_env_var_to_parse_retry_statuses(self, retry_statuses, monkeypatch):
        if not is_undefined(retry_statuses):
            monkeypatch.setenv(RETRY_STATUSES_ENV_VAR, str(retry_statuses))

        with raises(ValueError):
            Config()

    # RETRY LOGS -------------------------------------------------------------------
    @mark.parametrize("retry_logs", [UNDEFINED, False, True])
    def test_valid_value_to_parse_retry_logs(self, retry_logs):
        try:
            Config(retry_logs=retry_logs)
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize(
        "retry_logs",
        [UNDEFINED, "false", "true", "0", "1", "n", "y"],
    )
    def test_valid_env_var_to_parse_retry_logs(self, retry_logs, monkeypatch):
        if not is_undefined(retry_logs):
            monkeypatch.setenv(RETRY_LOGS_ENV_VAR, str(retry_logs))

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("retry_logs", [None, "", "test", 0, 1])
    def test_invalid_value_to_parse_retry_logs(self, retry_logs):
        with raises(ValueError):
            Config(retry_logs=retry_logs)

    @mark.parametrize("retry_logs", ["", "test", "0.0", "1.0"])
    def test_invalid_env_var_to_parse_retry_logs(self, retry_logs, monkeypatch):
        if not is_undefined(retry_logs):
            monkeypatch.setenv(RETRY_LOGS_ENV_VAR, str(retry_logs))

        with raises(ValueError):
            Config()

    # RAISE FOR STATUS -----------------------------------------------------------------
    @mark.parametrize("raise_for_status", [UNDEFINED, False, True])
    def test_valid_value_to_parse_raise_for_status(self, raise_for_status):
        try:
            Config(raise_for_status=raise_for_status)
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize(
        "raise_for_status",
        [UNDEFINED, "false", "true", "0", "1", "n", "y"],
    )
    def test_valid_env_var_to_parse_raise_for_status(
        self,
        raise_for_status,
        monkeypatch,
    ):
        if not is_undefined(raise_for_status):
            monkeypatch.setenv(RAISE_FOR_STATUS_ENV_VAR, str(raise_for_status))

        try:
            Config()
        except Exception as exception:
            fail(f"Raised {type(exception).__name__}")

    @mark.parametrize("raise_for_status", [None, "", "test", 0, 1])
    def test_invalid_value_to_parse_raise_for_status(self, raise_for_status):
        with raises(ValueError):
            Config(raise_for_status=raise_for_status)

    @mark.parametrize("raise_for_status", ["", "test", "0.0", "1.0"])
    def test_invalid_env_var_to_parse_raise_for_status(
        self,
        raise_for_status,
        monkeypatch,
    ):
        if not is_undefined(raise_for_status):
            monkeypatch.setenv(RAISE_FOR_STATUS_ENV_VAR, str(raise_for_status))

        with raises(ValueError):
            Config()


class TestGetValues(UnitTest):
    def test_when_account_name_is_undefined_get_account_name_raises_value_error(self):
        config = Config(account_name=UNDEFINED)

        with raises(ValueError):
            config.get_account_name()

    def test_when_app_key_is_undefined_get_app_key_raises_value_error(self):
        config = Config(app_key=UNDEFINED)

        with raises(ValueError):
            config.get_app_key()

    def test_when_app_token_is_undefined_get_app_token_raises_value_error(self):
        config = Config(app_token=UNDEFINED)

        with raises(ValueError):
            config.get_app_token()


    # # ACCOUNT NAME ---------------------------------------------------------------------
    # @mark.parametrize(
    #     "account_name",
    #     [(UNDEFINED, ), "account_name"],
    # )
    # def test_get_account_name(self, account_name):
    #     try:
    #         Config(account_name=account_name)
    #     except Exception as exception:
    #         fail(f"Raised {type(exception).__name__}")
