"""문자열 유틸 함수 테스트."""

from src import string_utils as utils


def test_reverse_string_when_given_text() -> None:
    """문자열의 문자 순서를 뒤집는다."""
    # Given
    value = "Codyssey"

    # When
    result = utils.reverse_string(value)

    # Then
    assert result == "yessydoC"


def test_is_palindrome_when_case_differs() -> None:
    """대소문자를 무시해 회문을 판별한다."""
    # Given
    value = "RaceCar"

    # When
    result = utils.is_palindrome(value)

    # Then
    assert result is True


def test_is_palindrome_when_spaces_are_present() -> None:
    """일반 공백을 무시해 회문을 판별한다."""
    # Given
    value = "nurses run"

    # When
    result = utils.is_palindrome(value)

    # Then
    assert result is True


def test_is_palindrome_when_text_is_not_symmetric() -> None:
    """대칭이 아닌 문자열은 회문이 아니다."""
    # Given
    value = "Codyssey"

    # When
    result = utils.is_palindrome(value)

    # Then
    assert result is False
