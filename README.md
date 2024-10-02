# ZpyherCart

ZpyherCart is an e-commerce website that provides a seamless shopping experience. Built using HTML, CSS, Bootstrap for the front-end, and Python, Django for the back-end, it enables users to browse products, add items to the cart, and complete their purchases efficiently.

## Features

- **User Authentication**: Sign up, log in, and profile management for users.
- **Product Management**: Admins can add, edit, and delete products through the Django admin panel.
- **Shopping Cart**: Users can add products to their cart, update quantities, and proceed to checkout.
- **Order Processing**: View order history, place orders, and receive order confirmations.
- **Responsive Design**: Built with Bootstrap for responsiveness across all devices.


## Technologies Used

- **Frontend**:
  - HTML
  - CSS
  - Bootstrap
- **Backend**:
  - Python
  - Django
- **Database**:
  - SQLite (or any Django-supported database)

## Installation and Setup

Follow these steps to install and run ZpyherCart locally:

### Prerequisites

Make sure you have the following installed on your system:

- Python 3.x
- Git

### Steps to Setup

```bash
# 1. Clone the repository
git clone https://github.com/yourusername/ZpyherCart.git
cd ZpyherCart

# 2. Create a virtual environment
python -m venv venv

# 3. Activate the virtual environment
# On macOS/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate

# 4. Install dependencies
pip install -r requirements.txt

# 5. Apply migrations
python manage.py migrate

# 6. Create a superuser (optional)
python manage.py createsuperuser
# Follow the prompts to create a username, email, and password.

# 7. Run the development server
python manage.py runserver

# 8. Access the website
# Open your browser and navigate to:
http://127.0.0.1:8000/
