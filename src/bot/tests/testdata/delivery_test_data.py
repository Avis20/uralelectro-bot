from bot.dto.order import TotalOrderPrice
from faker import Faker

fake = Faker()


class DeliveryTestData:
    @staticmethod
    def get_valid_data():
        price = round(fake.random.uniform(100, 10000), 2)
        quantity = fake.random_int(1, 10)
        address = fake.address()
        
        product_price = float(price * quantity)
        delivery_price = float(2500)
        vat_price = float(product_price * 0.2)
        total_price = product_price + delivery_price + vat_price
        
        return {
            "price": price,
            "quantity": quantity,
            "address": address,
            "expected": TotalOrderPrice(
                product_price=product_price,
                delivery_price=delivery_price,
                vat_price=vat_price,
                total_price=total_price
            )
        }

    @staticmethod
    def get_zero_quantity_data():
        price = round(fake.random.uniform(100, 10000), 2)
        quantity = 0
        address = fake.address()
        
        product_price = float(price * quantity)
        delivery_price = float(2500)
        vat_price = float(product_price * 0.2)
        total_price = product_price + delivery_price + vat_price
        
        return {
            "price": price,
            "quantity": quantity,
            "address": address,
            "expected": TotalOrderPrice(
                product_price=product_price,
                delivery_price=delivery_price,
                vat_price=vat_price,
                total_price=total_price
            )
        }

    @staticmethod
    def get_negative_quantity_data():
        price = round(fake.random.uniform(100, 10000), 2)
        quantity = fake.random_int(-10, -1)
        address = fake.address()
        
        return {
            "price": price,
            "quantity": quantity,
            "address": address
        }

    @staticmethod
    def get_negative_price_data():
        price = round(fake.random.uniform(-10000, -100), 2)
        quantity = fake.random_int(1, 10)
        address = fake.address()
        
        return {
            "price": price,
            "quantity": quantity,
            "address": address
        }
