class Delivery:
    def __init__(self,order_id,destination):
        self.order_id = order_id
        self.destination = destination
    def deliver(self):
        print(f'{self.order_id} delivers {self.destination}')
class Trackable:
    def __init__(self,order_id):
        self.order_id = order_id
    def track(self):
        print(f'Tracking order {self.order_id}...')
class StandardDelivery(Delivery):
    def deliver(self):
        print(f'Order {self.order_id} will arrive in 3-5 days')
class ExpressDelivery(Delivery,Trackable):
    def deliver(self):
        print(f'Order {self.order_id} will arrive within 24 hours')
standard = StandardDelivery("D101",'CWH')
express = ExpressDelivery("D102",'CWH')
deliveries = [standard,express]
for delivery in deliveries:
    delivery.deliver()
express.track()