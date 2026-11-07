#!/usr/bin/env python3
"""Create a deterministic portfolio zip with a SHA-256 manifest."""
import argparse
import hashlib
import json
import zipfile
from pathlib import Path

def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 20), b""):
            h.update(chunk)
    return h.hexdigest()

def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default="portfolio")
    ap.add_argument("--out", default="portfolio-export.zip")
    args = ap.parse_args()
    root = Path(args.root)
    if not root.exists():
        raise SystemExit(f"missing {root}")
    files = sorted(p for p in root.rglob("*") if p.is_file() and ".DS_Store" not in p.name)
    manifest = {str(p.relative_to(root)): sha256(p) for p in files}
    with zipfile.ZipFile(args.out, "w", zipfile.ZIP_DEFLATED) as z:
        for p in files:
            z.write(p, p.relative_to(root))
        z.writestr("MANIFEST.json", json.dumps(manifest, indent=2, sort_keys=True))
    print(f"{len(files)} files -> {args.out}")

if __name__ == "__main__":
    main()
