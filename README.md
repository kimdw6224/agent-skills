# Agent Skills

기획·리서치·작문·게임 서사·영상 제작·한국 공공데이터·UI·Android 작업을 위한 **한국어 중심 Agent Skills 21개**입니다. 독립적으로 작성한 지침과 공개 저장소에서 선별·보정한 스킬을 함께 제공합니다.

각 스킬은 `skills/<name>/SKILL.md`에서 시작합니다. 필요한 참고 자료와 실행 도구는 같은 폴더에 있습니다. 고정된 승인·토론 인원·반복 리뷰보다 요청 범위에 맞는 작업과 실제 결과 확인을 우선하도록 구성했습니다.

## 설치

[Skills CLI](https://github.com/vercel-labs/skills)를 쓰면 필요한 스킬만 선택할 수 있습니다. 현재 CLI는 Node.js 22.20 이상이 필요합니다.

```sh
npx skills add kimdw6224/agent-skills --skill research-brief
npx skills add kimdw6224/agent-skills --skill product-plan --skill evidence-check
```

프로젝트 밖에서도 사용하려면 명령에 `-g`를 추가합니다. 전체 설치가 필요하면 스킬 이름을 생략하고 설치 화면에서 선택하세요. 기존의 같은 이름 스킬을 수정해 사용 중이라면 설치 도구의 교체 동작을 확인하세요.

수동 설치는 원하는 `skills/<name>` 폴더를 통째로 사용하는 에이전트의 스킬 디렉터리에 복사하면 됩니다. `references/`, `scripts/`, 라이선스 파일도 함께 가져와야 합니다. 실제 호출과 목록 갱신 방식은 사용하는 에이전트에 따릅니다.

## 스킬 목록

| 분야 | 스킬 | 용도 |
|---|---|---|
| 기획 | [product-plan](skills/product-plan/SKILL.md) | 사용자 문제·가치·MVP·검증 실험·PRD |
| 기획 | [debate](skills/debate/SKILL.md) | 셀프 인터뷰·독립 제안·교차 반론·수정안 |
| 리서치 | [research-brief](skills/research-brief/SKILL.md) | 웹·시장·커뮤니티·학술 자료 조사와 비교 |
| 근거 검증 | [evidence-check](skills/evidence-check/SKILL.md) | 기존 주장·수치·인용과 원출처 대조 |
| 작문 | [fiction-prose](skills/fiction-prose/SKILL.md) | 소설의 시점·내면·묘사·서술거리·문장 리듬 |
| 작문 | [nonfiction-writing](skills/nonfiction-writing/SKILL.md) | 에세이·칼럼·설명문·리포트 구성과 개정 |
| 게임 | [game-narrative](skills/game-narrative/SKILL.md) | 선택·분기·퀘스트·발견과 상태 변화 |
| 디자인 조사 | [reference-analysis](skills/reference-analysis/SKILL.md) | 제공된 화면에서 디자인 규칙과 사용자 흐름 추출 |
| 영상 | [video-plan](skills/video-plan/SKILL.md) | 목표·대상·음성과 화면·분량·제작 전달 |
| 영상 | [video-storyboard](skills/video-storyboard/SKILL.md) | 샷·콘티·인물·공간·소품의 연속성 |
| 영상 | [video-editing](skills/video-editing/SKILL.md) | 실제 컷·합치기·자막·음량·화면비·파일 출력 |
| 한국 공공데이터 | [government-support-survey](skills/government-support-survey/SKILL.md) | 정부지원 공고 수집·조건 대조·공식 공고 확인 |
| 한국 공공데이터 | [kosis-stats](skills/kosis-stats/SKILL.md) | KOSIS 공식 통계표·메타데이터·수치 조회 |
| 한국 법령 | [korean-law-search](skills/korean-law-search/SKILL.md) | 법령·조문·판례·유권해석·자치법규 조회 |
| 한국어 도구 | [korean-character-count](skills/korean-character-count/SKILL.md) | 글자·공백 제외 글자·줄·UTF-8/NEIS 방식 바이트 계산 |
| UI | [ui-polish](skills/ui-polish/SKILL.md) | 기존 UI 품질·접근성·반응형·상태 개선과 선택형 검사기 |
| Android | [anr-audit-and-fix](skills/anr-audit-and-fix/SKILL.md) | ANR 위험과 실제 스택 덤프 진단 |
| Android | [android-permissions-security](skills/android-permissions-security/SKILL.md) | 권한·IPC·컴포넌트 보안 검토 |
| Android | [r8-analyzer](skills/r8-analyzer/SKILL.md) | keep 규칙·앱 최적화 설정 분석 |
| Android | [jetpack-compose-performance](skills/jetpack-compose-performance/SKILL.md) | Compose UI 성능 분석과 개선 |
| Android | [edge-to-edge](skills/edge-to-edge/SKILL.md) | 시스템 바·키보드·화면 inset 처리 |

## 실행 환경과 데이터 경로

대부분은 지침만으로 사용할 수 있습니다. 필요한 전문 스킬이 이미 있을 때 선택적으로 연결하며, 모든 스킬을 연쇄 실행하는 구성이 아닙니다.

| 스킬 | 필요한 환경과 범위 |
|---|---|
| `video-editing` | Python 3.10+, 로컬 FFmpeg/ffprobe. 기본 도구는 Python 표준 라이브러리만 사용합니다. 전사는 선택 기능이며 ASR 엔진·모델은 포함하지 않습니다. |
| `korean-character-count` | Node.js 18+와 `Intl.Segmenter`. 로컬 계산이며 원문을 외부로 보내지 않습니다. 설치 CLI의 Node 요구사항과는 별개입니다. |
| `government-support-survey` | Python 3와 공개 조회 프록시. 소스·검색어·페이지 조건을 운영자 서버로 보냅니다. 사업 조건 대조는 로컬에서 합니다. |
| `kosis-stats` | Python 3.9+. 일반 조회는 공개 프록시, 직접 조회·대용량 조회는 별도 KOSIS 키가 필요합니다. |
| `korean-law-search` | HTTP 클라이언트. 기본 공개 프록시를 거쳐 법제처 데이터를 조회하며, 실패 시 공식 공개 원문을 확인할 수 있습니다. |
| `ui-polish` | 지침은 플랫폼과 무관하게 활용할 수 있습니다. 동봉된 선택형 detector는 **Windows x64** 엔진 0.1.17과 Python을 사용합니다. |
| Android 스킬 | 분석에는 대상 프로젝트·로그가 필요합니다. 빌드·기기 검사는 실제 프로젝트의 도구와 환경이 있어야 가능합니다. |

공개 프록시 기본 주소는 `https://k-skill-proxy.nomadamas.org`입니다. 운영·가용성은 이 저장소와 별개이며, 검색에 필요한 최소 조건만 전달하세요. API 키·사용자 문서·시크릿은 이 저장소에 포함하지 않습니다.

`ui-polish`의 Windows 엔진은 원본 릴리스 바이너리와 라이선스를 함께 보존했습니다. `scripts/detect.py`는 detect 명령만 호출하고 하위 프로세스의 텔레메트리를 끕니다. 자동 훅·라이브 서버·스타일 추첨·자동 갱신을 설치하거나 실행하지 않습니다. 정적 HTML 검사와 TSX/CSS 부분 분석은 실제 화면·접근성·성능 시험을 대체하지 않습니다.

`r8-analyzer`는 원본의 누락된 스크립트를 존재한다고 가정하지 않습니다. 작동하는 정량 분석 도구가 없으면 소스 근거에 따른 휴리스틱 분석으로 전환하고 측정하지 않은 수치는 보고하지 않습니다.

## 사용 예

- “이 아이디어를 사용자 문제와 MVP, 검증 실험으로 구체화해줘.”
- “이 주장과 인용이 원문에서 뒷받침되는지 확인해줘.”
- “이 소설 장면의 시점과 내면 서술을 다듬어줘.”
- “장면마다 같은 방과 인물·소품 상태가 이어지는 콘티를 만들어줘.”
- “이 파일에 한글 자막을 넣고 세로 영상으로 출력해줘.”
- “우리 조건에 맞는 정부지원 공고를 찾고 공식 모집 요건과 대조해줘.”
- “기존 UI를 유지하면서 긴 한글 문구와 빈 데이터에서 깨지는 부분을 고쳐줘.”

스킬 사용은 외부 게시·발송·제출·결제의 승인을 대신하지 않습니다. 실제 작업은 사용자가 요청한 범위와 에이전트의 권한 안에서 수행해야 합니다.

## 라이선스와 출처

독립 작성한 지침과 이 저장소의 패키징은 [루트 MIT 라이선스](LICENSE)를 따릅니다. **제3자에서 가져오거나 개작한 파일에는 각 폴더의 원본 라이선스·NOTICE가 우선합니다.** 저장소 전체가 일괄 MIT인 것은 아닙니다. Android 5개와 Impeccable 기반 구성에는 Apache-2.0 자료가 포함됩니다.

원저작자, 고정 커밋, 유지한 고지는 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md)에 정리했습니다. 스킬별 참고 출처도 해당 SKILL.md와 참조 문서에 남아 있습니다.
