# Bug Eradication Program

## Goal

Drive the repository toward **zero known reproducible unintended defects** for the selected Pokémon LEGENDS: Arceus target revision while preserving intended game rules, content, timing, encounter behavior, quest logic, and patch-era behavior.

Coverage includes crashes, hangs, softlocks, progression blockers, save/data corruption, battle-order and move logic, AI/behavior defects, invalid data, quest/event flags, field capture behavior, stealth/tool interactions, alpha Pokémon behavior, space-time distortions, outbreaks and massive mass outbreaks, ride Pokémon, crafting/inventory, map/collision, graphics/UI, audio, localization/text, performance/resource defects, update regressions, and other reproducible unintended behavior.

## Target identity gate

No binary-specific fix is verified until `config/target.json` records the exact release/region/revision and hashes of the locally supplied legal dump or extracted target. Full game images/installable packages are never committed.

## Evidence and severity

Evidence: `reported`, `probable`, `confirmed`, `not-a-bug`.
Severity: S0 critical, S1 high, S2 medium, S3 low, S4 cosmetic.

## Required lifecycle

Discovery/source citation → target/revision assignment → reproduction → expected/actual result → root cause → minimal fix → non-ROM patch/diff → positive regression test → negative regression tests → quest/field/battle compatibility checks → `verified-fixed`.

## PLA-specific version axes

Track separately when applicable:

- main story, requests, post-game, and Daybreak content;
- field zones and base camps;
- wild Pokémon alert/attack/capture state;
- alpha Pokémon;
- space-time distortions;
- mass outbreaks and massive mass outbreaks;
- ride Pokémon traversal and collision;
- crafting, satchel, storage, and item use;
- strong/agile style and action-order behavior;
- region/language-specific text and data behavior;
- original release versus each supported update revision.

## Repository placement

- `manifests/bug-registry.json`: authoritative defect index.
- `analysis/bugs/`: reproduction and root-cause reports.
- `patches/bugs/`: diffs, patch material, address/symbol maps.
- `logs/bugs/`: execution and regression logs.
- `artifacts/bugs/`: retained non-ROM evidence.
- `tools/`: validators and automation.

## Completion rule

A target revision is clean only when every known registry item is `verified-fixed` or `not-a-bug`, validation passes, and no unresolved report or regression remains.
