clear
echo 'Running built-in Python Mailserver on port 1025'
python -m smtpd -n -c DebuggingServer localhost:1025