from configs_to_format.config_structure.config_field import ConfigField
from configs_to_format.processing.params import ProcessParams
from configs_to_format.yaml_config.yaml_accesor import YamlConfigAccessor

file_pattern = r'.+-config\.yaml'

params = ProcessParams(
    file_pattern= r'.+-config\.yaml',
    config_structure=[
        ConfigField(name='model', accessor=YamlConfigAccessor(path=['id'])),
        MultiConfigFile(name='model', accessor=YamlConfigAccessor(path=['id'])),
    ]
)