

sales_report = [
    {"month": "Jan", "units_sold": 800},
    {"month": "Feb", "units_sold": 1000},
    {"month": "Mar", "units_sold": 900},
    {"month": "Apr", "units_sold": 850},
    {"month": "May", "units_sold": 900},
    {"month": "Jun", "units_sold": 950},
]

if __name__ == "__main__":

    print("------------------")
    print("PROCESSING SALES REPORT DATA...")
    print("------------------")
    print(sales_report)
    # breakpoint()

    #
    # QUESTION A
    #
    # Define a function called top_month,
    # ...which accepts an input parameter called all_months,
    # ... which when invoked as top_month(sales_report)
    # ... will determine which month has the greatest number of units sold,
    # ... and "print" a human-friendly message including the name of that month
    # ... and the corresponding number of units sold (i.e. "Top Month: Feb (1000 units)"):
