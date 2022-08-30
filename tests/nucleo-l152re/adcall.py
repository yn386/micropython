from pyb import Pin, ADCAll

pins = [Pin.cpu.A0, Pin.cpu.A1, Pin.cpu.A4, Pin.cpu.A6]

# set pins to IN mode, init ADCAll, then check pins are ANALOG
for p in pins:
    p.init(p.IN)
adc = ADCAll(12, 0xD3)
for p in pins:
    print(p)

# set pins to IN mode, init ADCAll with mask, then check some pins are ANALOG
for p in pins:
    p.init(p.IN)
adc = ADCAll(12, 0x03)
for p in pins:
    print(p)

# init all pins to ANALOG
adc = ADCAll(12, 0xFFD3)
print(adc)

# read all channels
for c in range(16):
    print(type(adc.read_channel(c)))

# call special reading functions
print(0 < adc.read_core_temp() < 100)
try:
    core_vbat = adc.read_core_vbat()
    print("core_vbat", core_vbat)
except NotImplementedError:
    print("NotImplementedError")
print(0 < adc.read_core_vref() < 2)
print(0 < adc.read_vref() < 4)
