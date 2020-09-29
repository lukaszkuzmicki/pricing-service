from models.alert import Alert

alerts = Alert.all()
print(alerts)
for alert in alerts:
    alert.load_item_price()
    alert.notify_if_price_reached()
    alert.json()

if not alerts:
    print("nie ma alertow")