import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "results" / "guide_ranking.csv"
OUTPUT_FILE = BASE_DIR / "figures" / "guide_ranking.png"

df = pd.read_csv(INPUT_FILE)

colors = [
    "#2E8B57" if guide == "NONO_g01" else "#B0B0B0"
    for guide in df["guide_id"]
]

plt.figure(figsize=(8, 5))
plt.bar(df["guide_id"], df["composite_score"], color=colors)

plt.title("In-silico CRISPR Guide Ranking for NONO")
plt.xlabel("Candidate sgRNA")
plt.ylabel("Composite prioritisation score")
plt.text(
    0.5,
    -0.20,
    "NONO_g01 highlighted as the primary candidate after qualitative warning review.",
    ha="center",
    va="center",
    transform=plt.gca().transAxes,
    fontsize=9,
)

plt.tight_layout()
OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
plt.savefig(OUTPUT_FILE, dpi=300, bbox_inches="tight")
print(f"Figure saved to: {OUTPUT_FILE}")