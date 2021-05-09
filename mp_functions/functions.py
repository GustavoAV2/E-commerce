from mp_functions import ACCESS_TOKEN
import mercadopago
import json

sdk = mercadopago.SDK(ACCESS_TOKEN)


def create_preference(amount, product):
    preference_data = {
        'back_urls': {'failure': '', 'pending': '', 'success': 'https://undergroundstore-app.herokuapp.com/'},
        "items": [
            {
                "title": product.name,
                "quantity": amount,
                "currency_id": "BRL",
                "unit_price": product.price
            }
        ]
    }

    preference_response = sdk.preference().create(preference_data)
    print(preference_response)
    return json.dumps(preference_response["response"]["init_point"], indent=4)


