from __future__ import annotations
from abc import ABC, abstractmethod

class DataExtractor(ABC):

    @abstractmethod
    def create_google_analytics(self) -> GoogleAnalyticsExtractor:
        pass

    @abstractmethod
    def create_google_search_console(self) -> GoogleSearchConsoleExtractor:
        pass

    @abstractmethod
    def create_woocommerce(self) -> WooCommerceExtractor:
        pass

class APIDataExtractor(DataExtractor):

    def create_google_analytics(self) -> GoogleAnalyticsExtractor:
        return GoogleAnalyticsAPIExtractor()

    def create_google_search_console(self) -> GoogleSearchConsoleExtractor:
        return GoogleSearchConsoleAPIExtractor()

    def create_woocommerce(self) -> WooCommerceExtractor:
        return WooCommerceAPIExtractor()

class CSVDataExtractor(DataExtractor):

    def create_google_analytics(self) -> GoogleAnalyticsExtractor:
        return GoogleAnalyticsCSVExtractor()

    def create_google_search_console(self) -> GoogleSearchConsoleExtractor:
        return GoogleSearchConsoleCSVExtractor()

    def create_woocommerce(self) -> WooCommerceExtractor:
        return WooCommerceCSVExtractor()

"""
Google Analytics Extractor Setup
"""

class GoogleAnalyticsExtractor(ABC):

    @abstractmethod
    def setup_google_analytics(self) -> str:
        pass

    @abstractmethod
    def read_google_analytics(self) -> str:
        pass

    @abstractmethod
    def save_google_analytics(self) -> str:
        pass

class GoogleAnalyticsAPIExtractor(GoogleAnalyticsExtractor):
    def setup_google_analytics(self) -> str:
        return "Setup Google Analytics API extractor."

    def read_google_analytics(self) -> str:
        return "Read Google Anlytics API data"
    
    def save_google_analytics(self) -> str:
        return "Save Google Anlytics API data"

class GoogleAnalyticsCSVExtractor(GoogleAnalyticsExtractor):
    def setup_google_analytics(self) -> str:
        return "Setup Google Analytics CSV extractor."

    def read_google_analytics(self) -> str:
        return "Read Google Anlytics CSV data"
    
    def save_google_analytics(self) -> str:
        return "Save Google Anlytics CSV data"


class WooCommerceExtractor(ABC):

    @abstractmethod
    def setup_woocommerce(self) -> str:
        pass

    @abstractmethod
    def read_woocommerce(self) -> str:
        pass

    @abstractmethod
    def save_woocommerce(self) -> str:
        pass

class WooCommerceAPIExtractor(WooCommerceExtractor):
    def setup_woocommerce(self) -> str:
        return "Setup WooCommerce API extractor."

    def read_woocommerce(self) -> str:
        return "Read WooCommerce API data"
    
    def save_woocommerce(self) -> str:
        return "Save WooCommerce API data"

class WooCommerceCSVExtractor(WooCommerceExtractor):
    def setup_woocommerce(self) -> str:
        return "Setup WooCommerce CSV extractor."

    def read_woocommerce(self) -> str:
        return "Read WooCommerce CSV data"
    
    def save_woocommerce(self) -> str:
        return "Save WooCommerce CSV data"


class GoogleSearchConsoleExtractor(ABC):

    @abstractmethod
    def setup_google_search_console(self) -> str:
        pass

    @abstractmethod
    def read_google_search_console(self) -> str:
        pass

    @abstractmethod
    def save_google_search_console(self) -> str:
        pass

class GoogleSearchConsoleAPIExtractor(GoogleSearchConsoleExtractor):
    def setup_google_search_console(self) -> str:
        return "Setup Google Search Console API extractor."

    def read_google_search_console(self) -> str:
        return "Read Google Search Console API data"
    
    def save_google_search_console(self) -> str:
        return "Save Google Search Console API data"

class GoogleSearchConsoleCSVExtractor(GoogleSearchConsoleExtractor):
    def setup_google_search_console(self) -> str:
        return "Setup the Google Search Console CSV extractor."

    def read_google_search_console(self) -> str:
        return "Read Google Search Console CSV data"
    
    def save_google_search_console(self) -> str:
        return "Save Google Search Console CSV data"
