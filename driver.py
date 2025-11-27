from PerformScraping import Scraper
from crn_check import run_crn_lookup


class Driver:

    def main():
        print("Welcome to the Tsunamis CPSC Help Desk!\n")
        print("1) Find the drop date for your semester")
        print("2) Look up a course CRN, prerequisites, and add/drop dates")
        choice = input("Enter your choice (1 or 2): ").strip()

        if choice == "1":
            select_soup = Scraper.getAcademicCalander()
            semesterDropDates = Scraper.getDropDates(select_soup)

            print("\nFind the drop date for your semester!")
            usrchoice = input("Which semester are you looking for? (Fall/Spring/Summer): ")
            print("\n")

            for key, values in semesterDropDates.items():
                if usrchoice.lower() in key.lower():
                    for value in values:
                        print("Drop Dates: ", value)

        elif choice == "2":
            run_crn_lookup()
        else:
            print("Invalid choice.")


    
    
    if __name__ == "__main__":
        main()