# 역할별 세션 기본안과 시작 프롬프트

대상 프로젝트 `docs/agent-kit/` 배치를 전제로 한다. 아래 CLI는 기본안이며 사용자 환경에 맞게 바꿀 수 있다. 특정 모델명은 고정하지 않는다. 8개 역할을 모두 실행하지 말고 [문서 선택](../../common/START_HERE.md)을 따른다.
모든 프롬프트의 `[목표]`, `[TASK 또는 입력 정본 경로]`, `[승인 범위·시간 상한]`을 실제 값으로 채운다. 프로젝트 경로표가 없다면 기존 문서 위치부터 확인한다. 각 역할 링크의 시작 문서와 기능을 읽으면 충분하며 다른 역할 전체를 읽지 않는다.

계획/리뷰 CLI 기본: `codex --sandbox read-only`. 문서 쓰기가 승인된 계획 세션은 `workspace-write --ask-for-approval on-request`로 시작하거나 읽기 결과를 사람이 문서에 저장한다. Claude 계획은 `--permission-mode plan`, 승인된 문서/코드 작성은 `--permission-mode manual`. UI 저장 프롬프트가 이 옵션을 자동 적용한다고 가정하지 않는다.

## 기획·진행

- 세션 이름: `plan-TASK-ID`
- CLI 기본안: Codex
- 읽기: [공통 규칙](../../common/WORKING_RULES.md), [기획·진행 역할](../../roles/coordinator.md), TASK/입력 정본과 역할에 연결된 기능.
- 예상 산출물: PROJECT·TASK·HANDOFF
- 인계 대상: 선택한 전문 역할
- worktree: 읽기 중심 작업에는 불필요. 문서/토큰을 병렬 수정할 때만 별도 소유 경로 또는 worktree를 배정한다.

```text
목표: [목표]. 입력: [TASK 또는 입력 정본 경로]. 승인 범위·시간 상한: [범위·상한].
실제 작업 디렉터리와 적용 지침·사용자 변경을 먼저 확인하라.
docs/agent-kit/common/WORKING_RULES.md와 docs/agent-kit/roles/coordinator.md를 읽고,
역할이 지정한 기능과 이번 입력 정본만 추가로 읽어라.
문서만; 승인/경로표·작업 분해를 정리. 소유 파일과 제외 범위를 지켜라.
아이디어/기획서 원문 경로·절·버전을 요구사항과 연결하고 가정/미답을 구분하라.
첫 TASK의 수용 기준·선행·상태·검사·다음 전이·구현 착수 조건을 정하라.
필수 산출물·실제 검증·미검증·다음 담당에게 넘길 내용을 반환하라.
승인되지 않은 범위 확대·추가 비용·원격 쓰기·출시는 실행하지 마라.
```

## 리서치

- 세션 이름: `research-TASK-ID`
- CLI 기본안: Codex
- 읽기: [공통 규칙](../../common/WORKING_RULES.md), [리서치 역할](../../roles/researcher.md), TASK/입력 정본과 역할에 연결된 기능.
- 예상 산출물: RESEARCH 또는 조사 응답
- 인계 대상: 제품 기획·기술 설계
- worktree: 읽기 중심 작업에는 불필요. 문서/토큰을 병렬 수정할 때만 별도 소유 경로 또는 worktree를 배정한다.

```text
목표: [목표]. 입력: [TASK 또는 입력 정본 경로]. 승인 범위·시간 상한: [범위·상한].
실제 작업 디렉터리와 적용 지침·사용자 변경을 먼저 확인하라.
docs/agent-kit/common/WORKING_RULES.md와 docs/agent-kit/roles/researcher.md를 읽고,
역할이 지정한 기능과 이번 입력 정본만 추가로 읽어라.
지정 질문의 원문 근거만 조사. 소유 파일과 제외 범위를 지켜라.
필수 산출물·실제 검증·미검증·다음 담당에게 넘길 내용을 반환하라.
승인되지 않은 범위 확대·추가 비용·원격 쓰기·출시는 실행하지 마라.
```

## 제품 기획

