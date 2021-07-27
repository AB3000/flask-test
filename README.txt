Usage:

Direct JSON input (execute command from any directory):
curl localhost:5000/post -d "{\"foo\": \"bar\"}" -H 'Content-Type: application/json'


File JSON input (execute command from flask-test/ directory):
curl -vX POST "localhost:5000/post" --data-binary "@files/poe_port_1.json" -H "Content-type:application/json"