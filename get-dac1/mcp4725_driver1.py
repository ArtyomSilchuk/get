import smbus

class MCP4725:
    def __init__(self, dynamic_range, address=0x61, verbose=True):
        self.bus = smbus.SMBus(1)
        
        self.address = address
        self.wm = 0x00  # Write to DAC register
        self.pds = 0x00  # Power Down Selection: Normal mode
        
        self.verbose = verbose
        self.dynamic_range = dynamic_range
        
        if self.verbose:
            print(f"MCP4725 инициализирован по адресу: 0x{self.address:02X}")
            print(f"Динамический диапазон: {self.dynamic_range} В")
            print(f"Разрядность: 12 бит (0-4095)")

    def deinit(self):
        self.bus.close()
        if self.verbose:
            print("MCP4725 деинициализирован")

    def set_number(self, number):
        if not isinstance(number, int):
            print("На вход ЦАП можно подавать только целые числа")
            return

        if not (0 <= number <= 4095):
            print("Число выходит за разрядность MCP4725 (12 бит)")
            number = max(0, min(number, 4095))

        first_byte = self.wm | self.pds | (number >> 8)
        second_byte = number & 0xFF
        
        try:
            self.bus.write_byte_data(self.address, first_byte, second_byte)
        except Exception as e:
            print(f"Ошибка передачи по I2C: {e}")
            return

        if self.verbose:
            print(f"Число: {number}, отправленные по I2C данные: [0x{(self.address << 1):02X}, 0x{first_byte:02X}, 0x{second_byte:02X}]")

    def set_voltage(self, voltage):
        if not (0.0 <= voltage <= self.dynamic_range):
            if self.verbose:
                print(f"Напряжение {voltage:.2f} В выходит за динамический диапазон ЦАП (0.00 - {self.dynamic_range:.2f} В)")
                print("Устанавливаем 0.0 В")
            voltage = 0.0

        # Преобразуем напряжение в 12-битное число
        number = int(voltage / self.dynamic_range * 4095)
        
        # Ограничиваем диапазон 0-4095
        number = max(0, min(number, 4095))
        
        self.set_number(number)
        
        if self.verbose:
            print(f"Установлено напряжение: {voltage:.2f} В, код ЦАП: {number}")


if __name__ == "__main__":
    try:
        dac = MCP4725(3.3, 0x61, True)
        
        while True:
            try:
                voltage = float(input("Введите напряжение в Вольтах: "))
                dac.set_voltage(voltage)
                print()  # Пустая строка для удобства чтения

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    except KeyboardInterrupt:
        print("\nПрограмма завершена пользователем")

    finally:
        dac.deinit()