import gspread
from google.oauth2.service_account import Credentials#

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
    print("please enter sales data from the last market.")
    print("data should be six numbers seperated by commas.")
    print("example: 1 , 2 , 3 , 4 , 5 , 6.\n")

    data_str = input("Enter you data here: ")
    print(f"The data provided is {data_str}")

get_sales_data()