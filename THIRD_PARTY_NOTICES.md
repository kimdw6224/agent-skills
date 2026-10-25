# Third-party notices and provenance

이 저장소에는 독립 작성 지침과 제3자 자료를 선별·개작한 스킬이 함께 있습니다. 루트 MIT는 독립 작성한 부분과 패키징에 적용합니다. 아래 제3자 파일의 기존 저작권·라이선스·NOTICE는 그대로 유지하며, 해당 자료에는 그 조건이 우선합니다.

## 독립 작성한 지침

`product-plan`, `research-brief`, `evidence-check`, `debate`, `fiction-prose`, `nonfiction-writing`, `reference-analysis`는 작법·설계 개념을 참고해 별도로 작성했습니다. 참고한 자료는 각 스킬에 기재돼 있습니다. 이 그룹은 원본 저장소의 코드·설치 도구를 실행 의존성으로 요구하지 않습니다.

## 포함하거나 개작한 제3자 자료

| 스킬 | 원저장소와 고정 버전 | 적용 고지 |
|---|---|---|
| `game-narrative` | [mattstruble/skills](https://github.com/mattstruble/skills/tree/6f5f38bfdb1591b4e771cff60cc32c744d56f634) | Matt Struble의 MIT [LICENSE](skills/game-narrative/LICENSE) |
| `video-plan` | [social-media-skills/skills](https://github.com/social-media-skills/skills/tree/f28cef2b7067ec64e79c9d85421c022c06659e03/skills/scripting-and-storyboarding) | Frank Heijdenrijk의 MIT [LICENSE](skills/video-plan/LICENSE) |
| `video-storyboard` | [zenstory-ai/drama-skills](https://github.com/zenstory-ai/drama-skills/tree/fdb7b7c58017e3eae64eca382c2a85ede368dab0) | drama-skills contributors의 MIT [LICENSE](skills/video-storyboard/LICENSE) |
| `video-editing` | [kajisho5/ffmpeg-skill](https://github.com/kajisho5/ffmpeg-skill/tree/2d9f5ac05f33a0cb9cf74b1707d816bbdc0cdeaf) | kajisho5의 MIT [LICENSE](skills/video-editing/LICENSE). 실행 도구·기술 참조 포함 |
| `video-editing` 편집 연출 개념 | [kevinbadi/open-edits](https://github.com/kevinbadi/open-edits/tree/7fbd74651ea945711792b207e8a9f0a167f78132) | Kevin Bahrabadi의 MIT [LICENSE.open-edits](skills/video-editing/LICENSE.open-edits). 원본 영상·음악·폰트·렌더러는 포함하지 않음 |
| `government-support-survey`, `kosis-stats`, `korean-law-search`, `korean-character-count` | [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill/tree/283388095e2b1a784b6f5c04bed570174f45edf4) | 각 폴더의 MIT LICENSE 유지. 본문을 독립 실행 지침으로 정리하고 CLI 전체 설치·갱신 의존 제거 |
| `government-support-survey` 조사 로직 | [djfksjd/ir-search](https://github.com/djfksjd/ir-search) | Copyright (c) 2026 ir-search contributors. MIT 및 데이터 재배포 범위는 [NOTICE](skills/government-support-survey/references/NOTICE.md) 참조 |
| Android 5개 | [android/skills](https://github.com/android/skills/tree/4ebabf2b0fd6c04b7150023c8b612f80592a6226) | Google LLC의 Apache-2.0. 각 스킬의 `LICENSE.txt` 유지 |
| `ui-polish` 지침과 detector | [pbakaus/impeccable](https://github.com/pbakaus/impeccable/tree/936867543ac2576920d663cc9803597f6044f3ac) | [LICENSE.impeccable](skills/ui-polish/LICENSE.impeccable), [NOTICE.impeccable.md](skills/ui-polish/NOTICE.impeccable.md). NOTICE 안의 ehmo/platform-design-skills MIT attribution도 유지 |

Android 5개는 `anr-audit-and-fix`, `android-permissions-security`, `r8-analyzer`, `jetpack-compose-performance`, `edge-to-edge`입니다. 로컬 경로·누락 도구·불필요한 작업 확장을 보정한 부분은 각 스킬 본문에 표시했습니다.

`video-editing/scripts/loudness.py`는 음량 정규화 후 필터 결과가 입력 오디오 길이를 넘지 않게 보정했습니다. 나머지 도구는 원본을 유지합니다. `korean-character-count`의 원본 테스트는 배포 디렉터리에 맞게 import 경로만 바꿨습니다.

`ui-polish`에 동봉된 Windows x64 엔진은 [engine-v0.1.17](https://github.com/pbakaus/impeccable/releases/tag/engine-v0.1.17)의 원본 바이너리입니다.

```text
asset: impeccable-windows-x64.exe
size: 20285328 bytes
sha256: edb62bff4ee48dc59b6b34f5788b9052ff0efc73019a4e4fc3b1067a4ebf94ee
```

Python 진입점 `scripts/detect.py`는 이 저장소의 선택 실행 어댑터이며, 원본 설치 도구·자동 훅·라이브 서버·스타일 추첨 흐름을 실행하지 않습니다.

## 데이터와 외부 서비스

정부 포털·통계·법령 원문과 API 응답에는 각 제공기관의 조건이 적용됩니다. 코드의 MIT 또는 Apache-2.0 라이선스가 외부 데이터·첨부 문서·상표·영상·음악의 이용권을 뜻하지는 않습니다. 이 저장소는 사용자 자료나 공고 본문을 미러링하지 않습니다.

공개 조회 프록시와 upstream 서비스의 운영·가용성은 해당 운영자에게 달려 있습니다. 특정 서비스의 공식 승인·보증·제휴를 주장하지 않습니다.
