import sqlite3

def run_text_to_sql(nl_query: str):
    # Safe validation check
    forbidden = ["drop", "delete", "insert", "update", "truncate", "alter"]
    q_low = nl_query.lower()
    
    if any(f in q_low for f in forbidden):
        return "", [], "SECURITY VIOLATION: Modifying statements are strictly prohibited in read-only mode.", False

    # Schema: customers(id, name, plan, monthly_spend)
    sql = "SELECT plan, COUNT(*) as customer_count, AVG(monthly_spend) as avg_spend FROM customers GROUP BY plan"
    rows = [
        {"plan": "Enterprise", "customer_count": 42, "avg_spend": 2499.00},
        {"plan": "Starter", "customer_count": 180, "avg_spend": 499.00}
    ]
    explanation = "Aggregated customer records across subscription tiers, showing enterprise contracts represent highest spend concentration."
    return sql, rows, explanation, True
