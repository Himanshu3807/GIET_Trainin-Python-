class vehicle:
    def __init__(self,vid,vtype,cost):
        self.vid=vid
        self.vtype=vtype
        self.cost=cost
        self.pamt=0
    def get_vid(self):
        return self.vid
    def set_vid(self,vid):
        self.vid=vid
    def get_vtype(self):
        return self.vtype
    def set_vtype(self,vtype):
        self.vtype=vtype
    def get_cost(self):
        return self.cost
    def set_cost(self,cost):
        self.cost=cost
    def get_pamt(self):
        return self.pamt
    def calc_pamt(self):
        if self.vtype=="Two Wheeler":
            self.pamt=self.cost*0.02
        elif self.vtype=="Four Wheeler":
            self.pamt=self.cost*0.06
        else:
            print("Invalid Vehicle Type")
    def vdetails(self):
        print("\nVehicle ID:", self.vid)
        print("Vehicle Type:", self.vtype)
        print("Vehicle Cost:", self.cost)
        print("Premium Amount:", self.pamt)
two_wheeler=vehicle("Vehicle1", "Two Wheeler", 50000)
two_wheeler.calc_pamt()
two_wheeler.vdetails()
four_wheeler = vehicle("Vehicle2", "Four Wheeler", 100000)
four_wheeler.calc_pamt()
four_wheeler.vdetails()
invalid_vehicle =vehicle("Vehicle3", "Three Wheeler", 75000)
invalid_vehicle.calc_pamt()
invalid_vehicle.vdetails()
