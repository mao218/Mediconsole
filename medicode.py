import datetime
import os

FILENAME = "patients.txt"
patient_records = {}

def load_records():
    if not os.path.exists(FILENAME):
        return
    with open(FILENAME, "r") as file:
        for line in file:
            line = line.strip()
            if line:
                pid, name, age, diagnosis, room, date = line.split(" | ")
                patient_records[pid] = {
                    "Name": name,
                    "Age": age,
                    "Diagnosis": diagnosis,
                    "Room": room,
                    "Date of Admission": date
                }

def save_records():
    with open(FILENAME, "w") as file:
        for pid, info in patient_records.items():
            line = f"{pid} | {info['Name']} | {info['Age']} | {info['Diagnosis']} | {info['Room']} | {info['Date of Admission']}"
            file.write(line + "\n")

def add_patient():
    patient_id = input("Enter Patient ID: ")
    if patient_id in patient_records:
        print("Patient ID already exists.")
        return
    name = input("Enter Full Name: ")
    age = input("Enter Age: ")
    diagnosis = input("Enter Diagnosis: ")
    room = input("Enter Room Number: ")
    date_admitted = input("Enter Date of Admission (YYYY-MM-DD): ")

    try:
        datetime.datetime.strptime(date_admitted, "%Y-%m-%d")
    except ValueError:
        print("Invalid date format. Use YYYY-MM-DD.")
        return

    patient_records[patient_id] = {
        "Name": name,
        "Age": age,
        "Diagnosis": diagnosis,
        "Room": room,
        "Date of Admission": date_admitted
    }
    save_records()
    print("Patient added and saved successfully!\n")

def search_patient():
    search_id = input("Enter Patient ID to search: ")
    if search_id in patient_records:
        print("\n--- Patient Record ---")
        for key, value in patient_records[search_id].items():
            print(f"{key}: {value}")
    else:
        print("Patient record not found.\n")

def delete_patient():
    del_id = input("Enter Patient ID to delete: ")
    if del_id in patient_records:
        confirm = input("Are you sure you want to delete this record? (y/n): ")
        if confirm.lower() == 'y':
            del patient_records[del_id]
            save_records()
            print("Patient record deleted and file updated.\n")
        else:
            print("Deletion cancelled.\n")
    else:
        print("Patient record not found.\n")

def view_all_patients():
    if not patient_records:
        print("No patient records available.\n")
        return
    print("\n--- All Patient Records ---")
    for pid, info in patient_records.items():
        print(f"\nPatient ID: {pid}")
        for key, value in info.items():
            print(f"  {key}: {value}")

def show_menu():
    print("\n--- MediConsole: Terminal Patient Records Manager ---")
    print("1. Add New Patient")
    print("2. Search Patient by ID")
    print("3. Delete Patient")
    print("4. View All Patients")
    print("5. Exit")

# Run on startup
load_records()

# Main loop
while True:
    show_menu()
    choice = input("Choose an option (1-5): ")
    if choice == '1':
        add_patient()
    elif choice == '2':
        search_patient()
    elif choice == '3':
        delete_patient()
    elif choice == '4':
        view_all_patients()
    elif choice == '5':
        print("Exiting MediConsole... Goodbye!")
        break
    else:
        print("Invalid choice. Please select 1-5.")
