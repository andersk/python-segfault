#!/bin/sh
set -eux
python -m django migrate --settings=myapp.settings
python -m coverage run --timid -m django test --settings=myapp.settings
