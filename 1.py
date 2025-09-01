def process_sale(inventory, sku, qty_sold):
    """
    Process a sale by reducing the quantity of a given SKU.

    Args:
        inventory (list of tuples): [(SKU, quantity), ...]
        sku (int): SKU to be sold
        qty_sold (int): Number of units sold

    Returns:
        updated_inventory (list of tuples): Inventory after processing the sale
    """
    updated_inventory = []  # Creates a new empty list called updated_inventory.
    sku_found = False

    for item in inventory:
        current_sku, current_qty = item
        if current_sku == sku:
            sku_found = True
            if current_qty >= qty_sold:
                # Append the updated tuple (SKU, new_qty) to updated_inventory
                updated_inventory.append((current_sku, current_qty - qty_sold))
                print(f"Sale processed: {qty_sold} units of SKU {sku}.")
            else:
                updated_inventory.append((current_sku, current_qty))
                print(f"Insufficient stock for SKU {sku}. Available: {current_qty}")
        else:
            updated_inventory.append(item)

    if not sku_found:
        print(f"SKU {sku} not found in inventory.")

    return updated_inventory


def identify_zero_stock(inventory):
    """
    Identify all SKUs with zero stock.

    Args:
        inventory (list of tuples): [(SKU, quantity), ...]
    Returns:
        zero_stock_list (list of int): SKUs with zero quantity
    """
    zero_stock_list = [sku for sku, qty in inventory if qty == 0]
    if zero_stock_list:
        print(f"Zero stock SKUs: {zero_stock_list}")
    else:
        print("No zero stock items found.")
    return zero_stock_list


# --- Example Usage ---
if __name__ == "__main__":
    inventory = [(101, 50), (102, 20), (103, 0)]

    # Process sales
    inventory = process_sale(inventory, 101, 50)   # Normal sale
    inventory = process_sale(inventory, 102, 25)   # Insufficient stock
    inventory = process_sale(inventory, 107, 10)   # SKU not found

    # Identify zero stock
    zero_stock_items = identify_zero_stock(inventory)

    print("Updated Inventory:", inventory)