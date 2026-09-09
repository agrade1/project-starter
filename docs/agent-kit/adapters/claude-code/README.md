# Claude Code 어댑터

템플릿 루트에는 CLAUDE.md가 이미 포함돼 있다. 기존 프로젝트에 적용할 때는 [CLAUDE 병합 조각](CLAUDE.template.md)을 참고하여 기존 지침을 보존하고 필요한 절만 추가한다.

Claude Code는 CLAUDE.md를 프로젝트 맥락으로 읽지만 지침은 권한 강제 장치가 아니다. 자동 로딩은 시작 경로·모드·설정의 영향을 받으므로 `/memory`로 확인할 수 있다. [공식 기억 문서](https://code.claude.com/docs/en/memory)(2026-09-09 확인). 킷 전체를 import하지 않고 첫 메시지에서 필요한 경로를 지정한다.

```text
적용 지침과 사용자 변경을 먼저 확인하라.
docs/agent-kit/common/START_HERE.md,
docs/agent-kit/common/WORKING_RULES.md,
docs/agent-kit/roles/frontend.md를 읽어라.
작업 지시: [프로젝트의 TASK 경로]. 승인 범위와 소유 파일을 확인하고
관련 기존 코드·디자인·API 계약만 읽어 구현·focused 검증·인계까지 완료하라.
독립 리뷰는 다른 세션에서 받도록 실제 diff·검사 근거·미검증을 반환하라.
```

실행 전에 `claude --version`과 `claude --help`로 해당 설치의 옵션을 확인한다. `--permission-mode`의 `plan`은 기획, `manual`은 승인된 구현의 예시다. 이것만으로 읽기 전용 보안 경계가 완성된다고 주장하지 않는다. 구현자와 리뷰어는 fresh 세션으로 분리하고 기본 독립 리뷰는 Codex 읽기 전용 모드를 쓴다.
Claude Code의 custom agent 등록도 가능하다고 도움말에 나오지만 이 킷은 공통 Markdown+첫 프롬프트만 사용한다. 전역 설정·상시 subagent 등록·모델 고정이 필요 없다. 기존 인증을 사용하고 새 로그인·유료 API 사용이 필요하면 승인 범위를 먼저 확인한다.
