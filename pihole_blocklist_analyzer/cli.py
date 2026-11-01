import argparse, json
from pathlib import Path
from .analyzer import analyze

def main():
    p = argparse.ArgumentParser()
    p.add_argument("adlists", type=Path)
    p.add_argument("--output", type=Path, default=Path("./report"))
    args = p.parse_args()
    data = analyze(args.adlists)
    args.output.mkdir(parents=True, exist_ok=True)
    (args.output / "report.json").write_text(json.dumps(data, indent=2))
    print(f"Report written to {args.output}")

if __name__ == "__main__":
    main()
