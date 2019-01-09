import os
import yaml

with open(os.path.join('constructor', 'template-construct.yaml')) as fp:
    template = fp.read()

with open('config.yaml') as fp:
    conf = yaml.load(fp)

with open(os.path.join('constructor', 'construct.yaml'), 'w') as fp:
    fp.write(template.format(conf['espei_version'], conf['pycalphad_version'], conf['build_number']))

