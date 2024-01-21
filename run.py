import gspread
from google.oauth2.service_account import Credentials
from pprint import pprint

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("love_sandwiches")

def get_sales_data():

    """
    get sales data input from the user
    """
    while True:
        print("please enter sales data from the last market.")
        print("data should be six numbers seperated by commas.")
        print("example: 1 , 2 , 3 , 4 , 5 , 6.\n")

        data_str = input("Enter you data here: ")
        
        sales_data = data_str.split(",")

        if validate_data(sales_data):
            print("Data is valid")
            break

    return sales_data

def validate_data(values):

    """
    inside the try statement there will be a check to see if strings
    are there, also value error will be displayed if not intergers
    """

    try: 
        [int(value) for value in values]
        if len(values) != 6:
            raise ValueError(
                f"Exactly six values are required, you have provided {len(values)}")
    except ValueError as e:
        print(f"invalid data: {e}, please try again.\n")
        return False
    
    return True

def update_worksheet(data, worksheet):
    """
    updating worksheet
    """
    print("updating worksheet...\n")
    worksheet_to_update = SHEET.worksheet(worksheet)
    worksheet_to_update.append_row(data)
    print(f"{worksheet} worksheet has been updated successfully.\n")

def calculate_surplus_data(sales_row):
    """
    calculate surplus of each day
    """
    print("calculating surplus data...\n")
    stock = SHEET.worksheet("stock").get_all_values()
    stock_row = stock[-1]

    surplus_data = []

    for stock,sales in zip(stock_row, sales_row):
        surplus = int(stock) - sales
        surplus_data.append(surplus)
    
    return surplus_data

def main():
    """
    program functions
    """
    data = get_sales_data()
    sales_data = [int(num) for num in data]
    new_surplus_data = calculate_surplus_data(sales_data)
    update_worksheet(sales_data, "sales")
    update_worksheet(new_surplus_data, "surplus")
    

print("\nWelcome to love sandwiches data automation service.\n")
main()