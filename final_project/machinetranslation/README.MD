
cd /home/project/xzceb-flask_eng_fr/final_project/machinetranslation
touch .env
echo "apikey=" >> .env
echo "url=https://api.us-south.language-translator.watson.cloud.ibm.com/instances/5a31567d-f079-47a2-b81a-170105d2ca85" >> .env

pip install virtualenv

virtualenv -p /usr/bin/python3.8 virtualenv_name

source virtualenv_name/bin/activate

python3 -m pip install python-dotenv
python3 -m pip install ibm_watson
python3 -m pip install Flask


(https://www.coursera.org/learn/python-project-for-ai-application-development/discussions/forums/Zaew5s8aEeu2Hwq_Ldnalw/threads/eJk0pGkGEe2xJQrpAvB8UQ)