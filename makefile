FILE_NAME := test_calculator.py
CACHE := ./__pycache__  .coverage ./htmlcov 

.PHONY: clean

coverage:
	@flake8 --max-line-length=255 $(FILE_NAME)
	@coverage run -m unittest $(FILE_NAME)

report: .coverage
	@coverage report
	@coverage html

clean:
	@$(RM) -r $(CACHE)