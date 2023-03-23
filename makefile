FILE_NAME := calculator.py
SRC := ./src/$(FILE_NAME)
TEST := ./test/test_$(FILE_NAME)
CACHE := */__pycache__  .coverage ./htmlcov 

.PHONY: clean

flake8:
	@flake8 --max-line-length=255 $(SRC) $(TEST)

run: flake8
	@python3 $(SRC)

test: flake8
	@coverage run -m unittest $(TEST)

report: test
	@coverage report -m
	@coverage html

clean:
	@$(RM) -r $(CACHE)