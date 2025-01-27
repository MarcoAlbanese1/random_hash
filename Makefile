install:
	pip install --upgrade pip &&\
	pip install -r requirements.txt

lint:
	pylint --disable=R,C random_hash.py

format:
	black *.py

test:
	python -m pytest -vv --cov=hash test_random_hash.py
