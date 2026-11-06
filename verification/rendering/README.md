# Check the actual GitHub mathematics

The collector compares every recognized mathematical expression in commit-pinned Markdown with its actual GitHub MathML, at viewport widths of 1440 and 760 pixels. It keeps expression counts, source hashes, mathematical structure, relations and visible labels together with HTML captures and screenshots. A report is tied to one exact commit and tree.

## Run locally

Use Node.js 18 or newer, Python 3.10 or newer, Git and an anonymous Chromium browser that can reach the public repository. Install the pinned dependencies outside the source checkout:

```bash
mkdir -p /tmp/autonomous-noise-render-deps
cp verification/rendering/package.json verification/rendering/package-lock.json /tmp/autonomous-noise-render-deps/
npm ci --prefix /tmp/autonomous-noise-render-deps --ignore-scripts --no-audit --no-fund
/tmp/autonomous-noise-render-deps/node_modules/.bin/playwright install chromium
```

Then run the collector, replacing `FULL_COMMIT_SHA` with the complete commit to inspect and choosing a new empty output directory:

```bash
NODE_PATH=/tmp/autonomous-noise-render-deps/node_modules node verification/rendering/capture_hosted_math.cjs \
  --root . \
  --repository GoGoKo699/Autonomous-Markovian-Noise \
  --revision FULL_COMMIT_SHA \
  --contract verification/rendering/math-contract.json \
  --output /tmp/autonomous-noise-hosted-evidence
```

The default scope includes all tracked Markdown pages at the specified commit. The source inventory uses committed Git objects, so uncommitted changes cannot silently enter a capture. A changed expression covered by the text contract needs a reviewed contract update. Use a separate output directory after any source repair, preserving the earlier failure record.

The pull-request workflow runs this same read-only command on the proposed head commit. It has only `contents: read`, stores no authentication in the checkout, and captures public GitHub pages in a fresh unsigned-in browser. Its artifact includes `hosted-report.json`, the source inventory, both viewport comparisons and the screenshots. Actions artifacts expire; download evidence needed for a particular review.

## What a passing report establishes

The automated comparison detects missing expressions, renderer errors, structural changes, altered scripts or operands, selected text mismatches, and bounded display-geometry defects. The explicit text contract covers the main resource claims and the operator-norm table entry. Local MathJax supplies the source-side reference; it is not itself evidence of hosted rendering.

Inspect representative screenshots and every flagged or repaired expression against the source before accepting a revision. A structural pass does not certify every pixel, navigation, scientific correctness, other browsers or future GitHub rendering behavior. The [scientific verification](../README.md) is a separate check.

The two collector scripts are retained unchanged from the reviewed verification-tool snapshot. Their SHA256 identities are:

```text
capture_hosted_math.cjs  49182eaf354e86f685a4976814d672de5d7329a2d9e42f62a5227e2bc07c2d18
check_rendered_math.py   edbc2d72af94e96b78166d74b66fcea150134f2f3ebaaea121e9057768e1dbfe
```
