git clone https://www.github.com/odoo/odoo --depth 1 --branch 16.0 /opt/odoo16/odoo
python3 -m venv odoo-venv
cd /opt/odoo15
cd /opt/odoo16
python3 -m venv odoo-venv
source odoo-venv/bin/activate
pip3 install wheel
pip3 install -r odoo/requirements.txt
deactivate
mkdir /opt/odoo16/odoo-custom-addons
exit
