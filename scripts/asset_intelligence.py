import json
from pathlib import Path

# Simple asset inventory – list image files and basic metadata
def inventory_assets(dir_path):
    assets = []
    for p in Path(dir_path).rglob("*.[jJ][pP][gG]"):
        asset = {
            "path": str(p.relative_to(Path(dir_path).parent)),
            "size_kb": round(p.stat().st_size/1024, 2),
            "type": "image/jpeg"
        }
        assets.append(asset)
    for p in Path(dir_path).rglob("*.[pP][nN][gG]"):
        asset = {
            "path": str(p.relative_to(Path(dir_path).parent)),
            "size_kb": round(p.stat().st_size/1024, 2),
            "type": "image/png"
        }
        assets.append(asset)
    return assets

if __name__ == "__main__":
    repo_root = Path(__file__).resolve().parents[1]
    assets_dir = repo_root / "frontend" / "public" / "assets"
    report = {
        "asset_count": 0,
        "total_size_kb": 0,
        "assets": []
    }
    assets = inventory_assets(str(assets_dir))
    report["assets"] = assets
    report["asset_count"] = len(assets)
    report["total_size_kb"] = round(sum(a["size_kb"] for a in assets), 2)
    out_path = repo_root / "asset_report.json"
    out_path.write_text(json.dumps(report, indent=2))
    print(json.dumps({"status": "ok", "report": str(out_path)}))
