from fuzzywuzzy import fuzz
from fuzzywuzzy import process

courseRoles = [
    ['Accounting'],

    ['Actuarial'],

    ['Architecture'],

    ['AppMath'],

    ['AppChemistry'],

    ['BioInformatics'],

    ['Biology'],

    ['ComSci'],

    ['Civil Engineering'],

    ['China Studies'],

    ['DigitalMedia'],

    ['Finance'],

    ['Environmental Science'],

    ['English'],

    ['ElectricEngineering'],

    ['ItlBusiness'],

    ['IndustryDesign'],

    ['ManufaEngineering'],

    ['MechaEngineering'],

    ['TeleCom'],

    ['UrbanDesign']]



input = input("Enter Input: ")
output = process.extract(input, courseRoles, limit = 2)
print(output[0][0][0])
'''def compare(input, list):

    valueList = []
    for roles in list:
        valueList.append(0)

    #for char in input:

        #for roles in list:'''
