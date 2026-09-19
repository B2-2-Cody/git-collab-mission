"""숫자 유틸 함수 테스트."""

import pytest

from src import utils


def test_clamp_when_value_is_above_range() -> None:
    """범위를 초과한 값은 상한으로 제한한다."""
    # Given
    value = 15

    # When
    result = utils.clamp(value, 0, 10)

    # Then
    assert result == 10


def test_clamp_when_value_is_below_range() -> None:
    """범위 미만인 값은 하한으로 제한한다."""
    # Given
    value = -5

    # When
    result = utils.clamp(value, 0, 10)

    # Then
    assert result == 0


def test_clamp_when_value_is_within_range() -> None:
    """범위 안의 값은 그대로 반환한다."""
    # Given
    value = 7

    # When
    result = utils.clamp(value, 0, 10)

    # Then
    assert result == 7


def test_clamp_when_low_is_greater_than_high() -> None:
    """low가 high보다 크면 ValueError를 발생시킨다."""
    # Given
    low, high = 10, 0

    # When / Then
    with pytest.raises(ValueError):
        utils.clamp(5, low, high)


def test_is_even_when_number_is_even() -> None:
    """짝수는 True를 반환한다."""
    # Given
    number = 4

    # When
    result = utils.is_even(number)

    # Then
    assert result is True


def test_is_even_when_number_is_odd() -> None:
    """홀수는 False를 반환한다."""
    # Given
    number = 7

    # When
    result = utils.is_even(number)

    # Then
    assert result is False


def test_is_even_when_number_is_negative_even() -> None:
    """음수 짝수도 True를 반환한다."""
    # Given
    number = -2

    # When
    result = utils.is_even(number)

    # Then
    assert result is True


def test_average_when_given_numbers() -> None:
    """숫자 리스트의 평균을 반환한다."""
    # Given
    numbers = [1, 2, 3, 4]

    # When
    result = utils.average(numbers)

    # Then
    assert result == 2.5


def test_average_when_list_is_empty() -> None:
    """빈 리스트는 ValueError를 발생시킨다."""
    # Given
    numbers: list[float] = []

    # When / Then
    with pytest.raises(ValueError):
        utils.average(numbers)


def test_factorial_when_number_is_positive() -> None:
    """양의 정수의 팩토리얼을 반환한다."""
    # Given
    number = 5

    # When
    result = utils.factorial(number)

    # Then
    assert result == 120


def test_factorial_when_number_is_zero() -> None:
    """0의 팩토리얼은 1이다."""
    # Given
    number = 0

    # When
    result = utils.factorial(number)

    # Then
    assert result == 1


def test_factorial_when_number_is_negative() -> None:
    """음수는 ValueError를 발생시킨다."""
    # Given
    number = -1

    # When / Then
    with pytest.raises(ValueError):
        utils.factorial(number)
