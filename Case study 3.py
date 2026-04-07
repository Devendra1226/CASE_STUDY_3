from abc import ABC, abstractmethod

# Abstract Base Class
class Payment(ABC):
    def __init__(self, user_name):
        self.user_name = user_name
        self.original_amount = 0
        self.final_amount = 0

    @abstractmethod
    def pay(self, amount):
        pass

    def generate_receipt(self):
        print(f"--- Payment Receipt ---")
        print(f"User: {self.user_name}")
        print(f"Original Amount: ₹{self.original_amount:.2f}")
        print(f"Final Amount Paid: ₹{self.final_amount:.2f}")
        print("----------------------\n")

# Credit Card Payment
class CreditCardPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        gateway_fee = 0.02 * amount
        gst = 0.18 * gateway_fee
        self.final_amount = amount + gateway_fee + gst
        print(f"Processing Credit Card Payment...")
        self.generate_receipt()

# UPI Payment
class UPIPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        cashback = 50 if amount > 1000 else 0
        self.final_amount = amount - cashback
        print(f"Processing UPI Payment...")
        self.generate_receipt()

# PayPal Payment
class PayPalPayment(Payment):
    def pay(self, amount):
        self.original_amount = amount
        intl_fee = 0.03 * amount
        conversion_fee = 20
        self.final_amount = amount + intl_fee + conversion_fee
        print(f"Processing PayPal Payment...")
        self.generate_receipt()

# Wallet Payment
class WalletPayment(Payment):
    def __init__(self, user_name, wallet_balance):
        super().__init__(user_name)
        self.wallet_balance = wallet_balance

    def pay(self, amount):
        self.original_amount = amount
        if amount > self.wallet_balance:
            print(f"Wallet Payment Failed: Insufficient balance!")
            self.final_amount = 0
        else:
            self.wallet_balance -= amount
            self.final_amount = amount
            print(f"Processing Wallet Payment...")
        self.generate_receipt()
        print(f"Remaining Wallet Balance: ₹{self.wallet_balance:.2f}\n")

# Function to process any payment (demonstrates polymorphism)
def process_payment(payment, amount):
    payment.pay(amount)

# ===== Demonstration =====
if __name__ == "__main__":
    # Create payment objects
    cc_payment = CreditCardPayment("Alice")
    upi_payment = UPIPayment("Bob")
    paypal_payment = PayPalPayment("Charlie")
    wallet_payment = WalletPayment("David", wallet_balance=2000)

    # Process multiple transactions
    process_payment(cc_payment, 500)
    process_payment(upi_payment, 1500)
    process_payment(paypal_payment, 2000)
    process_payment(wallet_payment, 1800)
    process_payment(wallet_payment, 500)   