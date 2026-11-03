
# ShopEase Product Service

## 1. Project Overview

ShopEase Product Service is an independent REST API application
developed using Python and FastAPI.

It provides product management functionality through CRUD
(Create, Read, Update and Delete) operations.

The application uses an in-memory Python dictionary for storing
product information. MySQL integration is not included in this
implementation.

The application is containerized using Docker.

## 2. Technology Stack

- Python 3.11+
- FastAPI
- Uvicorn
- Pydantic
- Python-dotenv
- Docker
- Swagger UI
- Git and GitHub

## 3. Features

- Create a new product.
- Retrieve all products.
- Retrieve a product by ID.
- Update an existing product.
- Delete a product.
- Filter products by category.
- Support pagination using skip and limit.
- Validate product information using Pydantic.
- Handle application exceptions.
- Run independently inside a Docker container.

## 4. Project Structure

```text
shopease-product-service/
│
├── app/
│   ├── main.py
│   ├── routers/
│   │   └── product_routes.py
│   ├── schemas/
│   │   └── product_schema.py
│   ├── models/
│   │   └── product_model.py
│   ├── services/
│   │   └── product_service.py
│   └── config/
│       └── settings.py
│
├── Dockerfile
├── .dockerignore
├── .gitignore
├── requirements.txt
├── .env
└── README.md
```

Note: The local .env file is excluded from Git.

## 5. Installation

Clone the repository:

```bash
git clone https://github.com/YOUR_USERNAME/shopease-product-service.git
cd shopease-product-service
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment on Windows:

```powershell
.\venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## 6. Local Execution

Run the application:

```bash
uvicorn app.main:app --reload --host 127.0.0.1 --port 8003
```

Application URL:

http://localhost:8003

Swagger documentation:

http://localhost:8003/docs

## 7. Docker Image Build

Build the Docker image:

```bash
docker build -t shopease-product-service .
```

Verify the image:

```bash
docker images
```

## 8. Docker Container Execution

Run the container:

```bash
docker run -d --name shopease-product-container --env-file .env -p 8003:8003 shopease-product-service
```

Check running containers:

```bash
docker ps
```

Check application logs:

```bash
docker logs shopease-product-container
```

Stop the container:

```bash
docker stop shopease-product-container
```

Start the container:

```bash
docker start shopease-product-container
```

## 9. API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | /api/products/ | Create product |
| GET | /api/products/ | Retrieve all products |
| GET | /api/products/{product_id} | Retrieve product by ID |
| PUT | /api/products/{product_id} | Update product |
| DELETE | /api/products/{product_id} | Delete product |

### Product Creation Example

```json
{
  "name": "Wireless Mouse",
  "description": "Bluetooth wireless mouse",
  "price": 599.00,
  "stock_quantity": 50,
  "category": "Electronics",
  "status": "Active"
}
```

### Category Filtering

```text
GET /api/products/?category=Electronics
```

### Pagination

```text
GET /api/products/?skip=0&limit=10
```

## 10. Validation and Exception Handling

The application validates:

- Required product name.
- Maximum product name length.
- Optional product description length.
- Positive product price.
- Non-negative stock quantity.
- Valid product category.
- Allowed product status values.

### HTTP Status Codes

| Status | Description |
|---|---|
| 200 | Successful request |
| 201 | Product created |
| 204 | Product deleted |
| 404 | Product not found |
| 409 | Duplicate product ID conflict |
| 422 | Validation error |
| 500 | Unexpected server error |

## 11. Testing

The Product Service is tested through Swagger UI.

Testing scenarios include:

- Create product with valid information.
- Reject empty product names.
- Reject negative prices.
- Reject negative stock quantities.
- Retrieve all products.
- Retrieve products by ID.
- Update products.
- Delete products.
- Handle non-existing product IDs.
- Filter products by category.
- Test pagination.

Testing is performed against the Docker-hosted application.

## 12. Docker Application URL

http://localhost:8003/docs

## 13. Storage Information

This assignment uses in-memory Python dictionary storage.

Product information is temporary and is lost when the application process restarts.

Database integration is outside the scope of this standalone assignment.

## 14. Author

ShopEase Product Service

Developed as part of the ShopEase Microservices Training Project.
