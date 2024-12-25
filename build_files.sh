python3 -m pip install --upgrade pip
echo "upgraded pip"

echo "Now will install packages"
python3 -m pip3 install -r requirements.txt
echo "Package installed"

echo "Collecting static folder"
python3 manage.py collectstatic --noinput
echo "Collected"
