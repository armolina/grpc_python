class SaleRecord():
    
    region: str
    country: str
    item_type: str
    sales_channel: str
    order_priority: str
    order_date: str
    order_id: str
    ship_date: str
    units_sold: str
    unit_price: str
    unit_cost: str
    total_revenue: str
    total_cost: str
    total_profit: str    

    def __init__(self, region,country,item_type,sales_channel,order_priority,order_date,order_id,ship_date,units_sold,unit_price,unit_cost,total_revenue,total_cost,total_profit) -> None:
        self.region = region,
        self.country = country,
        self.item_type = item_type,
        self.sales_channel = sales_channel,
        self.order_priority = order_priority,
        self.order = order_date,
        self.order_id = order_id,
        self.ship_date = ship_date,
        self.units_sold = units_sold,
        self.unit_price = unit_price,
        self.unit_cost = unit_cost,
        self.total_revenue = total_revenue,
        self.total_cost = total_cost,
        self.total_profit = total_profit