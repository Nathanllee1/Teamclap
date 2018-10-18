#web: gunicorn teemsnep.wsgi --log-file -
web: waitress-serve --port=$PORT {project_name}.wsgi:application