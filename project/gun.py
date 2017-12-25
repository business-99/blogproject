# import os
# import gevent.monkey
# gevent.monkey.patch_all()
# import logging
# import logging.handlers
# from logging.handlers import WatchedFileHandler

DEBUG = False
timeout = 50
bind = '0.0.0.0:3323'
ALLOWED_HOSTS = ['.jointlike.com', '.jointlike.com.']
workers = 1

# loglevel = 'info'
# access_log_format = '%(t)s %(p)s %(h)s "%(r)s" %(s)s %(L)s %(b)s %(f)s" "%(a)s"'
# accesslog = "/dev/null"
# errorlog = "/dev/null"
# acclog = logging.getLogger('gunicorn.access')
# acclog.addHandler(WatchedFileHandler('/home/test/server/log/gunicorn_access.log'))
# acclog.propagate = False
# errlog = logging.getLogger('gunicorn.error')
# errlog.addHandler(WatchedFileHandler('/home/test/server/log/gunicorn_error.log'))
# errlog.propagate = False