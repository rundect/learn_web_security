openssl ecparam -name prime256v1 -genkey -noout -out private_key.pem
openssl req -x509 -nodes -days 3650 -key private_key.pem -out certificate.pem
gunicorn alice.wsgi --keyfile private_key.pem --certfile certificate.pem