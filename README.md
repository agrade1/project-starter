# Project Starter

1인 창업자가 Orca와 CLI 에이전트로 새 프로젝트를 시작할 때 복사하는 템플릿 저장소다. 공통 지침을 관리하는 이 저장소와 각 서비스의 코드·Git 이력은 분리한다.

```text
AGENTS.md          Codex 진입 지침
CLAUDE.md          Claude Code 진입 지침
README.md         사용 방법
docs/agent-kit/   역할·기능·워크플로·양식·도구별 안내
```

시작은 [QUICKSTART](docs/agent-kit/QUICKSTART.md). 템플릿 파일만 새 폴더에 복사하고 독립 Git 저장소를 초기화하는 절차가 있다. 기존 프로젝트에 가져갈 때는 루트 지침과 문서를 보존하면서 필요한 부분만 병합한다.

- [문서 선택](docs/agent-kit/common/START_HERE.md): 요청에 필요한 역할만 읽는다.
- [하네스·루프·그래프](docs/agent-kit/common/OPERATING_MODEL.md): 작업 상태·분기·비평 후 수정·세션 재개를 연결한다.
- [아이디어 접수 예시](docs/agent-kit/examples/idea-to-first-task.md): 원문 → 수용 기준 → 첫 TASK → 독립 비평·개선.
- [역할별 시작 프롬프트](docs/agent-kit/adapters/orca/SESSION_PRESETS.md): 목표·승인 범위·입력 경로를 채워 사용한다.
- [작은 기능 예시](docs/agent-kit/examples/favorite-filter.md): 구현·검증·인계 흐름을 문서로 따라간다.

8개 역할, 9개 기능, 4개 워크플로, 8개 산출물 양식을 제공한다. 모든 역할·문서를 매번 실행하거나 생성하지 않는다. 프로젝트별 요구사항·승인·진행은 기존 정본 또는 `docs/project/`에 작업을 시작하면서 기록한다.

아이디어/기획서 원문을 지정하면 AI가 요구·가정·질문을 구분하고 첫 사용자 흐름부터 진행한다. 리뷰는 [문제·제약 입력](docs/agent-kit/templates/REVIEW_PACKET.md)으로 기준을 먼저 세운 뒤 실제 산출물을 검사한다. 이 팩은 문서 기반 운영 계약이며 자동 실행기나 편향 제거 보증을 제공하지 않는다.

## 검증

저장소 루트에서 실행한다. Python 3.9 이상이 이미 설치돼 있어야 한다.

```sh
python3 docs/agent-kit/capabilities/check-links.py
python3 docs/agent-kit/capabilities/check-links.py .
python3 docs/agent-kit/capabilities/check-links.py --self-test
```

첫 명령은 킷 링크·역할/기능 필수 절, 두 번째는 루트 문서까지 포함한 링크, 세 번째는 검사 도구의 실패 감지를 확인한다. 파일 구조를 바꾸면 역할 8개·기능 9개·워크플로 4개·양식 8개의 구성을 별도 확인한다. [검사 도구의 한계와 유지보수 조건](docs/agent-kit/capabilities/verification.md)을 따른다.

공통 지침을 개선할 때는 템플릿에서 수정하고, 이미 시작한 프로젝트에는 필요한 변경만 diff로 검토해 가져간다. 템플릿 업데이트로 프로젝트의 코드·결정·기존 지침을 덮어쓰지 않는다.

[이번 비평·개선 근거](docs/agent-kit/maintenance/REVIEW-2026-09-10.md)에 변경 이유·외부 원문·검증 범위를 기록했다.
