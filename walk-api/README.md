Install the packages:

`pipenv shell`

Start the server:

`gunicorn --reload walk-api.app`

Test it:

`http localhost:8000/predict`
