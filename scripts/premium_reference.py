import json
from pathlib import Path

def get_premium_refs():
    # In a real system we would scrape top‑tier e‑commerce sites.
    # Here we return a static list of example URLs.
    refs = [
        "https://www.patagonia.com",
        "https://www.bonobos.com",
        "https://www.warbyparker.com",
        "https://www.allbirds.com"
    ]
    return {"premium_refs": refs}

if __name__ == "__main__":
    report = get_premium_refs()
    out_path = Path(__file__).resolve().parents[1] / "premium_reference_report.json"
    out_path.write_text(json.dumps(report, indent=2))
    print(json.dumps({"status": "ok", "report": str(out_path)}))
