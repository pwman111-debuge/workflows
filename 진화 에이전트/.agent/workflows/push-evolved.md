---
version: "2.0 (Evolved)"
description: "공유 메모리 상태를 감지하여 자동 실행되는 푸시 워크플로우"
---

# 📤 보고서 Push v2.0 - 연계형 워크플로우

이 워크플로우는 상위 워크플로우에서 전달받은 상태 값을 바탕으로 작업을 수행합니다.

## 1. 실행 트리거 (Communication Check)
- `.agent/memory/state.json` 파일의 `next_action` 값이 "trigger_push"인 지 확인합니다.
- 값에 따라 사용자에게 "제네시스의 분석 결과를 GitHub로 Push하겠습니다"라고 보고합니다.

## 2. 자동 검증 (Automated Validation)
- `state.json`의 `last_artifact` 경로에 있는 파일의 프론트매터를 자동 검사합니다.
  - `date`, `category`, `title` 값에 따옴표(`" "`)가 모두 포함되어 있는지 확인합니다.
  - 따옴표 누락 시 자동으로 삽입하여 파일을 수정합니다.

## 3. GitHub Push 실행 (Execution)
// turbo-all
- 현재 작업 디렉토리를 Git 저장소로 확인합니다.
- 변경된 파일들을 스테이징하고, 날짜별 커밋 메시지로 커밋을 생성합니다.
- 원격 저장소(`origin/main`)로 Push를 실행합니다.

## 4. 완료 및 상태 리셋 (Finalization)
- 작업 성공 시 사용자에게 GitHub 저장소 링크를 함께 제공합니다.
- `.agent/memory/state.json`의 `status`를 "idle"로, `next_action`을 `null`로 초기화합니다.
