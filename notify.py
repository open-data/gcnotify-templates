from notifications_python_client.notifications import NotificationsAPIClient
import configparser
from invoke import task
from contextlib import contextmanager

config = configparser.ConfigParser()
config.read('gcnotify.ini')

notificactions_client = NotificationsAPIClient(config.get(section="gcnotify",option="api_key"))   

@task
def pull(ctx):
    templates = notificactions_client.get_all_templates
    print(templates)