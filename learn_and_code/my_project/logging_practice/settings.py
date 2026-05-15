import os.path

import yaml

env_var = yaml.safe_load(open(os.path.join(os.path.dirname(__file__), 'config.yml')))
print('File read')