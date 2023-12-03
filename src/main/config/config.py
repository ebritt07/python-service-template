import yaml

config = None

# TODO pick up this config path dynamically
with open('src/main/config/local_config.yaml', 'r') as file:
    config = yaml.safe_load(file)

