from flask import Flask, jsonify
import xmlrpc.client

url = 'http://url:8069'
db = 'bd'
username = 'admin'
password = 'admin'

# Conectar a la API
common = xmlrpc.client.ServerProxy('{}/xmlrpc/2/common'.format(url))
uid = common.authenticate(db, username, password, {})

if uid:
    print('Autenticación exitosa, UID:', uid)
else:
    print('Error en la autenticación')
    exit()

# Conectar al objeto
models = xmlrpc.client.ServerProxy('{}/xmlrpc/2/object'.format(url))

# Buscar clientes
def get_client():
    try:
        customer_ids = models.execute_kw(db, uid, password, 'res.partner', 'search', [[['customer', '=', True]]])
        print('IDs de clientes:', customer_ids)

        # Leer datos de los clientes
        customer_data = models.execute_kw(db, uid, password, 'res.partner', 'read', [customer_ids, ['name', 'email', 'phone']])
        print('Datos de los clientes:', customer_data)
    except Exception as e:
        print('Error al extraer datos de los clientes:', e)

get_client()
