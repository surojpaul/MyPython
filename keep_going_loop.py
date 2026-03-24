keep_going = "YES"
count = 0
while keep_going == "YES":
    count = count + 1
    print("Keep quiet and practice")
    keep_going = input("Do you want me to continue, YES/NO ").strip().upper()
print(f"Total session completed {count}")
print("Stop and Rest")