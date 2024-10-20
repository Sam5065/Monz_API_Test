#This code is used to get the account balance from the Monzo API
#The access token is used to authenticate the user and get the account balance
#The account ID is used to get the account balance
#The balance is returned in GBP
#The access token is valid for 1 hour

#Importing the required libraries:
import requests

#Access token for authentication
#Insert your access token here:
access_token = ''

#Function to get account ID
def get_account_id():
    url = 'https://api.monzo.com/accounts'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    response = requests.get(url, headers=headers)
    
    #Check if the request was successful
    if response.status_code == 200:
        accounts = response.json()['accounts']
        if accounts:
            return accounts[0]['id']  #Returns the first account's ID
        else:
            print("No accounts found.")
            return None
    else:
        print(f"Failed to get accounts. Status code: {response.status_code}")
        return None

#Function to get balance for the account
def get_balance(account_id):
    url = f'https://api.monzo.com/balance?account_id={account_id}'
    headers = {
        'Authorization': f'Bearer {access_token}'
    }
    
    #Get the balance data
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        balance_data = response.json()
        balance_in_pennies = balance_data['balance']
        currency = balance_data['currency']
        balance_in_pounds = balance_in_pennies / 100  #Convert to pounds
        print(f"Balance: {balance_in_pounds} {currency}")
    else:
        print(f"Failed to get balance. Status code: {response.status_code}")

#Main function to print the account balance
def main():
    account_id = get_account_id()
    if account_id:
        get_balance(account_id)

#Run the main function
if __name__ == '__main__':
    main()