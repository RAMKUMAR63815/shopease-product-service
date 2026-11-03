
from itertools import count

from app.models.product_model import Product
from app.schemas.product_schema import (
    ProductCreate,
    ProductUpdate,
)


# --------------------------------------------------
# 1. In-memory product storage
# --------------------------------------------------

# Dictionary stores products using product ID as key.
# Example: {1: Product(...), 2: Product(...)}

products: dict[int, Product] = {}


# Automatically generates unique product IDs.
product_id_counter = count(start=1)


# --------------------------------------------------
# 2. Custom exceptions
# --------------------------------------------------

class ProductNotFoundError(Exception):
    """Raised when a product does not exist."""


class DuplicateProductError(Exception):
    """Raised when a generated product ID already exists."""


# --------------------------------------------------
# 3. Create product
# --------------------------------------------------

def create_product(
    product_data: ProductCreate,
) -> Product:

    # Generate a unique product ID.
    product_id = next(product_id_counter)

    # Protect against duplicate IDs.
    if product_id in products:
        raise DuplicateProductError(
            "Product ID already exists"
        )

    # Create a Product object using validated data.
    product = Product(
        id=product_id,
        **product_data.model_dump(),
    )

    # Store the product in the dictionary.
    products[product_id] = product

    return product


# --------------------------------------------------
# 4. Retrieve all products
# --------------------------------------------------

def get_all_products(
    category: str | None = None,
    skip: int = 0,
    limit: int = 10,
) -> list[Product]:

    # Retrieve all stored products.
    product_list = list(products.values())

    # Apply category filtering when requested.
    if category:
        product_list = [
            product
            for product in product_list
            if product.category.casefold() == category.strip().casefold()
        ]

    # Apply pagination.
    return product_list[skip:skip + limit]


# --------------------------------------------------
# 5. Retrieve product by ID
# --------------------------------------------------

def get_product_by_id(
    product_id: int,
) -> Product:

    product = products.get(product_id)

    if product is None:
        raise ProductNotFoundError(
            f"Product with ID {product_id} not found"
        )

    return product


# --------------------------------------------------
# 6. Update product
# --------------------------------------------------

def update_product(
    product_id: int,
    product_data: ProductUpdate,
) -> Product:

    # Find the existing product.
    product = get_product_by_id(product_id)

    # Get all validated update fields.
    update_data = product_data.model_dump()

    # Update product information.
    for field, value in update_data.items():
        setattr(product, field, value)

    return product


# --------------------------------------------------
# 7. Delete product
# --------------------------------------------------

def delete_product(
    product_id: int,
) -> None:

    # Verify that the product exists.
    get_product_by_id(product_id)

    # Remove product from dictionary.
    del products[product_id]

    return None
