import yaml

class Config(yaml.YAMLObject):
    yaml_tag = '!Config'
    yaml_loader = yaml.SafeLoader
