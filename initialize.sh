pip3 install PyYAML
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

cp -av gslocalize.py /usr/local/bin
cp -av gslocalize_src /usr/local/bin
cd /usr/local/bin
chmod +x gslocalize.py

echo ""
echo ""
echo "GSLocalize installed. Launch in terminal from any folder with 'gslocalize.py %mode% %path_to_yaml_config%'"