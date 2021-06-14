# Created on: 04.03.2021
# Author: LK

class Feature(object):
    def hasFeature(self, feature_class):
        return isinstance(self, feature_class)
