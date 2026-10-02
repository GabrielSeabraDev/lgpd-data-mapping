# LGPD Data Mapping
# Educational project using fictional data only.

print("LGPD DATA MAPPING")
print("-----------------")
print("Use fictional data only.\n")

processing_activities = []

while True:
    print("\nNEW PROCESSING ACTIVITY")
    print("-----------------------")

    process = input("Process: ")
    data_subject = input("Data subject: ")
    personal_data = input("Personal data: ")
    purpose = input("Purpose: ")
    legal_basis = input("Legal basis: ")
    sharing = input("Data sharing: ")
    retention_period = input("Retention period: ")

    processing_activity = {
        "Process": process,
        "Data subject": data_subject,
        "Personal data": personal_data,
        "Purpose": purpose,
        "Legal basis": legal_basis,
        "Data sharing": sharing,
        "Retention period": retention_period
    }

    processing_activities.append(processing_activity)

    another = input("\nAdd another activity? (y/n): ").lower()

    if another != "y":
        break

print("\nREGISTERED PROCESSING ACTIVITIES")
print("--------------------------------")

for number, activity in enumerate(processing_activities, start=1):
    print(f"\nActivity {number}")

    for field, value in activity.items():
        print(f"{field}: {value}")