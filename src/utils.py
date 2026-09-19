"""팀 공용 유틸 함수 모음."""


def reverse_string(value: str) -> str:
    """문자열의 문자 순서를 뒤집어 반환한다.

    Example:
        >>> reverse_string("Codyssey")
        'yessydoC'
    """
    return value[::-1]


def is_palindrome(value: str) -> bool:
    """공백과 대소문자를 무시하고 회문 여부를 반환한다.

    Example:
        >>> is_palindrome("Never odd or even")
        True
    """
    normalized = value.replace(" ", "").lower()
    return normalized == normalized[::-1]
