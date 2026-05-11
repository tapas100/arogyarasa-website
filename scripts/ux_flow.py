import json, re
from pathlib import Path

# Very simple static mapping for now – can be extended later
flow = {
    "steps": [
        {"name": "Landing (Hero)", "url": "/#hero"},
        {"name": "Browse Products", "url": "/#products"},
        {"name": "View Product Detail", "url": "/product/:id"},
        {"name": "Add to Cart", "url": "/cart"},
        {"name": "Checkout", "url": "/checkout"}
    ]
}

# Write to MEMORY (simulated by a file for now)
Path("/tmp/ux_flow.json").write_text(json.dumps(flow, indent=2))
print(json.dumps({"status": "ok", "flow": flow}))
