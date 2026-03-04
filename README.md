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

## Project Structure
------------------

The project is structured into the following apps:

* `buyer`: Handles buyer-related functionality, including product browsing and quote requests.
* `core`: Provides core functionality, including user authentication and dashboard views.
* `sawmill`: Handles seller-related functionality, including inventory management and quote responses.

## Contributing
------------

To contribute to the Sawmill Marketplace project, please follow these steps:

1. Fork the repository on GitHub.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your fork.
4. Submit a pull request to the main repository.

Please ensure that your code follows the project's coding standards and includes tests for any new functionality.

## Code Examples
--------------

### Buyer Views

The `buyer` app contains views for product browsing and quote requests. For example, the `product_list` view filters products based on user input:
```python
def product_list(request):
    products = Product.objects.filter(is_active=True)
    # ...
    if query:
        products = products.filter(
            Q(species__name__icontains=query) |
            Q(dimensions__icontains=query) |
            Q(grade__name__icontains=query)
        )
    # ...
    return render(request, 'buyer/product_list.html', {'products': products})
```
### Seller Views

The `sawmill` app contains views for inventory management and quote responses. For example, the `inventory_list` view displays a list of products for the seller:
```python
def inventory_list(request):
    products = Product.objects.filter(seller=request.user)
    return render(request, 'sawmill/inventory_list.html', {'products': products})
```
### Models

The project uses Django models to represent data in the database. For example, the `Product` model represents a wood product:
```python
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    # ...
```
### Forms

The project uses Django forms to handle user input. For example, the `RFQForm` form handles quote requests:
```python
class RFQForm(forms.ModelForm):
    class Meta:
        model = RFQ
        fields = ['quantity', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 4}),
        }
```