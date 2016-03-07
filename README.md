# django-metrics

Django app providing simple metrics dashboard.

## Installation

- Add `metrics` folder to Python path.
- Add `"metrics"` to your `INSTALLED_APPS`.
- Update your `urls.py`:


    from metrics import urls as metrics_urls

    urlpatterns = [
        ...
        url(r'^metrics/', include(metrics_urls)),
    ]

- Create `metrics.py` file and add `METRICS_MODULE` to your `settings.py`. Example:


    METRICS_MODULE = 'myapp.metrics'

## Usage

Firstly, define your metrics in created `metrics.py` file.


    from metrics.metrics import LineChartMetric, ValueMetric

    class MySingleValueMetric(ValueMetric):
        name = 'my single-value metric'
    
        def get_value(self):
            return 123
            
    class MyLineChartMetric(LineChartMetric):
        name = 'my line chart metric'
        xlabel = 'my x label'
        ylabel = 'my y label'
    
        def get_values(self):
            return [
                [1, 1],
                [2, 2],
                [3, 3],
            ]

Now you can analyse your metrics at `/metrics` (accessible for staff members only).

## Demo

`django-metrics` provides a simple demo with example usage. To install it from a console, execute `fab install` command. To run it, type ``fab runserver``.

Of course, to do that you need to have `fabric` installed on your computer.

## Tests

Tests assume that Selenium's ChromeDriver can be found at:
> /usr/bin/chromedriver

It also needs correct permissions. Make sure to run:


    $ sudo chmod a+x /usr/bin/chromedriver

To run all the tests simply type:


    $ fab install
    $ fab testall

## Notes

This package was tested with Python 3.4 and Django 1.8.

## License

MIT
