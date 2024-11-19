from astrapy import DataAPIClient
import os
# Initialize the client
client = DataAPIClient("AstraCS:ZmdvCsGXASzamzwSMQEFpeqC:3655a76fd19d16fee2bb997a6d10432eee29016bb030800f47e97764ab6b9c33")
db = client.get_database_by_api_endpoint(
  "https://46428400-738f-4555-8f4a-9196884d48b3-us-east-2.apps.astra.datastax.com"
)







print(f"Connected to Astra DB: {db.list_collection_names()}")

