import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# =========================
# Data
# =========================
models = ["DAE", "VAE", "NDAE", "DiFF-RF", "iForest", "KitNET", "DMSN"]

recall = np.array([0.8315, 0.8426, 0.8539, 0.8911, 0.8410, 0.8765, 0.9510])
precision = np.array([0.8183, 0.7913, 0.8135, 0.8809, 0.8310, 0.8654, 0.9309])

f1 = 2 * recall * precision / (recall + precision)
f1 = np.round(f1, 4)

df = pd.DataFrame({
    "Model": models,
    "Recall": recall,
    "Precision": precision,
    "F1": f1
})

print(df)

# =========================
# Color scheme options
# =========================
COLOR_SCHEME = "cyber"
# Options:
# "classic"
# "colorblind"
# "high_contrast"
# "grayscale"
# "pastel"
# "cyber"

color_schemes = {
    "classic": {
        "Recall": "#1f77b4",
        "Precision": "#ff7f0e",
        "F1": "#2ca02c"
    },
    "colorblind": {
        "Recall": "#0072B2",
        "Precision": "#E69F00",
        "F1": "#009E73"
    },
    "high_contrast": {
        "Recall": "#003f5c",
        "Precision": "#bc5090",
        "F1": "#ffa600"
    },
    "grayscale": {
        "Recall": "#222222",
        "Precision": "#777777",
        "F1": "#bbbbbb"
    },
    "pastel": {
        "Recall": "#8ecae6",
        "Precision": "#ffb703",
        "F1": "#90be6d"
    },
    "cyber": {
        "Recall": "#00b4d8",
        "Precision": "#f72585",
        "F1": "#80ed99"
    }
}

colors = color_schemes[COLOR_SCHEME]

# =========================
# Very large font settings
# =========================
plt.rcParams.update({
    "font.size": 32,
    "axes.titlesize": 44,
    "axes.labelsize": 40,
    "xtick.labelsize": 34,
    "ytick.labelsize": 34,
    "legend.fontsize": 34,
    "figure.titlesize": 46,
    "axes.linewidth": 2.0,
})

# =========================
# Plot
# =========================
x = np.arange(len(models))
width = 0.27

fig, ax = plt.subplots(figsize=(24, 13))

bars1 = ax.bar(
    x - width,
    recall,
    width,
    label="Recall",
    color=colors["Recall"],
    edgecolor="black",
    linewidth=1.8
)

bars2 = ax.bar(
    x,
    precision,
    width,
    label="Precision",
    color=colors["Precision"],
    edgecolor="black",
    linewidth=1.8,
    hatch="//"
)

bars3 = ax.bar(
    x + width,
    f1,
    width,
    label="F1",
    color=colors["F1"],
    edgecolor="black",
    linewidth=1.8,
    hatch="xx"
)

# =========================
# Labels, title, and axis
# =========================
ax.set_title("Performance Comparison of Models used by IDS", pad=30)
ax.set_xlabel("Model", labelpad=24)
ax.set_ylabel("Score", labelpad=24)

ax.set_xticks(x)
ax.set_xticklabels(models)

ax.set_ylim(0.75, 1.00)
ax.tick_params(axis="both", width=2.0, length=8)

ax.grid(
    axis="y",
    linestyle="--",
    linewidth=1.2,
    alpha=0.65
)

ax.legend(
    loc="upper left",
    frameon=True,
    edgecolor="black"
)

# =========================
# Value labels
# =========================
for bars in [bars1, bars2, bars3]:
    for bar in bars:
        height = bar.get_height()
        ax.text(
            bar.get_x() + bar.get_width() / 2,
            height + 0.005,
            f"{height:.4f}",
            ha="center",
            va="bottom",
            fontsize=25,
            rotation=90
        )

fig.tight_layout()

# =========================
# Save figure
# =========================
png_path = Path(f"ids_model_performance_{COLOR_SCHEME}.png")
pdf_path = Path(f"ids_model_performance_{COLOR_SCHEME}.pdf")

fig.savefig(png_path, dpi=300, bbox_inches="tight")
fig.savefig(pdf_path, bbox_inches="tight")

plt.show()