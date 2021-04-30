import logging
import os
import sys
import yaml

logger = logging.getLogger(__name__)


class ConfigParser():
    def __init__(self, config_path):

        self.config_path = os.path.abspath(config_path)

        logger.debug("config file: %s", config_path)

        with open(config_path) as f:
            self.config_data = yaml.load(f, Loader=yaml.FullLoader)


    @property
    def inp_path(self):
        p = self.config_data.get("inp_file")
        p = os.path.join(os.path.dirname(self.config_path), p)
        p = os.path.abspath(p)
        return p

    @property
    def cpa_path(self):
        cpa_path = self.config_data.get("cpa_file")
        cpa_path = os.path.join(os.path.dirname(self.config_path), cpa_path)
        cpa_path = os.path.abspath(cpa_path)
        return cpa_path

    @property
    def cpa_data(self):
        with open(self.cpa_path) as f:
            return yaml.load(f, Loader=yaml.FullLoader)

if __name__ == '__main__':
    logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
    parser = ConfigParser(sys.argv[1])
    print(parser.inp_path)