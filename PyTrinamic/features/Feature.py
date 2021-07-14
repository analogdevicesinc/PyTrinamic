# Created on: 04.03.2021
# Author: LK

class FeatureProvider(object):
    pass

class Feature(object):

    def has_feature(self, feature_class):
        return isinstance(self, feature_class)

    def list_features(self):
        features = self.__class__.__mro__
        # Filter self
        features = features[1:]
        # Filter FeatureProviders
        features = [feature for feature in features if issubclass(feature, FeatureProvider)]
        # Filter FeatureProvider itself
        features = [feature for feature in features if feature != FeatureProvider]
        # Names only
        features = [feature.__name__ for feature in features]
        return set(features)
