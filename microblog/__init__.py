import os
from flask.ext.login import LoginManager
from flask.ext.openid import OpenID
from microblog import settings
from settings import basedir, ADMINS, MAIL_SERVER, MAIL_PORT, MAIL_USERNAME, MAIL_PASSWORD
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(settings)
db = SQLAlchemy(app)

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'login'
oid = OpenID(app, os.path.join(basedir, 'tmp'))

#========================= SMTP setting start ============================
if not app.debug:
    import logging
    from logging.handlers import SMTPHandler
    credentials = None
    if MAIL_USERNAME or MAIL_PASSWORD:
        credentials = (MAIL_USERNAME, MAIL_PASSWORD)
    mail_handler = SMTPHandler((MAIL_SERVER, MAIL_PORT), 'no-reply@' + MAIL_SERVER, ADMINS, 'microblog failure', credentials)
    mail_handler.setLevel(logging.ERROR)
    app.logger.addHandler(mail_handler)
#------------------------- SMTP setting end -------------------------

#========================= log setting start ============================
if not app.debug:
    import logging
    from logging.handlers import RotatingFileHandler
    LOG_FILENAME = 'microblog/tmp/example.log'
    ## Streamhandler could show result console
    #ch = logging.StreamHandler()
    #ch.setFormatter(logging.Formatter("%(asctime)s;%(levelname)s;%(message)s"))

    file_handler = RotatingFileHandler(LOG_FILENAME, 'a', 1 * 1024 * 1024, 10)
    file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))

    file_handler.setLevel(logging.INFO)
    app.logger.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.info('microblog  startup')

    # ============Log Debug messages test============
    #import glob
    #app.logger.setLevel(logging.DEBUG)
    #app.logger.debug('This message let you know you are in debug environment')
    #for i in range(5):
    #    app.logger.debug('i = %d' % i)
    #logfiles = glob.glob('%s*' % LOG_FILENAME)
    #for filename in logfiles:
    #    print(filename)

#------------------------- log setting end -------------------------

from microblog import views, models