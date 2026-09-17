#!/usr/bin/env python3
import json
from pathlib import Path

REGISTRY = Path(__file__).resolve().parents[1] / "manifests" / "bug-registry.json"
REQUIRED = {"id", "title", "category", "severity", "evidence", "status", "versions", "reproduction", "expected", "actual", "root_cause", "fix", "regression_tests", "sources"}
SEVERITY = {"S0", "S1", "S2", "S3", "S4"}


def fail(message: str) -> None:
    print(f"ERROR: {message}")
    raise SystemExit(1)


def main() -> None:
    data = json.loads(REGISTRY.read_text(encoding="utf-8"))
    categories = set(data.get("categories", []))
    evidence = set(data.get("allowed_evidence", []))
    statuses = set(data.get("allowed_status", []))
    seen = set()
    for index, item in enumerate(data.get("items", [])):
        missing = REQUIRED - set(item)
        if missing:
            fail(f"item {index} missing fields: {sorted(missing)}")
        if item["id"] in seen:
            fail(f"duplicate id: {item['id']}")
        seen.add(item["id"])
        if item["category"] not in categories:
            fail(f"{item['id']}: invalid category {item['category']}")
        if item["severity"] not in SEVERITY:
            fail(f"{item['id']}: invalid severity {item['severity']}")
        if item["evidence"] not in evidence:
            fail(f"{item['id']}: invalid evidence {item['evidence']}")
        if item["status"] not in statuses:
            fail(f"{item['id']}: invalid status {item['status']}")
        if item["status"] == "verified-fixed" and not item["regression_tests"]:
            fail(f"{item['id']}: verified-fixed requires regression tests")
    print(f"OK: {len(seen)} bug-registry item(s) validated")


if __name__ == "__main__":
    main()
