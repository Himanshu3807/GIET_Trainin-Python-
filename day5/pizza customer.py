class Customer:
    def __init__(self, name: str, address: str, phone_number: str):
        self.name = name
        self.address = address
        self.phone_number = phone_number
        self.quantity: int = 0

    def validate_quantity(self, quantity: int) -> bool:
        if quantity > 0 and quantity <= 2:
            self.quantity = quantity
            return True
        else:
            return False
class PizzaService:
    counter: int = 100
    def __init__(self, pizza_type: str, additional_topping: bool):
        self.pizza_type: str = pizza_type
        self.additional_topping: bool = additional_topping
        self.pizza_cost: int = 0
        self.service_id: str = chr(ord(pizza_type[0].upper())) + str(PizzaService.counter)
        PizzaService.counter += 1
    def validate_pizza_type(self) -> bool:
        return self.pizza_type.lower() in ['small', 'medium']
    def calculate_pizza_cost(self) -> None:
        if self.validate_pizza_type() and customer.validate_quantity(customer.quantity):
            if self.pizza_type.lower() == 'small':
                self.pizza_cost = 150
            elif self.pizza_type.lower() == 'medium':
                self.pizza_cost = 200
            if self.additional_topping:
                self.pizza_cost += 50
        else:
            self.pizza_cost = -1
class DoorDelivery(PizzaService):
    def __init__(self, pizza_type: str, additional_topping: bool, distance_in_kms: int):
        super().__init__(pizza_type, additional_topping)
        self.distance_in_kms: int = distance_in_kms
        self.delivery_charge: int = 0
    def validate_distance_in_kms(self) -> bool:
        return self.distance_in_kms >= 1 and self.distance_in_kms <= 10
    def calculate_pizza_cost(self) -> None:
        if self.validate_distance_in_kms() and super().validate_pizza_type() and customer.validate_quantity(customer.quantity):
            super().calculate_pizza_cost()
            if self.pizza_cost != -1:
                if self.distance_in_kms <= 5:
                    self.delivery_charge = 5
                else:
                    self.delivery_charge = 5 + (self.distance_in_kms - 5) * 7
        else:
            self.pizza_cost = -1
# Test the program
customer = Customer("John Doe", "123 Main Street", "555-1234")
# Test PizzaService
pizza_service = PizzaService("small", True)
pizza_service.calculate_pizza_cost()
print("PizzaService Details:")
print("Service ID:", pizza_service.service_id)
print("Pizza Type:", pizza_service.pizza_type)
print("Additional Topping:", pizza_service.additional_topping)
print("Pizza Cost:", pizza_service.pizza_cost)
# Test DoorDelivery
door_delivery = DoorDelivery("medium", False, 7)
door_delivery.calculate_pizza_cost()
print("DoorDelivery Details:")
print("Service ID:", door_delivery.service_id)
print("Pizza Type:", door_delivery.pizza_type)
print("Additional Topping:", door_delivery.additional_topping)
print("Distance in KMs:", door_delivery.distance_in_kms)
print("Pizza Cost:", door_delivery.pizza_cost)
print("Delivery Charge:", door_delivery.delivery_charge)
