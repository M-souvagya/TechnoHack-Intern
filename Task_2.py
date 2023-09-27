#Currency converter                                                                               using API 
import requests 

def Convert_currency(amount,toCurrency,fromCurrency):
    #API
    url = f"https://v6.exchangerate-api.com/v6/21c86fd5ad52b6397a12548f/latest/{fromCurrency}"
    #Making the request to the API
    response=requests.get(url)
    data=response.json()
    #extracting the conversion rates
    exchange_rate=data['conversion_rates'][toCurrency]
    #calculating the converted amount
    converted_amount=amount*exchange_rate
    return converted_amount

def currency():
    a=input("\nEnter the name of the currency you want to convert from:")
    fromCurrency=a.upper()
    b=input("\nEnter the name of the currency you want to convert:")
    toCurrency=b.upper()
    amount=float(input(f"\nEnter the amount in {fromCurrency}:"))
    cc=Convert_currency(amount,toCurrency,fromCurrency)
    print(cc) 

x=True
while x==True: 
    currency() 
    y=input('Do you want to convert any other currency? ')
    y=y.upper()
    if y=='YES' or y=='Y':
        x=True
    else :
        print("\n\n--- Thank You ---\n\n")
        break

