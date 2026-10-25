---
name: r8-analyzer
description: Analyzes Android build files and R8 keep rules to identify redundancies,
  broad package-wide rules, and rules that subsume library consumer keep rules. Use
  when developers want to optimize their app's size, remove redundant or overly broad
  keep rules, or troubleshoot Proguard configurations.
license: Complete terms in LICENSE.txt
metadata:
  author: Google LLC
  last-updated: '2026-09-22'
  keywords:
  - R8
  - proguard
  - keep rules
  - app size
  - optimization
---

> Local adaptation (2026-10-24) of [android/skills at 4ebabf2](https://github.com/android/skills/tree/4ebabf2b0fd6c04b7150023c8b612f80592a6226/performance/r8-analyzer): corrected missing-tool assumptions, platform/module paths, and reporting provenance. Original references are preserved under the accompanying Apache-2.0 license.

## Step 1. Setup and configuration check

- Inspect `build.gradle`, `build.gradle.kts`, and `gradle.properties`.
- Use [references/CONFIGURATION.md](references/CONFIGURATION.md) to identify missing optimizations.
- **AGP** : If version is lower than 9.0, suggest migration to 9.0 for [build-time performance improvement](references/android/topic/performance/app-optimization/enable-app-optimization.md).
- **Full Mode** : Verify `android.enableR8.fullMode=false` is removed from gradle.properties.

## Step 2. Analysis path selection

- Inspect `build.gradle`, `build.gradle.kts`, and `gradle.properties` and
  `libs.versions.toml` to get the AGP and R8 versions.
- Identify the actual application module, release variant, and available Gradle tasks. Run the project's wrapper from its root (`.\gradlew.bat` in PowerShell, `./gradlew` in a POSIX shell); `:app` and `release` below are examples.
- This upstream snapshot does **not** include `scripts/convert_pb_to_json.py` or `scripts/analyze.py`. [references/CONFIGURATION-ANALYZER.md](references/CONFIGURATION-ANALYZER.md) contains inline examples, not ready-to-run helpers; its converter has an indentation error and its bindings require a compatible protobuf runtime (generated for 6.33.4). Do not invoke nonexistent paths or treat the examples as tested tools.
- Select a quantitative path only when the matching task/build, a working converter and analyzer, and compatible Python/protobuf are available. Otherwise use Path C and state the missing prerequisite; do not upgrade AGP/R8 or install dependencies merely to force quantitative analysis.

- **If AGP \>= 9.3.0** : Proceed to **Path A (Standalone Task)**.

- **If AGP \< 9.3.0 and R8 \>= 9.3.7-dev** : Proceed to **Path B (Quantitative)**.

- If none of the conditions are met, proceed to **Path C (Heuristic)**.

### Path A: Standalone Gradle task (AGP \>= 9.3.0)

- **Step 1: Run standalone task** : When present, run the actual module/variant's task (for example, `.\gradlew.bat :app:analyzeReleaseR8Config` on Windows). Wait for completion and check its exit code.
- **Step 2: Locate and convert** : Locate the report from this run (example: `app/build/reports/r8/r8-config-analyzer-release.pb`). Use the verified converter's actual path and arguments, not a presumed skill installation path.
- **Step 3: Analyze** : Use the available analyzer and record its actual output path. Confirm successful conversion and nonempty, current analysis data before reporting scores or rule impacts. If any prerequisite fails, report the reason and continue with Path C.

### Path B: Quantitative data generation (R8 \>= 9.3.7-dev and AGP \< 9.3.0)

- **Step 1: Check requirements** : Confirm the effective R8 version, an R8-enabled build, and working conversion/analysis tooling before starting a build.
- **Step 2: Generate and analyze** : Use the configuration-analyzer approach in [references/CONFIGURATION-ANALYZER.md](references/CONFIGURATION-ANALYZER.md), adapting commands to the actual shell, module, and variant. Use a fresh, task-owned output directory; do not follow the reference's blanket deletion or history-overwrite commands on existing artifacts.
- **Step 3: Analyze** : The inline example writes `tmp/r8analysis/analysis_result.txt`, not `tmp/keepradius/analysis_result.txt`. Read the actual verified output. Scores and per-rule impacts are separate steps in the reference; report only results actually produced. If tooling or valid data is unavailable, use Path C.

### Path C: Heuristic evaluation and recommendation

*(Use when versions, tooling, build access, or valid current outputs prevent quantitative analysis.)*

- **Step 1: Manual evaluation** : Inspect `proguard-rules.pro`.
- **Step 2: Library check** : Compare rules against [references/REDUNDANT-RULES.md](references/REDUNDANT-RULES.md). Suggest **Remove** for bundled rules.
- **Step 3: Custom rule check** : Use [references/KEEP-RULES-IMPACT-HIERARCHY.md](references/KEEP-RULES-IMPACT-HIERARCHY.md) and [references/REFLECTION-GUIDE.md](references/REFLECTION-GUIDE.md) to prioritize and evaluate. Suggest **Refine** for broad rules (for example, package-wide).
- **Step 4: Validation** : Suggest Macrobenchmark tests using [UI Automator](references/android/training/testing/other-components/ui-automator.md) for any proposed changes. Proceed to Step 3.

## Step 3. Report generation

- **Format** : Use [references/REPORT_FORMAT.md](references/REPORT_FORMAT.md), prefaced by a brief analysis-basis statement distinguishing measured results from heuristic findings and noting any unavailable tooling.
- **Input** : For Paths A/B, take metrics only from the successful current run's verified outputs, recording their location. For Path C, cite source/configuration evidence; omit numeric scores, percentages, impact counts, and historical comparisons that were not measured. Never fill template placeholders with estimates.
- **Output** : Return the Markdown report without conversational filler. Omit unsupported or irrelevant sections. The template's scores describe constraint coverage, not measured APK-size savings or guaranteed removal of code.

## Constraints

- **Strict output limit**: The final output MUST strictly be the Markdown report and nothing else.
- **No source changes**: Research and suggest only; do not edit project source, keep rules, dependencies, or build configuration. Quantitative analysis may generate build/report artifacts within the requested analysis scope.
- **No redundancy**: Do not explain R8 benefits or reference skill internal files in the report.
- **Focus**: Omit sections (for example, Subsumed Rules, Configuration) if no issues or items are found.
