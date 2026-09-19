# Troubleshooting Log

이 문서는 팀 전체가 수행하는 Git 트러블슈팅 4종 실습 기록입니다.
담당 배정은 [`docs/SCENARIO.md`](./SCENARIO.md) 9장을 따릅니다. 실습 후 각 항목의 `TODO`를 채워주세요.

## 시나리오: git commit --amend

### 참여자
- 정인호

### 상황
- 이 문서(`docs/troubleshooting-log.md`)의 amend 구간을 채우고 아직 `git push`하기 전에, 방금 로컬에 만든 커밋 메시지에 오타(`dcument`)가 있는 걸 발견함. 아직 원격에 올라가지 않은 커밋이라 안전하게 고칠 수 있는 상황.

### 시도한 명령/절차
```bash
git commit -m "docs: dcument amend troubleshooting scenario"
# 커밋 직후 메시지 오타 발견 (dcument -> document), 아직 push 전이므로 amend로 수정
git commit --amend -m "docs: document amend troubleshooting scenario"
```

### 결과
- `git commit --amend`는 방금 만든 커밋을 새 커밋으로 교체한다 — 해시가 바뀌지만(오타 커밋 `96bcd3d` → 수정 커밋 `b13e20c`), 파일 변경 내용은 그대로 유지된 채 메시지만 고쳐짐.
- 주의할 점: 아직 push하지 않은 로컬 커밋에서만 안전하다. 이미 push되어 다른 사람이 pull 받은 커밋을 amend하면 해시가 바뀌어 원격/로컬 히스토리가 어긋나고, 이후 `git push --force`가 필요해진다 — 공유 브랜치에서는 지양해야 함.

### 왜 이 방법을 선택했는가(Why)
- `git reset --soft`로 커밋을 풀었다가 새로 커밋해도 되지만, 메시지만 고치는 단순한 경우엔 `--amend`가 한 줄로 끝나 더 직관적이다. 아직 아무도 이 커밋을 받아가지 않은 로컬 전용 상태였기 때문에 안전 조건도 충족했다.

---

## 시나리오: git reset --soft HEAD~1

### 참여자
- 이교원

### 상황
- `feature/kyowon-string-utils`에서 문자열 함수와 테스트를 작성한 뒤, 잘못된 로컬 커밋을 취소하는 상황을 재현하기 위해 임시 커밋을 생성함.
- 임시 커밋 메시지는 `wip: temporary string utils commit`, 커밋 해시는 `f95d8d1`이었으며 원격에 push하기 전이었음.

### 시도한 명령/절차
```bash
git add src tests
git commit -m "wip: temporary string utils commit"
git log -1 --oneline
# f95d8d1 wip: temporary string utils commit

git reset --soft HEAD~1
git status --short
```
- `reset --soft` 직후 커밋만 취소되고 `src/__init__.py`, `src/utils.py`, `tests/test_utils.py` 등 변경 내용이 staged 상태로 남아 있는 것을 확인함.
- 테스트 실행 중 생성돼 함께 staged된 `__pycache__` 파일은 스테이징에서 제외하고 삭제한 뒤 정상 커밋을 다시 생성함.

### 결과
- 임시 커밋 `f95d8d1`은 현재 브랜치 히스토리에서 제거됐지만, 작성한 문자열 함수와 테스트는 삭제되지 않고 staged 상태로 유지됨.
- 불필요한 캐시 파일을 정리한 뒤 `feat: add string utilities to utils.py` 메시지로 정상 커밋 `3c46886`을 생성하고 PR #16으로 병합함.
- 관련 PR: [PR #16](https://github.com/B2-2-Cody/git-collab-mission/pull/16)
- 주의할 점: `reset --soft`는 커밋만 되돌리고 변경과 staging 상태를 유지한다. 이미 원격에 push해 팀원과 공유한 커밋을 reset하면 히스토리가 어긋나므로, 공유된 커밋 취소에는 `git revert`를 사용해야 한다.

### 왜 이 방법을 선택했는가(Why)
- 아직 원격에 push하지 않은 로컬 커밋이었고, 코드와 staging 상태를 보존하면서 커밋 메시지와 포함 파일을 다시 정리해야 했기 때문에 `reset --soft`를 선택함.

---

## 시나리오: git revert

### 참여자
- 박기태

### 상황
- TODO: 이미 원격(main)에 push된 커밋에서 발견한 문제(재현 가능하게 설명)

### 시도한 명령/절차
- TODO (예: `git revert <commit-sha>`)

### 결과
- TODO: 히스토리를 유지한 채 되돌린 결과
- TODO: 주의할 점(원격 히스토리/협업에 미치는 영향)

### 왜 이 방법을 선택했는가(Why)
- TODO: reset 대신 revert를 선택한 이유(이미 공유된 히스토리를 재작성하지 않기 위해 등)

---

## 시나리오: git stash / git stash pop

### 참여자
- 정인호

### 상황
- 이 stash 구간을 작성하던 중, `main`에 PR #21(충돌 기록 문서)이 이미 머지됐는지 급히 확인해야 했음. 커밋하지 않은 채로 `main`으로 전환하면 편집 중이던 내용이 `main`에 그대로 남아 있는 상태로 보이거나 충돌할 위험이 있어 stash가 필요했음.

### 시도한 명령/절차
```bash
git stash push -m "wip: troubleshooting-log stash section"
git checkout main
git log --oneline -1   # PR #21 머지 여부 확인
git checkout feature/inho-troubleshooting-doc
git stash pop
```

### 결과
- `git stash push`로 작업 중이던 변경 내용이 스택에 안전하게 보관되고, working tree는 마지막 커밋 상태로 깨끗해짐. `main`으로 전환해 확인 작업을 마친 뒤 원래 브랜치로 돌아와 `git stash pop`으로 변경 내용을 그대로 복원함.
- 주의할 점: stash한 파일과 복귀 후 브랜치의 파일이 같은 부분을 건드리면 pop 시 충돌이 날 수 있다. 또한 `git stash` 대신 `git stash pop` 없이 `git stash apply`를 쓰면 스택에 항목이 남아 나중에 헷갈릴 수 있어, 복원 후에는 `git stash list`로 남은 항목이 없는지 확인하는 습관이 필요하다.

### 왜 이 방법을 선택했는가(Why)
- 커밋하기엔 아직 미완성인 변경을 임시로 치워두고 다른 브랜치를 확인해야 하는 상황이라, 불필요한 WIP 커밋을 남기지 않고 작업 상태를 그대로 보존할 수 있는 `stash`가 가장 적합했다.
