from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt

ROOT = Path(__file__).resolve().parent
DATA_FILE = ROOT / "data" / "student_marks.csv"
CHART_FILE = ROOT / "subject_averages.png"

def main():
    df = pd.read_csv(DATA_FILE)
    subjects = ["数学", "Science", "English", "Computer"]
    # Use ASCII subject labels for compatibility and clear plots.
    subjects = ["Math", "Science", "English", "Computer"]

    df["Total"] = df[subjects].sum(axis=1)
    df["Average"] = df[subjects].mean(axis=1)

    print("\nSTUDENT PERFORMANCE SUMMARY")
    print("=" * 32)
    print(df[["Student", "Total", "Average"]].to_string(index=False))
    print(f"\nClass average: {df['Average'].mean():.2f}")
    top = df.loc[df["Average"].idxmax()]
    print(f"Top performer: {top['Student']} ({top['Average']:.2f})")

    subject_avg = df[subjects].mean().sort_values(ascending=False)
    print("\nSubject averages:")
    print(subject_avg.round(2).to_string())

    ax = subject_avg.plot(kind="bar", title="Average Marks by Subject")
    ax.set_xlabel("Subject")
    ax.set_ylabel("Average marks")
    ax.set_ylim(0, 100)
    plt.tight_layout()
    plt.savefig(CHART_FILE, dpi=150)
    print(f"\nChart saved to: {CHART_FILE.name}")

if __name__ == "__main__":
    main()
