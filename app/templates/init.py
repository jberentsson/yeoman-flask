from flask import Flask, url_for
import os

<%= appName %> = Flask(__name__)

# Determines the destination of the build. Only usefull if you're using Frozen-Flask
<%= appName %>.config['FREEZER_DESTINATION'] = os.path.dirname(os.path.abspath(__file__))+'/../build'

# Function to easily find your assets
# In your template use <link rel=stylesheet href="{{ static('filename') }}">
# In your template use <link rel=stylesheet href="{{ bower('filename') }}"> for bower components
<%= appName %>.jinja_env.globals['static'] = (
    lambda filename: url_for('static', filename = filename)
)
<%= appName %>.jinja_env.globals['bower'] = (
    lambda filename: url_for('static', filename = "components/" + filename)
)

from <%= appName %> import views