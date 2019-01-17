import math, csv

##def join(numList):
##    s = ''.join(map(str, numList))
##    return s
##
##def remove_duplicates(values):
##    print(values)#debug
##    output = []
##    seen = set()
##    for element in values:
##        for value in element:
##            # If value has not been encountered yet,
##            # ... add it to both list and set.
##            if value not in seen:
##                output.append(value)
##                seen.add(value)
##    trash = join(output)
##    return trash

def restock(List, ID, Amount):

    stock = get_stock()

    for item in stock:
        for GTIN in ID:
            if GTIN in item:
                stock[2] = stock[2] + List[2]


    
def finish_buy(List, Amount):
    order = []
    print("\nOrder Finished!\nYou Shopping List:\n...................")
    stock = get_stock()
    #print(stock)
    #print(List)

    products = []
    numbers = []
    result = []
    result_trash = []

    for i in stock:
        product = i[1]
        products.append(product)
        number = i[2]
        numbers.append(number)
    
    longest_product = product_length(products)
    longest_number = product_length(numbers)

    space = len(longest_product)

    item_found = False
    counter = 0
    counter2= 0

    for ID in List:
        for stocks in stock:
            f = False
            if ID in stocks:
                #print("Found")
                result.append(stocks)
                f = True
                break

        if not f:
            result_trash.append(ID)

    quantity_counter = 0

    for item in result:
        item[2] = Amount[quantity_counter]
        quantity_counter += 1
        #print(item)
        
    space = product_length(product)

    counter = 0

    for item in result:

        space2 = len(longest_product)-len(item[1])
        space3 = len(longest_number)-len(item[2])
        space4 = len(longest_product)-len("Item")

        if counter == 0:
            print()
            print("GTIN" + (10-len("GTIN"))*" ", "Item", (space4-2)*" ", "Quant.", " Price")
            print("-"*50)
        counter += 1
            
        print(item[0] + 2*" " + item[1] + (space2+2)*" " + item[2] + (space3+4)*" " + item [3])

    for item in result_trash:
        print(item ," ", "product not found")

    print()

    for item in result:
        if item != 0:
            #print(item)
            total_cost = float(item[2]) * float(item[3])
        else:
            total_cost = 0.00

    print("Total Cost", 27*".", "£{0:.2f}".format(total_cost))

#------------------------Updating Stock-------------------------------#

    stock_update = get_stock()
##    print("Stock Update:", stock_update)
##
##    print("\n", 20*"-", "Initiating Stock Update", 20*"-")
##    print("\n")


    
    for stocks in stock_update:
        #print("Current Stocks:",stocks)
        for item in result:
            #print("Bought Stocks:",item)
            if item[0] in stocks[0]:
                stocks[2] = int(stocks[2])-int(item[2])
                #print("GTIN Matched! Updating Stock Levels...")

##    print("UPDATED:")
##    for item in stock_update:
##        print(item)

#-------------------------Ending Update------------------------------#

    with open("Stocks.txt", "w") as update_stock:
        writer = csv.writer(update_stock)
        for item in stock_update:
            writer.writerow(item)
        
##    print("\n")
##    print("", 20*"-", "Ending Stock Update", 20*"-")
                
    
def menu_stock_buy():
    item_id = []
    item_numb = []
    finished = False

    print("You will finish ordering when you press enter.")

    while not finished:
        userInput = input("Enter GTIN Code or <<back>>: ")

        if userInput.lower() == "back":
            main()
        if userInput == "":
            finish_buy(item_id, item_numb)
            break

        GTIN = [number for number in userInput]
        #print(len(GTIN))
        if len(GTIN) == 7 or len(GTIN) == 8:
            quant = input("How Many: ")

            print("Next item...")

            item_id.append(userInput)
            item_numb.append(quant)
        else:
            print("Invalid GTIN-8 Code.")


def product_length(word_list):
    longest_word = ''
    for word in word_list:
        if len(word) > len(longest_word):
            longest_word = word        
    return longest_word

def roundup(x):
    return int(math.ceil(x/10)) * 10

def get_stock():
    with open("Stocks.txt", "r") as stocks_list:
        reader = csv.reader(stocks_list)
        stocks = [item for item in reader if item != []]
    #print(stocks)
    return stocks

