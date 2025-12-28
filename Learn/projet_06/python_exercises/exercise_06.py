# Exercise 06: Complex Types (List, Dict, Optional)
# Before using complex data types in MCP, let's practice with collections

from typing import List, Dict, Optional
from pydantic import BaseModel, Field

# TODO: Create a Pydantic model called 'Product'
# Fields:
# - id: int (required)
# - name: str (required)
# - price: float (required, minimum 0)
# - tags: List[str] (default empty list)
# - metadata: Optional[Dict[str, str]] (optional)

# TODO: Create a function called 'filter_products_by_tag'
# Parameters: products (List[Product]), tag (str)
# Return List[Product] containing only products with the given tag

# TODO: Create a function called 'calculate_total_price'
# Parameters: products (List[Product]), tax_rate (float, default 0.2)
# Return the total price including tax
# Formula: sum(product.price for product in products) * (1 + tax_rate)

# TODO: Create a function called 'group_products_by_price_range'
# Parameters: products (List[Product])
# Return Dict[str, List[Product]] grouped by:
# - "cheap": price < 10
# - "medium": 10 <= price < 100
# - "expensive": price >= 100

# TODO: Create a function called 'find_product_with_metadata'
# Parameters: products (List[Product]), key (str), value (str)
# Return Optional[Product] - the first product where metadata[key] == value
# Return None if not found

def main():
    # Test your functions here
    pass

if __name__ == "__main__":
    main()
