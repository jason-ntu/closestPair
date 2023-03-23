FILE_NAME := calculator.py
SRC := src/$(FILE_NAME)
TEST := test/test_$(FILE_NAME)
CACHE := */__pycache__  .coverage ./htmlcov 

.PHONY: test clean

flake8:
	flake8 --max-line-length=255 $(SRC) $(TEST)

requirement:
	pip freeze > requirements.txt

run:
	python3 $(SRC)

test:
	coverage run -m unittest $(TEST)

report: test
	coverage report -m
	coverage html

clean:
	$(RM) -r $(CACHE)