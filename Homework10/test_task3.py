# Из набора тестов задания task_2 создайте один тест с параметрами, используя @pytest.mark.parametrize
# Промаркируйте 1 параметр из выборки как smokе, а 1 набор данных скипните

import pytest


def all_division(*arg1):
    division = arg1[0]
    for i in arg1[1:]:
        division /= i
    return division


@pytest.mark.parametrize("input_data, expected_output",
                         [pytest.param((8, 2), 4, marks=pytest.mark.smoke),
                          pytest.param((-15, 3), -5, marks=pytest.mark.skip(reason="Тест пропущен"))
                          ])
def test_all_division(input_data, expected_output):
    assert all_division(*input_data) == expected_output
