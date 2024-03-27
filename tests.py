class Match:
    def __init__(self, name: str):
        self.name = name
        self.result = "0-0"

    def get_name(self):
        return self.name

    def get_result(self):
        return self.result

    def set_result(self, score):
        self.result = score


class Liste:
    def __init__(self, name_list: str, list_match: list):
        self.list_match = list_match
        self.name_list = name_list

    def get_list(self):
        return self.list_match

    def get_name_list(self):
        return self.name_list


class AllListes:
    def __init__(self):
        self.liste = []

    def get_liste(self):
        return self.liste

    def add_liste_item(self, liste):
        self.liste.append(liste)


class Player:
    def __init__(self, name: str):
        self.name = name
        self.listes = []

    def get_name(self):
        return self.name

    def get_listes(self):
        return self.listes

    def set_listes(self, element):
        self.listes.append(element)


class PlayerProno:
    def __init__(self, player: str, name_list: str, list_match: list):
        self.player = player
        self.name_list = name_list
        self.list_match = list_match
        self.points = 0

    def get_name_list(self):
        return self.name_list

    def get_player(self):
        return self.player

    def get_list_match(self):
        return self.list_match

    def get_points(self):
        return self.points

    def set_points(self):
        total = 0
        for liste in toutes_listes.get_liste():
            if liste.get_name_list() == self.get_name_list():
                for match in liste.get_list():
                    for evenement in self.list_match:
                        if match.name == evenement["nom du match"]:
                            if match.result == evenement["resultat"]:
                                points = 3
                            else:
                                if eval(match.result) == eval(evenement['resultat']):
                                    points = 1
                                elif eval(match.result) > 0 and eval(evenement['resultat']) > 0:
                                    points = 1
                                elif eval(match.result) < 0 and eval(evenement['resultat']) < 0:
                                    points = 1
                                else:
                                    points = 0

                            total += points

        self.points = total


# liste de listes
toutes_listes = AllListes()

# matches
match1 = Match(name="barça - real madrid")
match1.set_result("1-2")
match2 = Match(name="chelsea - man city")
match2.set_result("4-4")
match3 = Match(name="juventus - inter")
match3.set_result("0-0")
matches = [match1, match2, match3]

# instanciation de la liste 1
liste1 = Liste(name_list="liste 1", list_match=matches)

# ajout de la liste 1 à toutes les listes
toutes_listes.add_liste_item(liste1)

# joueur 1
player1 = Player("carlos")

# pronos du joueur 1
list_prono = [
    {"nom du match": "barça - real madrid", "resultat": "1-2"},
    {"nom du match": "chelsea - man city", "resultat": "3-3"},
    {"nom du match": "juventus - inter", "resultat": "1-1"}
]
prono_player1_liste1 = PlayerProno(player=player1.get_name(), name_list="liste 1", list_match=list_prono)

# calcul des points du joueur 1 pour la liste 1
print(prono_player1_liste1.get_points())
prono_player1_liste1.set_points()
print(prono_player1_liste1.get_points())
