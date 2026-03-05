import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

def price_change_plots_2_symbols(df: pd.DataFrame, combinations: list) -> None:
    """
    Draws scatter plots of the price changes of two symbols for the given combinations.
    Then, it adds a regression line. The plots are saved to a PDF file.
    :param df: prepared dataframe
    :param combinations: list of tuples with two symbols
    :return: None
    """
    output_file = "price_change_plots_2_symbols.pdf"

    with PdfPages(output_file) as pdf:
        for combination in combinations:
            x = df[(combination[0], "perc_change")]
            y = df[(combination[1], "perc_change")]

            # Trend line ------------------------------------
            coef = np.polyfit(x, y, 1)
            func = np.poly1d(coef)

            x_range = np.linspace(x.min(), x.max(), 100)

            # Plot ------------------------------------------

            plt.figure(figsize=(10, 6))

            plt.scatter(x, y, s=10, alpha=0.3, color='blue', label='Percent price changes')
            plt.plot(x_range, func(x_range), color="red", linewidth=2, label=f"Trend (slope: {coef[0]:.2f})")

            plt.xlabel(f"Change for {combination[0]}")
            plt.ylabel(f"Change for: {combination[1]}")
            plt.title(f"{combination[0]} vs {combination[1]}")
            plt.legend()
            plt.grid(True, linestyle='--', alpha=0.6)
            plt.tight_layout()

            pdf.savefig()
            plt.close()

        print(f"Plots safed to: {output_file}")




