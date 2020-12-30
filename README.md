# Python Data Extractor

## Design Pattern Concept

For this Project I selected the Abstract Factory Pattern:

### Benefits
* easy to maintain and control the classes of objects
* consistency among objects and unification of the functions of different extractors
* quickly scalable project capacities


### Example
AbstractFactory => DataExtractor
ConcreteFactory => Data Format (CSV, API, SQL, JSON, Text, PDF, SAS, etc.)
AbstractProduct => Data Source / Tools (Analytics, CRM, Web Scraping, Streaming, Social Media, etc.)
ConcreteProduct => Source + Format (GoogleAnalyticsAPIExtractor, TwitterAPIExtractor, FacebookCSVExtractor)
