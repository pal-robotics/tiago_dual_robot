import yaml
from dataclasses import dataclass
from typing import List, Union, Dict


@dataclass
class RobotSetting:
    name: str
    description: str
    values: List[Union[str, bool]]
    default: Union[str, bool]


class RobotConfiguration:
    def __init__(self, robot_name: str):
        self.robot_name: str = robot_name
        self.configuration: Dict[str, RobotSetting] = self.load_configuration(robot_name)

    def load_configuration(self, robot_name: str) -> Dict[str, RobotSetting]:
        base_path = "/home/user/exchange/tiago_ros2/src/tiago_dual_robot/tiago_dual_description/tiago_dual_description"
        config_file = f"{base_path}/{robot_name}_config.yaml"
        configurations_raw = yaml.load(open(config_file), Loader=yaml.FullLoader)

        configuration = {}
        for config_name in configurations_raw.keys():
            description = configurations_raw[config_name]["description"]
            values = configurations_raw[config_name]["values"]
            default_value = configurations_raw[config_name]["default"]
            setting = RobotSetting(config_name, description, values, default_value)
            configuration[config_name] = setting

        return configuration

    def has_configuration(self, config_name: str) -> bool:

        configuration_exists = config_name in self.configurations
        return configuration_exists

    def get_configuration(self, config_name: str) -> RobotSetting:

        if not self.has_configuration(config_name):
            raise ValueError(f'The robot {self.robot_name} \
                             does not have the argument {config_name}')

        return self.configuration[config_name]
