
from typing import Annotated

from fastapi import (
    APIRouter,
    HTTPException,
    Query,
    Response,
    status,
)

from app.schemas.product_schema import (
    ProductCreate,
    ProductResponse,
    ProductUpdate,
)

from app.services.product_service import (
    create_product,
    get_all_products,
    get_product_by_id,
    update_product,
    delete_product,
    ProductNotFoundError,
    DuplicateProductError,
)


# --------------------------------------------------
# 1. Create Product API Router
# --------------------------------------------------

router = APIRouter(
    prefix="/api/products",
    tags=["Products"],
)


# --------------------------------------------------
# 2. Create Product
# POST /api/products/
# --------------------------------------------------

@router.post(
    "/",
    response_model=ProductResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_product_api(
    product_data: ProductCreate,
):

    try:
        product = create_product(product_data)
        return product

    except DuplicateProductError as error:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=str(error),
        )


# --------------------------------------------------
# 3. Retrieve All Products
# GET /api/products/
# --------------------------------------------------

@router.get(
    "/",
    response_model=list[ProductResponse],
)
def list_products_api(
    category: Annotated[str | None, Query()] = None,
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=100)] = 10,
):

    return get_all_products(
        category=category,
        skip=skip,
        limit=limit,
    )


# --------------------------------------------------
# 4. Retrieve Product by ID
# GET /api/products/{product_id}
# --------------------------------------------------

@router.get(
    "/{product_id}",
    response_model=ProductResponse,
)
def get_product_api(
    product_id: int,
):

    try:
        return get_product_by_id(product_id)

    except ProductNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        )


# --------------------------------------------------
# 5. Update Product
# PUT /api/products/{product_id}
# --------------------------------------------------

@router.put(
    "/{product_id}",
    response_model=ProductResponse,
)
def update_product_api(
    product_id: int,
    product_data: ProductUpdate,
):

    try:
        return update_product(
            product_id,
            product_data,
        )

    except ProductNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        )


# --------------------------------------------------
# 6. Delete Product
# DELETE /api/products/{product_id}
# --------------------------------------------------

@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT,
)
def delete_product_api(
    product_id: int,
):

    try:
        delete_product(product_id)

        return Response(
            status_code=status.HTTP_204_NO_CONTENT
        )

    except ProductNotFoundError as error:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(error),
        )
