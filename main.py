import geometry_helper

def get_positive_float_input(prompt: str) -> float:
    """Helper function to get a positive float input from the user."""
    while True:
        try:
            value = float(input(prompt))
            if value <= 0:
                print("Eingabe muss positiv sein. Bitte erneut versuchen.")
            else:
                return value
        except ValueError:
            print("Ungültige Eingabe. Bitte eine Zahl eingeben.")

def main():
    print("Willkommen beim Geometrie-Helfer!")

    while True:
        print("\n--- Hauptmenü ---")
        print("1. Kreis")
        print("2. Rechteck")
        print("3. Dreieck (Fläche)")
        print("4. Würfel")
        print("5. Kugel")
        print("6. Beenden")

        choice = input("Bitte wählen Sie eine Option (1-6): ").strip()

        if choice == '1': # Kreis
            print("\n--- Kreis ---")
            radius = get_positive_float_input("Geben Sie den Radius ein: ")
            try:
                area = geometry_helper.circle_area(radius)
                circumference = geometry_helper.circle_circumference(radius)
                print(f"Fläche: {area:.2f}")
                print(f"Umfang: {circumference:.2f}")
            except ValueError as e:
                print(f"Fehler: {e}")

        elif choice == '2': # Rechteck
            print("\n--- Rechteck ---")
            length = get_positive_float_input("Geben Sie die Länge ein: ")
            width = get_positive_float_input("Geben Sie die Breite ein: ")
            try:
                area = geometry_helper.rectangle_area(length, width)
                perimeter = geometry_helper.rectangle_perimeter(length, width)
                print(f"Fläche: {area:.2f}")
                print(f"Umfang: {perimeter:.2f}")
            except ValueError as e:
                print(f"Fehler: {e}")

        elif choice == '3': # Dreieck
            print("\n--- Dreieck (Fläche) ---")
            base = get_positive_float_input("Geben Sie die Basis ein: ")
            height = get_positive_float_input("Geben Sie die Höhe ein: ")
            try:
                area = geometry_helper.triangle_area(base, height)
                print(f"Fläche: {area:.2f}")
            except ValueError as e:
                print(f"Fehler: {e}")

        elif choice == '4': # Würfel
            print("\n--- Würfel ---")
            side = get_positive_float_input("Geben Sie die Seitenlänge ein: ")
            try:
                volume = geometry_helper.cube_volume(side)
                surface_area = geometry_helper.cube_surface_area(side)
                print(f"Volumen: {volume:.2f}")
                print(f"Oberfläche: {surface_area:.2f}")
            except ValueError as e:
                print(f"Fehler: {e}")

        elif choice == '5': # Kugel
            print("\n--- Kugel ---")
            radius = get_positive_float_input("Geben Sie den Radius ein: ")
            try:
                volume = geometry_helper.sphere_volume(radius)
                surface_area = geometry_helper.sphere_surface_area(radius)
                print(f"Volumen: {volume:.2f}")
                print(f"Oberfläche: {surface_area:.2f}")
            except ValueError as e:
                print(f"Fehler: {e}")

        elif choice == '6':
            print("Auf Wiedersehen!")
            break

        else:
            print("Ungültige Auswahl. Bitte wählen Sie eine Option von 1 bis 6.")

if __name__ == "__main__":
    main()
