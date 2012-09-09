# Safire

This is a dummy application to test using [Flask blueprints](http://guide.python-distribute.org/index.html) and [Python packages](http://guide.python-distribute.org/) to split up a Flask application into reusable application components.

For example, say I have a large Flask application (Myapp), and I want to take out part of it to be its own independent repository, while still using it in my main application. Let's call that application component Safire.

## Usage

To use Safire in Myapp, I first need to add this line to my `requirements.txt` file:

```python
git+git://github.com/nicolahery/safire
```

Then run:

```bash
$ pip install -r requirements.txt
```

Or run directly:

```bash
$ pip install git+git://github.com/nicolahery/safire
```

(You can also specify any branch, tag, or commit by appending `@` to the url, see [Heroku DevCenter](https://devcenter.heroku.com/articles/python-pip#gitbacked-distributions) for more information.)

Afterwards, I only need to register the blueprint to my app:

```python
from safire import safire_blueprint

app.register_blueprint(safire_blueprint, url_prefix='/safire')
```

That's it! Any routes registered by Safire will be available at the url endpoint `/safire`.

Of course, if Safire contains functions that are not web-based I can import those and use them as well.

## Limitations

The only limitation found, was that you have to register the blueprint with a url prefix (`url_prefix='/safire'`) if it uses files in its own `static` directory. (See: [https://github.com/mitsuhiko/flask/issues/348](https://github.com/mitsuhiko/flask/issues/348))

## Setting up the package

This repo can be used as an example to create a blueprint application component, but following are a few things to watch out for.

Make sure when you create the blueprint that you declare the static and templates folder if the blueprint uses them:

```python
safire_blueprint = Blueprint('safire', __name__, 
                                static_folder='static',
                                template_folder='templates')
```

In your blueprint templates, link to any static files using the `url_for` helper method:

```html
<script src="{{ url_for('.static', filename='js/app.js') }}"></script>
```

In the `setup.py` file of the package, use the `package_data` argument to include any static files and templates:

```python
setup(
    ...
    package_data={'safire': ['static/js/*',
                                'templates/*']
    },
)
```
