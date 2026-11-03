# 팀 프롬프팅 스킬 사용설명서

버전: 1.1.0 · 문서 기준일: 2026-11-03

## 1. 들어 있는 것

이미지·영상 모델별 영어 실무 매뉴얼을 읽어 자연어 요청을 프롬프트, 참조 역할, 필요한 설정으로 정리하는 7개 스킬입니다. 긴 본문을 매번 전부 읽지 않고 요청에 맞는 로컬 문서를 선택합니다. 공식 링크는 출처·업데이트 확인용입니다.

| 대상 | Codex 명시 호출 | Claude Code 명시 호출 |
|---|---|---|
| 미드저니 | `$midjourney-prompt` | `/midjourney-prompt` |
| Z-Image Turbo | `$z-image-turbo-prompt` | `/z-image-turbo-prompt` |
| MiniMax H3 R2V | `$minimax-r2v-prompt` | `/minimax-r2v-prompt` |
| Qwen Image | `$qwen-image-prompt` | `/qwen-image-prompt` |
| Krea | `$krea-prompt` | `/krea-prompt` |
| FLUX | `$flux-prompt` | `/flux-prompt` |
| Seedance R2V | `$seedance-r2v-prompt` | `/seedance-r2v-prompt` |

설치 후에는 “Qwen Image로 첫 이미지의 인물에게 두 번째 이미지의 안경을 씌우는 프롬프트를 써줘”처럼 자연어로 요청해도 자동 선택할 수 있습니다. 모델이 여러 가지로 해석되면 명시 호출을 사용하세요.

## 2. 가장 쉬운 설치: 에이전트에게 맡기기

ZIP을 압축 해제하고, 해당 폴더를 로컬 Codex 또는 Claude Code가 읽을 수 있게 지정한 뒤 다음처럼 요청합니다.

```text
이 폴더의 README.md와 USAGE_KO.md를 읽고 프롬프팅 스킬 7개를
현재 프로젝트에 설치해줘. 내가 쓰는 클라이언트에 맞는 경로를 사용하고,
이미 같은 이름의 스킬이 있으면 덮어쓰기 전에 알려줘.
설치 후 qwen-image-prompt가 보이는지 확인해줘.
```

Claude 웹/Cowork에서 ZIP을 단순 첨부하는 것은 로컬 Claude Code의 폴더 설치와 다릅니다. 웹·데스크톱 Skills 업로드 방식은 5절을 따르세요.

## 3. 수동 설치: Python이 없어도 가능

`skills` 안의 7개 폴더를 통째로 다음 대상에 복사합니다. `SKILL.md`만 복사하면 본문이 누락됩니다.

| 환경 | 현재 프로젝트에서만 | 모든 로컬 프로젝트에서 |
|---|---|---|
| Codex | `<프로젝트>/.agents/skills/` | `~/.agents/skills/` |
| Claude Code | `<프로젝트>/.claude/skills/` | `~/.claude/skills/` |

`~`는 본인의 사용자 홈입니다. Windows에서는 일반적으로 `C:\Users\본인계정`입니다.

예시 구조:
```text
프로젝트/
  .agents/skills/qwen-image-prompt/SKILL.md      ← Codex
  .agents/skills/qwen-image-prompt/references/...
```
Claude Code는 같은 구조에서 `.agents`를 `.claude`로 바꿉니다. 두 프로그램을 모두 쓰는 프로젝트는 두 위치에 각각 설치합니다. `agents/openai.yaml`은 Codex용 표시 메타데이터이며 Claude가 쓰는 핵심 진입점은 `SKILL.md`입니다.

현재 공식 Codex 문서의 권장 경로는 `.agents/skills`입니다. 구버전에서 경로가 다르면 클라이언트를 업데이트하거나 해당 버전의 공식 스킬 검색 경로를 확인하세요. 같은 이름의 스킬을 개인·프로젝트 위치에 중복 설치하면 선택이 혼동될 수 있습니다.

## 4. 설치 스크립트 사용: Python 3.8 이상, 추가 패키지 없음

아래 명령은 압축을 해제한 패키지 폴더에서 실행합니다. Windows에서 `python`이 없고 Python Launcher가 있으면 `py -3`, macOS/Linux에서는 보통 `python3`로 바꿉니다.

패키지 무결성 확인:
```powershell
python install.py --verify
```

Codex 프로젝트 설치(경로를 본인의 실제 프로젝트로 수정):
```powershell
python install.py --client codex --scope project --project "D:\TeamProject"
```

Claude Code 프로젝트 설치:
```powershell
python install.py --client claude --scope project --project "D:\TeamProject"
```

동일 프로젝트에서 두 클라이언트에 설치:
```powershell
python install.py --client both --scope project --project "D:\TeamProject"
```

개인 설치:
```powershell
python install.py --client codex --scope user
python install.py --client claude --scope user
```

Qwen과 MiniMax만 설치하거나 설치 경로만 미리 보기:
```powershell
python install.py --client codex --scope project --project "D:\TeamProject" --skills qwen-image-prompt minimax-r2v-prompt --dry-run
```

