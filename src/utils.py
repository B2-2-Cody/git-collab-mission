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
