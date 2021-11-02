pip3 install PyYAML
pip3 install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

cp -av gsl.py /usr/local/bin
cp -av gslCreateConfig.py /usr/local/bin
cp -av gslocalize_src /usr/local/bin
chmod +x /usr/local/bin/gsl.py
chmod +x /usr/local/bin/gslCreateConfig.py

cd 

echo "alias gsl=\"python3 /usr/local/bin/gsl.py\"" >> .zshrc
echo "alias gslCreateConfig=\"python3 /usr/local/bin/gslCreateConfig.py\"" >> .zshrc

echo ""
echo ""
echo "GSLocalize installed, please relaunch Terminal. Launch in Terminal from any folder with 'gsl %download|upload% %LocalizableStrings|LocalizablePlist% %path_to_yaml_config%'"