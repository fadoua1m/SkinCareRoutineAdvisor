# List of questions to ask the user about their skin
questions = [
    {"id": 1, "question": "Quel est votre type de peau ? ", 
     "choices": ["sèche", "grasse", "mixte", "normale"]},
    {"id": 2, "question": "Avez-vous des pores dilatés ? ", 
     "choices": ["oui", "non"]},
    {"id": 3, "question": "Avez-vous de l'acné ? ", 
     "choices": ["oui", "non"]},
    {"id": 4, "question": "Ressentez-vous des rougeurs ? ", 
     "choices": ["oui", "non"]},
    {"id": 5, "question": "Avez-vous des démangeaisons ? ", 
     "choices": ["oui", "non"]},
    {"id": 6, "question": "Votre peau ressent-elle des tiraillements ?", 
     "choices": ["oui", "non"]},
    {"id": 7, "question": "Avez-vous des taches pigmentaires ? ", 
     "choices": ["oui", "non"]},
    {"id": 8, "question": "Votre peau est-elle sensible ?", 
     "choices": ["oui", "non"]},
    {"id": 9, "question": "Avez-vous des rides ou des signes de vieillissement ? ", 
     "choices": ["oui", "non"]}
]


# List of rules that match the answers to the skin conditions and suggest routines
rules = [
    {
        "conditions": {
            "type": "sèche", "pores": "non", "acné": "non", 
            "rougeurs": "oui", "démangeaisons": "oui", "tiraillement": "oui", "sensibilité": "oui", "taches": "non", "rides": "non"
        },
        "routine": [
            "Nettoyant ultra-doux : Bioderma Sensibio H2O",
            "Crème hydratante : Avène Tolérance Extrême",
            "Sérum apaisant : La Roche-Posay Toleriane Ultra",
            "Protection solaire : Avène Très Haute Protection SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "grasse", "pores": "oui", "acné": "oui", 
            "rougeurs": "non", "démangeaisons": "non", "tiraillement": "non", "sensibilité": "non", "taches": "non", "rides": "non"
        },
        "routine": [
            "Nettoyant purifiant : Effaclar Gel Moussant",
            "Soin anti-acné : La Roche-Posay Effaclar Duo+",
            "Sérum réducteur de pores : Bioderma Sébium Pore Refiner",
            "Protection solaire : Avène Cleanance SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "mixte", "pores": "oui", "acné": "non", 
            "rougeurs": "oui", "démangeaisons": "non", "tiraillement": "non", "sensibilité": "non", "taches": "oui", "rides": "non"
        },
        "routine": [
            "Nettoyant équilibrant : La Roche-Posay Effaclar Gel",
            "Sérum éclaircissant : Caudalie Vinoperfect Radiance Serum",
            "Hydratant apaisant : Avène Antirougeurs",
            "Protection solaire anti-taches : Bioderma Photoderm AR SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "normale", "pores": "non", "acné": "non", 
            "rougeurs": "non", "démangeaisons": "non", "tiraillement": "non", "sensibilité": "non", "taches": "non", "rides": "oui"
        },
        "routine": [
            "Nettoyant anti-âge : Esthederm Lait Démaquillant",
            "Sérum anti-rides : Filorga Time-Filler",
            "Crème raffermissante : Vichy LiftActiv Supreme",
            "Protection solaire anti-âge : La Roche-Posay Anthelios Age Correct SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "sèche", "pores": "non", "acné": "non", 
            "rougeurs": "oui", "démangeaisons": "oui", "tiraillement": "oui", "sensibilité": "oui", "taches": "oui", "rides": "non"
        },
        "routine": [
            "Nettoyant ultra-doux : Bioderma Sensibio H2O",
            "Crème hydratante : Avène Tolérance Extrême",
            "Sérum apaisant : La Roche-Posay Toleriane Ultra",
            "Protection solaire : Avène Très Haute Protection SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "mixte", "pores": "oui", "acné": "oui", 
            "rougeurs": "non", "démangeaisons": "non", "tiraillement": "non", "sensibilité": "non", "taches": "oui", "rides": "non"
        },
        "routine": [
            "Nettoyant purifiant : La Roche-Posay Effaclar Gel",
            "Sérum anti-acné et anti-taches : Uriage Hyséac 3-Regul",
            "Hydratant léger : Avène Cleanance Mat",
            "Protection solaire anti-pigmentation : Bioderma Photoderm Spot SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "grasse", "pores": "oui", "acné": "oui", 
            "rougeurs": "non", "démangeaisons": "non", "tiraillement": "non", "sensibilité": "non", "taches": "non", "rides": "non"
        },
        "routine": [
            "Nettoyant purifiant : Bioderma Sébium Gel Moussant",
            "Sérum anti-acné : La Roche-Posay Effaclar Duo+",
            "Hydratant léger : La Roche-Posay Effaclar H",
            "Protection solaire : Bioderma Photoderm MAX SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "normale", "pores": "non", "acné": "non", 
            "rougeurs": "oui", "démangeaisons": "non", "tiraillement": "oui", "sensibilité": "oui", "taches": "oui", "rides": "non"
        },
        "routine": [
            "Nettoyant doux : Bioderma Sensibio Gel",
            "Sérum hydratant et anti-taches : Caudalie Vinoperfect Fluide Hydratant",
            "Sérum anti-rides : Vichy Minéral 89",
            "Protection solaire anti-pigmentation : Avène D-Pigment SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "sèche", "pores": "non", "acné": "oui", 
            "rougeurs": "non", "démangeaisons": "oui", "tiraillement": "oui", "sensibilité": "non", "taches": "oui", "rides": "non"
        },
        "routine": [
            "Nettoyant doux pour peau sensible : La Roche-Posay Toleriane",
            "Sérum anti-acné : Avene Cleanance Expert",
            "Crème hydratante : Vichy Aqualia Thermal",
            "Protection solaire : Bioderma Photoderm AR SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "mixte", "pores": "non", "acné": "non", 
            "rougeurs": "oui", "démangeaisons": "non", "tiraillement": "non", "sensibilité": "oui", "taches": "non", "rides": "oui"
        },
        "routine": [
            "Nettoyant apaisant : Avène Cleanance",
            "Sérum anti-rides et apaisant : La Roche-Posay Redermic R",
            "Crème anti-rides : Vichy LiftActiv Supreme",
            "Protection solaire anti-âge : La Roche-Posay Anthelios Age Correct SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "normale", "pores": "non", "acné": "non", 
            "rougeurs": "non", "démangeaisons": "non", "tiraillement": "non", "sensibilité": "non", "taches": "oui", "rides": "oui"
        },
        "routine": [
            "Nettoyant doux anti-taches : Bioderma Sensibio",
            "Sérum éclaircissant : Caudalie Vinoperfect",
            "Crème anti-rides et anti-taches : Filorga NCTF-Reverse",
            "Protection solaire anti-âge : La Roche-Posay Anthelios XL SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "sèche", "pores": "non", "acné": "non", 
            "rougeurs": "oui", "démangeaisons": "oui", "tiraillement": "oui", "sensibilité": "oui", "taches": "oui", "rides": "oui"
        },
        "routine": [
            "Nettoyant ultra-doux : Bioderma Sensibio H2O",
            "Crème nourrissante : Avène Cicalfate",
            "Sérum anti-âge : La Roche-Posay Redermic R",
            "Protection solaire : Avène Très Haute Protection SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "mixte", "pores": "oui", "acné": "oui", 
            "rougeurs": "non", "démangeaisons": "non", "tiraillement": "non", "sensibilité": "non", "taches": "oui", "rides": "oui"
        },
        "routine": [
            "Nettoyant purifiant : Bioderma Sébium Gel Moussant",
            "Sérum anti-acné et anti-âge : Caudalie Vinoperfect",
            "Hydratant léger : La Roche-Posay Effaclar H",
            "Protection solaire anti-rides : Vichy Idéal Soleil SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "grasse", "pores": "oui", "acné": "oui", 
            "rougeurs": "oui", "démangeaisons": "non", "tiraillement": "non", "sensibilité": "non", "taches": "non", "rides": "non"
        },
        "routine": [
            "Nettoyant purifiant : Effaclar Gel Moussant",
            "Sérum anti-acné : La Roche-Posay Effaclar Duo+",
            "Hydratant matifiant : Bioderma Sébium Mat Control",
            "Protection solaire : La Roche-Posay Anthelios SPF 50"
        ]
    },
    {
        "conditions": {
            "type": "sèche", "pores": "non", "acné": "non", 
            "rougeurs": "oui", "démangeaisons": "oui", "tiraillement": "oui", "sensibilité": "oui", "taches": "non", "rides": "oui"
        },
        "routine": [
            "Nettoyant doux pour peau sensible : La Roche-Posay Toleriane",
            "Sérum anti-âge : Vichy LiftActiv Serum 10",
            "Crème hydratante : Avène Hydrance Optimale Rich",
            "Protection solaire anti-âge : Bioderma Photoderm AR SPF 50"
        ]
    }
]
# Mapping user input keys to condition keys
key_mapping = {
    "Avez-vous de l'acné ? ": "acné",
    "Avez-vous des démangeaisons ? ": "démangeaisons",
    "Avez-vous des pores dilatés ? ": "pores",
    "Avez-vous des rides ou des signes de vieillissement ? ": "rides",
    "Avez-vous des taches pigmentaires ? ": "taches",
    "Quel est votre type de peau ? ": "type",
    "Ressentez-vous des rougeurs ? ": "rougeurs",
    "Votre peau est-elle sensible ?": "sensibilité",
    "Votre peau ressent-elle des tiraillements ?": "tiraillement"
}
def suggest_routine(user_input):
    # Map user input keys to condition keys using the mapping
    user_conditions = {key_mapping.get(k, k): v for k, v in user_input.items()}
    # Find the matching rule
    for rule in rules:
        all_conditions_met = True
        for key, value in rule["conditions"].items():
            user_value = user_conditions.get(key)
            if user_value != value:
                all_conditions_met = False
                break  
        
        if all_conditions_met:
           return rule["routine"]
        

    
    # If no match, return this message
    return ["Aucune routine ne correspond à vos critères, consultez un dermatologue."]
