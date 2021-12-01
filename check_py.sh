#!/usr/bin/env bash

autopep8 --in-place --aggressive --aggressive "*py"
flake8 . --count --show-source --statistics
pytest
