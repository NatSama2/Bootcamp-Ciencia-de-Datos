precio_original = input("Ingrese el precio del producto: $")
descuento = input("Ingrese el porcentaje de descuento (sin el %): ")

# Probar ejecutar y mostrar que recibimos los datos

print("Precio ingresado:", precio_original)
print("Descuento ingresado:", descuento)

precio = float(precio_original)  # Convertimos a decimal
porcentaje = float(descuento)    # Convertimos a decimal

# Mostrar el tipo de datos antes y después

print("Tipo de precio_original:", type(precio_original))
print("Tipo de precio:", type(precio))


# Cálculos
valor_descuento = precio * (porcentaje / 100)
precio_final = precio - valor_descuento
iva = precio_final * 0.19
total_con_iva = precio_final + iva

print(f"\n--- Resumen de la compra ---")
print(f"Precio original: ${precio:.2f}")
print(f"Descuento aplicado: {porcentaje:.2f}%") 
print(f"Descuento calculado: ${valor_descuento:.2f}")
print(f"Precio final sin IVA: ${precio_final:.2f}")
print(f"IVA (19%): ${iva:.2f}")
print(f"Precio final con IVA: ${total_con_iva:.2f}")
