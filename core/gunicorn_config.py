import multiprocessing

# bind = "http://unix:/tmp/gunicorn.sock"
bind = "0.0.0.0:8080"
workers = multiprocessing.cpu_count() * 2 + 1
loglevel = 'info'