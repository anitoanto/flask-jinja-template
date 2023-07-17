# Flask Jinja Template

Boiler plate code for starting full stack application with flask jinja stack. Demo app with dictionary api (https://dictionaryapi.dev) is included.

# Run the project

```
pip install -r requirements.txt
```

```
npm install
```

```
python app.py
```

# Stack

Python - Flask with Jinja templating.

##### CSS

- Tailwind CSS - https://tailwindcss.com/docs/installation/play-cdn
- DaisyUI - https://daisyui.com

##### JS Utility

- https://lodash.com
- https://jquery.com
- https://sweetalert.js.org
- https://flatpickr.js.org

##### Logging

- Javascript - Roarr - https://www.npmjs.com/package/roarr
- Python - Flask app logger - https://circleci.com/blog/application-logging-with-flask

##### Linters & Formatters

Python

- Jinja - https://www.djlint.com
- Python - https://pypi.org/project/black
- JavaScript, CSS - https://prettier.io

# Scripts for formatting code

```
djlint ./templates --reformat --format-css --format-js --profile=jinja
```

```
npm run prettify
```

```
black . --exclude "._[/\\](?:__pycache__|env)[/\\]._"
```

# Scripts for installing dependencing

```
npm install
```

```
pip install -r requirements.txt
```

# Scripts for setting up python virtual env

```
python -m venv env
```

# Scripts for updating dependencies

```
pip freeze >> requirements.txt
```
