import csv

def read_dictionary(filename, key_column_index):
    csv_dictionary = {}
    with open(filename, "rt") as file:
        reader = csv.reader(file)
        for row in reader:
            key_value =  row[key_column_index]
            csv_dictionary[key_value] = row
    return csv_dictionary

def main():
    try: 
        product_dict = read_dictionary("products.csv", 0)
        
        with open("request.csv", "rt") as file_content:
            reader = csv.reader(file_content)
            next(reader)

            total_item = 0
            subtotal = 0

            print("INTERNATIONAL STORE")
            for row in reader:
                product_num = row[0]
                quantity = row[1]
                quantity_convert = float(quantity)

                product = product_dict[product_num]

                product_name = product[1]
                price = float(product[2])
                
                item_cost = price * quantity_convert

                total_item += quantity_convert
                subtotal += item_cost

                print(f"{product_name}: {quantity_convert} @ {price:.2f}")

                sales_tax = subtotal * 0.06
                total = subtotal + sales_tax
    except FileNotFoundError as error:
        print("Error: Missing file.")
        print(error)

    except PermissionError as error:
        print("Error: You don't have permission to access this file.")
        print(error)

    except KeyError as error:
        print("Error: Unknown product in the customer's request.")
        print(error)


if __name__ == "__main__":
    main()