검토 후 `--dry-run`을 빼면 복사합니다. 이미 같은 이름의 스킬이 있으면 기본 동작은 중단입니다. 업데이트하려면 검토 후 `--replace`를 추가하세요. 기존 폴더는 대상 프로젝트/홈의 `.prompt-skills-backups/<시각>/<클라이언트>/`에 백업된 뒤 새 파일을 덮어씁니다. 업데이트 시 패키지에 없는 기존 추가 파일은 삭제하지 않습니다.

스크립트는 스킬 파일만 복사합니다. AI 클라이언트 설정·MCP 설정·프로젝트 지침을 자동 변경하거나 모델을 다운로드하지 않습니다.

## 5. Claude 웹·데스크톱·Cowork 사용자

`claude-upload` 폴더에 모델별 ZIP 7개를 따로 넣었습니다. Claude의 **Customize → Skills**에서 사용자 스킬 추가/업로드 기능을 이용해 필요한 모델의 ZIP을 등록하고 활성화합니다. 메뉴 문구나 제공 범위는 계정·앱 버전에 따라 다를 수 있습니다. 코드 실행 기능이 필요한 환경에서는 활성화하세요.

예: `claude-upload/qwen-image-prompt.zip`을 그대로 업로드합니다. 전체 팀 패키지 ZIP을 단일 스킬로 업로드하지 마세요. 개별 ZIP은 `qwen-image-prompt/SKILL.md`와 그 하위 참고문서가 있는 구조입니다.

웹/Cowork에서는 “qwen-image-prompt 스킬로…”처럼 이름을 포함한 자연어로 요청하세요. `/스킬명` 표는 로컬 Claude Code의 명시 호출 기준입니다. 계정 스킬 동기화·클라우드 환경은 로컬 `.claude/skills` 복사와 별도이므로 사용하는 환경의 스킬 목록에서 활성화 여부를 확인하세요.

업로드한 스킬이 프롬프트를 작성할 수 있어도, 팀원의 PC 파일이나 로컬 ComfyUI가 자동으로 연결되지는 않습니다.

## 6. 설치 확인과 첫 사용

Codex에서 `$` 스킬 목록에 이름이 보이는지 확인합니다. 보이지 않으면 프로젝트에서 새 채팅을 열거나 클라이언트를 재시작합니다. Claude Code에서는 `/` 목록 또는 `/skills`를 확인하고, 새로 만든 최상위 스킬 폴더를 인식하지 못하면 `/reload-skills` 또는 세션 재시작을 시도합니다.

먼저 실제 생성 없이 다음 요청으로 확인하면 됩니다.

Codex:
```text
$qwen-image-prompt
참조 이미지가 두 장이야. 첫 번째가 편집 원본이고 두 번째가 안경 디자인이야.
첫 번째 인물에게 안경만 씌우는 영어 프롬프트를 써줘.
인물 정체성, 배경, 자막은 유지해줘. 생성은 아직 하지 마.
```

Claude Code:
```text
/qwen-image-prompt
첫 번째 이미지를 원본, 두 번째 이미지를 안경 디자인 참조로 사용해.
안경만 추가하고 인물·배경·자막을 유지하는 영어 편집 프롬프트를 써줘.
생성은 아직 하지 마.
```

실제 참조 파일을 첨부하거나 접근 가능한 경로를 지정합니다. 두 이미지를 보지 못하는 환경에서는 실제 외형을 단정하지 않고 초안 또는 누락 입력으로 처리하는 것이 정상입니다.

일반적인 이미지 요청:
```text
$midjourney-prompt
유리로 만든 파란 새 한 마리의 제품 사진. 크림색 배경, 부드러운 측면광,
정사각형. 모델은 V8.2이고 Raw를 사용해줘.
```

참조 기반 영상 요청:
```text
$minimax-r2v-prompt
이 이미지는 캐릭터 외형 참조야. 캐릭터가 걸어와 한 번 손을 흔들고 멈춰.
카메라 고정, 배경음악 없음. 현재 선택한 H3 R2V 템플릿 기준으로 작성해줘.
```

Claude Code에서는 위 예시의 `$`를 `/`로 바꿉니다. 자연어 요청에서도 모델/버전, 원본과 참조의 순서·역할, 유지할 것, 바꿀 것, 원하는 비율·길이·소리를 알려주면 판단이 명확해집니다. 알려준 설정은 지원 여부를 확인한 뒤 사용하며, 모든 항목을 매번 작성할 필요는 없습니다.

## 7. ComfyUI 실행까지 요청할 때

**프롬프트 작성은 스킬만으로 가능하고, 실제 생성은 별도 실행 환경이 필요합니다.** 팀원 PC에 ComfyUI, 선택한 모델/인코더/VAE/필요 노드, 해당 클라이언트의 ComfyUI MCP 연결이 준비되어 있어야 합니다. 원래 환경의 서버 이름은 `comfy_local`이지만 팀원의 실제 등록 이름을 사용하면 됩니다. 이 패키지는 MCP 서버나 ComfyUI 워크플로우를 포함하지 않습니다.

