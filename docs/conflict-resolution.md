# Conflict Resolution Log

이 문서는 팀이 의도적으로 만든 충돌 상황과 해결 과정을 기록합니다.
아래 두 건은 [`docs/SCENARIO.md`](./SCENARIO.md) 8장에서 미리 설계한 시나리오입니다.
실습을 마친 뒤 각 항목의 `TODO`를 실제 내용으로 채워주세요.

## 충돌 기록 #1 (자명한 충돌 — add/add)

### 참여자
- 작성자: 정인호
- 상대: 이교원

### 상황(What happened)
- `main`에 아직 `src/utils.py`가 없는 상태에서, 정인호(`feature/inho-list-utils`)와 이교원(`feature/kyowon-string-utils`)이 같은 시점에 각자 브랜치를 만들어 `src/utils.py`를 새로 추가.
- 정인호 PR을 먼저 병합한 뒤, 이교원 PR을 병합하려는 과정에서 `CONFLICT (add/add)` 발생 (두 브랜치가 같은 경로에 서로 다른 내용의 파일을 각각 새로 추가한 상태).

### 충돌 내용(Conflict markers)
```txt
TODO: 실제 발생한 충돌 마커 원문을 붙여넣으세요.
<<<<<<< HEAD
...
=======
...
>>>>>>> feature/kyowon-string-utils
```

### 해결 과정(How)
- 선택한 해결 전략: TODO (keep both / choose one / refactor)
- 실제로 수행한 명령/절차: TODO (예: `git fetch origin && git merge origin/main`, 충돌 마커 직접 수정 후 `git add` → `git commit`)

### 결과(Outcome)
- 최종 병합 결과 요약: TODO
- 관련 PR/커밋 링크: TODO

### 배운 점(Learnings)
- TODO

---

## 충돌 기록 #2 (비자명한 충돌 — 파일 이동 vs 내용 수정)

### 참여자
- 작성자: 박기태
- 상대: TODO (정인호 또는 이교원)

### 상황(What happened)
- 박기태가 `git mv src/utils.py src/string_utils.py`로 파일명을 변경하는 `feature/gitae-split-utils` 브랜치 작업 중, 같은 줄(상단 docstring)을 함께 수정.
- 같은 시점에 다른 팀원이 `src/utils.py`의 같은 줄을 수정하는 브랜치를 먼저 병합.
- (같은 줄을 건드리지 않으면 git의 기본 병합 전략 `ort`가 rename을 자동 감지해 충돌 없이 조용히 병합해버리므로, 반드시 같은 줄을 겹치게 수정해야 충돌이 재현됨.)
- 박기태 PR 병합 시 "파일 이동 vs 내용 수정" 충돌(rename/modify, `CONFLICT (content)`)이 이동된 파일(`string_utils.py`) 안에서 발생. `git status`에는 `src/utils.py`가 삭제(D)로, `src/string_utils.py`가 충돌(UU)로 동시에 표시됨.

### 충돌 내용(Conflict markers)
```txt
TODO: 실제 발생한 충돌 메시지/마커 원문을 붙여넣으세요.
```

### 해결 과정(How)
- 선택한 해결 전략: TODO
- 실제로 수행한 명령/절차: TODO (예: `git fetch origin && git merge origin/main` → `git status`로 rename/modify 상태 확인 → 이동된 파일(`string_utils.py`) 안의 충돌 마커 직접 해결)

### 결과(Outcome)
- 최종 병합 결과 요약: TODO
- 관련 PR/커밋 링크: TODO

### 배운 점(Learnings)
- TODO
