from lection06_Modules.matimatic import task005_creat_base_math_module as base_math

x = base_math.mul  # Плохой приём
y = base_math._START_MULT  # Очень плохой приём
z = base_math.sub(73, 42)
print(x(2, 3))
print(y)
print(z)
