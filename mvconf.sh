#!/bin/bash
mv config/config_list/.env config/environment/
# mv config/config_list/.env webapp/chaesmos/

rm webapp/chaesmos/settings.py
mv config/config_list/prod_settings.py webapp/chaesmos/settings.py

mv config/config_list/config.js webapp/chaesmos/static/js/
