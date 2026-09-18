# 협업 시나리오 (Codyssey B2-2 Git 협업 미션)

이 문서는 팀이 실제로 어떤 순서로, 누가, 무엇을 하는지 못박아둔 "실행 대본"입니다.
셋 다 GitHub이 처음이라는 전제로, 각 단계에 구체적인 명령어/클릭 위치까지 적어둡니다.
막히면 이 문서를 기준으로 진행 상황을 서로 맞춰보세요.

## 0. 팀 정보

| 이름 | 역할 | GitHub ID |
|---|---|---|
| 정인호 | 리드 (org 관리, branch protection, 최종 점검) | `jih19984` |
| 이교원 | 팀원 | `<이교원 GitHub ID>` |
| 박기태 | 팀원 | `<박기태 GitHub ID>` |

저장소: https://github.com/B2-2-Cody/git-collab-mission (Organization 저장소, 옵션 A)

## 1. 사전 준비

### 1-1. (정인호) 팀원 초대
GitHub → Organization `B2-2-Cody` → **Settings → People → Invite member** → 이교원/박기태 GitHub 아이디 입력 → 초대.
초대 수락 후 저장소 접근 권한(Write 이상)을 확인합니다.

### 1-2. (전원) 로컬 준비
```bash
git config --global user.name "본인 이름"
git config --global user.email "본인 GitHub 이메일"
git clone https://github.com/B2-2-Cody/git-collab-mission.git
cd git-collab-mission
```

## 2. 저장소 구조

```
README.md
SUBMISSION.md
docs/
  SCENARIO.md            (이 문서 — 팀 실행 대본)
  CONTRIBUTING.md         (협업 규칙)
  conflict-resolution.md  (충돌 해결 기록)
  troubleshooting-log.md  (트러블슈팅 기록)
src/
  utils.py                (팀 공동 유틸 함수 — 의도적으로 공유 파일로 둠)
```

## 3. 브랜치 전략 (GitHub Flow)

- `main`: 항상 배포 가능한 상태 유지. 직접 push 금지, PR로만 병합.
- `feature/<name>-<topic>`: 작업 단위 브랜치. `<name>`은 아래 영문 아이디를 사용합니다.
  - 정인호 → `inho`
  - 이교원 → `gyowon`
  - 박기태 → `gitae`
  - 예: `feature/inho-list-utils`, `feature/gyowon-string-utils`

**왜 GitHub Flow인가 (README.md에도 기록)**
- main은 항상 배포 가능한 상태를 유지해야 하기 때문
- feature 브랜치로 작업을 격리해 충돌 범위를 줄이기 위해
- PR 기반 리뷰로 품질과 추적성을 확보하기 위해

## 4. 커밋 메시지 컨벤션

형식: `<type>: <무엇을/왜 바꿨는지 알 수 있는 subject>`

- `feat:` 새 기능 — 예) `feat: add reverse_string utility to utils.py`
- `fix:` 버그 수정 — 예) `fix: handle empty list in flatten()`
- `docs:` 문서 — 예) `docs: add branch naming rule to CONTRIBUTING.md`
- `refactor:` 리팩터링 — 예) `refactor: split utils.py into string_utils.py`

**금지**: `update`, `fix`, `temp`, `wip`, `final`, `bug fix`, `edit file` 처럼 대상/효과가 드러나지 않는 메시지.

## 5. Branch Protection 설정 (정인호, 팀원 초대 완료 후에 진행)

> 주의: 팀원 초대 전에 켜면 승인해줄 사람이 없어 아무도 머지를 못 합니다. 반드시 1-1 이후에 진행하세요.

GitHub 저장소 → **Settings → Branches → Add branch ruleset (또는 Add rule)**
1. Branch name pattern: `main`
2. "Require a pull request before merging" 체크
3. "Require approvals" → `1`
4. "Do not allow bypassing the above settings" 체크 (관리자도 우회 금지)
5. Save

## 6. 이슈 목록 (총 9개)

각 이슈는 GitHub Issue로 생성하고, 해당 PR 본문에 `Closes #번호`를 반드시 포함합니다.

