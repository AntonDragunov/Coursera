{
        "skus":
        [
        {
        "sku": "046140",
        "warehouseId": 191866,
        "items":
        [
        {
        "type": "FIT",
        "count": 10 | "{string}",
        "updatedAt": "2022-09-08T23:08:00+03:00"
        },
        ...
        ]
        },
        ...
        ]
        }


curl -i -X PUT \
-H 'Authorization: OAuth oauth_token="EA000001B3831EB8", oauth_client_id="23416332"' \
-H 'Content-Type: application/json' \
{
    "skus": [
        {
            "sku": "046140",
            "warehouseId": 191866,
            "items": [
                {
                    "type": "FIT",
                    "count": 4,
                    "updatedAt": "2022-09-08T23:08:00+03:00"
                }
            ]
        },
        {
            "sku": "A101.10",
            "warehouseId": 1,
            "items": [
                {
                    "type": "FIT",
                    "count": 5,
                    "updatedAt": "2020-03-20T15:34:17+03:00"
                }
            ]
        }
    ]
}'
https://api.partner.market.yandex.ru/v2/campaigns/10001/offers/stocks.json