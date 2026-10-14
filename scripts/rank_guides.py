import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
INPUT_FILE = BASE_DIR / "data" / "raw" / "candidate_guides.csv"
OUTPUT_FILE = BASE_DIR / "results" / "guide_ranking.csv"


def rank_guides(df):
    df = df.copy()

    df["gc_percent"] = df["gc_percent"].astype(float)
    df["on_target_score"] = df["on_target_score"].astype(float)
    df["specificity_score"] = df["specificity_score"].astype(float)
    df["off_target_count"] = df["off_target_count"].astype(int)

    df["gc_penalty"] = (df["gc_percent"] - 50).abs() / 50

    df["composite_score"] = (
        df["on_target_score"]
        + df["specificity_score"]
        - df["off_target_count"] * 0.1
        - df["gc_penalty"]
    )

    df = df.sort_values(
        by=["composite_score", "on_target_score", "specificity_score"],
        ascending=[False, False, False],
    )

    return df.reset_index(drop=True)


def main():
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            "Missing file: data/raw/candidate_guides.csv. "
            "Please add your CRISPOR or CHOPCHOP guide table."
        )

    guides = pd.read_csv(INPUT_FILE)
    ranked = rank_guides(guides)

    OUTPUT_FILE.parent.mkdir(parents=True, exist_ok=True)
    ranked.to_csv(OUTPUT_FILE, index=False)

    print(f"Ranked {len(ranked)} guides successfully.")
    print(f"Output saved to: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()