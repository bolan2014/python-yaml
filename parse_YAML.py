#!/usr/bin/env python

import yaml

# read yaml
fr = open('example.yaml', 'r')

x = yaml.load(fr)
data = x

print x
fr.close()

# write yaml
fw = open('example.yaml', 'w')

data['house']['family']['children'][2] = 123
print data
yaml.dump(data, fw)

fw.close()
