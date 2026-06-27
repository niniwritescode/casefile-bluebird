def show_welcome():
    print("=" * 50)
    print("  CASE FILE: THE BLUEBIRD KILLER")
    print("  STATUS: ACTIVE INVESTIGATION")
    print("=" * 50)
    print()

def read_case_file():
    print("\n[Opening case file...]\n")
    with open("clues.txt", "r") as f:
        contents = f.read()
    print(contents)

def interrogate_suspect():
    suspects = {
        "ethan": "Former dock worker. Knows Maritime rope knots intimately. Has a limp. Recently fired. Was whistleblower against Starbird Holdings 12 years ago. Lost everything.",
        "olivia": "Wife of Victim 5. Marriage problems. Large insurance payout on Daniel Carter's death. Alibi unconfirmed.",
        "nathan": "Was investigating all five victims for corruption linked to Starbird Holdings. Had access to their schedules.",
        "unknown": "Multiple witnesses report a young woman, 24-28, seen near two crime scenes during heavy rain. Dark hooded coat. Identity unknown. Police actively searching."    
    }
    name = input("\nWho do you want to interrogate? (ethan / olivia / nathan / unknown):").lower()
    if name in suspects:
        print(f"\n>>> {name.upper()}: {suspects[name]}")
    else:
        print("Suspect not found.")

def make_accusation():
    print("\n" + "=" * 50)
    print("   FINAL ACCUSATION")
    print("=" * 50)
    print("\nYou have reviewed the evidence.")
    print("You have interrogated the suspects.")
    print("Now name the killer.\n")
    
    print("1. Ethan Cole — former dock worker")
    print("2. Olivia Carter — wife of Victim 5")
    print("3. Nathan Reeves — journalist")
    print("4. Stephanie Cole — financial analyst\n")
    
    answer = input("Your accusation (1-4): ").strip()
    
    if answer == "4":
        print("\n" + "=" * 50)
        print("   CORRECT. CASE CLOSED.")
        print("=" * 50)
        print("""
STEPHANIE COLE. Age 29. Financial Analyst.

Twelve years ago, Starbird Holdings destroyed her family.
Her father Ethan tried to expose the fraud.
They framed him instead. He lost everything.
Her mother never recovered. She died two years later.

Stephanie spent a decade getting close to each victim.
Working inside their companies. Learning their routines.
Waiting.

She drugged their coffee first.
"Men like them don't fear prison. They fear helplessness."
Then she strangled them. Controlled. Deliberate.
The Maritime knot — her father taught her as a child.

BLUEBIRD was the internal codename of the fraud.
She signed every murder with it.
Not as a threat. As a receipt.

The limp, the boots, the planted footprint — all misdirection.
She made you look at her father.

When we brought Ethan in, he said nothing for two hours.
Then, quietly:

Detective: "Who tied the knots?"
Ethan: "...I did."

He had found out three murders in.
He didn't stop her.
He helped her cover it.

STEPHANIE COLE — arrested. Murder x5.
ETHAN COLE — arrested. Accessory x3.

The corrupt men are dead.
The family that exposed them is in prison.

Justice? You decide.
        """)
    elif answer in ["1", "2", "3"]:
        names = {"1": "Ethan Cole", "2": "Olivia Carter", "3": "Nathan Reeves"}
        print(f"\n✗ Wrong. You accused {names[answer]}.")
        print("Stephanie Cole disappears into the city.")
        print("The Bluebird killings stop. No one knows why.")
        print("Case goes cold.")
    else:
        print("Invalid choice.")
    
def review_evidence():
    evidence = [
        "A: Bluebird note - handwriting deliberately disguised.",
        "B: Maritime Constricter Knot - known by sailors, climbers, rescue workers.",
        "C; Footprint size US 10 - star engraving on sole. NOTE: possibly planted.",
        "D: Blue industrial paint on Victim 5's shirt."
        "E: Defensive wounds on Victim 5. Incomplete DNA under fingernails."
    ]
    print("\n--- EVIDENCE LOCKER ---")
    for item in evidence:
        print(f"\n[EVIDENCE {item}]")
        input("Press Enter for next...")
def open_notebook():
    print("\n---DETECTIVE'S NOTEBOOK---")
    print("Type your notes. Type 'done' when finished.\n")
    notes = []
    while True:
        line = input("> ")
        if line.lower() == "done":
            break
        notes.append(line)
    with open("notebook.txt", "a") as f:
        for line in notes:
            f.write(line + "\n")
    print("\nNotes saved to notebook.txt.")

def breaking_news():
    print("\n" + "=" * 50)
    print("   BREAKING: ATTEMPTED SIXTH MURDER")
    print("=" * 50)
    input("\nPress Enter to read the update...\n")
    print("""
Another stormy night.

At 11:47 PM, Detective Marcus received an anonymous tip —
the Bluebird Killer would strike again at Skyline Grand Hotel.
Businessman Leonard Hayes. Room 708.

Marcus noticed the rainfall. The pattern.
He didn't wait for backup.

Inside room 708 — Hayes unconscious on the floor.
Spilled coffee beside him.

Standing at the window:
A young woman. Rain-soaked black coat.
Rope in one hand.
A note marked BLUEBIRD in the other.

Lightning filled the room.

Marcus saw the star-marked boots.
He saw her face.
Cold. Unsurprised. Like she'd been expecting him.

For the first time, the Bluebird Killer had a face.
She dropped the rope and ran before backup arrived.
Hayes survived.

The unknown female suspect is now the primary lead.
    """)
    input("Press Enter to continue...\n")
def main():
    show_welcome()
    while True:
        print("\nWHAT DO YOU WANT TO DO?")
        print("1. Read case file")
        print("2. Interrogate a suspect")
        print("3. Make your accusation")
        print("4. Quit")
        print("5. Review evidence")
        print("6. Open notebook.")
        print("7. Breaking news - sixth murder attempt")
        choice = input("\nEnter 1-7: ")
        if choice == "1":
            read_case_file()
        elif choice == "2":
            interrogate_suspect()
        elif choice == "3":
            make_accusation()
            break
        elif choice == "4":
            print("Case abandoned.")
        elif choice == "5":
            review_evidence()
        elif choice == "6":
            open_notebook()
        elif choice == "7":
            breaking_news()
        else:
            print("Invalid choice.")

main()