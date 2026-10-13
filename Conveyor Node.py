import time
import random
obj = 1
items_processed = 0
labels = ["Tokyo", "Osaka", "Nagoya", "New York", "London", "Seoul", "Sydney", "GAS LEAK"]
conveyorqueue = [
    {"type":"parcel", "weight":random.randint(1, 100), "label":random.choice(labels)},
    {"type":"parcel", "weight":random.randint(1, 100), "label":random.choice(labels)},
    {"type":"parcel", "weight":random.randint(1, 100), "label":random.choice(labels)},
    {"type":"parcel", "weight":random.randint(1, 100), "label":random.choice(labels)},
    {"type":"parcel", "weight":random.randint(1, 100), "label":random.choice(labels)},
    {"type":"parcel", "weight":random.randint(1, 100), "label":random.choice(labels)},
    {"type":"parcel", "weight":random.randint(1, 100), "label":random.choice(labels)},
    {"type":"parcel", "weight":random.randint(1, 100), "label":random.choice(labels)}


]
print ("===AUTOMATED PACKAGE CHECKER CONVEYOR BELT===")
time.sleep(1.5)
print("INITIATING BELT...")
time.sleep(2)
for item in conveyorqueue:
    unapproved = False

    print ("Object", obj)
    time.sleep(1.5)
    print ("Processing...")
    time.sleep(1.5)
    print("WEIGHT:",item["weight"])
    if item["weight"] > 70:
        print("OBJECT TOO HEAVY TO PACKAGE")
        unapproved = True
    else:
        print("OBJECT SUITABLE SIZE")
    time.sleep(1.5)
    print("LABEL:",item["label"])
    if item["label"] != "GAS LEAK":
        print("OBJECT SAFE. SHIPPING TO", item["label"])
    else:
        print("GAS LEAK PRESENT")
        unapproved = True
    time.sleep(1.5)
    print ("DETERMINING OBJECT TYPE...")
    time.sleep(3)
    if unapproved == True:
        print("OBJECT NOT SUITABLE.")
        item["type"] = "Rejected"
        print ("TYPE:", item["type"])
    else:
        print("OBJECT SUITABLE.")
        items_processed += 1
        print("TYPE:", item["type"])
    obj += 1
    time.sleep(3)
print("Package checking complete")
time.sleep(2)
print("Processed", items_processed, "packages")