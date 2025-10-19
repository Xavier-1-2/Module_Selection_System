from kafka import KafkaConsumer
import json

consumer = KafkaConsumer(
    "module_selection_topic",        # Topic name (must match producer)
    bootstrap_servers='localhost:9092',  # Kafka broker
    auto_offset_reset='earliest',    # Read messages from the beginning
    group_id='module_selection_group',   # Consumer group
    value_deserializer=lambda m: json.loads(m.decode('utf-8'))  # Decode JSON messages
)

print("Kafka consumer is running. Listening for module selections...\n")

for message in consumer:
    try:
        # Extract message data
        selection = message.value
        year = selection.get("year")
        semester = selection.get("semester")
        faculty = selection.get("faculty")
        school = selection.get("school")  # optional if producer sends school
        module = selection.get("module")  # optional if producer sends module


        print("Received module selection:")
        print(f"  Year: {year}")
        print(f"  Semester: {semester}")
        print(f"  Faculty: {faculty}")
        if school:
            print(f"  School: {school}")
        if module:
            print(f"  Module: {module}")
        print("---------------------------")

    except Exception as e:
        print(f"Error processing message: {e}")
