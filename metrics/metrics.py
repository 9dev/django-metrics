
class BaseMetric(object):
    name = None

    def get_name(self):
        return self.name


class ValueMetric(BaseMetric):
    value = None

    def get_value(self):
        return self.value


class LineChartMetric(BaseMetric):
    x = []
    y = []
    xlabel = 'X Label'
    ylabel = 'Y Label'

    def get_values(self):
        return zip(self.x, self.y)

    def get_points(self):
        return ['[{},{}]'.format(x, y) for x, y in self.get_values()]
