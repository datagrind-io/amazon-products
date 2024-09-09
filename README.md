# Amazon Products Recipe

This is the official DataGrind recipe for scrape Amazon products.

Recipe Id:
```yaml
datagrind-io/amazon-products
```

Configuration
---

```yaml
id: datagrind-io/amazon-products
name: Amazon Products Scraper
description: A web scraper that extracts product information from Amazon, including product name, price, rating, and more.
author: clint21.eth
version: 0.1.0
requirements:
    - selenium
    - requests
    - beautifulsoup4
    - lxml
parameters:
    - name: search_query
      description: The search term to find products on Amazon
      required: true
      type: string
    - name: num_products
      description: The number of products to scrape
      required: false
      type: integer
      default: 10
```