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

### Production (on Heroku)

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

1. Create an app on Heroku and set the same env variables as above and also `ON_HEROKU` to any string:

        heroku create app_name
        heroku config:set SECRET_KEY='something very secret' SPARKPOST_API_KEY='sparkpost_key' ON_HEROKU='OHYEAH'

2. Push to Heroku and run migration:

        git push heroku master
        heroku run python manage.py migrate --settings='nightreads.settings.heroku'

## License

The mighty MIT license. Please check `LICENSE` for more details.
