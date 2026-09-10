# 시작과 문서 선택

1. 작업 디렉터리, 적용 지침, 실제 브랜치·HEAD·dirty 상태를 확인한다. 기존 요구사항·코드·테스트를 먼저 찾는다.
2. [공통 규칙](WORKING_RULES.md)을 읽고 사용자 요청의 승인 범위와 종료 지점을 확인한다.
3. 아래에서 워크플로 하나, 맡은 역할 하나, 그 역할이 지정한 기능만 읽는다. 관련 없는 보고서·다른 역할 전문은 기본 컨텍스트에 넣지 않는다.
4. 산출물 경로는 프로젝트의 기존 위치를 우선한다. 없으면 [프로젝트 양식](../templates/PROJECT.md)의 경로표를 채운다. 아래 `docs/project/` 경로는 대상 프로젝트용 기본값이지 킷 안에 이미 있는 파일이 아니다.
5. 새 서비스·여러 단계·비평 후 수정·세션 재개에는 [하네스·루프·그래프 운영](OPERATING_MODEL.md)을 적용한다. 아이디어 문서는 원문을 보존하고 [접수 절차](../workflows/new-service.md#아이디어와-기획서-접수)부터 진행한다. 리뷰어에게는 [독립 비평 입력](../templates/REVIEW_PACKET.md)을 전달한다.

| 요청 | 시작 역할 | 워크플로 | 필요할 때만 읽는 기능 |
|---|---|---|---|
| 새 서비스·아이디어 | [기획·진행](../roles/coordinator.md) | [새 서비스](../workflows/new-service.md) | [사업 가설·MVP](../capabilities/product.md), [리서치](../capabilities/research.md) |
| 기존 기능 추가 | [기획·진행](../roles/coordinator.md) 또는 해당 구현자 | [기능 추가](../workflows/feature.md) | [작업 분해](../capabilities/task-planning.md) |
| 재현 가능한 버그 | [프론트엔드](../roles/frontend.md) 또는 [백엔드](../roles/backend.md) | [버그 수정](../workflows/bugfix.md) | [구현](../capabilities/implementation.md), [검증](../capabilities/verification.md) |
| 기획만 | [제품 기획](../roles/product.md) | [기획·디자인만](../workflows/planning-design.md) | [사업 가설·MVP](../capabilities/product.md) |
| 조사만 | [리서치](../roles/researcher.md) | [기획·디자인만](../workflows/planning-design.md) | [리서치](../capabilities/research.md) |
| UX·화면·토큰 | [UX·UI](../roles/designer.md) | [기획·디자인만](../workflows/planning-design.md) | [디자인](../capabilities/design.md) |
| 기술 선택·계약 | [기술 설계](../roles/architect.md) | [기획·디자인만](../workflows/planning-design.md) | [아키텍처](../capabilities/architecture.md) |
| 비평·코드 리뷰·QA | [독립 리뷰·QA](../roles/reviewer.md) | [기능 추가](../workflows/feature.md)의 검증 단계 | [독립 리뷰](../capabilities/review.md), [검증](../capabilities/verification.md) |
| 출시 준비·운영 인계 | [기획·진행](../roles/coordinator.md) + 해당 책임자 | 현재 워크플로의 인계 단계 | [출시 준비](../capabilities/release.md) |

템플릿은 [PROJECT](../templates/PROJECT.md), [RESEARCH](../templates/RESEARCH.md), [DESIGN](../templates/DESIGN.md), [TECH_PLAN](../templates/TECH_PLAN.md), [TASK](../templates/TASK.md), [REVIEW_PACKET](../templates/REVIEW_PACKET.md), [REVIEW](../templates/REVIEW.md), [HANDOFF](../templates/HANDOFF.md) 중 필요한 것만 사용한다.
