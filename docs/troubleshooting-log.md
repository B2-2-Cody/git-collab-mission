# Troubleshooting Log

이 문서는 팀 전체가 수행하는 Git 트러블슈팅 4종 실습 기록입니다.
담당 배정은 [`docs/SCENARIO.md`](./SCENARIO.md) 9장을 따릅니다. 실습 후 각 항목의 `TODO`를 채워주세요.

## 시나리오: git commit --amend

### 참여자
- 정인호

### 상황
- TODO: 방금 커밋한 메시지에서 발견한 문제(예: 오타, 누락된 내용)를 재현 가능하게 설명

### 시도한 명령/절차
- TODO (예: `git commit --amend -m "..."`)

### 결과
- TODO: 무엇이 어떻게 해결됐는지
- TODO: 주의할 점(이미 push된 커밋을 amend하면 원격 히스토리와 어긋난다는 점 등)

### 왜 이 방법을 선택했는가(Why)
- TODO

---

## 시나리오: git reset --soft HEAD~1

### 참여자
- 이교원

### 상황
- TODO: 로컬에서 실수로 만든 커밋 상황(재현 가능하게 설명)

### 시도한 명령/절차
- TODO (예: `git reset --soft HEAD~1`)

### 결과
- TODO: 커밋은 취소되고 변경 내용은 스테이징 상태로 유지됨을 확인한 과정
- TODO: 주의할 점(이미 push된 커밋에는 사용하면 안 되는 이유 등)

### 왜 이 방법을 선택했는가(Why)
- TODO

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
- TODO: 작업 중 급하게 다른 브랜치로 전환해야 했던 상황(재현 가능하게 설명)

### 시도한 명령/절차
- TODO (예: `git stash`, 브랜치 전환 후 작업, `git checkout` 복귀, `git stash pop`)

### 결과
- TODO: 임시 보관한 작업을 안전하게 복귀시킨 과정
- TODO: 주의할 점(스태시 충돌 가능성 등)

### 왜 이 방법을 선택했는가(Why)
- TODO
