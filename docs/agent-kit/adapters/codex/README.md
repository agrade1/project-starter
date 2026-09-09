# Codex 어댑터

대상 프로젝트 루트에서 시작한다. 템플릿 루트에는 AGENTS.md가 이미 포함돼 있다. 기존 프로젝트에 적용할 때는 [AGENTS 병합 조각](AGENTS.template.md)을 참고하여 기존 파일을 보존하고 필요한 절만 추가한다.

Codex의 지침 탐색은 전역 및 프로젝트 경로 계층과 설정의 영향을 받는다. 킷을 복사했다고 임의 Markdown 전체가 자동으로 로딩되지는 않는다. 자세한 탐색 규칙은 [공식 AGENTS 문서](https://learn.chatgpt.com/docs/agent-configuration/agents-md)를 참조한다(2026-09-09 확인). 첫 메시지에서 경로를 명시하는 방식이 기본이다.

```text
적용 지침과 사용자 변경을 먼저 확인하라.
docs/agent-kit/common/START_HERE.md,
docs/agent-kit/common/WORKING_RULES.md,
docs/agent-kit/roles/coordinator.md를 읽어라.
목표: [작업]. 승인 범위: [범위]. 기존 코드·문서를 먼저 파악하고
이번에 필요한 역할만 선택하여 결과·검증·인계까지 진행하라.
```

계획·독립 리뷰 기본 CLI는 `codex --sandbox read-only`다. 검사가 파일을 쓰면 읽기 전용 리뷰 세션에서 권한을 풀어 실행하지 말고 별도 QA 담당/환경의 증거를 요구한다. 승인된 구현은 `codex --sandbox workspace-write --ask-for-approval on-request`를 사용할 수 있다.
실행 전에 `codex --version`과 `codex --help`로 해당 설치의 옵션을 확인한다.
모델명·reasoning effort는 프로젝트/구독에 맞게 세션에서 선택한다. 전역 config를 복사하지 않는다. Orca가 만든 worktree 안에서 Codex `--worktree`를 중복 사용하지 않는다.