| 이슈 | 제목 | 담당 | 브랜치 |
|---|---|---|---|
| [#4](https://github.com/B2-2-Cody/git-collab-mission/issues/4) | `[chore] Branch protection 설정` | 정인호 | `feature/inho-branch-protection` |
| [#5](https://github.com/B2-2-Cody/git-collab-mission/issues/5) | `[docs] CONTRIBUTING.md 작성` | 정인호 | `feature/inho-contributing` |
| [#6](https://github.com/B2-2-Cody/git-collab-mission/issues/6) | `[feat] utils.py 리스트 유틸 함수 추가` | 정인호 | `feature/inho-list-utils` |
| [#7](https://github.com/B2-2-Cody/git-collab-mission/issues/7) | `[feat] utils.py 문자열 유틸 함수 추가` | 이교원 | `feature/gyowon-string-utils` |
| [#8](https://github.com/B2-2-Cody/git-collab-mission/issues/8) | `[feat] utils.py 숫자 유틸 함수 추가` | 박기태 | `feature/gitae-math-utils` |
| [#9](https://github.com/B2-2-Cody/git-collab-mission/issues/9) | `[refactor] utils.py를 string_utils.py로 분리` | 박기태 | `feature/gitae-split-utils` |
| [#10](https://github.com/B2-2-Cody/git-collab-mission/issues/10) | `[docs] conflict-resolution.md 기록` | 이교원 | `feature/gyowon-conflict-doc` |
| [#11](https://github.com/B2-2-Cody/git-collab-mission/issues/11) | `[docs] troubleshooting-log.md 기록` | 전원 (정인호 취합) | `feature/inho-troubleshooting-doc` |
| [#12](https://github.com/B2-2-Cody/git-collab-mission/issues/12) | `[docs] SUBMISSION.md 인덱스 작성` | 정인호 | `feature/inho-submission` |

이 배정대로면 팀원별 병합 PR 개수: 정인호 4개, 이교원 2개, 박기태 2개 (모두 최소 기준 2개 이상 충족).

## 7. PR 작업 흐름 (모든 이슈 공통)

```bash
git checkout main
git pull
git checkout -b feature/<name>-<topic>
# 코드/문서 수정
git add <파일>
git commit -m "feat: <무엇을 했는지>"
git push -u origin feature/<name>-<topic>
```
GitHub에서 PR 생성 시 아래 템플릿을 사용합니다.

```markdown
## 연결 이슈
- Closes #<이슈번호>

## 변경 사항(What)
- ...

## 변경 이유(Why)
- ...

## 테스트/검증(How)
- [ ] 로컬 실행 확인
- [ ] 충돌 가능성 체크
```

**리뷰 규칙**: 작성자를 제외한 나머지 2명 중 최소 1명이 리뷰합니다("LGTM"만 금지, 특정 라인/파일 근거로 질문·대안·리스크 지적 중 1개 이상 포함). 팀원별로 본인 PR이 아닌 PR에 리뷰를 2건 이상 남기면 "코드 리뷰 최소 기준"이 자동으로 충족됩니다. 최소 1개 PR은 리뷰 코멘트를 받은 뒤 커밋을 추가하거나 답글로 반영한 기록을 남기세요("리뷰 반영 경험" 요건).

## 8. 충돌 시나리오 (의도적으로 2회 유발)

### 충돌 #1 — 자명한 충돌 (같은 hunk)
- 정인호(#6)와 이교원(#7)이 **같은 시점**에 `main`에서 각자 브랜치를 생성합니다.
- 두 사람 모두 `src/utils.py` **파일 맨 끝**에 자기 함수를 추가합니다.
- 정인호 PR을 먼저 머지 → 이교원 PR을 머지하려 하면 같은 줄(파일 끝)에서 충돌 발생.
- 이교원이 로컬에서 `git pull origin main`(또는 `git merge main`) 후 충돌 마커를 직접 해결하고 push.

### 충돌 #2 — 비자명한 충돌 (파일 이동 vs 내용 수정)
- 박기태(#9)가 `git mv src/utils.py src/string_utils.py`로 파일명을 바꾸는 브랜치를 작업하는 동안,
- 같은 시점에 다른 팀원(정인호 또는 이교원)이 `src/utils.py` **내용을 수정**하는 브랜치를 먼저 머지합니다.
- 박기태가 나중에 머지하면 "파일이 이동됐는데 원본에 새 변경이 있다"는 rename/modify 충돌이 발생합니다.
- `git status`로 상황 확인 후, 이동된 파일(`string_utils.py`)에 최신 변경 내용을 수동으로 반영해서 해결.

두 사례 모두 `docs/conflict-resolution.md`에 아래 항목으로 기록합니다: 참여자 / 상황 / 충돌 마커 원문 / 해결 과정 / 결과(PR·커밋 링크) / 배운 점.

## 9. 트러블슈팅 4종 실습 배정

| 시나리오 | 담당 | 상황 예시 |
|---|---|---|
| `git commit --amend` | 정인호 | 방금 커밋한 메시지에 오타 발견 → 수정 |
| `git reset --soft HEAD~1` | 이교원 | 로컬에서 실수로 커밋 → 변경 내용은 유지한 채 커밋만 취소 |
| `git revert` | 박기태 | 이미 원격에 push된 커밋에 문제 발견 → 히스토리를 유지하며 되돌림 |
| `git stash` / `git stash pop` | 정인호 | 작업 중 급하게 다른 브랜치로 전환해야 함 → 작업 임시 보관 후 복귀 |

각자 실습 후 `docs/troubleshooting-log.md`에 시나리오/참여자/상황/시도한 명령/결과/선택 이유를 기록합니다. (정인호가 2건을 맡아 리드로서 amend·stash를 담당하고, 이교원·박기태는 각자 1건씩 맡아 "전원 최소 1개 참여" 요건을 충족합니다.)

## 10. 진행 순서 체크리스트

- [x] 1. 저장소 스캐폴드 + SCENARIO.md 작성 — *(정인호, PR #1)*
- [x] 2. CONTRIBUTING.md 작성 (#5) — *(정인호, PR #2)*
- [x] 3. conflict-resolution.md / troubleshooting-log.md 템플릿 준비 (#10, #11 선행 작업) — *(정인호, PR #3)*
- [x] 4. 이슈 #4~#12 생성 — *(정인호)*
- [ ] 5. Org 초대 + 팀원 로컬 clone
- [ ] 6. Branch Protection 설정 (#4) — *(팀원 합류 후에만)*
- [ ] 7. 기능 PR 3개(#6,#7,#8) 진행 → 충돌 #1 발생/해결
- [ ] 8. 리팩터 PR(#9) 진행 → 충돌 #2 발생/해결
- [ ] 9. 트러블슈팅 4종 실습 + 로그 작성 (#11)
- [ ] 10. conflict-resolution.md 마무리 (#10)
- [ ] 11. SUBMISSION.md 최종 정리 (#12), 아래 11번 체크리스트로 자가 점검

## 11. 평가문항 자가 점검

| 평가 항목 | 이 시나리오에서 충족되는 지점 |
|---|---|
| 저장소 1개 + 팀원 협업 권한 | 1-1 Org 초대 |
| Branch Protection + PR로만 병합 | 5. Branch Protection 설정 |
| PR ↔ 이슈 연동(Closes #n) | 7. PR 템플릿 |
| 팀원별 PR 2개 이상 + SUBMISSION.md 확인 | 6. 이슈 목록 표 (정인호 4 / 이교원 2 / 박기태 2) |
| 팀원별 리뷰 2개 이상 + 리뷰 반영 1회 | 7. 리뷰 규칙 |
| 충돌 해결 2회(비자명 1회 포함) | 8. 충돌 #1, #2 |
| 트러블슈팅 4종 + 팀원별 참여 | 9. 트러블슈팅 배정표 |
| CONTRIBUTING / conflict-resolution / troubleshooting-log 존재 | 2, 6, 8, 9 |
