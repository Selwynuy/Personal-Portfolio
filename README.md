# Personal Portfolio

A modern, responsive personal portfolio website built with Django.

## Features

- Responsive design
- Project showcase
- Skills and timeline display
- Contact form
- Modern UI with animations

## Project Structure

```
portfolio/
├── manage.py
├── requirements.txt
├── .gitignore
├── README.md
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── development.py
│   │   └── production.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── apps/
│   ├── core/
│   └── main/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── components/
│   └── main/
├── media/
├── tests/
└── docs/
```

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run migrations:
   ```bash
   python manage.py migrate
   ```

4. Create a superuser:
   ```bash
   python manage.py createsuperuser
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Development

- Development settings are in `config/settings/development.py`
- Production settings are in `config/settings/production.py`
- Static files are in `static/`
- Templates are in `templates/`
- Media files are in `media/`

## Testing

Run tests with:
```bash
python manage.py test
```

## Deployment

1. Set `DEBUG = False` in production settings
2. Update `ALLOWED_HOSTS` with your domain
3. Set up a proper database
4. Configure static and media file serving
5. Set up SSL/TLS
6. Use a production-grade server (e.g., Gunicorn)
7. Set up a reverse proxy (e.g., Nginx)

## Email Sending (Resend Test Mode)

- **In test mode (no verified domain):**
  - You can only send emails to the email address you used to sign up for Resend (e.g., uywenwen@gmail.com).
  - The `from` address must be `onboarding@resend.dev`.
  - Any attempt to send to other addresses will result in a 403 error with a message about verifying a domain.

- **To send to any address in production:**
  1. Go to [resend.com/domains](https://resend.com/domains) and add/verify your domain (follow DNS instructions).
  2. Change the `from` address in your Supabase Edge Function to use an email at your verified domain (e.g., `noreply@yourdomain.com`).
  3. Redeploy your Edge Function after making changes.

- **For local/dev testing:**
  - Only send to your own Resend account email.
  - If you want to test with other addresses, use a different provider (e.g., Gmail SMTP, Mailgun sandbox) or wait until you have a domain.

## License

MIT 