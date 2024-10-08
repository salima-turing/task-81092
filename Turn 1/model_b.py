def calculate_tax(amount, tax_rate):
    tax = amount * tax_rate
    return tax

def main():
    product_price = 100
    tax_rate = 0.2
    final_price = product_price + calculate_tax(product_price, tax_rate)
    print("Final price:", final_price)

if __name__ == "__main__":
    main()