- 세션 이름: `product-TASK-ID`
- CLI 기본안: Codex
- 읽기: [공통 규칙](../../common/WORKING_RULES.md), [제품 기획 역할](../../roles/product.md), TASK/입력 정본과 역할에 연결된 기능.
- 예상 산출물: PRD/PROJECT의 범위·수용 기준
- 인계 대상: UX·UI·기술 설계
- worktree: 읽기 중심 작업에는 불필요. 문서/토큰을 병렬 수정할 때만 별도 소유 경로 또는 worktree를 배정한다.

```text
목표: [목표]. 입력: [TASK 또는 입력 정본 경로]. 승인 범위·시간 상한: [범위·상한].
실제 작업 디렉터리와 적용 지침·사용자 변경을 먼저 확인하라.
docs/agent-kit/common/WORKING_RULES.md와 docs/agent-kit/roles/product.md를 읽고,
역할이 지정한 기능과 이번 입력 정본만 추가로 읽어라.
MVP·가정·실험·개발 승인 경계를 정리. 소유 파일과 제외 범위를 지켜라.
필수 산출물·실제 검증·미검증·다음 담당에게 넘길 내용을 반환하라.
승인되지 않은 범위 확대·추가 비용·원격 쓰기·출시는 실행하지 마라.
```

## UX·UI

- 세션 이름: `design-TASK-ID`
- CLI 기본안: Claude Code
- 읽기: [공통 규칙](../../common/WORKING_RULES.md), [UX·UI 역할](../../roles/designer.md), TASK/입력 정본과 역할에 연결된 기능.
- 예상 산출물: DESIGN·필요한 토큰 계약
- 인계 대상: FE·BE·QA
- worktree: 읽기 중심 작업에는 불필요. 문서/토큰을 병렬 수정할 때만 별도 소유 경로 또는 worktree를 배정한다.

```text
목표: [목표]. 입력: [TASK 또는 입력 정본 경로]. 승인 범위·시간 상한: [범위·상한].
실제 작업 디렉터리와 적용 지침·사용자 변경을 먼저 확인하라.
docs/agent-kit/common/WORKING_RULES.md와 docs/agent-kit/roles/designer.md를 읽고,
역할이 지정한 기능과 이번 입력 정본만 추가로 읽어라.
요청된 디자인 문서만 작성. 소유 파일과 제외 범위를 지켜라.
필수 산출물·실제 검증·미검증·다음 담당에게 넘길 내용을 반환하라.
승인되지 않은 범위 확대·추가 비용·원격 쓰기·출시는 실행하지 마라.
```

## 기술 설계

- 세션 이름: `architecture-TASK-ID`
- CLI 기본안: Codex
- 읽기: [공통 규칙](../../common/WORKING_RULES.md), [기술 설계 역할](../../roles/architect.md), TASK/입력 정본과 역할에 연결된 기능.
- 예상 산출물: TECH_PLAN/API 계약·의존성
- 인계 대상: 구현자·기획·진행
- worktree: 읽기 중심 작업에는 불필요. 문서/토큰을 병렬 수정할 때만 별도 소유 경로 또는 worktree를 배정한다.

```text
목표: [목표]. 입력: [TASK 또는 입력 정본 경로]. 승인 범위·시간 상한: [범위·상한].
실제 작업 디렉터리와 적용 지침·사용자 변경을 먼저 확인하라.
docs/agent-kit/common/WORKING_RULES.md와 docs/agent-kit/roles/architect.md를 읽고,
역할이 지정한 기능과 이번 입력 정본만 추가로 읽어라.
기존 코드를 읽고 기술 계약/영향 파일을 정리. 소유 파일과 제외 범위를 지켜라.
필수 산출물·실제 검증·미검증·다음 담당에게 넘길 내용을 반환하라.
승인되지 않은 범위 확대·추가 비용·원격 쓰기·출시는 실행하지 마라.
```

## 프론트엔드

- 세션 이름: `frontend-TASK-ID`
- CLI 기본안: Claude Code
- 읽기: [공통 규칙](../../common/WORKING_RULES.md), [프론트엔드 역할](../../roles/frontend.md), TASK/입력 정본과 역할에 연결된 기능.
- 예상 산출물: UI 코드·검사·인계
- 인계 대상: 독립 리뷰·QA
- worktree: 병렬 코드 writer마다 별도 worktree·겹치지 않는 파일 범위 필수. 단일 수정은 현재 checkout 가능.

