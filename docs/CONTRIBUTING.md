# Contributing Guide

이 문서는 `git-collab-mission` 팀(정인호/이교원/박기태)의 협업 규칙을 정리합니다.
자세한 실행 순서/담당자 배정은 [`docs/SCENARIO.md`](./SCENARIO.md)를 참고하세요.

## 브랜치 전략 (GitHub Flow)

- `main`: 항상 배포 가능한 상태(팀 기준 "깨지지 않는 상태")를 유지합니다. 직접 push는 금지하며, PR을 통해서만 병합합니다.
- `feature/*`: 작업 단위 브랜치. 이슈 하나당 브랜치 하나를 기본으로 합니다.

**우리 팀이 GitHub Flow를 선택한 이유**
- main은 언제든 배포 가능한 상태여야 하고, feature 브랜치가 이를 보호해주기 때문입니다.
- 작업을 브랜치로 격리하면 충돌 범위가 좁아지고, 문제가 생겨도 되돌리기 쉽습니다.
- PR 기반 리뷰를 거치므로 품질과 변경 이력의 추적성이 확보됩니다.

## 브랜치 네이밍 규칙

`feature/<name>-<topic>` 형식을 사용합니다.

| 이름 | 브랜치 접두사 |
|---|---|
| 정인호 | `inho` |
| 이교원 | `kyowon` |
| 박기태 | `gitae` |

예시: `feature/inho-list-utils`, `feature/kyowon-string-utils`, `feature/gitae-split-utils`

## 커밋 메시지 컨벤션

형식: `<type>: <무엇을/왜 바꿨는지 알 수 있는 subject>`

- `feat:` 새 기능 추가 — 예) `feat: add reverse_string utility to utils.py`
- `fix:` 버그 수정 — 예) `fix: handle empty list in flatten()`
- `docs:` 문서 변경 — 예) `docs: add branch naming rule to CONTRIBUTING.md`
- `refactor:` 동작 변화 없는 구조 개선 — 예) `refactor: split utils.py into string_utils.py`

**금지 예시** (대상/효과가 드러나지 않는 메시지는 의미없는 커밋으로 간주):
- `update`, `fix`, `temp`, `wip`, `final` 같은 단어만 있는 경우
- `bug fix`, `edit file` 처럼 무엇을/왜 바꿨는지 알 수 없는 경우

## PR 작성 규칙

모든 feature 브랜치는 PR로만 `main`에 병합합니다. PR 본문에는 최소 아래 항목을 포함합니다.

```markdown
## 연결 이슈
- Closes #<이슈번호>

## 변경 사항(What)
- ...

## 변경 이유(Why)
- ...

## 테스트/검증(How)
- [ ] 로컬 실행/간단 테스트
- [ ] 충돌 가능성 체크(필요 시)
```

**병합 조건**: 리뷰 최소 1명 승인(approve) 필요, main 직접 push 불가.

## 코드 리뷰 규칙

- "LGTM"/"좋아요" 한 마디만 남기는 리뷰는 금지합니다. 아래 중 하나 이상을 포함한 실질 코멘트를 1개 이상 남겨야 합니다.
  - 특정 라인/파일을 근거로 한 질문
  - 대안 제안
  - 리스크 지적
  - 개선 제안
- 리뷰어는 작성자 본인을 제외한 팀원이 맡습니다.
- 리뷰를 받은 작성자는 최소 1회 이상 커밋 추가/수정 또는 답글로 반영 여부를 남깁니다(리뷰-작성자 간 상호작용 기록).

## 충돌 대응 흐름

1. **공유**: 충돌을 발견한 사람이 즉시 관련 팀원에게 어떤 브랜치/파일에서 충돌이 났는지 공유합니다.
2. **해결**: `git pull`/`git merge`로 충돌을 재현한 뒤, 충돌 마커(`<<<<<<<`, `=======`, `>>>>>>>`)를 직접 검토하여 keep-both / choose-one / refactor 중 적절한 전략으로 해결합니다.
3. **기록**: 해결 즉시 [`docs/conflict-resolution.md`](./conflict-resolution.md)에 참여자·상황·충돌 마커·해결 과정·결과·배운 점을 남깁니다.

트러블슈팅(amend/reset/revert/stash) 관련 기록은 [`docs/troubleshooting-log.md`](./troubleshooting-log.md)에 남깁니다.
