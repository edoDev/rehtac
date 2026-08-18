"""Copy seasons-2026.json into the offline <script id="seasonData"> block."""
from pathlib import Path

root = Path(__file__).resolve().parent
data = (root / "seasons-2026.json").read_text(encoding="utf-8").strip()
html_path = root / "index.html"
html = html_path.read_text(encoding="utf-8")
start = html.find('<script type="application/json" id="seasonData">')
end = html.find("</script>", start)
if start < 0 or end < 0:
    raise SystemExit("seasonData block not found")
open_tag_end = html.find(">", start) + 1
html = html[:open_tag_end] + "\n" + data + "\n" + html[end:]
html_path.write_text(html, encoding="utf-8", newline="\n")
print("synced seasons-2026.json -> index.html#seasonData")
