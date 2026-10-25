"""Build a clean reading copy of the paper draft, as Markdown and PDF.

The paper's opening carries dated editorial notes between the title and the
first "---" rule. The reading copy keeps the title, drops those notes, and
keeps everything after the rule as it stands. The PDF goes through pandoc
(Markdown to HTML) and headless Chrome (HTML to PDF).

Usage: python3 scripts/build_reading_copy.py OUT_DIR [DATE]
Written 2026-10-25 for step 1 of docs/paper-readiness-checklist-2026-10-18.md.
"""
import pathlib
import subprocess
import sys

REPO = pathlib.Path(__file__).resolve().parent.parent
PAPER = REPO / "drafts" / "paper-removal-test-nature-draft.md"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

CSS = """
@page { size: A4; margin: 22mm 20mm 20mm 20mm;
  @bottom-center { content: "page " counter(page) " of " counter(pages);
                   font: 9pt Georgia, serif; color: #555; } }
body { font: 11pt/1.5 Georgia, 'Times New Roman', serif; color: #111; max-width: none; }
h1 { font-size: 17pt; line-height: 1.25; } h2 { font-size: 14pt; margin-top: 1.6em; }
h3 { font-size: 12pt; margin-top: 1.4em; }
table { border-collapse: collapse; font-size: 8.5pt; margin: 0.8em 0; }
th, td { border: 1px solid #999; padding: 3px 5px; vertical-align: top; }
code { font-size: 9pt; word-break: break-all; }
.label { color: #555; font-size: 9.5pt; }
"""


def clean_text(src: str, label: str) -> str:
    lines = src.splitlines()
    title = lines[0]
    rule = lines.index("---")
    return "\n".join([title, "", f"*{label}*", ""] + lines[rule:]) + "\n"


def main() -> None:
    out = pathlib.Path(sys.argv[1]).expanduser()
    date = sys.argv[2] if len(sys.argv) > 2 else "undated"
    commit = subprocess.run(["git", "-C", str(REPO), "rev-parse", "--short", "HEAD"],
                            capture_output=True, text=True, check=True).stdout.strip()
    label = f"Reading copy, {date}: draft version 0.3 as on main at commit {commit}, editorial notes removed."
    out.mkdir(parents=True, exist_ok=True)
    md = out / f"mvm-paper-reading-copy-{date}.md"
    md.write_text(clean_text(PAPER.read_text(), label))
    html = out / f"mvm-paper-reading-copy-{date}.html"
    css = out / "reading-copy.css"
    css.write_text(CSS)
    subprocess.run(["pandoc", str(md), "-f", "markdown-smart", "-s", "-o", str(html),
                    "--metadata", "pagetitle=Minimum Viable Mind paper, reading copy",
                    "--css", css.name], check=True)
    pdf = out / f"mvm-paper-reading-copy-{date}.pdf"
    subprocess.run([CHROME, "--headless", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={pdf}", html.as_uri()], check=True,
                   capture_output=True)
    html.unlink()
    css.unlink()
    print(md, pdf, sep="\n")


if __name__ == "__main__":
    main()
