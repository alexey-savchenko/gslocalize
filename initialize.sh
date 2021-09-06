pip3 install PyYAML
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

cp -av gslocalize.py /usr/local/bin
cp -av gslocalize_src /usr/local/bin
chmod +x /usr/local/bin/gslocalize.py

echo ""
echo ""
echo "GSLocalize installed, please relaunch Terminal. Launch in Terminal from any folder with 'gslocalize.py %mode% %path_to_yaml_config%'"