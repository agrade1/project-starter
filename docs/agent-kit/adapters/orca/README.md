# Orca에서 사용하기

프로젝트·worktree·세션은 Orca의 기본 기능으로 관리한다. 역할과 작업 지시의 정본은 [세션 프롬프트](SESSION_PRESETS.md)와 프로젝트 문서다. 별도 실행 엔진·자동 호출·역할 API를 만들 필요는 없다.

## 설치 기능 확인

```sh
orca --version
orca --help
orca status --json
orca worktree current --json
```

명령 형식과 UI 경로는 버전에 따라 달라질 수 있으므로 해당 설치의 도움말과 UI에서 먼저 확인한다. CLI 경로가 작동하지 않으면 앱 설치 위치와 CLI 등록 상태를 확인하고, 지원되는 앱 내 실행 경로 또는 UI를 사용한다. 전역 설정이나 설치를 임의 변경하지 않는다.

| 작업 | 지원 방식 | 확인할 점 |
|---|---|---|
| 프로젝트 등록 | 프로젝트 폴더 열기 또는 `repo add --path` | 실제 프로젝트 경로와 기존 등록 여부 |
| 같은 checkout의 새 세션 | UI 새 탭 또는 `terminal create` | CLI·권한·세션 이름·첫 프롬프트 |
| 병렬 코드 수정 | 새 작업 트리 만들기 또는 `worktree create` | 선행 계약·기준 commit·파일 소유권·setup/default terminals |
| 역할 프롬프트 저장 | 설정 → 빠른 명령어 → Agent 프롬프트 | 프로젝트 범위·대상·CLI·본문 |
| 브라우저 검증 | 설치에서 지원하는 tab/snapshot 등 | 실제 로컬 앱·현재 탭·권한·검증 시나리오 |

프롬프트 저장은 권한 설정이나 실행 성공을 뜻하지 않는다. 역할 전용 설정 파일/API가 있다고 추측하지 않는다. `orca.yaml` 같은 설정도 설치 버전이 지원하는 목적과 schema를 확인한 경우에만 사용한다.

## 프로젝트별 프롬프트 저장

1. 실제 작업할 프로젝트를 Orca에서 선택한다.
2. **설정 → 빠른 명령어 → 명령 추가**를 연다.
3. **Agent 프롬프트**를 선택하고 [세션 기본안](SESSION_PRESETS.md)의 레이블·CLI·본문을 입력한다. TASK 경로와 승인 범위를 실제 작업에 맞춘다.
4. **범위 → 프로젝트**에서 대상 이름을 확인하고 **저장**한다. 목록에서 프로젝트·CLI·본문을 다시 확인한다.
5. 작업을 시작할 때만 탭 바의 빠른 명령 메뉴에서 호출한다. 저장된 문구가 CLI 권한 모드를 자동 적용한다고 가정하지 않는다.

설정은 프로젝트마다 선택 적용한다. 이 저장소를 복사해도 Orca의 저장 프롬프트·계정·권한이 자동 복사되지는 않는다. 등록하지 않고 새 CLI 세션에 프롬프트를 직접 붙여넣어도 된다.

## 세션과 병렬 작업

계획·조사는 같은 checkout을 읽어도 된다. 다음은 현재 worktree에 독립 리뷰 세션을 시작하는 예시다. `create`는 실제 CLI를 시작하므로 작업 승인이 있을 때 실행한다.

```sh
orca terminal create --worktree active --title 'review-TASK-ID' --command 'codex --sandbox read-only' --json
```

[작업 분해](../../capabilities/task-planning.md)로 DAG·공유 API·파일 소유권·예산을 확정한 뒤에만 병렬 writer별 worktree를 만든다. setup/default terminal 설정을 먼저 읽는다. `--setup skip`은 setup 후크만 건너뛰며 기본 탭의 명령까지 차단하지 않는다. 설치·데이터 변경 후크는 승인 범위를 확인한다.
미커밋 문서는 새 worktree에 자동으로 포함되지 않는다. 킷과 공유 계약이 포함된 기준 commit을 사용한다. Orca가 만든 worktree 안에서 CLI 자체 worktree 기능을 중복 사용하지 않는다.

통합 담당 1명이 HEAD·소유 파일·선행 증거를 확인하고 로컬 통합을 순차 수행한다. idle/exit만으로 기능 완료를 판단하지 않는다. 터미널 핸들은 `terminal list`에서 확인한다. 브라우저 작업도 최신 화면을 다시 관측하고 실제 사용자 흐름의 결과를 기록한다.
