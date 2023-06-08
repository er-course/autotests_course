import time

import pytest
import datetime


@pytest.fixture
def test_time():
    start_time = datetime.datetime.now()
    print(f"\nТест стартовал: {start_time.strftime('%H:%M:%S')}")
    yield
    end_time = datetime.datetime.now()
    print(f"\nТест завершился: {end_time.strftime('%H:%M:%S')}")


@pytest.fixture
def test_duration():
    start_time = datetime.datetime.now()
    yield
    end_time = datetime.datetime.now()
    duration = end_time - start_time
    return print(f'\nВремя выполнения теста {duration}')
