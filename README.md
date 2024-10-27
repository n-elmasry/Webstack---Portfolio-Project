# WhiskerHaven 🐾

Welcome to WhiskerHaven, a unique cat hospitality platform that allows cat owners to book stays for their furry friends with trusted hosts while they’re away. This project was built using Django and includes essential features like user registration, listing searches, booking management, and a streamlined admin interface for managing listings.

## Table of Contents
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Features
- **User Authentication**: Register, log in, and log out.
- **Search Listings**: Search for available stays based on location.
- **Booking System**: View listings, check availability, and make bookings.
- **Admin-Only Management**: Admins can create, edit, and delete listings, with management accessible only in the admin panel.
- **Dynamic Pricing Calculation**: Automatically calculates booking prices based on selected dates.
- **Responsive Design**: Styled with Bootstrap, optimized for different screen sizes.

## Technologies Used
- **Backend**: Django 5.1.2
- **Frontend**: HTML, CSS, Bootstrap
- **Database**: SQLite
- **Deployment**: Local development server

## Installation
To set up WhiskerHaven on your local machine:

1. Clone the repository:
   ```bash
   git clone https://github.com/n-elmasry/whiskerhaven.git
   cd whiskerhaven

2. Create a virtual environment:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`

3. Install dependencies:
    ```bash
    pip install -r requirements.txt

4. Run migrations:
    ```bash
    python manage.py migrate

5. Create a superuser to access the Django admin panel:
    ```bash
    python manage.py createsuperuser

6. Run the development server:
    ```bash
    python manage.py runserver

7. Visit http://127.0.0.1:8000 in your browser to view the application.


## Usage
**User**:
- Register an account and log in.
- Browse and search for listings by location.
- Book a stay for specific dates if available.
- Manage your bookings from your profile.

**Admin**:
- Log in with superuser credentials.
- Add or manage listings through the Django admin panel at http://127.0.0.1:8000/admin.
- View bookings and user details in the admin panel.


## Contributing
If you'd like to contribute to WhiskerHaven, please follow these steps:

1. Fork the repository.
2. Create a feature branch (git checkout -b feature-branch-name).
3. Commit your changes (git commit -am 'Add new feature').
4. Push to the branch (git push origin feature-branch-name).
5. Open a Pull Request.

## License

This project is proprietary and all rights are reserved by the creator. Unauthorized use, distribution, or modification of this code is strictly prohibited. For permissions or inquiries, please contact [almassrynada411@gmail.com].

# Copyright (c) 2024 NADA ELMASRY
# All rights reserved.
