# Django App Secret key
SECRET_KEY = ""

# to send emails
SPARKPOST_API_KEY = "NIGHTREADSOHYEAH"

# From Email to be used in sending mails
SENDER_EMAIL = 'nightreads@devup.in'

# List of email recipients who will receive preview email
PREVIEW_RECEPIENTS = ('hi@nightreads.in', 'v@nightreads.in')

# Django Admins
ADMINS = (
    ('v', 'v@nightreads.in'),
    ('avinassh', 'avinash@nightreads.in')
)

# Postgres DB Settings
DB_SETTINGS = {
    'NAME': 'DB_NAME',
    'USER': 'DB_USERNAME',
    'PASSWORD': 'DB_PASSWORD',
    'HOST': 'localhost',
    'PORT': ''
}
