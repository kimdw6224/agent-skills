---
name: kosis-stats
description: KOSIS(국가통계포털) Open API로 한국 공식 통계표를 검색하고 메타데이터·수치·통계설명·주요지표를 조회한다. 인구·가구·물가·고용 등 공식 통계 수치와 그 출처가 필요할 때 사용한다. 분석·시각화·보고서 작성 자체, 실시간 시세, 통계 등록·수정에는 적용하지 않는다.
license: MIT
metadata:
  category: data
  locale: ko-KR
  phase: v1
---

# KOSIS 통계 조회

국가데이터처(구 통계청)의 KOSIS Open API를 로컬 헬퍼 `scripts/run_kosis_stats.py`로 조회한다. **조회 전용**이며 사용자별 통계자료(`userStatsId`) 등록, 데이터 수정, KOSIS 웹 자동화는 하지 않는다.

출처: [NomaDamas/k-skill](https://github.com/NomaDamas/k-skill) `kosis-stats`, commit `283388095e2b1a784b6f5c04bed570174f45edf4`, MIT 라이선스(`LICENSE`). k-skill CLI(`npx @nomadamas/k-skill`)의 `instruct`·`exec`·`read`·`update`는 쓰지 않는다. 특히 `update`는 전체 스킬을 전역 설치·갱신하므로 실행하지 않는다.

## 실행 환경

- Python 3.9+ 표준 라이브러리만 사용한다. 헬퍼 경로는 이 SKILL.md 폴더 기준 `scripts/run_kosis_stats.py`다.
- Windows에서는 실제 사용 가능한 인터프리터를 확인하고 한글 출력을 위해 `-X utf8`을 붙인다. 아래 예시는 `py -3`이 사용 가능한 경우다. Store 실행 별칭을 정상 Python으로 가정하지 않는다.

```powershell
# $skillDir은 이 SKILL.md가 있는 폴더 경로입니다.
$kosisScript = Join-Path $skillDir 'scripts/run_kosis_stats.py'
py -3 -X utf8 $kosisScript search --query "1인 가구" --text
```

- `--json`(기본)·`--text`·`--dry-run`·`--timeout N`·`--proxy-base-url`·`--direct`는 **서브커맨드 뒤**에 둔다.

## 일반 조회와 개인 키 조회 구분

| 경로 | 대상 | 키 |
|---|---|---|
| hosted proxy(기본) | `search`, `meta`, `data`, `list`, `explain`, `indicator` | 필요 없음. 기본 `https://k-skill-proxy.nomadamas.org`가 서버 쪽에서 KOSIS 키를 주입한다. |
| 직접 호출 | `bigdata` 전부, 위 명령에 `--direct`를 붙인 경우 | 개인 KOSIS 키 `KSKILL_KOSIS_API_KEY` 필요 |

- hosted proxy는 제3자 운영 서버이므로 검색어·조회 조건이 그 서버를 거친다. 다른 프록시는 `KSKILL_PROXY_BASE_URL` 또는 `--proxy-base-url`로 지정한다. 이 값을 `off`·`false`·`0`·`disable(d)`·`none`으로 두면 proxy 경로가 종료되므로 `--direct`를 써야 한다.
- 직접 호출 키는 헬퍼가 환경변수 `KSKILL_KOSIS_API_KEY` → `~/.config/k-skill/secrets.env`(Windows: `%USERPROFILE%\.config\k-skill\secrets.env`, `KSKILL_KOSIS_API_KEY=...` 한 줄) 순서로 읽는다. 둘 다 없으면 발급 안내와 함께 종료코드 1로 끝난다.
- 키가 없으면 사용자에게 https://kosis.kr/openapi/ 에서 무료 발급 후 위 둘 중 하나에 **직접** 설정하도록 안내한다. 키를 채팅으로 받거나, 명령 인자·로그·파일 내용으로 출력하거나, 대신 저장하지 않는다. `--dry-run`은 키 자리를 `<PROXY>` 또는 `<DRY-RUN>`으로 바꿔 출력한다.
- 직접 호출 키나 프록시를 사용할 수 없으면 KOSIS의 공식 공개 화면에서 확인할 수 있다. 경로 변경과 확보 범위를 밝히며 비공식 수치를 KOSIS 응답처럼 제시하지 않는다.

## 서브커맨드

- `search --query "키워드" [--result-count 1-5000(기본 20)] [--start-count N(기본 1)]`: 통계표 검색. `[ORG_ID/TBL_ID]`를 얻는다.
- `meta --table-id ID [--org-id 101] [--meta-type TBL|ITM|OBJ(기본 TBL)]`: 표 명칭·항목·분류·단위.
- `data --table-id ID --prd-se M|Q|S|Y|F|IR --start 기간 --end 기간 [--org-id 101] [--itm-id ALL] [--obj-l 1=ALL ...]`: 수치 조회. `--obj-l`은 반복 가능하며 생략하면 `1=ALL`만 보낸다.
- `explain --org-id 101 --table-id ID` 또는 `--stat-id ID`, `[--meta-itm All|statsPeriod|writingPurps|...]`: 통계설명. 조사주기만 볼 때는 `--meta-itm statsPeriod`.
- `list --vw-cd MT_ZTITLE|MT_OTITLE|MT_RTITLE|MT_BUKHAN|... [--parent-id LIST_ID]`: 통계목록 트리(`MT_ZTITLE` 국내주제별, `MT_OTITLE` 기관별, `MT_RTITLE` 국제, `MT_BUKHAN` 북한).
- `indicator --jipyo-id ID [--service 1|2|3(기본 1)] [--page-no N] [--num-of-rows N]`: 주요지표 개념(1)·산정방법·출처(2)·전체(3).
- `bigdata --user-stats-id ID [--format json|sdmx|csv] [--prd-se ...] [--new-est-prd-cnt N]`: 40,000셀 초과 자료. KOSIS 웹에서 미리 등록한 본인 `userStatsId`와 개인 키가 필요하다. 미등록이면 등록 방법만 안내하고 멈춘다. `xls`는 지원하지 않는다.

## 조회 순서

1. 질문을 짧은 한국어 키워드로 바꿔 `search`하고, 표 이름·기관·수록 범위로 후보를 고른다.
2. `meta`로 항목·분류 코드·단위를 확인한다. 분류가 OBJ 메타에 없고 ITM 안에 들어 있는 표가 많으므로 `--meta-type ITM --json`도 본다.
3. **`--prd-se`를 먼저 확정한다.** 검색 메타데이터의 주기 코드를 조회 API 코드로 그대로 옮기지 말고 `explain --meta-itm statsPeriod`나 공식 통계표에서 수록주기를 확인한다. 과거 표의 코드·분류값을 새 표에 복사하지 않는다. 주기가 불명확하면 근거가 있는 후보만 좁은 기간·최소 분류로 확인하고, 성공한 뒤 다른 코드를 계속 시험하지 않는다.

4. 작은 슬라이스를 먼저 받은 뒤 범위를 넓힌다. 기간 형식은 `M` `YYYYMM`, `Q` `YYYYQQ`, `S` `YYYYHH`, `Y`·`F` `YYYY`, `IR` `YYYY` 또는 `YYYYMMDD`다. 행정구역 `C1`은 보통 시도 2자리(`11` 서울), 시군구 5자리다.
5. 결과의 통계표 ID·기간·분류·단위가 질문과 맞는지 대조한다. `UNIT_NM`이 비어 있으면 헬퍼가 `unit=(KOSIS 응답에 UNIT_NM 미포함)`으로 표시하므로 `meta`나 KOSIS 화면에서 단위를 확인한 뒤 수치를 제시한다.
6. 답변에 `org_id`/`tbl_id`, 기간, 분류 조건, 단위, 원 endpoint(`--text` 출력의 `source:`)를 적는다.

## 결과 없음과 오류 구분

- **종료코드 0 + 빈 결과**: 요청은 성공했지만 행이 없다. `--text`는 "조회 결과가 없습니다"·"데이터가 없습니다"처럼 안내한다. 조건을 조정해 다시 찾는다.
- **종료코드 2 + `KOSIS error 30`**: KOSIS가 결과 없음을 반환했다. `data`면 먼저 `--prd-se` 오지정, `search`면 키워드, `meta`면 메타 타입을 의심한다.
- **종료코드 2 + 다른 KOSIS 코드**: `20` 필수 분류 누락(ITM/OBJ 메타로 필요한 `--obj-l` 차원을 모두 지정), `21` ID·기간 형식 오류, `31`/`41` 40,000셀 초과(기간·분류를 나누거나 `bigdata`), `40` 분당 1,000건 한도(대기), `50` 서버 오류(잠시 후 재시도), `10`/`11` 키 누락·만료 또는 `bigdata`에서 본인 것이 아닌 `userStatsId`.
- **종료코드 2 + `HTTP 503 ... KOSIS API 키가 설정되어 있지 않습니다`, `k-skill-proxy 서버가 응답하지 않습니다`, `network error`**: 통계가 없는 것이 아니라 proxy·네트워크 문제다. 결과 없음으로 보고하지 않는다. 개인 키가 있으면 `--direct`로 대체할 수 있다.
- **종료코드 1**: 개인 키 누락. **종료코드 2 + usage 메시지**: 인자 형식 오류.

헬퍼가 KOSIS의 비표준 JSON(따옴표 없는 키)을 자동 보정한다. 인증키 발급, 호출 한도, endpoint 원형, 에러 코드 전체, 오류별 회복 예시는 [references/kosis-openapi-guide.md](references/kosis-openapi-guide.md)를 필요할 때 읽는다.
