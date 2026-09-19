"""팀 공용 유틸 함수 모음."""


def flatten(nested):
    """중첩 리스트를 1단계 평탄화한다."""
    result = []
    for item in nested:
        if isinstance(item, list):
            result.extend(item)
        else:
            result.append(item)
    return result


def unique(items):
    """순서를 유지하면서 중복을 제거한다."""
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


def reverse_string(value: str) -> str:
    """문자열의 문자 순서를 뒤집어 반환한다.

    Example:
        >>> reverse_string("Codyssey")
        'yessydoC'
    """
    return value[::-1]


def is_palindrome(value: str) -> bool:
    """일반 공백과 대소문자만 무시하고 회문 여부를 반환한다.

    문장부호와 탭, 줄바꿈은 비교 대상에 포함한다.

    Example:
        >>> is_palindrome("RaceCar")
        True
    """
    normalized = value.replace(" ", "").lower()
    return normalized == normalized[::-1]


def clamp(value: float, low: float, high: float) -> float:
    """값을 [low, high] 범위로 제한해 반환한다.

    low가 high보다 크면 ValueError를 발생시킨다.

    Example:
        >>> clamp(15, 0, 10)
        10
    """
    if low > high:
        raise ValueError("low must be less than or equal to high")
    return max(low, min(value, high))


def is_even(number: int) -> bool:
    """정수가 짝수인지 여부를 반환한다.

    Example:
        >>> is_even(4)
        True
    """
    return number % 2 == 0


def average(numbers: list[float]) -> float:
    """숫자 리스트의 평균을 반환한다.

    빈 리스트는 평균을 정의할 수 없으므로 ValueError를 발생시킨다.

    Example:
        >>> average([1, 2, 3, 4])
        2.5
    """
    if not numbers:
        raise ValueError("numbers must not be empty")
    return sum(numbers) / len(numbers)


def factorial(number: int) -> int:
    """음이 아닌 정수의 팩토리얼을 반환한다.

    음수는 정의되지 않으므로 ValueError를 발생시킨다.

    Example:
        >>> factorial(5)
        120
    """
    if number < 0:
        raise ValueError("number must be non-negative")
    result = 1
    for factor in range(2, number + 1):
        result *= factor
    return result
