import pandas as pd
from ConfigDB import *
import calendar
import datetime



def addCategoryToFile():
    ##############################################################################################
    #  This function adds and populates column 'Category' to the file downloaded from Rabobank.  #
    #  See the first statement in this function for the required file location and name.         #
    #  It will create the new file 'processedTransactions.csv'                                   #
    ##############################################################################################
    fi = 'C:/transactions.csv'
    df = pd.read_csv(fi, encoding="ISO-8859-1")  # latin-1 format; to prevent utf-8 error
    # print(df.info)  # shows dataframe values (rows and columns)
    # add column 'Category' as column 9:
    df.insert(8, 'Category', '')

    # The following statement is required to search strings for specific values; to prevent errors NaN (no value)
    df = df.where(pd.notnull(df), "TemporaryFill")

    # Go over rows in file and populate new column Category with Budget Category

    # Category AbonnementBibliotheek
    df.loc[df['Naam tegenpartij'].str.contains('BIBLIOTHEEK', case=False), ['Category']] = 'AbonnementBibliotheek'

    # Category AbonnementPostcodeLoterij
    df.loc[df['Naam tegenpartij'].str.contains('NAT POSTCODE LOTERIJ', case=False), ['Category']] = 'AbonnementPostcodeLoterij'

    # Category AbonnementSqula
    df.loc[df['Naam uiteindelijke partij'].str.contains('Squla.nl', case=False), ['Category']] = 'AbonnementSqula'

    # Category AutoOnderhoud
    df.loc[df['Naam tegenpartij'].str.contains('Carlux', case=False), ['Category']] = 'AutoOnderhoud'
    df.loc[df['Naam tegenpartij'].str.contains('Nieuwkoop Auto', case=False), ['Category']] = 'AutoOnderhoud'
    df.loc[df['Naam tegenpartij'].str.contains('Schellings Auto', case=False), ['Category']] = 'AutoOnderhoud'
    df.loc[df['Naam tegenpartij'].str.contains('VAN DEN UDENHOUT', case=False), ['Category']] = 'AutoOnderhoud'

    # Category Bankkosten
    df.loc[df['Naam tegenpartij'].str.contains('Kosten', case=False), ['Category']] = 'Bankkosten'

    # Category BenzineParkeerkosten
    df.loc[df['Naam tegenpartij'].str.contains('Esso', case=False), ['Category']] = 'BenzineParkeerkosten'
    df.loc[df['Naam tegenpartij'].str.contains('Shell', case=False), ['Category']] = 'BenzineParkeerkosten'
    df.loc[df['Naam tegenpartij'].str.contains('Parkeren', case=False), ['Category']] = 'BenzineParkeerkosten'
    df.loc[df['Naam tegenpartij'].str.contains('Tango', case=False), ['Category']] = 'BenzineParkeerkosten'
    df.loc[df['Naam tegenpartij'].str.contains('Q PARK', case=False), ['Category']] = 'BenzineParkeerkosten'
    df.loc[df['Naam tegenpartij'].str.contains('TAMOIL', case=False), ['Category']] = 'BenzineParkeerkosten'
    df.loc[df['Naam tegenpartij'].str.contains('TINQ', case=False), ['Category']] = 'BenzineParkeerkosten'

    # Category Fiets
    df.loc[df['Naam tegenpartij'] == 'CCV*Q BIKE', ['Category']] = 'Fiets'

    # Category Gitaarles
    df.loc[df['Naam tegenpartij'] == 'Stichting Medez', ['Category']] = 'Gitaarles'

    # Category Huishouden
    df.loc[df['Naam tegenpartij'].str.contains('Action', case=False), ['Category']] = 'Huishouden' 
    df.loc[df['Naam tegenpartij'].str.contains('Albert Heijn', case=False), ['Category']] = 'Huishouden'
    df.loc[df['Naam tegenpartij'].str.contains('Aldi', case=False), ['Category']] = 'Huishouden'
    df.loc[df['Naam tegenpartij'].str.contains('Coop Supermarkt', case=False), ['Category']] = 'Huishouden'
    df.loc[df['Naam tegenpartij'].str.contains('EMTE', case=False), ['Category']] = 'Huishouden'
    df.loc[df['Naam tegenpartij'].str.contains('Jumbo', case=False), ['Category']] = 'Huishouden'
    df.loc[df['Naam tegenpartij'].str.contains('Kruidvat', case=False), ['Category']] = 'Huishouden'
    df.loc[df['Naam tegenpartij'].str.contains('Lidl', case=False), ['Category']] = 'Huishouden'
    df.loc[df['Naam tegenpartij'].str.contains('Nettorama', case=False), ['Category']] = 'Huishouden'

    # Category HypotheekRente
    df.loc[df['Omschrijving-1'].str.contains('RENTE LENING', case=False), ['Category']] = 'HypotheekRente'

    # Category InlegBanksparenHypotheek
    df.loc[df['Omschrijving-1'].str.contains('OpbouwSpaarrekening', case=False), ['Category']] = 'InlegBanksparenHypotheek'

    # Category Kapper
    df.loc[df['Omschrijving-1'].str.contains('kapper', case=False), ['Category']] = 'Kapper'
    df.loc[df['Naam tegenpartij'].str.contains('kokky', case=False), ['Category']] = 'Kapper'

    # Category Kleding
    df.loc[df['Omschrijving-1'].str.contains('Bonprix', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('Bristol', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('C&A', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('Coolcat', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('KiK Fil', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('Durlinger', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('Fashion Outlet', case=False), ['Category']] = 'Kleding'
    df.loc[df['Omschrijving-1'].str.contains('van Haren Schoenen', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('vanHaren', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('H&M', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('Jeans Centre', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('Jola Mode', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('Livera', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('Perry Sport', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('Scapino', case=False), ['Category']] = 'Kleding'
    df.loc[df['Omschrijving-1'].str.contains('Scapino', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('Sporthuis', case=False), ['Category']] = 'Kleding'
    df.loc[df['Omschrijving-1'].str.contains('VoetbalDirect', case=False), ['Category']] = 'Kleding'
    df.loc[df['Omschrijving-1'].str.contains('WE Fashion', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('Wibra', case=False), ['Category']] = 'Kleding'
    df.loc[df['Omschrijving-1'].str.contains('Zalando', case=False), ['Category']] = 'Kleding'
    df.loc[df['Naam tegenpartij'].str.contains('Zeeman', case=False), ['Category']] = 'Kleding'

    # Category MedischeKostenEigenRisico
    df.loc[df['Naam tegenpartij'].str.contains('Apotheek', case=False), ['Category']] = 'MedischeKostenEigenRisico'
    df.loc[df['Naam tegenpartij'].str.contains('PEARLE', case=False), ['Category']] = 'MedischeKostenEigenRisico'
    df.loc[df['Naam tegenpartij'].str.contains('TOP CHIROPRACTIE', case=False), ['Category']] = 'MedischeKostenEigenRisico'

    # Category Netflix
    df.loc[df['Omschrijving-1'].str.contains('Netflix', case=False), ['Category']] = 'Netflix'

    # Category OpenbaarVervoer
    df.loc[df['Naam tegenpartij'].str.contains('OV-CHIPKAART', case=False), ['Category']] = 'OpenbaarVervoer'
    df.loc[df['Naam tegenpartij'].str.contains('Trans Link Systems', case=False), ['Category']] = 'OpenbaarVervoer'

    # Category Overig
    df.loc[df['Naam tegenpartij'].str.contains('Coolblue', case=False), ['Category']] = 'Overig'
    df.loc[df['Naam tegenpartij'].str.contains('Milieustr', case=False), ['Category']] = 'Overig'
    df.loc[df['Omschrijving-1'].str.contains('123inkt.nl', case=False), ['Category']] = 'Overig'

    # Category PremieKapitaalverzekeringHypotheek
    df.loc[df['Omschrijving-1'].str.contains('SpaarZeker Verzekering', case=False), ['Category']] = 'PremieKapitaalverzekeringHypotheek'

    # Category SportTafeltennis
    df.loc[df['Naam tegenpartij'].str.contains('TAFELTENNIS', case=False), ['Category']] = 'SportTafeltennis'

    # Category SportTennis
    df.loc[df['Naam tegenpartij'].str.contains('LTV Berlicum', case=False), ['Category']] = 'SportTennis'
    df.loc[df['Omschrijving-1'].str.contains('LTV Berlicum', case=False), ['Category']] = 'SportTennis'

    # Category SportVoetbal
    df.loc[df['Tegenrekening IBAN/BBAN'] == 'NL33RABO0106934104', ['Category']] = 'SportVoetbal'

    # Category TeruggaveInkomstenbelasting
    df.loc[df['Omschrijving-1'].str.contains('IB/PVV', case=False), ['Category']] = 'TeruggaveInkomstenbelasting'

    # Category TVTelefoonInternet
    df.loc[df['Naam tegenpartij'].str.contains('ZIGGO', case=False), ['Category']] = 'TVTelefoonInternet'

    # Category UitEten
    df.loc[df['Naam tegenpartij'].str.contains('Burger King', case=False), ['Category']] = 'UitEten'
    df.loc[df['Naam tegenpartij'].str.contains('Domino', case=False), ['Category']] = 'UitEten'
    df.loc[df['Naam tegenpartij'].str.contains('Happy Italy', case=False), ['Category']] = 'UitEten'
    df.loc[df['Naam tegenpartij'].str.contains('Happy den Bosch', case=False), ['Category']] = 'UitEten'
    df.loc[df['Naam tegenpartij'].str.contains('McDonald', case=False), ['Category']] = 'UitEten'
    df.loc[df['Omschrijving-1'].str.contains('New York Pizza', case=False), ['Category']] = 'UitEten'

    # Category VakantieUitjes
    df.loc[df['Naam tegenpartij'].str.contains('bioscoop', case=False), ['Category']] = 'VakantieUitjes'
    df.loc[df['Naam tegenpartij'].str.contains('d-reizen', case=False), ['Category']] = 'VakantieUitjes'
    df.loc[df['Naam tegenpartij'].str.contains('Efteling', case=False), ['Category']] = 'VakantieUitjes'
    df.loc[df['Naam tegenpartij'].str.contains('JumpXL', case=False), ['Category']] = 'VakantieUitjes'
    df.loc[df['Naam tegenpartij'].str.contains('Meerdal', case=False), ['Category']] = 'VakantieUitjes'

    # Category WonenCV
    df.loc[df['Naam tegenpartij'].str.contains('VDN-Services', case=False), ['Category']] = 'WonenCV'

    # Category WonenGasElectra
    df.loc[df['Naam tegenpartij'].str.contains('Eneco', case=False), ['Category']] = 'WonenGasElectra'
    df.loc[df['Naam tegenpartij'].str.contains('Nuon', case=False), ['Category']] = 'WonenGasElectra'
    df.loc[df['Naam tegenpartij'].str.contains('Vattenfall', case=False), ['Category']] = 'WonenGasElectra'

    # Category WoningOnderhoud
    df.loc[df['Omschrijving-1'].str.contains('Gamma', case=False), ['Category']] = 'WoningOnderhoud'
    df.loc[df['Naam tegenpartij'].str.contains('Gamma', case=False), ['Category']] = 'WoningOnderhoud'
    df.loc[df['Naam tegenpartij'].str.contains('Praxis', case=False), ['Category']] = 'WoningOnderhoud'
    df.loc[df['Naam tegenpartij'].str.contains('Karwei', case=False), ['Category']] = 'WoningOnderhoud'

    # Category Zakgeld
    df.loc[df['Omschrijving-1'].str.contains('Zakgeld', case=False), ['Category']] = 'Zakgeld'

    # Remove the temporary fill
    df = df.replace(to_replace="TemporaryFill", value="")

    # Change format of date fields to dd-mm-yyyy
    df["Datum"] = pd.to_datetime(df["Datum"]).dt.strftime('%d-%m-%Y')
    df["Rentedatum"] = pd.to_datetime(df["Rentedatum"]).dt.strftime('%d-%m-%Y')

    # Write dataframe to new file
    df.to_csv('C:/processedTransactions.csv', index=False)  # index argument is required to prevent writing the index (row numbering) that is present in the dataframe

    print("Processed file.")


# --- Script ---
addCategoryToFile()
# calculateNewBalance()
# calculateSavingsRate()
