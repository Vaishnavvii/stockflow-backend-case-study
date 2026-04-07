
from flask import Flask, jsonify
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route('/api/companies/<int:company_id>/alerts/low-stock', methods=['GET'])
def low_stock_alerts(company_id):
    # Dummy response (simulation)
    alerts = [
        {
            "product_id": 1,
            "product_name": "Sample Product",
            "sku": "SKU-001",
            "warehouse_id": 101,
            "warehouse_name": "Main Warehouse",
            "current_stock": 5,
            "threshold": 10,
            "days_until_stockout": 7,
            "supplier": {
                "id": 201,
                "name": "Sample Supplier",
                "contact_email": "supplier@example.com"
            }
        }
    ]

    return jsonify({
        "alerts": alerts,
        "total_alerts": len(alerts)
    })

if __name__ == '__main__':
    app.run(debug=True)
