from dataclasses import dataclass,field
from datetime import datetime, timezone
from decimal import Decimal


@dataclass
class Product:
    # Unique product ID.
    id: int

    # Product name.
    name: str

    # Optional product description.
    description: str | None

    # Product price.
    price: Decimal

    # Available stock quantity.
    stock_quantity: int

    # Product category.
    category: str

    # Product status.
    status: str = "Active"


    # Generate a separate creation time for each product.
    created_at: datetime = field(
        default_factory=lambda: datetime.now(timezone.utc) #create a new value whenever a new object is created.
    )