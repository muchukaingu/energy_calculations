#Inverter class provides the model inverters
class Inverter:
    brand = ''
    output_in_kva = 0
    output_in_watts = 0
    input_votage = 12
    def __init__(brand, output_in_kva, output_in_watts,input_votage):
        self.brand = brand
        self.output_in_kva = output_in_kva
        self.output_in_watts = brand
        self.input_votage = input_votage