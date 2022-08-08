import os, sys, argparse, json, yaml
from notifications_python_client.notifications import NotificationsAPIClient


class GCNotifySorceController(object):

    api_key: str

    def __init__(self) -> None:
        arg_parser = argparse.ArgumentParser()
        arg_parser.add_argument('-k', '--key', help='Supply a GC Notify API key.')
        arg_parser.add_argument('-p', '--pull', help='Flag to get all templates and parse them into yaml files.', action='store_true')
        arg_parser.add_argument('-c', '--commit', help='Flag to commit the templates.', action='store_true')
        args = arg_parser.parse_args()
    
        if len(sys.argv) < 2:
            arg_parser.print_help(sys.stderr)
            return
            
        if args.key:
            self.set_key(args.key)

        if args.pull:
            self.pull()

        if args.commit:
            self.commit()


    def set_key(self, api_key: str) -> str:
        self.api_key = api_key


    def pull(self) -> None:
        notificactions_client = NotificationsAPIClient(self.api_key)
        print('Retrieving all templates')
        templates = notificactions_client.get_all_templates() # get all templates
        if not templates: return # exit if there are no templates
        with open('./dump.json', mode='w') as file: # write the templates json to dump file
            print('Writing json dump file')
            file.write(json.dumps(templates))


    def commit(self) -> None:
        with open('./dump.json', mode='r') as file: # read templates json dump file
            print('Reading json dump file')
            templates = json.loads(file.read()) # load the object from string
            if not os.path.isdir('./templates'): # create templates directory if it does not exist
                print('Creating templates directory')
                os.mkdir('./templates')
            if not templates['templates']: return # exit if dump object does not have templates
            templates_to_keep = []
            for template in templates['templates']:
                templates_to_keep.append(template['id'])
                with open('./templates/{}.yaml'.format(template['id']), mode='w') as file: # write template data to its yaml file
                    print('Writing yaml file templates/{}.yaml'.format(template['id']))
                    yaml.dump(template, file, default_flow_style=False)
            for filename in os.listdir('./templates'): # delete non-existent templates
                if os.path.splitext(filename)[0] not in templates_to_keep:
                    print('Deleting yaml file templates/{}'.format(filename))


source_controller = GCNotifySorceController()