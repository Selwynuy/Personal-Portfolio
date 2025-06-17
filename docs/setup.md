# Setup Guide

This guide will help you set up the portfolio project for development.

## Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git (optional, for version control)

## Installation Steps

1. **Clone the repository** (if using Git):
   ```bash
   git clone <repository-url>
   cd portfolio
   ```

2. **Create a virtual environment**:
   ```bash
   # Windows
   python -m venv venv
   venv\Scripts\activate

   # Linux/Mac
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**:
   Create a `.env` file in the project root with the following variables:
   ```
   DEBUG=True
   SECRET_KEY=your-secret-key
   EMAIL_HOST=smtp.office365.com
   EMAIL_PORT=587
   EMAIL_HOST_USER=your-email@example.com
   EMAIL_HOST_PASSWORD=your-password
   ```

5. **Run migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Create a superuser**:
   ```bash
   python manage.py createsuperuser
   ```

7. **Collect static files**:
   ```bash
   python manage.py collectstatic
   ```

8. **Run the development server**:
   ```bash
   python manage.py runserver
   ```

## Project Structure

The project follows a modular structure:

- `config/`: Project configuration
  - `settings/`: Django settings
  - `urls.py`: Main URL configuration
- `apps/`: Django applications
  - `core/`: Core functionality
  - `main/`: Main portfolio app
- `static/`: Static files (CSS, JS, images)
- `templates/`: HTML templates
- `media/`: User-uploaded files
- `tests/`: Test files
- `docs/`: Documentation

## Development Workflow

1. Make changes to the code
2. Run tests: `python manage.py test`
3. Check for linting issues: `flake8`
4. Commit changes (if using Git)

## Common Issues

1. **Static files not loading**:
   - Run `python manage.py collectstatic`
   - Check `STATIC_URL` and `STATIC_ROOT` in settings

2. **Database issues**:
   - Delete `db.sqlite3` and run migrations again
   - Check database settings in `config/settings/`

3. **Email not working**:
   - Verify email settings in `.env`
   - Check if using the correct SMTP server

## Next Steps

- Set up a production environment
- Configure a proper database
- Set up CI/CD
- Add more tests
- Improve documentation 