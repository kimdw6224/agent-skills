---
name: korean-character-count
description: 한국어·영문·이모지가 섞인 텍스트의 글자 수, 공백 제외 글자 수, 줄 수와 UTF-8·NEIS 방식 바이트를 로컬 코드로 계산한다. 지원서·자기소개서·입력 폼의 분량 확인에 사용하며 문장 윤문이나 일반 글쓰기에 자동 적용하지 않는다.
license: MIT
metadata:
  category: writing
  locale: ko-KR
  phase: v1
---

# 한국어 글자 수와 바이트 계산

텍스트를 눈대중으로 세지 않고 함께 설치된 [계산 스크립트](scripts/korean_character_count.js)로 측정한다. Node.js 18+가 필요하며 외부 패키지·API·프록시를 사용하지 않는다. k-skill CLI나 전체 갱신 명령도 필요 없다.

## 실행

현재 SKILL.md가 있는 폴더를 `$skillDir`로 정한다. 경로가 확인된 실제 `node`로 실행한다.

```powershell
node (Join-Path $skillDir 'scripts/korean_character_count.js') --file 'C:\work\essay.txt' --profile default --format json
node (Join-Path $skillDir 'scripts/korean_character_count.js') --text '가나다🙂' --format text
```

- 입력은 `--text`, `--file`, `--stdin` 중 하나만 고른다. 비공개·긴 내용은 명령행 인자 대신 UTF-8 파일이나 정확한 STDIN 바이트로 전달한다.
- 원문을 trim·정규화·재작성하지 않는다. 파일의 BOM, 마지막 개행, 앞뒤 공백도 원문에 있으면 계산에 포함될 수 있다. PowerShell 파이프가 추가하는 개행이나 인코딩 변환을 피하려면 `--file`을 우선한다.
- 반환된 `counts`와 `contract`를 기준으로 수치를 보고한다. 실패·빈 출력·파싱 오류를 0자로 처리하지 않는다.

## 계산 기준

| 항목 | 기준 |
|---|---|
| `characters` | `Intl.Segmenter('ko', { granularity: 'grapheme' })`의 문자 묶음 수. 공백·줄바꿈 포함 |
| `characters_without_whitespace` | 스크립트의 공백 제외 문자 묶음 수 |
| `code_points` / `utf16_code_units` | 코드 포인트·UTF-16 코드 단위 수. grapheme 수와 다를 수 있음 |
| `lines` | 빈 문자열은 0. 그 외 줄바꿈 수 + 1. CRLF는 한 번, LF·CR·U+2028·U+2029도 각각 한 번 |
| `bytes_utf8` | 실제 UTF-8 인코딩 바이트 수 |
| `bytes_neis` | 이 도구의 NEIS 호환 계산: 한글 묶음 3B, ASCII 묶음 1B, 개행 시퀀스 2B, 그 외 UTF-8 바이트 |
| `bytes` | 선택한 `--profile default` 또는 `--profile neis`의 바이트 수 |

기본 프로필은 `default`다. NEIS/학교생활기록부 방식이 요청될 때만 `neis`를 사용한다. 제출처의 계산기가 코드 단위·개행·공백을 다르게 셀 수 있으므로 이 도구의 결과를 모든 사이트와 같다고 보장하지 않는다. 제출처가 명시한 계약이나 실제 입력창 결과가 있으면 그것과 대조한다.

## 전달

요청한 글자 수·공백 제외 수·줄 수·바이트와 적용 기준을 간단히 알린다. 명확한 상한이 있으면 계산값이 상한 이내인지 판단한다. '정확히 1000자'에 임의 오차를 허용하거나, 계산만 요청받고 글을 바꾸지 않는다. 글을 수정한 경우 최종 텍스트를 다시 계산한다.

## 출처

[NomaDamas/k-skill](https://github.com/NomaDamas/k-skill/tree/283388095e2b1a784b6f5c04bed570174f45edf4/korean-character-count)의 실행 코드를 보존하고 instruction을 독립 지침으로 정리했다. [MIT LICENSE](LICENSE)를 따른다. 기존 테스트는 로컬 설치 경로에 맞춘 import만 보정해 `tests/`에 보존했다.
