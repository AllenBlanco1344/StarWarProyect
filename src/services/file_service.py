from models.mission import Mission
import csv

class FileService:
    def save_missions_to_file(self, missions, filename="missions.csv"):
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Name", "Planet", "Starship", "Weapons", "Members"])
            for mission in missions:
                writer.writerow([mission.name, mission.planet, mission.starship, ",".join(mission.weapons), ",".join(mission.members)])

    def load_missions_from_file(self, filename="missions.csv"):
        missions = []
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                mission = mission(
                    name=row["Name"],
                    planet=row["Planet"],
                    starship=row["Starship"],
                    weapons=row["Weapons"].split(","),
                    members=row["Members"].split(",")
                )
                missions.append(mission)
        return missions
