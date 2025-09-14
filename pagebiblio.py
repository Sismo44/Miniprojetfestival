# coordonnées des scènes
scenes = {"dave": (0, 0),
          "suppo": (50, 50),
          "massey": (300, 300),
          "bruce": (450, 250)
          }

# running order dans l'ordre des scènes : dave, suppo, massey, bruce
# début à 17h
running_order = {   "17h": ["Benediction", "-", "-","Blackbriar"],
                    "18h": ["-", "Darkenhold", "The Gorge", "-"],
                    "19h": ["Lacuna Coil", "-", "-", "Skamold"],
                    "20h": ["-", "Fleshgod Apocalypse", "Klone", "-"],
                    "21h": ["Kerry King","-", "-", "Eivor"],
                    "22h": ["-", "Tribulation", "Solstafir", "-"],
                    "23h": ["Dimmu Borgir", "-", "-", "Finntroll"],
                    "00h": ["-", "Forbidden", "Ihsahn", "-"],
                    "01h": ["Carpenter Brut", "-", "-", "Sir Reg"]
                    }

# souhaits suivant les créneaux dans l'ordre
souhaits = {"17h": ["Blackbriar"],
            "18h": ["Darkenhold", "The Gorge"],
            "19h": ["Lacuna Coil"],
            "20h": ["Fleshgod Apocalypse", "Klone"],
            "21h": ["Kerry King"],
            "22h": ["Solstafir"],
            "23h": ["Dimmu Borgir", "Finntroll"],
            "00h": ["Ihsahn"],
            "01h": ["Carpenter Brut"]
            }