<p align="center">
	<img src ="https://cdn.urbvan.com/website1.0/menu/logo.svg" alt="Urbvan Transit"
	width="400" height="150"
	/>
</p>

# Consumer app

## Creator Note:

#### Remember:

*"...with great power comes great responsibility"* - _Uncle Ben_

This application was created for devops test only.

If you want to apply to any of our positions please send an email to tech@urbvan.com

Thank u


## Project Organization
 - src : All application source, normally you shouldn't add any file here
 - application: Application logic
 - http_api: Your flask environment.

## Hands on

### Create an env variable file
Required environment variables:
- FLASK_CONFIG=conf.dev.Config
- SECRET_KEY=abcd123

### Setup Environment
- Go to src directory
- Install poetry to manage dependencies: [poetry](https://python-poetry.org/docs/)
- Install dependencies with poetry:
```
poetry install
```

### Run application locally
````
gunicorn --chdir src/http_api main:app --log-level debug  --reload --bind :9001 --workers 1
````

Thank u! good luck and happy coding!
