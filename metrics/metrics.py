
class BaseMetric(object):
    name = None

    def get_name(self):
        return self.name


class ValueMetric(BaseMetric):
    value = None

    def get_value(self):
        return self.value