```text
qwen-image-prompt 스킬을 사용해 첫 번째 이미지의 인물에게 두 번째 이미지의
안경을 씌워줘. ComfyUI MCP로 실행하고, 내가 지정한 기존 편집 워크플로우를 써줘.
원본 인물·배경·자막은 유지해줘.
```

기본 규칙은 사용자가 선택한 기존 워크플로우를 우선하고, 별도 지정이 없으면 공식 기본 템플릿을 사용하며 입력·프롬프트·노출된 파라미터를 조절하는 것입니다. 구조 변경이나 새 워크플로우 제작은 별도 요청이 필요합니다. 영상 길이·크롭·색 보정 등의 결과물 변환도 ComfyUI 안에서 재현하도록 안내합니다.

공식 템플릿의 사전검증 오류나 누락 모델이 있으면 실행 대신 정확한 제약을 설명할 수 있습니다. 사용자 지정 모델을 다른 모델로 조용히 바꾸지 않습니다. 유료 API 모델은 계정·비용 동의가 별도로 필요합니다.

팀의 공통 작업 지침으로 쓰려면 `PROJECT_INSTRUCTIONS.md`의 블록을 검토해 기존 `AGENTS.md`(Codex) 또는 `CLAUDE.md`(Claude Code)에 추가하세요. 설치 스크립트는 이 지침 파일을 건드리지 않습니다.

## 8. 내용을 직접 수정하는 방법

각 스킬의 `references/guide.md`는 목차와 분기 안내입니다. 실제 상세 내용은 `prompt-writing.md`, `image-references.md`, `parameters.md`, `editing.md` 또는 `audio.md`, `examples.md`, `troubleshooting.md`에 있습니다. 모델에 따라 `format.md`, `layout.md`, `versions.md` 같은 추가 장이 있습니다.

`sources.md`는 출처·반영 범위·확인일입니다. `parameter-snapshot.json`, `compatibility.json`, `native-node-snapshot.json`은 특정 날짜/경로의 사실 자료이며 현재 팀원 PC의 설치 상태나 최신 API 지원을 증명하지 않습니다.

버전이 바뀌면 해당 모델의 규칙과 예시를 함께 갱신하고 확인일을 기록합니다. 모든 모델 내용을 하나의 긴 SKILL.md에 합치지 않습니다. 팀원과 수정본을 공유할 때 `SKILL.md`와 `references` 폴더를 함께 전달합니다.

## 9. 문제 해결

| 증상 | 확인할 것 |
|---|---|
| 스킬이 안 보임 | 올바른 프로젝트/개인 경로, 한 단계 더 들어간 중첩 폴더, 새 세션/재로드 |
| 이름은 보이는데 내용이 짧음 | guide.md는 목차인지, references 전체를 복사했는지, 필요한 본문을 읽었는지 |
| Claude에서 `$`가 안 먹음 | 로컬 Claude Code는 `/스킬명`; 웹은 활성화 후 이름을 포함한 자연어 |
| ComfyUI 작업이 안 됨 | 스킬 설치와 MCP 연결·실행 서버·모델 설치는 별도 |
| 첨부 이미지를 못 찾음 | 해당 호스트가 읽을 수 있는 실제 파일/첨부인지; 로컬 파일 접근 여부 |
| 다른 모델 문법을 섞음 | 선택한 모델/버전과 작업 모드를 명시해 다시 요청 |
| 비율·길이 설정이 거절됨 | 현재 템플릿/노드/제공사의 실제 허용 범위와 스냅샷 차이 |
| 설치 무결성 검증 실패 | 원본 ZIP을 다시 해제; 수동 수정본은 원본과 해시가 달라짐 |

## 10. 공식 설치·사용 문서

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [Anthropic: Claude Code Skills](https://code.claude.com/docs/en/skills)
- [Anthropic: Custom Skills 만들기·패키징](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills)

공식 문서 확인일: 2026-11-03. 이 패키지는 로컬 파일 설치 및 Claude 개별 ZIP 업로드용이며, 외부 플러그인 마켓에 게시한 패키지는 아닙니다.

## 11. 1.1.0 개선 사항

상세 영어 매뉴얼은 유지하고, 단순 요청은 짧은 진입점부터 처리하도록 바꿨습니다. 일반적인 프롬프트 작성 요청에는 필요한 참조 입력 역할과 설정도 안내합니다. 사용자가 명시적으로 “본문만”을 요청하면 그 형식을 따릅니다. H3와 Seedance의 필수 문법 문서는 계속 읽습니다.

팀에서 스킬을 수정했다면 `python scripts/build_package.py --version 1.1.0`과 `python install.py --verify`로 개별 ZIP·전체 ZIP·해시를 함께 갱신합니다. 이 검증은 배포 무결성 확인이며, 생성 품질 검증은 별도의 비교 실험이 필요합니다. 대표 행동 평가 사례는 `evals/README.md`에 있습니다.
