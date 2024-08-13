from controllers.film_controller import FilmController
from controllers.species_controller import SpeciesController
from controllers.planet_controller import PlanetController
from controllers.character_controller import CharacterController
from controllers.mission_controller import MissionController

class StarWarsSystem:
    def __init__(self):
        self.film_controller = FilmController()
        self.species_controller = SpeciesController()
        self.planet_controller = PlanetController()
        self.character_controller = CharacterController()
        self.mission_controller = MissionController()

    def display_menu(self):
        print("\nBienvenido al Sistema de Información de Star Wars")
        print("Seleccione una opción:")
        print("1. Lista de películas de la saga")
        print("2. Lista de especies de seres vivos")
        print("3. Lista de planetas")
        print("4. Buscar personaje")
        print("5. Gráficos y estadísticas de naves")
        print("6. Gestionar misiones")
        print("7. Salir")

    def run(self):
        while True:
            self.display_menu()
            choice = input("\nIngrese su elección: ")

            if choice == '1':
                self.film_controller.list_films()
            elif choice == '2':
                self.species_controller.list_species()
            elif choice == '3':
                self.planet_controller.list_planets()
            elif choice == '4':
                query = input("\nIngrese parte del nombre del personaje a buscar: ")
                self.character_controller.search_characters(query)
            elif choice == '5':
                self.display_ship_statistics_menu()
            elif choice == '6':
                self.manage_missions()
            elif choice == '7':
                print("¡Hasta luego!")
                break
            else:
                print("Opción inválida. Por favor, intente nuevamente.")

    def display_ship_statistics_menu(self):
        print("\nOpciones de estadísticas de naves:")
        print("1. Gráfico de cantidad de personajes nacidos en cada planeta")
        print("2. Gráfico de características de naves")
        print("3. Estadísticas de naves")
        print("4. Volver al menú principal")

        choice = input("\nIngrese su elección: ")

        if choice == '1':
            self.character_controller.plot_characters_per_planet()
        elif choice == '2':
            self.mission_controller.plot_ship_comparison()
        elif choice == '3':
            self.mission_controller.show_ship_statistics()
        elif choice == '4':
            return
        else:
            print("Opción inválida. Volviendo al menú principal.")

    def manage_missions(self):
        print("\nOpciones de gestión de misiones:")
        print("1. Crear nueva misión")
        print("2. Modificar misión existente")
        print("3. Visualizar misiones")
        print("4. Guardar misiones")
        print("5. Cargar misiones")
        print("6. Volver al menú principal")

        choice = input("\nIngrese su elección: ")

        if choice == '1':
            self.mission_controller.create_mission()
        elif choice == '2':
            self.mission_controller.modify_mission()
        elif choice == '3':
            self.mission_controller.view_missions()
        elif choice == '4':
            self.mission_controller.save_missions()
        elif choice == '5':
            self.mission_controller.load_missions()
        elif choice == '6':
            return
        else:
            print("Opción inválida. Volviendo al menú principal.")

if __name__ == "__main__":
    system = StarWarsSystem()
    system.run()
