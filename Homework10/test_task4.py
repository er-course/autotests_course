# Создайте класс с тестами и напишите фикстуры в conftest.py:
# 1) Фикстуру для класса и используйте её. Например, печать времени начала выполнения класса с тестами и окончания
# 2) Фикстуру для конкретного теста и используйте её не для всех тестов. Например, время выполнения теста.
import time

import pytest


@pytest.mark.usefixtures("test_time")
class TestClass:
    def test_01(self):
        time.sleep(1)
        assert 1 + 1 == 2

    def test_02(self):
        assert 200 * 2 == 400

    def test_03(self):
        assert 3 - 3 == 0


def test_04(test_duration):
    assert 10000 / 1000 == 10
