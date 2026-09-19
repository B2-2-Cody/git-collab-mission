# Submission Index

평가자가 팀원별 기여와 핵심 문서를 한 곳에서 확인할 수 있도록 모은 제출 인덱스입니다.
PR/리뷰가 쌓일 때마다 아래 링크를 채워주세요.

## Team
- 팀명: (팀명 결정 후 작성)
- 저장소: https://github.com/B2-2-Cody/git-collab-mission

## Member PRs

각 팀원은 최소 2개의 PR을 병합해야 합니다.

- 정인호 (`jih19984`)
  - [PR #1](https://github.com/B2-2-Cody/git-collab-mission/pull/1) — docs: 팀 협업 시나리오 문서 추가
  - [PR #2](https://github.com/B2-2-Cody/git-collab-mission/pull/2) — docs: CONTRIBUTING.md 초안 추가
  - [PR #3](https://github.com/B2-2-Cody/git-collab-mission/pull/3) — docs: conflict-resolution / troubleshooting-log 템플릿 추가
  - [PR #13](https://github.com/B2-2-Cody/git-collab-mission/pull/13) — docs: README 팀 정보 + SUBMISSION.md 인덱스 추가
  - [PR #15](https://github.com/B2-2-Cody/git-collab-mission/pull/15) — feat: utils.py 리스트 유틸 함수 추가
  - [PR #22](https://github.com/B2-2-Cody/git-collab-mission/pull/22) — docs: troubleshooting-log.md 기록
- 이교원 (`kyowon1108`)
  - [PR #16](https://github.com/B2-2-Cody/git-collab-mission/pull/16) — feat: utils.py 문자열 유틸 함수 추가
  - [PR #19](https://github.com/B2-2-Cody/git-collab-mission/pull/19) — docs: utils.py 모듈 설명 개선
  - [PR #21](https://github.com/B2-2-Cody/git-collab-mission/pull/21) — docs: 충돌 해결 기록 완성
- 박기태 (`SeouliteParker`)
  - [PR #17](https://github.com/B2-2-Cody/git-collab-mission/pull/17) — feat: utils.py 숫자 유틸 함수 추가
  - [PR #20](https://github.com/B2-2-Cody/git-collab-mission/pull/20) — refactor: utils.py를 string_utils.py로 분리

## Member Reviews

각 팀원은 본인 PR 이외에 최소 2건의 실질 리뷰를 남겨야 합니다.

- 정인호: [PR #19](https://github.com/B2-2-Cody/git-collab-mission/pull/19), [PR #20](https://github.com/B2-2-Cody/git-collab-mission/pull/20), [PR #21](https://github.com/B2-2-Cody/git-collab-mission/pull/21) (이교원·박기태 PR 리뷰)
- 이교원: [PR #1](https://github.com/B2-2-Cody/git-collab-mission/pull/1), [PR #2](https://github.com/B2-2-Cody/git-collab-mission/pull/2), [PR #3](https://github.com/B2-2-Cody/git-collab-mission/pull/3), [PR #13](https://github.com/B2-2-Cody/git-collab-mission/pull/13), [PR #15](https://github.com/B2-2-Cody/git-collab-mission/pull/15), [PR #17](https://github.com/B2-2-Cody/git-collab-mission/pull/17), [PR #22](https://github.com/B2-2-Cody/git-collab-mission/pull/22) (정인호·박기태 PR 리뷰)
- 박기태: [PR #15](https://github.com/B2-2-Cody/git-collab-mission/pull/15), [PR #16](https://github.com/B2-2-Cody/git-collab-mission/pull/16) (정인호·이교원 PR 리뷰)

리뷰 반영 경험(리뷰 코멘트를 받고 커밋/답글로 반영): [PR #7/#16 논의](https://github.com/B2-2-Cody/git-collab-mission/pull/16)(박기태 지적 → 이교원 docstring 반영 커밋), [PR #19](https://github.com/B2-2-Cody/git-collab-mission/pull/19)(정인호 지적 → 이교원 문구 보완), [PR #20](https://github.com/B2-2-Cody/git-collab-mission/pull/20)(정인호 지적 → 후속 논의), [PR #21](https://github.com/B2-2-Cody/git-collab-mission/pull/21)(정인호 마커 서식 지적 → 이교원 수정).

## Key Docs
- Scenario: [docs/SCENARIO.md](./docs/SCENARIO.md)
- Contributing: [docs/CONTRIBUTING.md](./docs/CONTRIBUTING.md)
- Conflict log: [docs/conflict-resolution.md](./docs/conflict-resolution.md)
- Troubleshooting: [docs/troubleshooting-log.md](./docs/troubleshooting-log.md)

## Evidence
`git log --oneline --graph --all` 결과 (2026-09-19 기준, 총 39개 커밋):

```
*   98369c8 Merge pull request #22 from B2-2-Cody/feature/inho-troubleshooting-doc
|\
| * 677487e docs: record revert troubleshooting scenario
| | * df3cdc9 Revert "refactor: simplify is_even modulo check"
| | * ef03e8e refactor: simplify is_even modulo check
| |/
|/|
| * 42ae8bb docs: record reset soft troubleshooting
| * 3ea0436 docs: fill stash troubleshooting scenario
* |   6c15167 Merge pull request #21 from B2-2-Cody/feature/kyowon-conflict-doc
|\ \
| | * 9153013 docs: document amend troubleshooting scenario
| |/
|/|
| * 4f64c5b docs: align recorded conflict markers
| * 82754ad docs: complete conflict resolution log
|/
*   123067a Merge pull request #20 from B2-2-Cody/feature/gitae-split-utils
|\
| * 68bd729 docs: record rename vs modify conflict in conflict-resolution.md
| *   15dd216 fix: resolve docstring conflict after utils.py -> string_utils.py rename
| |\
| |/
|/|
* |   4fb9de3 Merge pull request #19 from B2-2-Cody/feature/kyowon-fix-docstring
|\ \
| * | ad4f813 docs: note temporary conflict scenario wording
| * | 8ba58a6 docs: clarify shared utility module scope
|/ /
| * 0cfa982 refactor: split utils.py into string_utils.py
|/
*   fa6afe8 Merge pull request #17 from B2-2-Cody/feature/gitae-math-utils
|\
| * 34ead2e feat: add numeric utilities to utils.py
|/
*   c683adc Merge pull request #16 from B2-2-Cody/feature/kyowon-string-utils
|\
| * 83f7598 docs: clarify palindrome normalization behavior
| *   2799131 fix: resolve add/add conflict in utils.py
| |\
| |/
|/|
* |   d2178f1 Merge pull request #15 from B2-2-Cody/feature/inho-list-utils
|\ \
| | * 3c46886 feat: add string utilities to utils.py
| |/
|/|
| * a1ed940 feat: add flatten and unique list utilities to utils.py
|/
*   5c1ec0c Merge pull request #13 from B2-2-Cody/feature/inho-submission
|\
| * 37eba5c docs: add team info to README (real GitHub IDs) and create SUBMISSION.md index
* |   ba87fb6 Merge pull request #3 from B2-2-Cody/feature/inho-doc-templates
|\ \
* \ \   be228eb Merge pull request #2 from B2-2-Cody/feature/inho-contributing
|\ \ \
* \ \ \   4fe64ae Merge pull request #1 from B2-2-Cody/feature/inho-scenario-doc
|\ \ \ \
| |_|_|/
|/| | |
| | | * bc27dde docs: sync conflict-resolution.md template with corrected SCENARIO.md
| | * | 3e2f27a docs: unify kyowon branch prefix to match GitHub ID (kyowon1108)
| * | | fedb52b docs: update team GitHub IDs, unify kyowon branch prefix, clarify checklist status
| * | | f7954ab docs: fix conflict #1/#2 scenarios to reflect actual git merge behavior
| * | | 661e394 docs: sync scenario doc with actual GitHub issue numbers
| | | * c8b750f docs: add conflict-resolution and troubleshooting-log templates
| |_|/
|/| |
| | * 971ad07 docs: add team contributing guide
| |/
|/|
| * 55cf6de docs: add detailed team collaboration scenario
|/
* 5b20f8e Initial commit
```
