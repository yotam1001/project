"""Legacy generation entry point, intentionally disabled.

The current proposal is maintained in native Google Docs. The former generator
created a stale laptop/generic-camera architecture and must not overwrite exports.
"""
from pathlib import Path

if __name__ == "__main__":
    raise SystemExit("Edit/export the current Google Docs proposal instead. See " + str(Path(__file__).with_name("README.md")))
