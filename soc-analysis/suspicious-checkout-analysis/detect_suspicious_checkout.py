import json

with open('example-logs.json') as f:
    data = json.load(f)

suspicious = []

for order in data["data"]:
    reasons = []
    if order.get("delivered") is False and order["deliveryPrice"] == 0:
        reasons.append("Delivery is free and not marked as delivered")
    if "Bearer " in order.get("authHeader", ""):
        reasons.append("Authorization token found in log")
    if order["totalPrice"] < 5 or order["totalPrice"] > 100:
        reasons.append(f"Unusual total price: {order['totalPrice']}")

    if reasons:
        suspicious.append({"orderId": order["orderId"], "reasons": reasons})

print(json.dumps(suspicious, indent=2))