```text
목표: [목표]. 입력: [TASK 또는 입력 정본 경로]. 승인 범위·시간 상한: [범위·상한].
실제 작업 디렉터리와 적용 지침·사용자 변경을 먼저 확인하라.
docs/agent-kit/common/WORKING_RULES.md와 docs/agent-kit/roles/frontend.md를 읽고,
역할이 지정한 기능과 이번 입력 정본만 추가로 읽어라.
TASK에 이미 승인된 UI·테스트만 구현. 소유 파일과 제외 범위를 지켜라.
필수 산출물·실제 검증·미검증·다음 담당에게 넘길 내용을 반환하라.
승인되지 않은 범위 확대·추가 비용·원격 쓰기·출시는 실행하지 마라.
```

## 백엔드

- 세션 이름: `backend-TASK-ID`
- CLI 기본안: Claude Code
- 읽기: [공통 규칙](../../common/WORKING_RULES.md), [백엔드 역할](../../roles/backend.md), TASK/입력 정본과 역할에 연결된 기능.
- 예상 산출물: 서버 코드·검사·인계
- 인계 대상: 독립 리뷰·QA
- worktree: 병렬 코드 writer마다 별도 worktree·겹치지 않는 파일 범위 필수. 단일 수정은 현재 checkout 가능.

```text
목표: [목표]. 입력: [TASK 또는 입력 정본 경로]. 승인 범위·시간 상한: [범위·상한].
실제 작업 디렉터리와 적용 지침·사용자 변경을 먼저 확인하라.
docs/agent-kit/common/WORKING_RULES.md와 docs/agent-kit/roles/backend.md를 읽고,
역할이 지정한 기능과 이번 입력 정본만 추가로 읽어라.
TASK에 이미 승인된 서버·테스트만 구현. 소유 파일과 제외 범위를 지켜라.
필수 산출물·실제 검증·미검증·다음 담당에게 넘길 내용을 반환하라.
승인되지 않은 범위 확대·추가 비용·원격 쓰기·출시는 실행하지 마라.
```

## 독립 리뷰·QA

- 세션 이름: `review-TASK-ID`
- CLI 기본안: Codex
- 읽기: [공통 규칙](../../common/WORKING_RULES.md), [독립 리뷰·QA 역할](../../roles/reviewer.md), 채워진 REVIEW_PACKET의 지정 절과 역할에 연결된 기능.
- 예상 산출물: REVIEW 형식의 응답
- 인계 대상: 구현자·기획·진행·사람
- worktree: 읽기 중심 작업에는 불필요. 문서/토큰을 병렬 수정할 때만 별도 소유 경로 또는 worktree를 배정한다.

```text
목표: [목표]. 입력: [채워진 REVIEW_PACKET 실제 경로·절]. 승인 범위·시간 상한: [범위·상한].
실제 작업 디렉터리와 적용 지침·사용자 변경을 먼저 확인하라.
docs/agent-kit/common/WORKING_RULES.md와 docs/agent-kit/roles/reviewer.md를 읽고,
역할이 지정한 기능과 채워진 입력 패킷만 추가로 읽어라. 빈 양식은 실제 입력을 대신하지 않는다.
docs/agent-kit/templates/REVIEW_PACKET.md의 1차 입력으로 먼저 판정 기준과 실패 시나리오를 기록하라.
그 뒤 2차 입력의 실제 산출물·diff·검사 원문을 열어 계약·안전 경계·거짓 성공을 검토하라.
방향 비평이면 현 방향 유지·단순화·다른 접근의 근거를 비교하라. 소유 파일과 제외 범위를 지켜라.
필수 산출물·실제 검증·미검증·다음 담당에게 넘길 내용을 반환하라.
승인되지 않은 범위 확대·추가 비용·원격 쓰기·출시는 실행하지 마라.
```

리뷰 세션은 fresh로 시작하고 작성자의 대화/자기평가를 전달하지 않는다. 입력은 TASK 전체 서사 대신 [REVIEW_PACKET](../../templates/REVIEW_PACKET.md)의 필요한 절로 준비한다. 1차 기준 기록 후 2차 증거를 전달하면 분리가 더 명확하다. QA 검사가 파일을 쓰면 별도 허용된 환경에서 실행하게 하고 리뷰어는 원문 증거를 읽는다. 검증되지 않은 결과는 미실행/미확인으로 남긴다.
