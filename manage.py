#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

"""
docker network create drf_net
fc40b028e57724547c49f04691b93eaf4dcddaeb2940162e9f448834dfd64c7f
docker run -d --network=drf_net --name=postgres_container -p 5433:5432 -e POSTGRES_DB=dockerDRF -e POSTGRES_USER=postgres -e POSTGRES_PASSWORD=12345 postgres:latest
7af10efff72b0f9b190f282745a94df87ae14db755ba0575e854dd8dbc342760
"""