"""Тесты для проверки модуля practicum."""

import practicum

EXPECTED_FUNC_NAME = "say_hello"


def test_say_hello_exists():
    """Проверить, что функция say_hello есть в модуле practicum."""
    assert hasattr(practicum, EXPECTED_FUNC_NAME), (
        f"Функция {EXPECTED_FUNC_NAME} не обнаружена в модуле practicum"
    )


def test_say_hello_run_without_exceptions():
    """Проверить, что say_hello запускается без исключений."""
    try:
        practicum.say_hello()
    except Exception as error:
        raise AssertionError(
            f"При запуске функции {EXPECTED_FUNC_NAME} возникло "
            f"исключение: {type(error).name}: {error}"
        )
