# install:
# 	pip install --upgrade pip&\
# 	pip install -r requirements.txt
# lint:
# 	pylint --disable=C,R functions.py
	
# test:
# 	python -m pytest -vv --cov=functions test.py


install:
	pip install --upgrade pip
	pip install -r requirements.txt

lint:
	flake8 .
	
test:
	pytest -vv --cov=functions test.py
