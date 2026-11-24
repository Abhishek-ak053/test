import sys
def temperature_conversion(c):
    return (c * 9/5) + 32
print(f"{c}°C is equal to {fahrenheit}°F")
if __name__ == "__main__":
    c = float(sys.argv[1])
    fahrenheit = temperature_conversion(c)
  