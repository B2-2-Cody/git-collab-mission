# Conflict Resolution Log

이 문서는 팀이 의도적으로 만든 충돌 상황과 해결 과정을 기록합니다.
아래 두 건은 [`docs/SCENARIO.md`](./SCENARIO.md) 8장에서 미리 설계한 시나리오입니다.
두 충돌 실습에서 실제로 확인한 마커, 해결 절차와 관련 링크를 기록합니다.

## 충돌 기록 #1 (자명한 충돌 — add/add)

### 참여자
- 충돌 해결자: 이교원
- 상대 변경 작성자: 정인호

### 상황(What happened)
- `main`에 아직 `src/utils.py`가 없는 상태에서, 정인호(`feature/inho-list-utils`)와 이교원(`feature/kyowon-string-utils`)이 같은 시점에 각자 브랜치를 만들어 `src/utils.py`를 새로 추가.
- 정인호 PR을 먼저 병합한 뒤, 이교원 PR을 병합하려는 과정에서 `CONFLICT (add/add)` 발생 (두 브랜치가 같은 경로에 서로 다른 내용의 파일을 각각 새로 추가한 상태).

### 충돌 내용(Conflict markers)
```txt
<<<<<<< HEAD
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
=======
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
>>>>>>> origin/main
```

### 해결 과정(How)
- 선택한 해결 전략: keep both (정인호의 리스트 함수와 이교원의 문자열 함수가 서로 다른 책임을 가지므로 모두 유지)
- 실제로 수행한 명령/절차:
  1. `git fetch origin && git merge origin/main` → `CONFLICT (add/add): Merge conflict in src/utils.py`
  2. `git status --short`에서 `AA src/utils.py`를 확인
  3. 충돌 마커를 제거하고 `flatten`, `unique`, `reverse_string`, `is_palindrome`을 모두 유지
  4. 문자열 테스트 3개·doctest와 리스트 함수 스모크 테스트를 실행해 양쪽 동작 확인
  5. `git add src/utils.py` → `git commit -m "fix: resolve add/add conflict in utils.py"` → `git push`

