def get_trending_keywords():
    # Simulate a scrape from a mock site
    return ["eco-friendly", "durable", "minimalist", "budget"]

def enrich_product_description(product_description):
    trends = get_trending_keywords()
    enriched = product_description + "\nTrending Tags: " + ", ".join(trends)
    return enriched
