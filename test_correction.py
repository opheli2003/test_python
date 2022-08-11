import unittest

from exercices import Spaceport, Ship, is_same_ship
from exercices import filter_letters, count_letters, mask_letters, puissances, return_int


class Exercice1Test(unittest.TestCase):
    def test_exercice1_question1(self):
        try:
            ship1 = Ship("Misericorde", "small", "Ann Leckie")
            ship2 = Ship("Épée", "small", "Ann Leckie")
            self.assertFalse(is_same_ship(ship1, ship2), "les vaisseaux ont des names differents")

            ship1 = Ship("Épée", "small", "Ann Leckie")
            ship2 = Ship("Épée", "large", "Ann Leckie")
            self.assertFalse(is_same_ship(ship1, ship2), "les vaisseaux ont des size differentes")

            ship1 = Ship("Justice", "large", "Ann Leckie")
            ship2 = Ship("Justice", "large", "Peter F. Hamilton")
            self.assertFalse(is_same_ship(ship1, ship2), "les vaisseaux ont des auteurs differentes")

            ship1 = Ship("Misericorde", "small", "Ann Leckie")
            ship2 = Ship("Misericorde", "small", "Ann Leckie")
            self.assertTrue(is_same_ship(ship1, ship2), "les deux vaisseaux sont bien les mêmes")
        except NotImplementedError:
            assert False, "question non traitée"

    def test_exercice1_question2(self):
        try:
            spaceport = Spaceport(
                docked=[
                    Ship("Épée", "large", "Ann Leckie"),
                    Ship("Justice", "large", "Ann Leckie"),
                    Ship("Misericorde", "small", "Ann Leckie"),
                ]
            )
            ship = Ship("Épée", "large", "Ann Leckie")
            self.assertTrue(spaceport.contains(ship))

            ship = Ship("Épée", "small", "Ann Leckie")
            self.assertFalse(spaceport.contains(ship))
        except NotImplementedError:
            assert False, "question non traitée"

    def test_exercice1_question3(self):
        try:
            spaceport = Spaceport(
                docked=[
                    Ship("Épée", "large", "Ann Leckie"),
                    Ship("Justice", "large", "Ann Leckie"),
                ]
            )
            ship = Ship("Justice de Toren", "large", "Ann Leckie")
            try:
                spaceport.dock(ship)
            except NotImplementedError:
                raise
            except Exception as exp:
                assert True
            else:
                assert False, "il y a deja 2 large, toutes les places sont occupés"

            spaceport = Spaceport(
                docked=[
                    Ship("Heart of gold", "large", "Douglas Adams"),
                    Ship("Canterbury", "large", "James S.A. Corey"),
                    Ship("Misericorde", "small", "Ann Leckie"),
                    Ship("Scopuli", "small", "James S.A. Corey"),
                    Ship("Hermes", "small", "Egosoft"),
                    Ship("Dolphin", "small", "Egosoft"),
                    Ship("Harrier", "small", "Egosoft"),
                ]
            )
            ship = Ship("Razorback", "small", "James S.A. Corey")
            try:
                spaceport.dock(ship)
            except NotImplementedError:
                raise
            except Exception as exp:
                assert True
            else:
                assert False, "il y a deja 2 large et 5 small, toutes les places sont occupés"

            spaceport = Spaceport()
            ship = Ship("Razorback", "small", "James S.A. Corey")
            try:
                spaceport.dock(ship)
            except NotImplementedError:
                raise
            except Exception as exp:
                assert False, "le dock est vide il y a de la place"
            else:
                assert [docked for docked in spaceport.docked if id(ship) == id(docked)], "le vaisseau ne semble pas être docké"

            spaceport = Spaceport()
            ship = Ship("Razorback", "large", "James S.A. Corey")
            try:
                spaceport.dock(ship)
            except NotImplementedError:
                raise
            except Exception as exp:
                assert False, "le dock est vide il y a de la place"
            else:
                assert [docked for docked in spaceport.docked if id(ship) == id(docked)], "le vaisseau ne semble pas être docké"

            spaceport = Spaceport(
                docked=[
                    Ship("Canterbury", "large", "James S.A. Corey"),
                    Ship("Misericorde", "small", "Ann Leckie"),
                    Ship("Scopuli", "small", "James S.A. Corey"),
                    Ship("Hermes", "small", "Egosoft"),
                    Ship("Dolphin", "small", "Egosoft"),
                    Ship("Harrier", "small", "Egosoft"),
                ]
            )
            ship = Ship("Razorback", "small", "James S.A. Corey")
            try:
                spaceport.dock(ship)
            except NotImplementedError:
                raise
            except Exception as exp:
                assert False,  "il reste une place large pour un vaisseau small"
            else:
                assert [docked for docked in spaceport.docked if id(ship) == id(docked)], "le vaisseau ne semble pas être docké"


        except NotImplementedError:
            assert False, "question non traitée"


    def test_exercice1_question4(self):
        try:
            spaceport = Spaceport(
                docked=[
                    Ship("Misericorde", "small", "Ann Leckie"),
                    Ship("Scopuli", "small", "James S.A. Corey"),
                    Ship("Hermes", "small", "Egosoft"),
                    Ship("Misericorde", "small", "Ann Leckie"),
                ]
            )
            ship = Ship("Misericorde", "small", "Ann Leckie")
            spaceport.undock(ship)
            assert [docked for docked in spaceport.docked if id(ship) == id(docked)] == [], "le vaisseau semble encore être docké"

            ship = Ship("Heart of gold", "Large", "Douglas Adams")
            spaceport = Spaceport(
                docked=[
                    Ship("Misericorde", "small", "Ann Leckie"),
                    Ship("Scopuli", "small", "James S.A. Corey"),
                    Ship("Hermes", "small", "Egosoft"),
                ]
            )
            try:
                spaceport.undock(ship)
            except:
                assert True
            else:
                assert False, "le vaisseau n'est pas docké"
        except NotImplementedError:
            assert False, "question non traitée"


class Exercice2Test(unittest.TestCase):
    def test_exercice2_question1(self):
        try:
            string = "TIRBOUSCHTROUMPF"
            expected = "IOUSCOUM"
            self.assertEqual(filter_letters(string), expected)
        except NotImplementedError:
            assert False, "question non traitée"

    def test_exercice2_question2(self):
        try:
            string = "TIRBOUSCHTROUMPF"
            expected = {'T': 2, 'I': 1, 'R': 2, 'B': 1, 'O': 2, 'U': 2, 'S': 1, 'C': 1, 'H': 1, 'M': 1, 'P': 1, 'F': 1}
            self.assertEqual(count_letters(string), expected)
        except NotImplementedError:
            assert False, "question non traitée"

    def test_exercice2_question3(self):
        try:
            string = "TIRBOUSCHTROUMPF"
            mask = "1011000101010011"
            expected = "TRBCTOPF"
            self.assertEqual(mask_letters(string, mask), expected)
        except NotImplementedError:
            assert False, "question non traitée"

    def test_exercice2_question4(self):
        try:
            start = 4
            end = 10
            expected = [16, 25, 36, 49, 64, 81, 100]
            self.assertEqual(puissances(start, end), expected)
        except NotImplementedError:
            assert False, "question non traitée"


    def test_exercice2_question5(self):
        expected = "42"
        result = return_int()
        self.assertEqual(result, expected)
        self.assertIsInstance(result, str)


if __name__ == '__main__':
    unittest.main()
