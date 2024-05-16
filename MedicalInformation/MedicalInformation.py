class MedicalInformation:
    def __init__(
        self,
        name,
        brithday,
        blood_type,
        phone_number,
        health_conditions,
        allergy_information,
        current_medications,
        history_surgeries_N_medical_events
    ):
        self.name = name
        self.brithday = brithday
        self.blood_type = blood_type
        self.phone_number = phone_number
        self.health_conditions = health_conditions
        self.allergy_information = allergy_information
        self.current_medications = current_medications
        self.history_surgeries_N_medical_events = history_surgeries_N_medical_events

def get_medical_informations():
    medical_informations = []

    jayden = MedicalInformation(
        "Jayden",
        "2000-04-18",
        "B",
        "13600000000",
        "健康",
        "无",
        "无",
        "无",
    )
    medical_informations.append(jayden)

    return medical_informations