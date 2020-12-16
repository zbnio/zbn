import gevent.monkey
import multiprocessing

gevent.monkey.patch_all()

bind = '0.0.0.0:8888'

worker_class = 'flask_sockets.worker'

workers = multiprocessing.cpu_count() * 2 + 1
threads = 2

x_forwarded_for_header = 'X-FORWARDED-FOR'
