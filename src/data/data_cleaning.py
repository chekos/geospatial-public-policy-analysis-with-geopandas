# -*- coding: utf-8 -*-

import pandas as pd
from pathlib import Path
from zipfile import ZipFile
import re


def main():
    THIS_DIR = Path(__file__).parent
    DATA_DIR = THIS_DIR.joinpath("../../data/")

    RAW_ZIPPED_DATA = DATA_DIR.joinpath("./external/4-8-2020---748.zip")
    PROCESSED_DATA = DATA_DIR.joinpath("./processed/")

    z = ZipFile(RAW_ZIPPED_DATA)

    data = pd.read_csv(z.open("Data_4-8-2020---748.csv"))
    value_labels = pd.read_csv(z.open("ValueLabels_4-8-2020---748.csv"))

    # Clean empty column
    data.drop(columns=["Unnamed: 49"], inplace=True)

    # Adding value labels to dataframe
    labels = {}
    var_names = value_labels["VariableName"].unique()

    for var in var_names:
        mask = value_labels["VariableName"] == var
        working_df = value_labels[mask].copy()

        labels[var] = {}
        for row in working_df.itertuples():
            labels[var][row.Value] = row.ValueLabel

    for key in labels.keys():
        data[key] = data[key].map(labels[key])

    # Clean column names
    def clean_column(col: str) -> str:
        """Cleans column name from unwanted chars.
        
        Parameters
        ----------
        col : str
            Column name to clean
        
        Returns
        -------
        str
            Cleaned column name
        """
        col = (
            col.replace("'s", "")
            .replace(" - ", "_")
            .replace(" ", "_")
            .replace("/", "-")
            .replace("__", "_")
            .lower()
            # specifically for this context - after some iteration
            .replace("graduation_rate", "gradrate")
            .replace("_within_", "_")
            .replace("two_or_more_races", "multirace")
            .replace("_of_institution", "")
            .replace("_location", "")
            .replace("_or_post_office_box", "")
            .replace("_of_", "_")
            .replace("_that_are_", "_")
        )
        col = re.sub("_\([^()]*\)", "", col)

        return col

    data.columns = [clean_column(col) for col in data.columns]

    data.to_csv(PROCESSED_DATA / "processed_data.csv", encoding="utf-8", index=False)


if __name__ == "__main__":
    main()
