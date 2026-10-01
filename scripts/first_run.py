#!/usr/bin/env python3
"""One-time, cross-conversation tutorial gate for this Codex skill."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from datetime import datetime, timezone


SKILL_NAME = "seedance-2-5-fight-director"
MARKER_NAME = "first-run-v1.json"


def marker_path(state_dir: str | None) -> Path:
    if state_dir:
        base = Path(state_dir).expanduser()
    else:
        codex_home = os.environ.get("CODEX_HOME")
        base = Path(codex_home).expanduser() if codex_home else Path.home() / ".codex"
        base = base / "skill-state" / SKILL_NAME
    return base.resolve() / MARKER_NAME


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("action", choices=("claim", "status"))
    parser.add_argument(
        "--state-dir",
        help="Override the state directory for isolated tests; do not use for normal calls.",
    )
    args = parser.parse_args()
    marker = marker_path(args.state_dir)

    if args.action == "status":
        first_run = not marker.exists()
    else:
        marker.parent.mkdir(parents=True, exist_ok=True)
        try:
            fd = os.open(marker, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        except FileExistsError:
            first_run = False
        else:
            try:
                with os.fdopen(fd, "w", encoding="utf-8") as output:
                    json.dump(
                        {"skill": SKILL_NAME, "claimed_at": datetime.now(timezone.utc).isoformat()},
                        output,
                        ensure_ascii=False,
                    )
                    output.write("\n")
            except BaseException:
                marker.unlink(missing_ok=True)
                raise
            first_run = True

    print(
        json.dumps(
            {
                "show_tutorial": first_run,
                "marker": str(marker),
                "action": args.action,
            },
            ensure_ascii=False,
        )
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
