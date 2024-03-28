from api_usage import installs, costs, events, orders

dt = {"date": "2024-03-25"}

installs.installs_fn(dt)
costs.costs_fn(dt)
orders.orders_fn(dt)
events.events_fn(dt)
