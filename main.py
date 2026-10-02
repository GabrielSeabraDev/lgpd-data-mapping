# LGPD Data Mapping
# Educational project using fictional data only.

print("LGPD DATA MAPPING")
print("-----------------")
print("Use fictional data only.\n")

process = input("Process: ")
personal_data = input("Personal data: ")
purpose = input("Purpose: ")
legal_basis = input("Legal basis: ")
sharing = input("Data sharing: ")
retention_period = input("Retention period: ")

processing_activity = {
    "Process": process,
    "Personal data": personal_data,
    "Purpose": purpose,
    "Legal basis": legal_basis,
    "Data sharing": sharing,
    "Retention period": retention_period
}

print("\nREGISTERED PROCESSING ACTIVITY")
print("------------------------------")

for field, value in processing_activity.items():
    print(f"{field}: {value}")
