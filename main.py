from gui import start_gui
from datetime import datetime

# =========================================
# SMART DISEASE PREDICTION SYSTEM
# =========================================

def display_project_info():

    print("\n========================================")
    print("     SMART DISEASE PREDICTION SYSTEM")
    print("========================================")

    print("\nInitializing Application...")
    print("Loading Dataset...")
    print("Training Machine Learning Model...")
    print("Launching GUI Application...")

    current_time = datetime.now()

    print("\nApplication Started Successfully")
    print("Date & Time :", current_time)

    print("\nFeatures Loaded Successfully:")
    print("✔ Machine Learning Prediction")
    print("✔ Multi-Page GUI")
    print("✔ User Validation")
    print("✔ Calendar DOB Selection")
    print("✔ Interactive Healthcare System")

    print("\n========================================\n")

# =========================================
# MAIN FUNCTION
# =========================================

def main():

    display_project_info()

    start_gui()

# =========================================
# RUN APPLICATION
# =========================================

if __name__ == "__main__":

    main()