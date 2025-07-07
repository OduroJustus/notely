# Django Subscription Platform

A comprehensive Django-based subscription platform that manages users, content, and subscriptions with role-based access control.

## 📋 Overview

This platform provides a subscription-based content management system with the following key features:

- **User Management**: Custom user authentication with email-based login
- **Role-Based Access**: Support for writers, editors, and subscribers
- **Content Management**: Article creation and categorization with rich text editing
- **Subscription System**: PayPal-integrated subscription management
- **Premium Content**: Tiered content access based on subscription status
- **Audit Logging**: Complete audit trail for content modifications

## 🚀 Features

### User Roles
- **Writers**: Create and manage articles and categories
- **Editors**: Edit and moderate content
- **Subscribers**: Access premium content based on subscription plan

### Content Management
- Rich text editor with CKEditor 5
- Article categorization and tagging
- Premium content gating
- Publication workflow
- Audit trail for all content changes

### Subscription System
- PayPal integration for payments
- Multiple subscription plans
- Automatic subscription management
- User subscription status tracking

## 🛠️ Tech Stack

- **Backend**: Django 5.0.14
- **Database**: SQLite (development)
- **Frontend**: Bootstrap 5 with Crispy Forms
- **Rich Text Editor**: CKEditor 5
- **Image Processing**: Pillow
- **Payment Processing**: PayPal (integrated)

## 📦 Installation

### Prerequisites
- Python 3.8+
- pip (Python package installer)

### Setup Instructions

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd subplatform
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the database**
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create a superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Collect static files**
   ```bash
   python manage.py collectstatic
   ```

7. **Run the development server**
   ```bash
   python manage.py runserver
   ```

The application will be available at `http://127.0.0.1:8000/`

## 📁 Project Structure

```
subplatform/
├── account/           # User authentication and management
├── client/            # Subscription management
├── writer/            # Content creation and management
├── static/            # Static files (CSS, JS, images)
├── staticfiles/       # Collected static files
├── subplatform/       # Main project settings
├── manage.py          # Django management script
├── requirements.txt   # Python dependencies
└── db.sqlite3        # SQLite database (development)
```

## 🔧 Configuration

### Environment Variables
Before running in production, make sure to set the following environment variables:

- `SECRET_KEY`: Django secret key
- `DEBUG`: Set to `False` in production
- `ALLOWED_HOSTS`: Comma-separated list of allowed hosts
- `DATABASE_URL`: Database connection string (if not using SQLite)

### CKEditor Configuration
The project includes custom CKEditor 5 configurations for:
- Basic editing toolbar
- Extended editing features
- Custom color palettes
- Image upload and styling
- Table editing capabilities

## 🔐 Security Features

- Email-based authentication
- Custom user model with role-based permissions
- CSRF protection
- Secure password handling
- Role-based access control for content

## 🔄 API Endpoints

The platform provides web-based interfaces for:
- User registration and authentication
- Content management (CRUD operations)
- Subscription management
- Administrative functions

## 📊 Database Models

### CustomUser
- Email-based authentication
- Role flags (writer, editor)
- User profile information

### Subscription
- PayPal integration
- Subscription plans and pricing
- Active/inactive status tracking

### Article
- Rich content with CKEditor
- Category association
- Premium content flagging
- Publication workflow

### Category
- Article categorization
- User-specific categories

### AuditLog
- Change tracking for articles
- User attribution
- Timestamp logging

## 🧪 Testing

Run the test suite with:
```bash
python manage.py test
```

## 📝 Usage

1. **Admin Access**: Visit `/admin/` to manage users, subscriptions, and content
2. **User Registration**: New users can register and select their role
3. **Content Creation**: Writers can create articles and categories
4. **Subscription Management**: Users can subscribe to access premium content
5. **Content Access**: Premium content is gated based on subscription status

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For support and questions, please contact the development team or open an issue in the repository.

---

**Note**: This is a development version. For production deployment, ensure proper security configurations, environment variables, and database setup.

