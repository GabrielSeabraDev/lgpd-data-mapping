# LGPD Data Mapping
# Educational project using fictional data only.

processing_activity = {
    "process": "Customer registration",
    "personal_data": "Name and email address",
    "purpose": "Provide access to the service",
    "legal_basis": "To be evaluated",
    "sharing": "No external sharing",
    "retention_period": "To be defined"
}

print("LGPD DATA MAPPING")
print("-----------------")

for field, value in processing_activity.items():
    print(f"{field}: {value}")
