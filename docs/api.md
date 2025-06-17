# API Documentation

This document describes the API endpoints and data structures used in the portfolio project.

## Models

### Project
```python
{
    'title': str,  # Project title
    'description': str,  # Project description
    'image': ImageField,  # Project image
    'url': URLField,  # Project URL (optional)
    'github_url': URLField  # GitHub repository URL (optional)
}
```

### SkillCategory
```python
{
    'name': str  # Category name (e.g., "Frontend", "Backend")
}
```

### Skill
```python
{
    'category': SkillCategory,  # Foreign key to SkillCategory
    'name': str,  # Skill name
    'proficiency': int  # Proficiency percentage (0-100)
}
```

### Timeline
```python
{
    'title': str,  # Event title
    'date': date,  # Event date
    'description': str,  # Event description
    'event_type': str  # One of: 'achievement', 'milestone', 'education', 'experience'
}
```

## Views

### Home View
- **URL**: `/`
- **Method**: GET
- **Description**: Displays the home page with projects, skills, and timeline
- **Context**:
  - `projects`: List of all projects
  - `skill_categories`: List of skill categories with their skills
  - `timeline_events`: List of timeline events

### Contact View
- **URL**: `/contact/`
- **Method**: GET, POST
- **Description**: Handles contact form submissions
- **Form Fields**:
  - `name`: Sender's name
  - `email`: Sender's email
  - `message`: Message content
- **Response**: Redirects to home page after successful submission

## Admin Interface

### Project Admin
- List display: title, url, github_url
- Search fields: title, description
- Filter: None

### SkillCategory Admin
- List display: name
- Search fields: name
- Filter: None

### Skill Admin
- List display: name, category, proficiency
- Search fields: name, category
- Filter: category

### Timeline Admin
- List display: title, date, event_type
- Search fields: title, description
- Filter: event_type

## Static Files

### CSS
- `base.css`: Main stylesheet
- Location: `static/css/`

### JavaScript
- `particles.json`: Particle.js configuration
- Location: `static/js/`

### Images
- Profile and project images
- Location: `static/images/`

## Templates

### Base Template
- `base.html`: Main layout template
- Location: `templates/`

### Main Templates
- `home.html`: Home page
- `about.html`: About section
- `projects.html`: Projects section
- `contact.html`: Contact form
- Location: `templates/main/`

### Component Templates
- `navbar.html`: Navigation bar
- `skills.html`: Skills section
- `timeline.html`: Timeline section
- Location: `templates/components/`

## Security

- CSRF protection enabled
- Form validation
- Secure password handling
- XSS protection
- Clickjacking protection

## Performance

- Static file caching
- Database query optimization
- Template fragment caching
- Image optimization

## Deployment

- Static files served by Nginx
- Media files served by Nginx
- SSL/TLS enabled
- Gunicorn as WSGI server
- PostgreSQL database
- Redis for caching 