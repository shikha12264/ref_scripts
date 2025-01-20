from oms_v2.tasks.hsn_tasks import hsn_upsert
from datetime import datetime, timezone

current_date = datetime.now().isoformat()
effective_date = datetime.now(timezone.utc).isoformat(timespec='seconds')

current_timestamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S%z")
payload = {
    "data": [
        {
            "type": "services",
            "taxes": [
                {
                    "threshold": 0.0,
                    "effective_date": current_timestamp,
                    "rate": 0.25,
                    "cess": 7.0
                }
            ],
            "modified_on": "2025-01-19T19:03:45.796936",
            "description": "export delivery charges",
            "hsn_code": "996819",
            "company_id": 1,
            "modified_by": {
                "user_id": "d440b480e46a0350200265a3",
                "username": "shikhasingh_gofynd_com_42330"
            },
            "country_code": "IN",
            "created_by": {
                "user_id": "f47c84d672d3acad8a2d5590",
                "username": "junaidkazi_gofynd_com_88209"
            },
            "created_on": "2024-11-28T14:34:39",
            "id": "67487f7f7145498827d730bb",
            "reporting_hsn": "996819H2"
        }
    ]
}

# Call the function with the correct structure
hsn_upsert(data=payload["data"], action="upsert")

