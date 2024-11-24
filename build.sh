set -o errexit

pip install -r requirements.txt

python manage.py collecstatic --no-input
pyhton manage.py migrate