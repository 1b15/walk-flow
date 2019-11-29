Simple API based on [Falcon Framework](https://falconframework.org/).

Install the packages:

`pipenv install`
`pipenv shell`

Start the server:

`gunicorn --reload walk-api.app`

Test it:

`http localhost:8000/predict`

If you have questions, check the [tutorial](https://falcon.readthedocs.io/en/stable/user/tutorial.html)
