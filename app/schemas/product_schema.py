
from datetime import datetime
from decimal import Decimal
from typing import Literal

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    field_validator,
)


# --------------------------------------------------
# 1. Product Create Schema
# --------------------------------------------------

class ProductCreate(BaseModel):

    # Product name cannot be empty.
    name: str = Field(
        min_length=1,
        max_length=100,
    )

    # Description is optional.
    description: str | None = Field(
        default=None,
        max_length=500,
    )

    # Price must be greater than zero.
    price: Decimal = Field(
        gt=0,
        max_digits=10,
        decimal_places=2,
    )

    # Stock cannot be negative.
    stock_quantity: int = Field(
        ge=0,
        strict=True,#t rejects the string and expects an actual integer.
    )

    # Category is required.
    category: str = Field(
        min_length=1,
        max_length=60,
    )

    # Only predefined status values are allowed.
    status: Literal["Active", "Inactive"] = "Active"

    # Remove unnecessary spaces and reject empty names.
    @field_validator("name", mode="before") #@field_validator to clean and validate incoming API data before saving it to the database.
    @classmethod
    def validate_name(cls, value):
        if isinstance(value, str):
            value = value.strip()

        return value

    # Remove unnecessary spaces from category.
    @field_validator("category", mode="before")
    @classmethod
    def validate_category(cls, value):
        if isinstance(value, str):#Given value particular data type-ah irukka-nu check pannum.
            value = value.strip()

        return value

    # Convert blank descriptions to None.
    @field_validator("description", mode="before")
    @classmethod
    def validate_description(cls, value):
        if isinstance(value, str):
            value = value.strip()

            return value if value else None

        return value


# --------------------------------------------------
# 2. Product Update Schema
# --------------------------------------------------

# PUT requires the complete updated product information.
class ProductUpdate(ProductCreate):
    pass


# --------------------------------------------------
# 3. Product Response Schema
# --------------------------------------------------

class ProductResponse(BaseModel):

    # Read values from our Product dataclass object.
    model_config = ConfigDict(from_attributes=True)

    id: int
    name: str
    description: str | None
    price: Decimal
    stock_quantity: int
    category: str
    status: Literal["Active", "Inactive"]
    created_at: datetime
