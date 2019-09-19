#Battery class provides the model for batteries
class Battery:
    brand = ''
    output_in_ah = 0 # Amp Hours
    output_in_kwh = 0.0 # KiloWatt Hours
    voltage = 12

    def __init__(self, brand, output_in_ah, voltage):
        self.brand = brand
        self.output_in_ah = output_in_ah
        self.output_in_kwh = self.output_in_ah * self.voltage / 1000
        self.voltage = voltage

    def calculate_hours_from_load(self, load_in_watts):
        runtime = 0.0
        load_in_kilowatts = load_in_watts / 1000
        runtime = self.output_in_kwh / load_in_kilowatts
        return runtime