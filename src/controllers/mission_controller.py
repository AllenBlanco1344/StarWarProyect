from models.mission import Mission
from services.file_service import FileService

class MissionController:
    def __init__(self):
        self.missions = []
        self.file_service = FileService()

    def create_mission(self):
        name = input("Ingrese el nombre de la misión: ")
        planet = input("Ingrese el planeta destino: ")
        starship = input("Ingrese la nave a utilizar: ")
        weapons = self.get_weapons()
        members = self.get_members()

        mission = Mission(name, planet, starship, weapons, members)
        self.missions.append(mission)
        print("Misión creada exitosamente.")

    def modify_mission(self):
        self.view_missions()
        index = int(input("Seleccione el número de la misión a modificar: ")) - 1
        if 0 <= index < len(self.missions):
            self.edit_mission(self.missions[index])
        else:
            print("Misión no encontrada.")

    def view_missions(self):
        for i, mission in enumerate(self.missions):
            print(f"{i + 1}. {mission.name}")

    def save_missions(self):
        self.file_service.save_missions_to_file(self.missions)
        print("Misiones guardadas exitosamente.")

    def load_missions(self):
        self.missions = self.file_service.load_missions_from_file()
        print("Misiones cargadas exitosamente.")

    def get_weapons(self):
        weapons = []
        for _ in range(7):
            weapon = input("Ingrese el nombre de un arma: ")
            if weapon:
                weapons.append(weapon)
            else:
                break
        return weapons

    def get_members(self):
        members = []
        for _ in range(7):
            member = input("Ingrese el nombre de un integrante: ")
            if member:
                members.append(member)
            else:
                break
        return members

    def edit_mission(self, mission):
        print(f"Editando la misión: {mission.name}")
        mission.starship = input("Ingrese la nueva nave a utilizar (o presione Enter para mantener): ") or mission.starship
        mission.weapons = self.get_weapons()
        mission.members = self.get_members()
        print("Misión modificada exitosamente.")
