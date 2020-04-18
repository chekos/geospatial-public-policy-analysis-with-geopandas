# -*- coding: utf-8 -*-

import geopandas as gpd
from pathlib import Path
from zipfile import ZipFile

def main():
    """Extracts zipped files into geodata/ folder in data/processed.
    """

    THIS_DIR = Path(__file__).parent
    DATA_DIR = THIS_DIR.joinpath("../../data/")

    RAW_ZIPPED_DATA = DATA_DIR.joinpath("./external/tl_2019_us_county.zip")
    PROCESSED_DATA = DATA_DIR.joinpath("./processed/")

    z = ZipFile(RAW_ZIPPED_DATA)

    z.filelist

    PROCESSED_DATA.joinpath("geodata/").mkdir()

    z.extractall(PROCESSED_DATA / 'geodata')

    return None

if if __name__ == "__main__":
    main()