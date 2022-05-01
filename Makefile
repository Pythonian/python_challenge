run:
	flask run
setup: requirements.txt
	pip install -r requirements.txt
clean:
	rm -rf __pycache__
	rm -rf venv
	rm -rf .git