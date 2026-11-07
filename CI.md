# CI activation

The workflow is committed as `ci/verify.yml` rather than `.github/workflows/ci.yml`
because the current GitHub token does not carry the `workflow` scope.

To activate it, either:

1. Copy `ci/verify.yml` to `.github/workflows/ci.yml` using a token or GitHub App
   with **workflow** permission, then commit and push; or
2. Use GitHub's web UI: **Add file → Create new file**, name it
   `.github/workflows/ci.yml`, paste the contents of `ci/verify.yml`, and commit.

The workflow runs:

- 10 practice tests;
- all 10 labs;
- search-index freshness;
- local link, HTML and static accessibility checks;
- manifest validation;
- service worker syntax;
- `SHA256SUMS` verification.

Until activated, the same commands can be run locally from the repo root:

```bash
python -m pip install -r practice/requirements.txt
python -m unittest discover -s practice/tests -v
python practice/run_all.py
python tools/build_search_index.py
python tools/check_links.py
python tools/check_html.py
python tools/check_a11y.py
python -m json.tool manifest.webmanifest >/dev/null
node --check sw.js
sha256sum -c SHA256SUMS.txt
```
