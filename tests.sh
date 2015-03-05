#!/bin/sh

echo '-------------------------'
echo 'Running CORE tests.'
echo '-------------------------'

python -m unittest discover -s evaluator

echo '-------------------------'
echo 'Running INTEGRATION tests.'
echo '-------------------------'

python manage.py test