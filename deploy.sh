cd /home/renorb03/bs-ecommerce
git pull origin main
. venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput
sudo systemctl restart bsloja