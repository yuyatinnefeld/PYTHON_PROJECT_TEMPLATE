#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" 
---------------------------------------------
# Data Extractor Software
# (C) 2021 Yuya Tinnefeld, Düsseldorf, Germany
# email: yuyatinnefeld@gmail.com
---------------------------------------------
"""

from extractor import *

def generate(extractor: DataExtractor) -> None:

    print("Generate Extractor Tools")
    google_analytics_extractor = extractor.create_google_analytics()
    google_search_console_extractor = extractor.create_google_search_console()
    woocommerce_extractor = extractor.create_woocommerce()

    print("## SETUP Google Analytics ##")    
    print(f"{google_analytics_extractor.setup_google_analytics()}")

    print("## SETUP Google Search Console ##")
    print(f"{google_search_console_extractor.setup_google_search_console()}")

    print("## SETUP WooCommerce ##")
    print(f"{woocommerce_extractor.setup_woocommerce()}")


if __name__ == "__main__":
    """
    The generator code can work with any concrete extractor class.
    """

    print("API Generator:")
    generate(APIDataExtractor())

    print("\n")
    print("##########################")
    print("\n")

    print("CSV Generator:")
    generate(CSVDataExtractor())

