# Advent of Code 2020

This repository contains my solutions to the [Advent of Code 2020](https://adventofcode.com/2020) programming puzzles.

## Constraints

I have chosen to work with the following constraints, just for the sake of practice:

- All solutions are in Python (tested with Python 3.7)
- Only base Python libraries can be used, except `pytest` which I am using for basic testing 
  (I have not included extensive unit tests this time)

## Conventions

I am using the following conventions:

- To avoid incorporating messy I/O within the solutions, I have dowloaded all the input files, renamed them with the day 
  number as a prefix and placed them in the data directory. 
  I then use a common function to import the data into a list where each element is a line of the input file. You can 
  find the function that does this in `problems/common.py`
- Although each day (except the last) has two puzzles, by convention I want to be able to run each independently, 
  so sometimes my solution for the second part requires computing similar or identical code to the first part. 
  I have used functions wherever possible to avoid code duplication. 

## How to Run the Code

The repository uses `pipenv` to set up dependencies, so use `pipenv install` to create a nice virtual environment for 
you and install the `pytest` dependency.

Here's how to get the answers for a particular day:

- Run `pipenv shell` if you have not already
- Run `python -m problems.day1` for the first day and simply change the day number as needed for subsequent problems 

## How to Run the Tests

For testing, I have simply used the test cases from the problem descriptions in the website. 
I have not included detailed unit tests in this repo.

- Run `pipenv shell` if you have not already
- Run `python -m pytest tests`
