# Arushop

Welcome to **Arushop**, your one-stop eCommerce platform, inspired by Amazon. Arushop provides a seamless online shopping experience with a wide range of products, user-friendly interface, and robust backend.

## Table of Contents

1. [Features](#features)
2. [Installation](#installation)
3. [Usage](#usage)
4. [Screenshots](#screenshots)
5. [Contributing](#contributing)
6. [License](#license)
7. [Contact](#contact)

## Features

- **User Authentication**: Secure user registration and login.
- **Product Catalog**: Extensive product listings with detailed descriptions and reviews.
- **Search Functionality**: Powerful search to find products easily.
- **Shopping Cart**: Add, remove, and update products in the cart.
- **Order Management**: Track orders and order history.
- **Payment Gateway Integration**: Secure payment processing.
- **Responsive Design**: Fully responsive, works on all devices.
- **Admin Panel**: Manage products, users, and orders.

## Installation

### Prerequisites

- Node.js
- npm (Node Package Manager)
- MongoDB
- Git

### Steps

1. **Clone the Repository**

    ```bash
    git clone https://github.com/MohammadrezaAmani/arushop.git
    cd arushop
    ```

2. **Install Dependencies**

    ```bash
    npm install
    ```

3. **Set Up Environment Variables**

    Create a `.env` file in the root directory and add the following:

    ```env
    NODE_ENV=development
    PORT=5000
    MONGO_URI=your_mongodb_connection_string
    JWT_SECRET=your_jwt_secret
    PAYPAL_CLIENT_ID=your_paypal_client_id
    ```

4. **Run the Application**

    ```bash
    npm run dev
    ```

    Your application should now be running on `http://localhost:5000`.

## Usage

### Browsing Products

- Navigate to the homepage to view featured products.
- Use the search bar to find specific products.

### User Account

- Sign up for a new account or log in with existing credentials.
- Manage your account details from the profile section.

### Shopping Cart

- Add products to your cart from the product detail page.
- View your cart and make adjustments as needed.

### Checkout

- Proceed to checkout from your cart.
- Enter shipping details and payment information.
- Review your order and place it.

### Admin Panel

- Access the admin panel to manage products, orders, and users.

## Screenshots

### Homepage

![Homepage](screenshots/homepage.png)

### Product Page

![Product Page](screenshots/product-page.png)

### Cart

![Cart](screenshots/cart.png)

### Checkout

![Checkout](screenshots/checkout.png)

## Contributing

We welcome contributions from the community! Please follow these steps to contribute:

1. **Fork the Repository**

    Click on the 'Fork' button at the top right of the repository page.

2. **Clone Your Fork**

    ```bash
    git clone https://github.com/yourusername/arushop.git
    cd arushop
    ```

3. **Create a New Branch**

    ```bash
    git checkout -b feature/your-feature-name
    ```

4. **Make Your Changes**

    Implement your feature or fix a bug.

5. **Commit and Push**

    ```bash
    git add .
    git commit -m "Describe your feature or fix"
    git push origin feature/your-feature-name
    ```

6. **Open a Pull Request**

    Navigate to the original repository and click on 'New Pull Request'.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For questions or support, please contact us at:

- Email: support@arushop.com
- Twitter: [@arushop](https://twitter.com/arushop)
- GitHub: [Arushop](https://github.com/yourusername/arushop)

---

Thank you for choosing Arushop! We hope you enjoy your shopping experience.