def validation(code):
    code = list(map(int, code))
    code_copy = list(map(int, code))
    x = 0
    for n in range(4):
        code_copy[x] = code_copy[x] * 3
        x += 2

##    for element in code_copy:
##        print(element)
            

    total = sum(code_copy)
    #print(total)
    closest_ten = roundup(total)

    #print(len(code))

    if len(code) == 7:
        validation = abs(total - closest_ten)
        
        code.append(validation)

##        print("="*40)
##        print("Validated Code:", *code)
##        print("="*40)

        #stock_choice = menu_stock(code)
        print("Not Developed Yet...")
        
    elif len(code) == 8:
        
        if total == closest_ten:
            #stock_choice = menu_stock(code)
            print("Not Developed Yet...")
        else:
            print("Invalid GTIN-8 Code.")
            main()

def menu_start():
    Okay = False
    while not Okay:
        print("\nAmana Corporation™:\n1. Stock List\n2. Buy Stock\n3. Re-Stock\n4. Enter GTIN-8 Code\n")
        choice = input("Say: ")
        if choice == "1" or choice == "2" or choice == "3" or choice == "4":
            Okay = True
    return choice

def introduction():
    print("""
======================================
          Amana Corporation™
  Household and industrial appliances
======================================

This is our online trading website where you can buy
straight from our warehouses.
          """)

def main():
    
    running = True
    
    while running:
        a = False
        choice = menu_start()

        products = []
        numbers = []
        counter = 0
        
        if choice == "1":
            stock = get_stock()
            #print(stock)

            for i in stock:
                product = i[1]
                products.append(product)
                number = i[2]
                numbers.append(number)

            longest_product = product_length(products)
            longest_number = product_length(numbers)

            space = len(longest_product)
            
                
            for item in stock:

                space2 = len(longest_product)-len(item[1])
                space3 = len(longest_number)-len(item[2])
                space4 = len(longest_product)-len("Item")
                
                if counter == 0:
                    print()
                    print("GTIN" + (12-len("GTIN"))*" ", "Item", space4*" ", "Quant.", 2*" ", "Price")
                    print("-"*50)

                print(item[0], 2*" ", item[1], space2*" ", item[2], (space3+4)*" ", item[3])

                counter += 1

        elif choice == "2":
            menu_stock_buy()
            break

        elif choice == "3":
            stock = get_stock()

            restock = []
            restock_code = []
            restock_amount = []

            while True:
                print("Press ENTER to finish re-stock!")
                userInput = input("Enter GTIN or <<back>>: ")

                if userInput.lower() == "back":
                    break
                if userInput.lower() == "" or userInput.lower() == " ":
                    break

                userAmount = int(input("Amount: "))
                
                restock_code.append(userInput)
                restock_amount.append(userAmount)

            #print(restock_code)
            #print(restock_amount)

            print("\nSupplier View\n")
            
            for item in stock:
                print("DEBUG ITEM:", item)
                for ID in restock_code:
                    print("DEBUG ID:", ID)
                    if ID in item:
                        print("ID MATCHED. RE-STOCKING!")
                        restock.append(item)

            print("\nRESTOCK:")
            for item in restock:
                print(item)

            restock_counter = 0

            for item in restock:
                item[2] = int(item[2]) + int(restock_amount[restock_counter])
                restock_counter += 1
                
            print("UPDATED STOCK:")
            for item in restock:
                print(item)

            for stocks in stock:
                for new_stocks in restock:
                    if new_stocks[0] in stocks[0]:
                        stocks = new_stocks

            print("\nNEW STOCKS:")
            for item in stock:
                print(item)

            with open("Stocks.txt", "w") as restock:
                writer = csv.writer(restock)
                for item in stock:
                    writer.writerow(item)
                    
                        

            
        elif choice == "4":
            Valid = False
            while not Valid:
                userInput = input("Enter the GTIN-8 code or <<back>>: ")

                if userInput.lower() == "back":
                    a = True
                    break
                    
                GTIN = [number for number in userInput]
                #print(len(GTIN))
                if len(GTIN) == 7 or len(GTIN) == 8:
                    Valid = True
                else:
                    print("Invalid GTIN-8 Code.")
            if a:
                continue
            elif not a:
                validation(userInput)
                break
                


        #print(GTIN)

introduction()
main()
