import os
import csv
from faker import Faker
import datetime
import uuid

fake = Faker()

def generate_patient_data(n):
    return [{
        "patient_id": str(uuid.uuid4()),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "birthdate": fake.date_of_birth(minimum_age=0, maximum_age=90).isoformat(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "address": fake.address().replace("\n", ", "),
        "gender": fake.random_element(elements=("M", "F", "Other"))
    } for _ in range(n)]

def generate_appointment_data(patients, n):
    return [{
        "appointment_id": str(uuid.uuid4()),
        "patient_id": fake.random_element(elements=patients)["patient_id"],
        "appointment_date": fake.date_time_between(start_date='-1y', end_date='now').isoformat(),
        "doctor_name": fake.name(),
        "department": fake.random_element(elements=["Cardiology", "Neurology", "Oncology", "Pediatrics", "General"])
    } for _ in range(n)]

def generate_prescription_data(patients, n):
    return [{
        "prescription_id": str(uuid.uuid4()),
        "patient_id": fake.random_element(elements=patients)["patient_id"],
        "medication_name": fake.word().capitalize(),
        "dosage": f"{fake.random_int(min=1, max=500)}mg",
        "start_date": fake.date_between(start_date='-1y', end_date='-1d').isoformat(),
        "end_date": fake.date_between(start_date='today', end_date='+6M').isoformat()
    } for _ in range(n)]

def save_to_csv(data, folder, prefix):
    os.makedirs(folder, exist_ok=True)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = os.path.join(folder, f"{prefix}_{timestamp}.csv")
    
    with open(filename, "w", newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
    
    print(f"Saved {len(data)} records to {filename}")
    return filename

if __name__ == "__main__":
    patient_data = generate_patient_data(10)
    appointment_data = generate_appointment_data(patient_data, 15)
    prescription_data = generate_prescription_data(patient_data, 15)

    save_to_csv(patient_data, "data/patients", "patients")
    save_to_csv(appointment_data, "data/appointments", "appointments")
    save_to_csv(prescription_data, "data/prescriptions", "prescriptions")
