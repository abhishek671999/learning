import settings


class A:
    def __init__(self):
        self.loaded_file = settings.env_var['node']['name']
        print(self.loaded_file)