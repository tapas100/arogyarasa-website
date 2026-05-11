import sys, json, re
from bs4 import BeautifulSoup

def score_hierarchy(html_path):
    with open(html_path, encoding="utf-8") as f:
        soup = BeautifulSoup(f, "html.parser")
    headings = soup.find_all(re.compile("^h[1-6]$"))
    score = 0
    if headings:
        levels = [int(h.name[1]) for h in headings]
        if levels == sorted(levels):
            score += 20
        else:
            score += 10
        score += min(len(headings)*5, 30)
    ctas = [el for el in soup.find_all(["a","button"]) if re.search(r"(shop|buy|learn|subscribe|cta)", (el.get_text() or ""), re.I)]
    score += min(len(ctas)*10, 30)
    brs = len(soup.find_all("br"))
    if brs > 3:
        score -= 10
    return max(0, min(100, score))

if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv)>1 else "frontend/src/app/page.tsx"
    print(json.dumps({"path": path, "score": score_hierarchy(path)}))
