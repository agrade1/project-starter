# 새 프로젝트 시작

## GitHub 템플릿으로 새 저장소 만들기

GitHub 템플릿으로 등록한 저장소에서는 **Use this template → Create a new repository**를 선택한다. 소유자·새 이름·공개 범위를 확인하고 기본 브랜치만 복사한다. 생성된 **새 저장소**를 clone한 뒤 Orca에서 그 폴더를 열고 아래 빈 프로젝트 절의 2~4단계를 따른다. 원격 저장소 생성이 승인된 경우에만 수행한다.

이 방식은 파일 구조를 가져오며 새 Git 이력으로 시작한다. 기존 프로젝트는 아래 병합 절차를 따른다. [GitHub 공식 안내](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-repository-from-a-template).

## 빈 프로젝트

1. 템플릿의 `AGENTS.md`, `CLAUDE.md`, `README.md`, `docs/`를 새 프로젝트 폴더에 복사한다. `.git`은 복사하지 않는다. 아래 두 절대경로를 실제 값으로 바꾸고 실행한다. 대상 경로가 이미 있으면 덮어쓰지 않고 실패한다.

```sh
TEMPLATE='/absolute/path/to/project-starter'
TARGET='/absolute/path/to/new-project'
if [ -e "$TARGET" ]; then
  echo '대상 경로가 이미 있습니다. 기존 파일을 확인하고 수동 병합하세요.'
  false
else
  mkdir -p "$TARGET" &&
  cp "$TEMPLATE/AGENTS.md" "$TEMPLATE/CLAUDE.md" "$TEMPLATE/README.md" "$TARGET/" &&
  cp -R "$TEMPLATE/docs" "$TARGET/docs" &&
  git -C "$TARGET" init -b main
fi
```

복사에 실패해 일부 파일만 생겼으면 해당 폴더를 확인하고 복구한다. 자동 삭제하지 않는다. 이 방식은 원격 연결과 이전 Git 이력을 가져오지 않는다.

2. Orca에서 **새 프로젝트 폴더**를 연다. 루트 `AGENTS.md`와 `CLAUDE.md` 진입 지침은 이미 포함돼 있다. 새 서비스 이름과 목표에 맞게 루트 README를 갱신한다.
3. 아이디어/기획서가 있으면 원본을 `docs/input/` 또는 기존 문서 위치에 두고 아래 첫 메시지에 실제 경로·목표·승인 범위를 적어 보낸다. [PROJECT 양식](templates/PROJECT.md)에서 원문 대응표·필요한 절만 `docs/project/PROJECT.md` 또는 기존 정본에 작성한다. 모든 양식을 미리 만들지 않는다.
4. [역할별 프롬프트](adapters/orca/SESSION_PRESETS.md) 중 필요한 것만 사용하고, 결과와 [인계](templates/HANDOFF.md)를 다음 세션에 전달한다.

## 기존 프로젝트에 적용

기존 Git 저장소는 유지한다. `docs/agent-kit/`이 없으면 킷 폴더만 복사하고, 이미 있으면 diff를 보고 병합한다. 기존 루트 파일을 덮어쓰지 말고 [AGENTS 병합 조각](adapters/codex/AGENTS.template.md)·[CLAUDE 병합 조각](adapters/claude-code/CLAUDE.template.md)의 필요한 절만 추가한다. 기존 README·요구사항·코드·사용자 변경은 보존한다.

스타터 저장소 자체를 이미 clone했다면 `.git`을 지우거나 원격을 자동 변경하지 않는다. 위 빈 프로젝트 2~4단계부터 진행하고, 서비스용 독립 이력이 필요하면 복사 방식이나 GitHub 템플릿 방식을 선택한다. 원격 반영 전에는 서비스 저장소가 맞는지 확인한다.

## 첫 메시지 — Codex·Claude Code 공통

```text
적용되는 지침과 사용자 변경을 먼저 확인하라.
docs/agent-kit/common/START_HERE.md와
docs/agent-kit/common/WORKING_RULES.md를 읽어라.
내 작업: [새 서비스 / 기능 추가 / 버그 수정 / 기획·디자인만] — [목표].
아이디어·기획서 원문: [실제 파일 경로/URL, 없으면 현재 요청].
승인 범위: [문서만 / 제한된 로컬 프로토타입 / 지정 기능 구현].
기존 코드·문서를 파악하고 필요한 역할·기능만 선택하라.
정본이 없으면 docs/agent-kit/templates/PROJECT.md에서 필요한 절만 작성하라.
원문을 보존하고 요구사항·가정·미답 질문을 구분해 원문 위치와 연결하라.
첫 사용자 흐름과 수용 기준, TASK의 선행·현재 상태·검사·다음 전이를 정하라.
여러 단계와 비평 후 개선은 docs/agent-kit/common/OPERATING_MODEL.md를 따르라.
비평은 작성자 대화를 넘기지 말고 REVIEW_PACKET으로 새 세션에 전달하라.
개발 승인 범위가 있으면 구현·검증으로 진행하고, 문서만 승인됐으면 문서 인계에서 끝내라.
승인된 범위 안에서 검증·인계까지 완료하고 미실행 검증은 완료로 적지 마라.
```

첫 메시지의 목표 예: “`docs/input/idea.md`의 1인 예약 관리 서비스를 비평하고 첫 예약 등록 흐름을 로컬 프로토타입으로 구현. 실제 고객 데이터·결제·출시는 제외.” [아이디어 접수 예시](examples/idea-to-first-task.md)에서 원문 연결·독립 비평·수정·재개까지 확인한다.

사용 가능한 CLI와 옵션은 `codex --help`, `claude --help`에서 확인한다. 계획·리뷰에는 읽기 전용 범위를, 승인된 구현에는 필요한 쓰기 권한만 선택한다. 구체적인 예시는 [Codex](adapters/codex/README.md)·[Claude Code](adapters/claude-code/README.md)를 참고한다. 제공사·모델은 세션 설정에서 선택한다.
