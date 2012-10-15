pyjsongooglechart
=================

pyjsongooglechart is a simple wrapper around the Google api for Javascript
charts. It is a slightly thicker wrapper than the Python wrapper that Google
provides. It enables the user to easily compile JSON data in the appropriate
format for the charts, without having to worry too much about the structure
of the JSON.


The Basics
----------
This library will provide a wrapper for each of the major Google Javascript
charts.


### Basic Chart
Pie charts are probably the most basic chart; therefore, a good place to start.

```python
from pyjsongooglechart import PieChart

chart = PieChart("Electoral College Votes")
chart.insert_row("California", 55)
chart.insert_row("Nevada", 5)
chart.insert_row("Texas", 34)
json = chart.render_json()
```

Depending on the framework you're using, you'll also need to create
an HTTP response. The following is how you could do it in Django:

```python
from django.http import HttpResponse

return HttpResponse(json, mimetype="application/json")
```

### Next Step
The PieChart produced by the above code is rather simple. However, we can spruce
it up. Google Charts allows you to change the display text for each row. This
library supports that:

```python
chart.insert_row("Washington", (12, "Twelve"))
chart.insert_row("Maine", (4, "Four"))
```

We can also some add some customization to the chart. The following options are
all defined within the Google Charts docs:

```python
chart.options.is3D = True
chart.options.legend.position = "left"
chart.options.height = 500
chart.options.width = 600
```
