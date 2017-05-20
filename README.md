# Nightreads

Nightreads is an email and newsletter management app.

## System Dependencies

- Python 3.5

## Installation Instructions

### Local development

1. Set following env variables:

    - `SECRET_KEY`: The [Django secret key](https://docs.djangoproject.com/en/1.9/ref/settings/#std:setting-SECRET_KEY)
    - `SPARKPOST_API_KEY`: Currently Nightreads uses [Sparkpost](https://www.sparkpost.com/) to send emails.

2. Install requirements:

        pip install -r requirements
        pip install ipdb django-debug-toolbar

3. Run migration:

        python manage.py migrate

## License

The mighty MIT license. Please check `LICENSE` for more details.
