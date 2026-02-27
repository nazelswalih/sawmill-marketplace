# Sawmill Marketplace
=====================

Sawmill Marketplace is a web-based platform built using Django, designed to facilitate transactions between buyers and sellers of wood products. The platform allows buyers to browse and request quotes for products, while sellers can manage their inventory and respond to quote requests.

## Prerequisites
---------------

* Python 3.8 or higher
* Django 3.2 or higher
* SQLite database (included by default with Django)

## Installation
------------

1. Clone the repository: `git clone https://github.com/your-repo/sawmill-marketplace.git`
2. Navigate to the project directory: `cd sawmill-marketplace`
3. Install dependencies: `pip install -r requirements.txt`
4. Run migrations: `python manage.py migrate`
5. Create a superuser: `python manage.py createsuperuser`

## Usage
-----

### Buyer

1. Register as a buyer: Navigate to `http://localhost:8000/users/register/` and fill out the registration form.
2. Browse products: Navigate to `http://localhost:8000/products/` to view available products.
3. Request a quote: Click on a product to view its details, then click the "Request Quote" button to submit a quote request.

### Seller

1. Register as a seller: Navigate to `http://localhost:8000/users/register/` and fill out the registration form, selecting the "Seller" role.
2. Manage inventory: Navigate to `http://localhost:8000/sawmill/inventory_list/` to view and manage your products.
3. Respond to quote requests: Navigate to `http://localhost:8000/transactions/admin_list/` to view and respond to quote requests.

## API Documentation
-----------------

The Sawmill Marketplace API is built using Django REST framework. API endpoints are available for the following resources:

* Products: `http://localhost:8000/products/`
* Quote requests: `http://localhost:8000/transactions/`

API documentation is available at `http://localhost:8000/api/docs/`.

## Testing
---------

To run tests, navigate to the project directory and execute the following command:
```bash
python manage.py test
```
This will run all tests in the `buyer`, `core`, and `sawmill` apps.

## Deployment
------------

To deploy the Sawmill Marketplace to a production environment, follow these steps:

1. Configure a production-ready database (e.g., PostgreSQL).
2. Set up a web server (e.g., Apache, Nginx) to serve the Django application.
3. Configure a WSGI server (e.g., Gunicorn) to run the Django application.
4. Deploy the application to a cloud platform (e.g., AWS, Heroku) or a virtual private server (VPS).

Note: This is a high-level overview of the deployment process. For detailed instructions, consult the official Django documentation and the documentation for your chosen deployment platform.