### 결과(Outcome)
- 최종 병합 결과 요약: 한 파일에 리스트 함수 2개와 문자열 함수 2개가 함께 유지되었고, 테스트를 통과한 뒤 `main`에 병합됨.
- 관련 PR: [PR #16](https://github.com/B2-2-Cody/git-collab-mission/pull/16)
- 관련 커밋: [2799131](https://github.com/B2-2-Cody/git-collab-mission/commit/27991318894f3ccc036c6af8af9e936a2feedc9a)

### 배운 점(Learnings)
- 같은 기준 커밋에서 같은 경로의 파일을 서로 다르게 새로 추가하면 `add/add` 충돌이 발생한다.
- 먼저 병합한 사람보다 나중에 최신 `main`을 자기 브랜치에 반영하는 사람이 충돌을 직접 해결한다.
- 충돌 마커의 양쪽 내용을 비교해 서로 독립적인 기능이면 한쪽을 버리지 않고 모두 유지할 수 있으며, 해결 후에는 양쪽 기능을 함께 검증해야 한다.

---

## 충돌 기록 #2 (비자명한 충돌 — 파일 이동 vs 내용 수정)

### 참여자
- 작성자: 박기태
- 상대: 이교원 (`feature/kyowon-fix-docstring`, PR #19)

### 상황(What happened)
- 박기태가 `git mv src/utils.py src/string_utils.py`로 파일명을 변경하는 `feature/gitae-split-utils` 브랜치 작업 중, 같은 줄(상단 docstring)을 함께 수정.
- 같은 시점에 다른 팀원이 `src/utils.py`의 같은 줄을 수정하는 브랜치를 먼저 병합.
- (같은 줄을 건드리지 않으면 git의 기본 병합 전략 `ort`가 rename을 자동 감지해 충돌 없이 조용히 병합해버리므로, 반드시 같은 줄을 겹치게 수정해야 충돌이 재현됨.)
- 이교원의 PR #19(`8ba58a6`, `ad4f813`)가 `main`에 먼저 병합되어 `src/utils.py` 1행 docstring이 바뀜.
- 박기태가 `feature/gitae-split-utils`에서 `git fetch origin && git merge origin/main`을 실행하자, git이 rename을 감지해 `origin/main`의 `src/utils.py` 변경을 이동된 파일(`src/string_utils.py`)에 적용하려다 `CONFLICT (content)`가 발생.
- 실제 `git status`에는 `src/string_utils.py`만 `UU`(양쪽에서 수정)로 표시되었고, `src/utils.py`는 별도 항목으로 나타나지 않았음. 충돌 마커의 경로 표기(`HEAD:src/string_utils.py` / `origin/main:src/utils.py`)로 rename이 관여했음을 알 수 있음.

### 충돌 내용(Conflict markers)
```txt
<<<<<<< HEAD:src/string_utils.py
"""팀 공용 문자열·리스트·숫자 유틸 함수 모음."""
=======
"""팀 공용 리스트·문자열·숫자 유틸 함수 모음.

충돌 #2 재현용 임시 설명이며, Issue #9 완료 후 모듈 역할에 맞게 재정리한다.
"""
>>>>>>> origin/main:src/utils.py
```
- 마커 위쪽(`HEAD`)은 박기태의 rename 브랜치(`src/string_utils.py`), 아래쪽(`origin/main`)은 이교원이 수정한 원래 경로(`src/utils.py`)의 내용. 마커 양쪽에 서로 다른 경로가 찍혀 있음.

### 해결 과정(How)
- 선택한 해결 전략: refactor (두 문구 중 하나를 고르지 않고, `origin/main` 쪽 문구를 기반으로 임시 안내 문장을 제거해 한 줄로 재정리)
- 실제로 수행한 명령/절차:
  1. `git fetch origin && git merge origin/main` → `CONFLICT (content): Merge conflict in src/string_utils.py`
  2. `git status`로 충돌 파일이 원래 경로가 아닌 이동된 경로(`src/string_utils.py`)임을 확인
  3. `src/string_utils.py`의 마커 3줄과 임시 안내 문장을 제거하고 docstring을 `"""팀 공용 리스트·문자열·숫자 유틸 함수 모음."""` 한 줄로 정리
  4. 마커 잔존 여부 확인(`grep -nE '^(<<<<<<<|=======|>>>>>>>)' src/string_utils.py` → 결과 없음), 테스트 16개·doctest 통과 확인
  5. `git add src/string_utils.py` → `git commit` (`fix: resolve docstring conflict after utils.py -> string_utils.py rename`)

### 결과(Outcome)
- 최종 병합 결과 요약: `src/utils.py` → `src/string_utils.py` rename이 유지되었고, docstring은 이교원이 정한 "리스트·문자열·숫자" 표현을 살리되 임시 안내 문장은 제거한 한 줄로 확정.
- 관련 PR/커밋: 이교원 [PR #19](https://github.com/B2-2-Cody/git-collab-mission/pull/19)(`8ba58a6`, `ad4f813`), 박기태 rename 커밋 `0cfa982`, 충돌 해결 커밋 `15dd216`, 박기태 [PR #20](https://github.com/B2-2-Cody/git-collab-mission/pull/20)

### 배운 점(Learnings)
- 겹치는 줄이 없으면 git이 rename을 자동 감지해 충돌 없이 병합하지만, 같은 줄을 양쪽에서 고치면 이동된 새 경로에서 충돌이 난다. 충돌이 원래 작업하던 경로가 아니라 이동된 경로에서 난다는 점을 알고 있어야 한다.
- 마커에 `HEAD:src/string_utils.py`, `origin/main:src/utils.py`처럼 서로 다른 경로가 함께 찍히므로, 각 쪽이 어느 파일 기준의 변경인지 마커에서 확인한다.
- 마커를 지운 뒤 `git add`하기 전에 마커 잔존 여부와 테스트를 확인해야 마커가 그대로 커밋되는 사고를 막을 수 있다.
- 상대가 남긴 "임시" 문구는 병합 시 그대로 가져오지 말고, 작성자에게 의도를 확인하거나 그 문구가 말하는 조건(이슈 #9 완료)이 충족됐는지 보고 정리한다.
