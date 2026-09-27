class Staff:
    def __init__(self,name,staff_id):
        self.name = name
        self.staff_id = staff_id
    def work(self):
        print(self.name)
class Doctor(Staff):
    def __init__(self,name,staff_id,specialization):
        super().__init__(name,staff_id)
        self.specialization = specialization
    def work(self):
        print(f'Dr.{self.name} is examining patients.')
class Nurse(Staff):
    def __init__(self,name,staff_id,ward):
        super().__init__(name,staff_id)
        self.ward = ward
    def work(self):
        print(f'Nurse {self.name} is caring for patients.')
class Receptionist(Staff):
    def __init__(self,name,staff_id,shift):
        super().__init__(name,staff_id)
        self.shift = shift
    def work(self):
        print(f'{self.name} is managing appointments.')
doctor = Doctor('Sara',12345,'OG')
nurse = Nurse('Ali',123456,'CWH')
receptionist = Receptionist('Mia',1234567,'Night')
staff = [doctor,nurse,receptionist]
for staff in staff:
    staff.work()