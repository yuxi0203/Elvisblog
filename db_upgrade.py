#!flask/bin/python
from migrate.versioning import api
from microblog.settings import SQLALCHEMY_DATABASE_URI
from microblog.settings import SQLALCHEMY_MIGRATE_REPO
api.upgrade(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
print 'Current database version: ' + str(api.db_version(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO))
