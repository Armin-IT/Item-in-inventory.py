import datetime
inventory={}
suppliers={}
#______________________________________________________________________________
#add_item
def add_item():
   code = input("enter your code item:")
   name = input("enter your name item:")
   quantity = int(input("enter your quantity in stock:"))
   price=float(input("enter yuor unit price:"))
   exp_date=input("expiration date (yyyy-mm_dd):")
   supplier_code=input("supplier code :")

   inventory[code]={
      "name":name,
      "quantity":quantity,
      'price':price,
      'exp':exp_date,
      'supplier':supplier_code,
}
#_____________________________________________________________________________
#delete_item
def delete_item():
   code=input('enter your item code to delete:')
   if code in inventory:
      del inventory[code]
      print('your item deleted successfully!!!!!')
   else:
      print('this item dont have exist!!!!')
#______________________________________________________________________________
#edit-item
def edit_item():
   code=input('enter your item you want edit it:')
   if code in inventory:
      item=inventory[code]
      item['name'] = input(f'name({item['name']}):/n') or item['name']     
      item['quantity'] = int(input(f'quantity({item['quantity']}):/n') or item['quantity'])
      item['price'] = float(input(f'price({item['price']}):') or item['price'])
      item['exp'] = input(f'expiration({item['exp']}):/n' or item['exp'])
   else:
      print('this item not found!!!')
#______________________________________________________________________________
#list_item
def list_item():
   for code, item in inventory.items():
      print(f'code:{code},info:{item}')
#______________________________________________________________________________
#search_item
def search_item():
   keyword = input('enter item name or code to search:')
   for code,item in inventory.items():
      if keyword.lower()in code.lower() or keyword.lower() in item['name'].lower():
         print(f'found:{code} --> {item}')
#_______________________________________________________________________________
#total_value
def total_value():
   print(total = sum(item['quantity']*item['price'] for item in inventory.values()))
#_______________________________________________________________________________
#report
def report():
   today = datetime.datetime.now()
   print('item close to expiration(within 30 day):')
   for code, item in inventory.items():
      exp_date = datetime.datetime.strptime(item['exp'],'%y-%M-%d')
      if (exp_date-today).days<=30:
         print(f'{code}:{item}')
      print('\nitem with low stock (under 10):')
      for code,item in inventory.items():
         if item['quantity']<10:
            print(f'{code}:{item}')
#_______________________________________________________________________________
#manage_suppliers 
def manage_suppliers():
   code = input('supplier___code:')
   name = input('supplier___name:')
   phone= input('supplier__phone:')
   addres=input('supplier_addres:')
   suppliers[code] = {
      'name':name,
      'phone':phone,
      'addres':addres
   }

#____________________________________________________________________________
#sample menu interface(expand as needed)
def main_menu():
   print("""
1.add item
2.delete item
3.edit item
4.list all items
5.search item
6.inventory value
7.generate report
8.manage suppliers
9.exit
""")
   choice = input('choose an 0ptionP:')
   if choice == '1':
      add_item()
   elif choice == '2':
      delete_item()
   elif choice == '3':
      edit_item()
   elif choice == '4':
      list_item()
   elif choice == '5':
      search_item()
   elif choice == '6':
      total_value()
   elif choice == '7':
      report()
   elif choice == '8':
      manage_suppliers()
   elif choice == '9':
      exit()
   else:
      print('invalid choice')
#________________________________________________________________________________
#main loop
while True:
   main_menu()
#________________________________________________________________________________
#finish