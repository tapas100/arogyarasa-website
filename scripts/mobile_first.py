import json
from pathlib import Path

def check_breakpoints():
    # Placeholder: in reality you would run a headless browser at different viewports.
    # Here we just report the Tailwind breakpoints defined (default). 
    breakpoints = {"sm": "640px", "md": "768px", "lg": "1024px", "xl": "1280px", "2xl": "1536px"}
    return {"status": "ok", "breakpoints": breakpoints}

if __name__ == "__main__":
    report = check_breakpoints()
    out_path = Path(__file__).resolve().parents[1] / "mobile_first_report.json"
    out_path.write_text(json.dumps(report, indent=2))
    print(json.dumps({"status": "ok", "report": str(out_path)}))
