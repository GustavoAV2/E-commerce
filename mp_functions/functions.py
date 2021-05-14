from mp_functions import ACCESS_TOKEN
from typing import Dict
import mercadopago
import json

sdk = mercadopago.SDK(ACCESS_TOKEN)


def create_preference(product_dictionary: Dict, amount: int = 1):
    preference_data = {
        'back_urls': {'failure': '', 'pending': '', 'success': 'https://undergroundstore-app.herokuapp.com/'},
        "items": [
            {
                "title": str(product_dictionary.get('name')),
                "quantity": amount,
                "currency_id": "BRL",
                "unit_price": float(product_dictionary.get('price'))
            }
        ]
    }

    preference_response = sdk.preference().create(preference_data)
    return json.dumps(preference_response["response"]["init_point"], indent=4)
