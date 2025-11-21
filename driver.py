from PerformScraping import Scraper
class Driver:

    def main():
        select_soup = Scraper.getAcademicCalander()
        semesterDropDates = Scraper.getDropDates(select_soup)

        print(semesterDropDates)
    
    if __name__ == "__main__":
        main()