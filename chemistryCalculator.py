#  Copyright 2022 Tyler Davis

#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at

#      https://www.apache.org/licenses/LICENSE-2.0

#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import math
import sortedcontainers
import sigfig
from sigfig import round
print("Chemistry Calculator")
print("Developed by Tyler Davis")
print("2022")
print("Version 1.4.0")
print()
print("Provided under the Apache 2.0 license, found at \"https://github.com/Tornado6464/Chemistry-Calculator/blob/main/LICENSE\".")
#Notes:
#Code for molar mass calculations was created by @elibroftw on GitHub can be found here: https://gist.github.com/elibroftw/22e3b4c1eb7fa0a6c83d099d24200f95
#Variables are the first letter of the calculation type, followed by what value they contain (eg. GLType = Gas Law Type and CMass = Calorimetry Mass)
#
#Define Molar Masses of Elements
MM_of_Elements = {'H': 1.00794, 'He': 4.002602, 'Li': 6.941, 'Be': 9.012182, 'B': 10.811, 'C': 12.0107, 'N': 14.0067,
                  'O': 15.9994, 'F': 18.9984032, 'Ne': 20.1797, 'Na': 22.98976928, 'Mg': 24.305, 'Al': 26.9815386,
                  'Si': 28.0855, 'P': 30.973762, 'S': 32.065, 'Cl': 35.453, 'Ar': 39.948, 'K': 39.0983, 'Ca': 40.078,
                  'Sc': 44.955912, 'Ti': 47.867, 'V': 50.9415, 'Cr': 51.9961, 'Mn': 54.938045,
                  'Fe': 55.845, 'Co': 58.933195, 'Ni': 58.6934, 'Cu': 63.546, 'Zn': 65.409, 'Ga': 69.723, 'Ge': 72.64,
                  'As': 74.9216, 'Se': 78.96, 'Br': 79.904, 'Kr': 83.798, 'Rb': 85.4678, 'Sr': 87.62, 'Y': 88.90585,
                  'Zr': 91.224, 'Nb': 92.90638, 'Mo': 95.94, 'Tc': 98.9063, 'Ru': 101.07, 'Rh': 102.9055, 'Pd': 106.42,
                  'Ag': 107.8682, 'Cd': 112.411, 'In': 114.818, 'Sn': 118.71, 'Sb': 121.760, 'Te': 127.6,
                  'I': 126.90447, 'Xe': 131.293, 'Cs': 132.9054519, 'Ba': 137.327, 'La': 138.90547, 'Ce': 140.116,
                  'Pr': 140.90465, 'Nd': 144.242, 'Pm': 146.9151, 'Sm': 150.36, 'Eu': 151.964, 'Gd': 157.25,
                  'Tb': 158.92535, 'Dy': 162.5, 'Ho': 164.93032, 'Er': 167.259, 'Tm': 168.93421, 'Yb': 173.04,
                  'Lu': 174.967, 'Hf': 178.49, 'Ta': 180.9479, 'W': 183.84, 'Re': 186.207, 'Os': 190.23, 'Ir': 192.217,
                  'Pt': 195.084, 'Au': 196.966569, 'Hg': 200.59, 'Tl': 204.3833, 'Pb': 207.2, 'Bi': 208.9804,
                  'Po': 208.9824, 'At': 209.9871, 'Rn': 222.0176, 'Fr': 223.0197, 'Ra': 226.0254, 'Ac': 227.0278,
                  'Th': 232.03806, 'Pa': 231.03588, 'U': 238.02891, 'Np': 237.0482, 'Pu': 244.0642, 'Am': 243.0614,
                  'Cm': 247.0703, 'Bk': 247.0703, 'Cf': 251.0796, 'Es': 252.0829, 'Fm': 257.0951, 'Md': 258.0951,
                  'No': 259.1009, 'Lr': 262, 'Rf': 267, 'Db': 268, 'Sg': 271, 'Bh': 270, 'Hs': 269, 'Mt': 278,
                  'Ds': 281, 'Rg': 281, 'Cn': 285, 'Nh': 284, 'Fl': 289, 'Mc': 289, 'Lv': 292, 'Ts': 294, 'Og': 294,
                  '': 0}

def molar_mass(compound: str, decimal_places=None) -> float:
    is_polyatomic = end = multiply = False
    polyatomic_mass, m_m, multiplier = 0, 0, 1
    element = ''

    for e in compound:
        if is_polyatomic:
            if end:
                is_polyatomic = False
                m_m += int(e) * polyatomic_mass if e.isdigit() else polyatomic_mass + MM_of_Elements[e]
            elif e.isdigit():
                multiplier = int(str(multiplier) + e) if multiply else int(e)
                multiply = True
            elif e.islower():
                element += e
            elif e.isupper():
                polyatomic_mass += multiplier * MM_of_Elements[element]
                element, multiplier, multiply = e, 1, False
            elif e == ')':
                polyatomic_mass += multiplier * MM_of_Elements[element]
                element, multiplier = '', 1
                end, multiply = True, False
        elif e == '(':
            m_m += multiplier * MM_of_Elements[element]
            element, multiplier = '', 1
            is_polyatomic, multiply = True, False
        elif e.isdigit():
            multiplier = int(str(multiplier) + e) if multiply else int(e)
            multiply = True
        elif e.islower():
            element += e
        elif e.isupper():
            m_m += multiplier * MM_of_Elements[element]
            element, multiplier, multiply = e, 1, False
    m_m += multiplier * MM_of_Elements[element]
    if decimal_places is not None:
        return round(m_m, decimal_places)
    return m_m


if __name__ == '__main__':
    # TESTS
    assert molar_mass('H') == 1.00794
    assert 18.015 < molar_mass('H2O') < 18.016
    assert 98.07 < molar_mass('H2SO4') < 98.08
    assert 386 < molar_mass('CF3OCF(CF3)CF2OCF2OCF3') < 386.1
    assert 159.6 < molar_mass('Fe2O3') < 159.7
    # OPTIONS
    DECIMAL_PLACES = 20

while True:
    #Get type of calculation
    print("\n\nMain Menu\n")
    print("1 = Molar Mass Calculator")
    print("2 = Stoichiometry Calculations")
    print("3 = Molarity Calculations")
    print("4 = Dilution Calculations")
    print("5 = pH/pOH/H+ Concentration/OH- Concentration Converter")
    print("6 = Gas Law Calculations")
    print("7 = Calorimetry Calculations")
    print("8 = Equilibrium Calculations")
    print("9 = Entropy Calculations")
    print("10 = Metric/Imperial Conversions")
    print("11 = Significant Figures\n")
    calculationType = int(input("Enter the number of the calculation shown above that you would like to be completed, or \"0\" to quit: "))
    #Go to calculation type
    if calculationType not in range(12):
        print("\nPlease enter a valid option.")

    if calculationType == 0:
        break

    if calculationType == 1:
        while True:
            MMCInput = input(str('\nEnter Compound Formula (capitalize elements, eg. Mn instead of mn), or enter \"0\" to quit: '))
            if MMCInput == "0":
                break
            else:
                print()
                print(f'The molar mass of {MMCInput} is {molar_mass(MMCInput, DECIMAL_PLACES)} g/mol')

    if calculationType == 2:
        #List number types
        print()
        print("Note: \"X\" represents the first compound, whereas \"Y\" represents the second compound.")
        print()
        print("1 = Grams of X --> Grams of Y")
        print("2 = Grams of X --> Moles of Y")
        print("3 = Grams of X --> Particles of Y")
        print("4 = Grams of X --> Volume of Y at STP")
        print("5 = Moles of X --> Grams of Y")
        print("6 = Moles of X --> Moles of Y")
        print("7 = Moles of X --> Particles of Y")
        print("8 = Moles of X --> Volume of Y at STP")
        print("9 = Particles of X --> Grams of Y")
        print("10 = Particles of X --> Moles of Y")
        print("11 = Particles of X --> Particles of Y")
        print("12 = Particles of X --> Volume of Y at STP")
        print("13 = Volume of X at STP --> Grams of Y")
        print("14 = Volume of X at STP --> Moles of Y")
        print("15 = Volume of X at STP --> Particles of Y")
        print("16 = Volume of X at STP --> Volume of Y at STP")
        print()
        while True:
            # Get type of calculation
            print()
            SType = int(input("Enter the number of the variable that you would like to find, or \"0\" to quit: "))
            print()
            if (SType != 1) & (SType != 2) & (SType != 3) & (SType != 4) & (SType != 5) & (SType != 6) & (SType != 7) & (SType != 8) & (SType != 9) & (SType != 10) & (SType != 11) & (SType != 12) & (SType != 13) & (SType != 14) & (SType != 15) & (SType != 16):
                print()
                print("Please enter a valid option.\n")
            if SType == 0:
                break

            if (SType == 1) or (SType == 2) or (SType == 3) or (SType == 4) or (SType == 5) or (SType == 6) or (SType == 7) or (SType == 8) or (SType == 9) or (SType == 10) or (SType == 11) or (SType == 12) or (SType == 13) or (SType == 14) or (SType == 15) or (SType == 16):
                if (SType == 1) or (SType == 2) or (SType == 3) or (SType == 4):
                    SFormula1 = input('Enter the first (X) compound formula (please capitalize elements, eg. Mn instead of mn): ')
                SCoefficient1 = int(input("What is the coefficient of the first (X) compount (Please make sure the reaction is balanced)? "))
                SAmount1 = float(input("Enter the amount of the first (X) item you have (eg. 5g, 2.4 mol, 7.0E23 particles, or 15.4L [do not include the unit]): "))
                SFormula2 = input('Enter the second (Y) compound formula (please capitalize elements, eg. Mn instead of mn): ')
                SCoefficient2 = int(input("What is the coefficient of the second (Y) compount (Please make sure the reaction is balanced)? "))
                #Format prints like this:
                if SType == 1:
                    MMSF1 = float(sum({molar_mass(SFormula1, DECIMAL_PLACES)}))
                    MMSF2 = float(sum({molar_mass(SFormula2, DECIMAL_PLACES)}))
                    SType1ANS = float(((SAmount1/MMSF1)*(SCoefficient2/SCoefficient1))*MMSF2)
                    print()
                    print("There will be", SType1ANS, "grams of", SFormula2 + '.')
                if SType == 2:
                    MMSF1 = float(sum({molar_mass(SFormula1, DECIMAL_PLACES)}))
                    SType2ANS = float((SAmount1 / MMSF1) * (SCoefficient2 / SCoefficient1))
                    print()
                    print("There will be", SType2ANS, "moles of", SFormula2 + '.')
                if SType == 3:
                    MMSF1 = float(sum({molar_mass(SFormula1, DECIMAL_PLACES)}))
                    SType3ANS = float((((SAmount1 / MMSF1) * (SCoefficient2 / SCoefficient1))*6.02214076E23))
                    print()
                    print("There will be", SType3ANS, "particles of", SFormula2 + '.')
                if SType == 4:
                    MMSF1 = float(sum({molar_mass(SFormula1, DECIMAL_PLACES)}))
                    SType4ANS = float(((SAmount1 / MMSF1) * (SCoefficient2 / SCoefficient1)) * 22.4)
                    print()
                    print("There will be", SType4ANS, "liters of", SFormula2 + '.')
                if SType == 5:
                    MMSF2 = float(sum({molar_mass(SFormula2, DECIMAL_PLACES)}))
                    SType5ANS = float(((SAmount1) * (SCoefficient2 / SCoefficient1))*MMSF2)
                    print()
                    print("There will be", SType5ANS, "grams of", SFormula2 + '.')
                if SType == 6:
                    SType6ANS = float((SAmount1) * (SCoefficient2 / SCoefficient1))
                    print()
                    print("There will be", SType6ANS, "moles of", SFormula2 + '.')
                if SType == 7:
                    SType7ANS = float((SAmount1 * (SCoefficient2 / SCoefficient1))*6.02214076E23)
                    print()
                    print("There will be", SType7ANS, "particles of", SFormula2 + '.')
                if SType == 8:
                    SType8ANS = float((SAmount1 * (SCoefficient2 / SCoefficient1)) * 22.4)
                    print()
                    print("There will be", SType8ANS, "liters of", SFormula2 + '.')
                if SType == 9:
                    MMSF2 = float(sum({molar_mass(SFormula2, DECIMAL_PLACES)}))
                    SType9ANS = float(((SAmount1/6.02214076E23)*(SCoefficient2/SCoefficient1))*MMSF2)
                    print()
                    print("There will be", SType9ANS, "grams of", SFormula2 + '.')
                if SType == 10:
                    SType10ANS = float((SAmount1 / 6.02214076E23) * (SCoefficient2 / SCoefficient1))
                    print()
                    print("There will be", SType10ANS, "moles of", SFormula2 + '.')
                if SType == 11:
                    SType11ANS = float(((SAmount1 / 6.02214076E23) * (SCoefficient2 / SCoefficient1))*6.02214076E23)
                    print()
                    print("There will be", SType11ANS, "particles of", SFormula2 + '.')
                if SType == 12:
                    SType12ANS = float(((SAmount1 / 6.02214076E23) * (SCoefficient2 / SCoefficient1)) * 22.4)
                    print()
                    print("There will be", SType12ANS, "liters of", SFormula2 + '.')
                if SType == 13:
                    MMSF2 = float(sum({molar_mass(SFormula2, DECIMAL_PLACES)}))
                    SType13ANS = float(((SAmount1 / 22.4) * (SCoefficient2 / SCoefficient1)) * MMSF2)
                    print()
                    print("There will be", SType13ANS, "grams of", SFormula2 + '.')
                if SType == 14:
                    SType14ANS = float(((SAmount1 / 22.4) * (SCoefficient2 / SCoefficient1)))
                    print()
                    print("There will be", SType14ANS, "moles of", SFormula2 + '.')
                if SType == 15:
                    SType15ANS = float(((SAmount1 / 22.4) * (SCoefficient2 / SCoefficient1)) * 6.02214076E23)
                    print()
                    print("There will be", SType15ANS, "particles of", SFormula2 + '.')
                if SType == 16:
                    SType16ANS = float(((SAmount1 / 22.4) * (SCoefficient2 / SCoefficient1)) * 22.4)
                    print()
                    print("There will be", SType16ANS, "liters of", SFormula2 + '.')

    if calculationType == 3:
    # Get the number to solve for
        print("\n1 = Molarity")
        print("2 = Moles of Solute")
        print("3 = Liters of Solution\n")
        while True:
            #Get type of calculation
            MType = int(input("Enter the number of the variable that you would like to find, or \"0\" to quit: "))
            print()
            #Do the calculation
            if (MType != 0) & (MType != 1) & (MType != 2) & (MType != 3):
                print("Please enter a valid option.\n")
            if MType == 0:
                break
            if MType == 1:
                MMolesOfSolute = float(input("How many moles of solute is there? "))
                MLitersOfSolution = float(input("How many liters of solution is there? "))
                MMolarity = MMolesOfSolute/MLitersOfSolution
                print()
                print("The molarity of this solution is", MMolarity)
            if MType == 2:
                MMolarity = float(input("What is the molarity of this solution? "))
                MLitersOfSolution = float(input("How many liters of solution is there? "))
                MMolesOfSolute = MMolarity*MLitersOfSolution
                print("\nThere is", MMolesOfSolute, "moles of the solute.")
            if MType == 3:
                MMolesOfSolute = float(input("How many moles of solute is there? "))
                MMolarity = float(input("What is the molarity of this solution? "))
                MLitersOfSolution = MMolesOfSolute/MMolarity
                print("\nThere is", MLitersOfSolution, "liters of solution.")

    if calculationType == 4:
        print("\n1 = Molarity")
        print("2 = Volume\n")
        while True:
            DType = int(input("Enter the number of the variable you would like to solve for, or \"0\" to quit: "))
            print()
            if (DType != 0) & (DType != 1) & (DType != 2):
                print("Please enter a valid option.\n")
            if DType == 0:
                break
            if DType == 1:
                print("Note: Please use liters for volume.")
                DM1 = float(input("Enter the value of the initial molarity (M1): "))
                DV1 = float(input("Enter the value of the initial volume (V1): "))
                DV2 = float(input("Enter the value of the final volume (V2): "))
                DANS1 = ((DM1*DV1)/DV2)
                print()
                print(DANS1, "is the final molarity.")
                print()
            if DType == 2:
                print("Note: Please use liters for volume.")
                DM1 = float(input("Enter the value of the initial molarity (M1): "))
                DV1 = float(input("Enter the value of the initial volume (V1): "))
                DM2 = float(input("Enter the value of the final molarity (M2): "))
                DANS2 = ((DM1*DV1)/DM2)
                print("\n", DANS2, "is the final volume.\n")

    if calculationType == 5:
        # Get type of conversion
        print("\n1 = pH to pOH")
        print("2 = pOH to pH")
        print("3 = pH to H+ Concentration")
        print("4 = H+ Concentration to pH")
        print("5 = pH to OH- Concentration")
        print("6 = OH- Concentration to pH")
        print("7 = pOH to OH- Concentration")
        print("8 = OH- Concentration to pOH")
        print("9 = pOH to H+ Concentration")
        print("10 = H+ Concentration to pOH")
        print("11 = H+ Concentration to OH- Concentration")
        print("12 = OH- Concentration to H+ Concentration\n")
        while True:
            pHtype = int(input("Enter the number of the conversion shown above that you would like to be done, or \"0\" to quit: "))
            #option to quit
            if pHtype == 0:
                break
            #Set names of variables for questions
            if pHtype == 1:
                pHV1 = str("pH")
                pHV2 = str("pOH")
            if pHtype == 2:
                pHV1 = str("pOH")
                pHV2 = str("pH")
            if pHtype == 3:
                pHV1 = str("pH")
                pHV2 = str("H+ Concentration")
            if pHtype == 4:
                pHV1 = str("H+ Concentration")
                pHV2 = str("pH")
            if pHtype == 5:
                pHV1 = str("pH")
                pHV2 = str("OH- Concentration")
            if pHtype == 6:
                pHV1 = str("OH- Concentration")
                pHV2 = str("pH")
            if pHtype == 7:
                pHV1 = str("pOH")
                pHV2 = str("OH- Concentration")
            if pHtype == 8:
                pHV1 = str("OH- Concentration")
                pHV2 = str("pOH")
            if pHtype == 9:
                pHV1 = str("pOH")
                pHV2 = str("H+ Concentration")
            if pHtype == 10:
                pHV1 = str("H+ Concentration")
                pHV2 = str("pOH")
            if pHtype == 11:
                pHV1 = str("H+ Concentration")
                pHV2 = str("OH- Concentration")
            if pHtype == 12:
                pHV1 = str("OH- Concentration")
                pHV2 = str("H+ Concentration")
            #get both numbers
            if (pHtype == 0) or (pHtype == 1) or (pHtype == 2) or (pHtype == 3) or (pHtype == 4) or (pHtype == 5) or (pHtype == 6) or (pHtype == 7) or (pHtype == 8) or (pHtype == 9) or (pHtype == 10) or (pHtype == 11) or (pHtype == 12):
                pHnumber1 = input("Enter the value of " + pHV1 + " that you would like to convert to " + pHV2 + ": ")
                pHnumber = float(pHnumber1)
            if (pHtype != 0) & (pHtype != 1) & (pHtype != 2) & (pHtype != 3) & (pHtype != 4) & (pHtype != 5) & (pHtype != 6) & (pHtype != 7) & (pHtype != 8) & (pHtype != 9) & (pHtype != 10) & (pHtype != 11) & (pHtype != 12):
                print()
                print("Please enter a valid option.\n")
            #type 1
            if pHtype == 1:
                pHanswer1 = 14-pHnumber
                print()
                print(pHanswer1, "is the pOH.")
            #type 2
            if pHtype == 2:
                pHanswer2 = 14-pHnumber
                print()
                print(pHanswer2, "is the pH.")
            #type 3
            if pHtype == 3:
                pHanswer3 = 10**-pHnumber
                print()
                print(pHanswer3, "is the H+ Concentration.")
            #type 4
            if pHtype == 4:
                pHanswer4 = -math.log10(pHnumber)
                print()
                print(pHanswer4, "is the pH.")
            #type 5
            if pHtype == 5:
                pHanswer5a = 14-pHnumber
                pHanswer5b = 10**-pHanswer5a
                print()
                print(pHanswer5b, "is the OH- Concentration.")
            #type 6
            if pHtype == 6:
                pHanswer6a = -math.log10(pHnumber)
                pHanswer6b = 14-pHanswer6a
                print()
                print(pHanswer6b, "is the pH.")
            #type 7
            if pHtype == 7:
                pHanswer7 = 10**-pHnumber
                print()
                print(pHanswer7, "is the OH- Concentration.")
            #type 8
            if pHtype == 8:
                pHanswer8 = math.log10(pHnumber)
                print()
                print(pHanswer8, "is the pOH.")
            #type 9
            if pHtype == 9:
                pHanswer9a = 14-pHnumber
                pHanswer9b = 10**-pHanswer9a
                print()
                print(pHanswer9b, "is the H+ Concentration.")
            #type 10
            if pHtype == 10:
                pHanswer10a = math.log10(pHnumber)
                pHanswer10b = 14-pHanswer10a
                print()
                print(pHanswer10b, "is the pOH.")
            #type 11
            if pHtype == 11:
                pHanswer11 = (1.0E-14)/pHnumber
                print()
                print(pHanswer11, "is the OH- Concentration.")
            #type 12
            if pHtype == 12:
                pHanswer12 = (1.0E-14)/pHnumber
                print()
                print(pHanswer12, "is the H+ Concentration.")

    if calculationType == 6:
        print("1 = Boyle's Law (Pressure and Volume)\n")
        print("2 = Charles' Law (Volume and Temperature)")
        print("3 = Gay-Lussac's Law (Pressure and Temperature)")
        print("4 = Avogadro's Law (Volume and Moles)")
        print("5 = Combined Gas Law (Volume, Pressure, and Temperature)")
        print("6 = Ideal Gas Law")

        while True:
            print()
            GLType = int(input("Enter the number of the gas law calculation shown above that you would like to be done, or \"0\" to quit: "))
            if (GLType != 0) & (GLType != 1) & (GLType != 2) & (GLType != 3) & (GLType != 4) & (GLType != 5) & (GLType != 6):
                print()
                print("Please enter a valid option.\n")
            if GLType == 0:
                break
            if GLType == 1:
                print("\nNote: All values must be in atmospheres or liters, respectively.")
                print("1 = Pressure")
                print("2 = Volume")
                GLType2 = int(input("Enter the number of the variable you would like to solve for: "))
                if (GLType2 != 1) & (GLType2 != 2):
                    print("Please enter a valid option.\n")
                if GLType2 == 1:
                    GLType2P1 = float(input("Enter the value of the first pressure variable (P1): "))
                    GLType2V1 = float(input("Enter the value of the first volume variable (V1): "))
                    GLType2V2 = float(input("Enter the value of the second volume variable (V2): "))
                    GLType21ANS = float(((GLType2P1*GLType2V1)/GLType2V2))
                    print()
                    print(GLType21ANS, "is the pressure.")
                if GLType2 == 2:
                    GLType2P1 = float(input("Enter the value of the first pressure variable (P1): "))
                    GLType2V1 = float(input("Enter the value of the first volume variable (V1): "))
                    GLType2P2 = float(input("Enter the value of the second pressure variable (P2): "))
                    GLType22ANS = float(((GLType2P1*GLType2V1) / GLType2P2))
                    print()
                    print(GLType22ANS, "is the volume.")
            if GLType == 2:
                print("\nNote: All values must be in liters or kelvin, respectively.")
                print("1 = Volume")
                print("2 = Temperature\n")
                GLType2 = int(input("Enter the number of the variable you would like to solve for: "))
                if (GLType2 != 1) & (GLType2 != 2):
                    print("Please enter a valid option.\n")
                if GLType2 == 1:
                    GLType2V1 = float(input("Enter the value of the first volume variable (V1): "))
                    GLType2T1 = float(input("Enter the value of the first temperature variable (T1)(make sure the temperature is in kelvin): "))
                    GLType2V2 = float(input("Enter the value of the second volume variable (V2): "))
                    GLType21ANS = ((GLType2V1/GLType2T1)/GLType2V2)
                    print()
                    print(GLType21ANS, "is the volume.")
                if GLType2 == 2:
                    GLType2V1 = float(input("Enter the value of the first volume variable (V1): "))
                    GLType2T1 = float(input("Enter the value of the first temperature variable (T1)(make sure the temperature is in kelvin): "))
                    GLType2T2 = float(input("Enter the value of the second temperature variable (T2)(make sure the temperature is in kelvin): "))
                    GLType22ANS = ((GLType2V1/GLType2T1)/GLType2T2)
                    print()
                    print(GLType22ANS, "is the temperature.")
            if GLType == 3:
                print("\nNote: All values must be in atmospheres or kelvin, respectively.")
                print("1 = Pressure")
                print("2 = Temperature\n")
                GLType2 = int(input("Enter the number of the variable you would like to solve for: "))
                if (GLType2 != 1) & (GLType2 != 2):
                    print("Please enter a valid option.\n")
                if GLType2 == 1:
                    GLType2P1 = float(input("Enter the value of the first pressure variable (P1): "))
                    GLType2T1 = float(input("Enter the value of the first temperature variable (V1)(make sure the temperature is in kelvin): "))
                    GLType2T2 = float(input("Enter the value of the second temperature variable (V2)(make sure the temperature is in kelvin): "))
                    GLType21ANS = ((GLType2P1*GLType2T2)/GLType2T1)
                    print()
                    print(GLType21ANS, "is the pressure.")
                if GLType2 == 2:
                    GLType2V1 = float(input("Enter the value of the first pressure variable (P1): "))
                    GLType2T1 = float(input("Enter the value of the first temperature variable (T1)(make sure the temperature is in kelvin): "))
                    GLType2T2 = float(input("Enter the value of the second pressure variable (P2): "))
                    GLType22ANS = ((GLType2P2*GLType2T1)/GLType2P1)
                    print()
                    print(GLType22ANS, "is the temperature.")
            if GLType == 4:
                print("\nNote: All values must be in liters or moles, respectively.")
                print("1 = Volume")
                print("2 = Moles\n")
                GLType2 = int(input("Enter the number of the variable you would like to solve for: "))
                if (GLType2 != 1) & (GLType2 != 2):
                    print("Please enter a valid option.\n")
                if GLType2 == 1:
                    GLType2V1 = float(input("Enter the value of the first pressure variable (P1): "))
                    GLType2M1 = float(input("Enter the value of the first amount of moles (M1): "))
                    GLType2M2 = float(input("Enter the value of the second amount of moles (M2): "))
                    GLType21ANS = ((GLType2V1*GLType2M2)/GLType2M1)
                    print()
                    print(GLType21ANS, "is the volume.")
                if GLType2 == 2:
                    GLType2V1 = float(input("Enter the value of the first volume variable (V1): "))
                    GLType2M1 = float(input("Enter the value of the first amount of moles (M1): "))
                    GLType2V2 = float(input("Enter the value of the second volume variable (V2): "))
                    GLType22ANS = ((GLType2M1*GLType2V2)/GLType2V1)
                    print()
                    print(GLType22ANS, "is the number of moles.")
            if GLType == 5:
                print("\nNote: All values must be in atmospheres, liters, or kelvin, respectively.")
                print("1 = Pressure")
                print("2 = Volume")
                print("3 = Temperature\n")
                GLType2 = int(input("Enter the number of the variable you would like to solve for: "))
                if (GLType2 != 1) & (GLType2 != 2) & (GLType2 !=3):
                    print("Please enter a valid option.\n")
                if GLType2 == 1:
                    GLP1 = float(input("Enter the initial pressure: "))
                    GLV1 = float(input("Enter the initial volume: "))
                    GLT1 = float(input("Enter the initial temperature: "))
                    GLV2 = float(input("Enter the final volume: "))
                    GLT2 = float(input("Enter the final temperature: "))
                    GLA = ((GLP1*GLV1*GLT2)/(GLV2*GLT1))
                    print()
                    print(GLA, "is the final pressure.")
                if GLType2 == 2:
                    GLP1 = float(input("Enter the initial pressure: "))
                    GLV1 = float(input("Enter the initial volume: "))
                    GLT1 = float(input("Enter the initial temperature: "))
                    GLP2 = float(input("Enter the final pressure: "))
                    GLT2 = float(input("Enter the final temperature: "))
                    GLA = ((GLP1*GLV1*GLT2)/(GLP2*GLT1))
                    print()
                    print(GLA, "is the final volume.")
                if GLType2 == 3:
                    GLP1 = float(input("Enter the initial pressure: "))
                    GLV1 = float(input("Enter the initial volume: "))
                    GLT1 = float(input("Enter the initial temperature: "))
                    GLP2 = float(input("Enter the final pressure: "))
                    GLV2 = float(input("Enter the final volume: "))
                    GLA = (((GLP1*GLV1)/GLT1)/(GLP2*GLV2))
                    print()
                    print(GLA, "is the final temperature.")
            if GLType == 6:
                print("\nNote: All values must be in atmospheres, liters, moles, or kelvin, respectively.")
                print("1 = Pressure")
                print("2 = Volume")
                print("3 = Moles")
                print("4 = Temperature\n")
                GLType2 = int(input("Enter the number of the variable you would like to solve for: "))
                R = float(0.082057366080960)
                if (GLType2 != 1) & (GLType2 != 2) & (GLType2 !=3) & (GLType2 != 4):
                    print("Please enter a valid option.\n")
                if GLType2 == 1:
                    GLIGLV = float(input("Enter the volume of the gas: "))
                    GLIGLM = float(input("Enter the amount of moles of the gas: "))
                    GLIGLT = float(input("Enter the temperature of the gas: "))
                    GLIGLA = ((GLIGLM*R*GLIGLT)/GLIGLV)
                    print()
                    print(GLIGLA, "is the pressure.")
                if GLType2 == 2:
                    GLIGLP = float(input("Enter the pressure of the gas: "))
                    GLIGLM = float(input("Enter the amount of moles of the gas: "))
                    GLIGLT = float(input("Enter the temperature of the gas: "))
                    GLIGLA = ((GLIGLM*R*GLIGLT)/GLIGLP)
                    print()
                    print(GLIGLA, "is the volume.")
                if GLType2 == 3:
                    GLIGLP = float(input("Enter the pressure of the gas: "))
                    GLIGLV = float(input("Enter the volume of the gas: "))
                    GLIGLT = float(input("Enter the temperature of the gas: "))
                    GLIGLA = ((GLIGLP*GLIGLV)/(R*GLIGLT))
                    print()
                    print(GLIGLA, "is the amount of moles.")
                if GLType2 == 4:
                    GLIGLP = float(input("Enter the pressure of the gas: "))
                    GLIGLV = float(input("Enter the volume of the gas: "))
                    GLIGLM = float(input("Enter the amount of moles of the gas: "))
                    GLIGLA = (((GLIGLP*GLIGLV)/(R*GLIGLM)))
                    print()
                    print(GLIGLA, "is the temperature.")

    if calculationType == 7:
        print("\n1 = Total Heat Energy Transferred")
        print("2 = Mass")
        print("3 = Specific Heat Capacity")
        print("4 = Change in Temperature")

        while True:
            print()
            CType = int(input("Enter the number of the calorimetry calculation shown above that you would like to be done, or \"0\" to quit: "))
            if (CType != 0) & (CType != 1) & (CType != 2) & (CType != 3) & (CType != 4):
                print()
                print("Please enter a valid option.\n")
            if CType == 0:
                break
            if CType == 1:
                CMass = float(input("Enter the mass (grams) of the substance that was exposed to the heat (usually water): "))
                CSHC = float(input("Enter the specific heat capacity of the substance that was exposed to the heat (usually water): "))
                CHiT = float(input("Enter the change in temperature (degreees kelvin/celsius) of the substance that was exposed to the heat (usually water): "))
                CAns = str(CMass * CSHC * CHiT)
                print("\nThe total heat energy transferred is", CAns + " joules.")
            if CType == 2:
                CTHE = float(input("Enter the total heat energy (J) transferred to the substance that was exposed to the heat (usually water): "))
                CSHC = float(input("Enter the specific heat capacity of the substance that was exposed to the heat (usually water): "))
                CHiT = float(input("Enter the change in temperature (degreees kelvin/celsius)of the substance that was exposed to the heat (usually water): "))
                CAns = str((CSHC * CHiT)/CTHE)
                print("\nThe mass of the substance that was exposed to the heat is", CAns + " grams.")
            if CType == 3:
                CMass = float(input("Enter the mass (grams) of the substance that was exposed to the heat (usually water): "))
                CTHE = float(input("Enter the total heat energy (J) transferred to the substance that was exposed to the heat (usually water): "))
                CHiT = float(input("Enter the change in temperature (degreees kelvin/celsius)of the substance that was exposed to the heat (usually water): "))
                CAns = str(CTHE/(CMass * CHiT))
                print("\nThe specific heat capacity of the substance that was exposed to the heat is", CAns + " J/g.")
            if CType == 4:
                CMass = float(input("Enter the mass (grams) of the substance that was exposed to the heat (usually water): "))
                CTHE = float(input("Enter the total heat energy (J) transferred to the substance that was exposed to the heat (usually water): "))
                CSHC = float(input("Enter the specific heat capacity (J/g of the substance that was exposed to the heat (usually water): "))
                CAns = str(CTHE/(CMass * CSHC))
                print("\nThe change in temperature is", CAns + " degrees kelvin/celsius.")

    if calculationType == 8:
        print("\n1 = Equilibrium Constant for Concentration")
        print("2 = Equilibrium Constant for Pressure\n")
        while True:
            EType = int(input("Enter the number of the calculation that you would like to perform, or \"0\" to quit: "))
            if (EType != 0) & (EType != 1) & (EType != 2):
                print()
                print("Please enter a valid option.\n")

            if EType == 0:
                break
            if EType == 1:
                ECount1 = int(input("Enter the total number of different reactants in the equation: "))
                ECount2 = int(input("Enter the total number of different products in the equation: "))
                print()
                EDummy1 = 1
                EDummy2 = 1
                EC1 = None
                EC2 = None
                ECon1 = None
                ECon2 = None
                ERea = None
                EPro = None
                while EDummy1 <= ECount1:
                    if EDummy1 == 1:
                        wordAns = str("1st")
                    if EDummy1 == 2:
                        wordAns = str("2nd")
                    if EDummy1 >= 3:
                        wordAns = str("3rd")
                    if EDummy1 >= 4:
                        wordAns = str(str(EDummy1) + "th")
                    EC1 = int(input("Enter the coefficient of the " + wordAns + " reactant: "))
                    ECon1 = float(input("Enter the concentration (molarity) of the " + wordAns + " reactant: "))
                    if ERea == None:
                        ERea = 1
                    ERea = float(ERea * (ECon1 ** float(EC1)))
                    EDummy1 = EDummy1 + 1
                while EDummy2 <= ECount2:
                    if EDummy2 == 1:
                        wordAns = str("1st")
                    if EDummy2 == 2:
                        wordAns = str("2nd")
                    if EDummy2 == 3:
                        wordAns = str("3rd")
                    if EDummy2 >= 4:
                        wordAns = str(str(EDummy2) + "th")
                    EC2 = int(input("Enter the coefficient of the " + wordAns + " product: "))
                    ECon2 = float(input("Enter the cocentration (molarity) of the " + wordAns + " product: "))
                    if EPro == None:
                        EPro = 1
                    EPro = float(EPro * (ECon2 ** float(EC2)))
                    EDummy2 = EDummy2 + 1
                EType1ANS = str(float(EPro) / float(ERea))
                print()
                print("The equilibrium constant of the concentration (Kc) of this reaction is " + EType1ANS + ".\n")
            if EType == 2:
                print()
                ECount1 = int(input("Enter the total number of different reactants in the equation: "))
                ECount2 = int(input("Enter the total number of different products in the equation: "))
                print()
                EDummy1 = 1
                EDummy2 = 1
                EC1 = None
                EC2 = None
                ECon1 = None
                ECon2 = None
                ERea = None
                EPro = None
                while EDummy1 <= ECount1:
                    if EDummy1 == 1:
                        wordAns = str("1st")
                    if EDummy1 == 2:
                        wordAns = str("2nd")
                    if EDummy1 >= 3:
                        wordAns = str("3rd")
                    if EDummy1 >= 4:
                        wordAns = str(str(EDummy1) + "th")
                    EC1 = int(input("Enter the coefficient of the " + wordAns + " reactant: "))
                    EPre1 = float(input("Enter the pressure in atm of the " + wordAns + " reactant: "))
                    if ERea == None:
                        ERea = 1
                    ERea = float(ERea * (EPre1 ** float(EC1)))
                    EDummy1 = EDummy1 + 1
                while EDummy2 <= ECount2:
                    if EDummy2 == 1:
                        wordAns = str("1st")
                    if EDummy2 == 2:
                        wordAns = str("2nd")
                    if EDummy2 == 3:
                        wordAns = str("3rd")
                    if EDummy2 >= 4:
                        wordAns = str(str(EDummy2) + "th")
                    EC2 = int(input("Enter the coefficient of the " + wordAns + " product: "))
                    EPre2 = float(input("Enter the pressure in atm of the " + wordAns + " product: "))
                    if EPro == None:
                        EPro = 1
                    EPro = float(EPro * (EPre2 ** float(EC2)))
                    EDummy2 = EDummy2 + 1
                EType1ANS = str(float(EPro) / float(ERea))
                print()
                print("The equilibrium constant of the pressure (Kp) of this reaction is " + EType1ANS + ".\n")

    if calculationType == 9:
        print("\n1 = Entropy")
        print("2 = Change in Entropy\n")
        while True:
            EnType = int(input("Enter the number of the entropy calculation that you would like to solve, or \"0\" to quit: : "))
            if (EnType != 0) & (EnType != 1) & (EnType != 2):
                print()
                print("Please enter a valid option.\n")
            if EnType == 0:
                break
            if EnType == 1:
                EnStates = float(input("Enter the total number of possible states (W): "))
                print()
                print("The entropy is " + str(1.38065e-23 * math.log(EnStates)) + ".\n")
            if EnType == 2:
                print()
                EnDH = float(input("Enter the enthalpy of the foward reaction: "))
                EnT = float(input("Enter the temperature in kelvin of which the reaction occured at: "))
                print("\nThe change in entropy is " + str(EnDH/EnT) + ".")

    if calculationType == 10:
        print()
        print("Note: Tons refers to the imperial unit equivalent to 2000 pounds for all conversions.\n")
        print("1 = Imperial to Metric")
        print("2 = Metric to Imperial\n")
        while True:
            UType = int(input("Enter the number the conversion type that you would like to solve, or \"0\" to quit : "))
            if (UType != 0) & (UType != 1) & (UType != 2):
                print()
                print("Please enter a valid option.\n")
            if UType == 0:
                break
            if UType == 1:
                print("\n1 = Feet")
                print("2 = Inches")
                print("3 = Yards")
                print("4 = Miles")
                print("5 = Nautical Miles")
                print("6 = Acres")
                print("7 = Square Miles")
                print("8 = Square Feet")
                print("9 = Fluid Ounces")
                print("10 = Pints")
                print("11 = Quarts")
                print("12 = Gallons")
                print("13 = Ounces")
                print("14 = Pounds")
                print("15 = Tons")
                print("16 = Fahrenheit")
                while True:
                    print()
                    UInput = int(input("Enter the number of the imperial unit that you have, or \"0\" to quit: "))
                    if UInput == 0:
                        break
                    if UInput == 1:
                        print()
                        UImp1 = float(input("Enter the number of feet that you have: "))
                        UImp = UImp1 * 0.3048
                        print("\n1 = Millimeters")
                        print("2 = Meters")
                        print("3 = Kilometers\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " feet is " + str(UImp * 1000) + " millimeters.")
                        if UMet == 2:
                            print(str(UImp1) + " feet is " + str(UImp) + " meters.")
                        if UMet == 3:
                            print(str(UImp1) + " feet is " + str(UImp / 1000) + " kilometers.")
                    if UInput == 2:
                        UImp1 = float(input("Enter the number of inches that you have: "))
                        UImp = (UImp1 / 12) * 0.3048
                        print("\n1 = Millimeters")
                        print("2 = Meters")
                        print("3 = Kilometers\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " inches is " + str(UImp * 1000) + " millimeters.")
                        if UMet == 2:
                            print(str(UImp1) + " inches is " + str(UImp) + " meters.")
                        if UMet == 3:
                            print(str(UImp1) + " inches is " + str(UImp / 1000) + " kilometers.")
                    if UInput == 3:
                        UImp1 = float(input("Enter the number of yards that you have: "))
                        UImp = (UImp1 * 3) * 0.3048
                        print("\n1 = Millimeters")
                        print("2 = Meters")
                        print("3 = Kilometers\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " yards is " + str(UImp * 1000) + " millimeters.")
                        if UMet == 2:
                            print(str(UImp1) + " yards is " + str(UImp) + " meters.")
                        if UMet == 3:
                            print(str(UImp1) + " yards is " + str(UImp / 1000) + " kilometers.")
                    if UInput == 4:
                        UImp1 = float(input("Enter the number of miles that you have: "))
                        UImp = (UImp1 * 5280) * 0.3048
                        print("\n1 = Millimeters")
                        print("2 = Meters")
                        print("3 = Kilometers\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " miles is " + str(UImp * 1000) + " millimeters.")
                        if UMet == 2:
                            print(str(UImp1) + " miles is " + str(UImp) + " meters.")
                        if UMet == 3:
                            print(str(UImp1) + " miles is " + str(UImp / 1000) + " kilometers.")
                    if UInput == 5:
                        UImp1 = float(input("Enter the number of nautical miles that you have: "))
                        UImp = (UImp1 * 6076.12) * 0.3048
                        print("\n1 = Millimeters")
                        print("2 = Meters")
                        print("3 = Kilometers\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " nautical miles is " + str(UImp * 1000) + " millimeters.")
                        if UMet == 2:
                            print(str(UImp1) + " nautical miles is " + str(UImp) + " meters.")
                        if UMet == 3:
                            print(str(UImp1) + " nautical miles is " + str(UImp / 1000) + " kilometers.")
                    if UInput == 6:
                        UImp1 = float(input("Enter the number of acres that you have: "))
                        UImp = (UImp1 * 4046.8564224)
                        print("\n1 = Square Millimeters")
                        print("2 = Square Meters")
                        print("3 = Square Kilometers\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " acres is " + str(UImp * 1000) + " square millimeters.")
                        if UMet == 2:
                            print(str(UImp1) + " acres is " + str(UImp) + " square meters.")
                        if UMet == 3:
                            print(str(UImp1) + " acres is " + str(UImp / 1000) + " square kilometers.")
                    if UInput == 7:
                        UImp1 = float(input("Enter the number of square miles that you have: "))
                        UImp = ((UImp1 * 640) * 4046.8564224)
                        print("\n1 = Square Millimeters")
                        print("2 = Square Meters")
                        print("3 = Square Kilometers\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " square miles is " + str(UImp * 1000) + " square millimeters.")
                        if UMet == 2:
                            print(str(UImp1) + " square miles is " + str(UImp) + " square meters.")
                        if UMet == 3:
                            print(str(UImp1) + " square miles is " + str(UImp / 1000) + " square kilometers.")
                    if UInput == 8:
                        UImp1 = float(input("Enter the number of square feet that you have: "))
                        UImp = (UImp1 * 0.09290304)
                        print("\n1 = Square Millimeters")
                        print("2 = Square Meters")
                        print("3 = Square Kilometers\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " square feet is " + str(UImp * 1000) + " square millimeters.")
                        if UMet == 2:
                            print(str(UImp1) + " square feet is " + str(UImp) + " square meters.")
                        if UMet == 3:
                            print(str(UImp1) + " square feet is " + str(UImp / 1000) + " square kilometers.")
                    if UInput == 9:
                        UImp1 = float(input("Enter the number of fluid ounces that you have: "))
                        UImp = (UImp1 * 0.0295735296)
                        print("\n1 = Milliliters")
                        print("2 = Liters")
                        print("3 = Kiloliters\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " fluid ounces is " + str(UImp * 1000) + " milliliters.")
                        if UMet == 2:
                            print(str(UImp1) + " fluid ounces is " + str(UImp) + " liters.")
                        if UMet == 3:
                            print(str(UImp1) + " fluid ounces is " + str(UImp / 1000) + " kiloliters.")
                    if UInput == 10:
                        UImp1 = float(input("Enter the number of pints that you have: "))
                        UImp = (UImp1 * 0.473176473)
                        print("\n1 = Milliliters")
                        print("2 = Liters")
                        print("3 = Kiloliters\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " pints is " + str(UImp * 1000) + " milliliters.")
                        if UMet == 2:
                            print(str(UImp1) + " pints is " + str(UImp) + " liters.")
                        if UMet == 3:
                            print(str(UImp1) + " pints is " + str(UImp / 1000) + " kiloliters.")
                    if UInput == 11:
                        UImp1 = float(input("Enter the number of quarts that you have: "))
                        UImp = (UImp1 * 0.946352946)
                        print("\n1 = Milliliters")
                        print("2 = Liters")
                        print("3 = Kiloliters\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " quarts is " + str(UImp * 1000) + " milliliters.")
                        if UMet == 2:
                            print(str(UImp1) + " quarts is " + str(UImp) + " liters.")
                        if UMet == 3:
                            print(str(UImp1) + " quarts is " + str(UImp / 1000) + " kiloliters.")
                    if UInput == 12:
                        UImp1 = float(input("Enter the number of gallons that you have: "))
                        UImp = (UImp1 * 3.785411784)
                        print("\n1 = Milliliters")
                        print("2 = Liters")
                        print("3 = Kiloliters\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " gallons is " + str(UImp * 1000) + " milliliters.")
                        if UMet == 2:
                            print(str(UImp1) + " gallons is " + str(UImp) + " liters.")
                        if UMet == 3:
                            print(str(UImp1) + " gallons is " + str(UImp / 1000) + " kiloliters.")
                    if UInput == 13:
                        UImp1 = float(input("Enter the number of ounces that you have: "))
                        UImp = (UImp1 * 28.349523125)
                        print("\n1 = Milligrams")
                        print("2 = Grams")
                        print("3 = Kilograms\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " ounces is " + str(UImp * 1000) + " milligrams.")
                        if UMet == 2:
                            print(str(UImp1) + " ounces is " + str(UImp) + " grams.")
                        if UMet == 3:
                            print(str(UImp1) + " ounces is " + str(UImp / 1000) + " kilograms.")
                    if UInput == 14:
                        UImp1 = float(input("Enter the number of pounds that you have: "))
                        UImp = (UImp1 * 453.59237)
                        print("\n1 = Milligrams")
                        print("2 = Grams")
                        print("3 = Kilograms\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " pounds is " + str(UImp * 1000) + " milligrams.")
                        if UMet == 2:
                            print(str(UImp1) + " pounds is " + str(UImp) + " grams.")
                        if UMet == 3:
                            print(str(UImp1) + " pounds is " + str(UImp / 1000) + " kilograms.")
                    if UInput == 15:
                        UImp1 = float(input("Enter the number of tons that you have: "))
                        UImp = (UImp1 * 907184.74)
                        print("\n1 = Milligrams")
                        print("2 = Grams")
                        print("3 = Kilograms\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " tons is " + str(UImp * 1000) + " milligrams.")
                        if UMet == 2:
                            print(str(UImp1) + " tons is " + str(UImp) + " grams.")
                        if UMet == 3:
                            print(str(UImp1) + " tons is " + str(UImp / 1000) + " kilograms.")
                    if UInput == 16:
                        UImp1 = float(input("Enter the temperature in fahrenheit that you have: "))
                        UImp = ((UImp1 - 32) * (5/9))
                        print("\n1 = Celsius")
                        print("2 = Kelvin\n")
                        UMet = int(input("Enter the number of the metric unit that you want to convert to: "))
                        print()
                        if UMet == 1:
                            print(str(UImp1) + " fahrenheit is " + str(UImp) + " celsius.")
                        if UMet == 2:
                            print(str(UImp1) + " fahrenheit is " + str(UImp + 273) + " kelvin.")
            if UType == 2:
                print("\n1 = Meters")
                print("2 = Millimeters")
                print("3 = Kilometers")
                print("4 = Square Meters")
                print("5 = Square Millimeters")
                print("6 = Square Kilometers")
                print("7 = Cubic Meters")
                print("8 = Cubic Millimeters")
                print("9 = Cubic Kilometers")
                print("10 = Grams")
                print("11 = Milligrams")
                print("12 = Kilograms")
                print("13 = Celsius")
                while True:
                    print()
                    UInput = int(input("Enter the number of the imperial unit that you have, or \"0\" to quit: "))
                    if UInput == 0:
                        break
                    if UInput == 1:
                        UMet1 = float(input("Enter the number of meters that you have: "))
                        print("\n1 = Feet")
                        print("2 = Inches")
                        print("3 = Yards")
                        print("4 = Miles")
                        print("5 = Nautical Miles\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = UMet1
                        if UImp == 1:
                            print(str(UMet1) + " meters is " + str(UMet * 3.280839895) + " feet.")
                        if UImp == 2:
                            print(str(UMet1) + " meters is " + str((UMet * 3.280839895) * 12) + " inches.")
                        if UImp == 3:
                            print(str(UMet1) + " meters is " + str((UMet * 3.280839895) * 3) + " yards.")
                        if UImp == 4:
                            print(str(UMet1) + " meters is " + str(UMet * 0.0006213689) + " miles.")
                        if UImp == 5:
                            print(str(UMet1) + " meters is " + str(UMet * 1852) + " nautical miles.")
                    if UInput == 2:
                        UMet1 = float(input("Enter the number of millimeters that you have: "))
                        print("\n1 = Feet")
                        print("2 = Inches")
                        print("3 = Yards")
                        print("4 = Miles")
                        print("5 = Nautical Miles\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = UMet1 / 1000
                        if UImp == 1:
                            print(str(UMet1) + " millimeters is " + str(UMet * 3.280839895) + " feet.")
                        if UImp == 2:
                            print(str(UMet1) + " millimeters is " + str((UMet * 3.280839895) * 12) + " inches.")
                        if UImp == 3:
                            print(str(UMet1) + " millimeters is " + str((UMet * 3.280839895) * 3) + " yards.")
                        if UImp == 4:
                            print(str(UMet1) + " millimeters is " + str(UMet * 0.0006213689) + " miles.")
                        if UImp == 5:
                            print(str(UMet1) + " millimeters is " + str(UMet * 1852) + " nautical miles.")
                    if UInput == 3:
                        UMet1 = float(input("Enter the number of kilometers that you have: "))
                        print("\n1 = Feet")
                        print("2 = Inches")
                        print("3 = Yards")
                        print("4 = Miles")
                        print("5 = Nautical Miles\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = UMet1 * 1000
                        if UImp == 1:
                            print(str(UMet1) + " kilometers is " + str(UMet * 3.280839895) + " feet.")
                        if UImp == 2:
                            print(str(UMet1) + " kilometers is " + str((UMet * 3.280839895) * 12) + " inches.")
                        if UImp == 3:
                            print(str(UMet1) + " kilometers is " + str((UMet * 3.280839895) * 3) + " yards.")
                        if UImp == 4:
                            print(str(UMet1) + " kilometers is " + str(UMet * 0.0006213689) + " miles.")
                        if UImp == 5:
                            print(str(UMet1) + " kilometers is " + str(UMet * 1852) + " nautical miles.")
                    if UInput == 4:
                        UMet1 = float(input("Enter the number of square meters that you have: "))
                        print("\n1 = Acres")
                        print("2 = Square Miles")
                        print("3 = Square Feet\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = UMet1
                        if UImp == 1:
                            print(str(UMet1) + " square meters is " + str(UMet * 3.280839895) + " acres.")
                        if UImp == 2:
                            print(str(UMet1) + " square meters is " + str(UMet * 3.861018768E-7) + " square miles.")
                        if UImp == 3:
                            print(str(UMet1) + " square meters is " + str(UMet * 10.763910417) + " square feet.")
                    if UInput == 5:
                        UMet1 = float(input("Enter the number of square millimeters that you have: "))
                        print("\n1 = Acres")
                        print("2 = Square Miles")
                        print("3 = Square Feet\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = UMet1 / 1000
                        if UImp == 1:
                            print(str(UMet1) + " square millimeters is " + str(UMet * 3.280839895) + " acres.")
                        if UImp == 2:
                            print(str(UMet1) + " square millimeters is " + str(UMet * 3.861018768E-7) + " square miles.")
                        if UImp == 3:
                            print(str(UMet1) + " square millimeters is " + str(UMet * 10.763910417) + " square feet.")
                    if UInput == 6:
                        UMet1 = float(input("Enter the number of square kilometers that you have: "))
                        print("\n1 = Acres")
                        print("2 = Square Miles")
                        print("3 = Square Feet\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = UMet1 * 1000
                        if UImp == 1:
                            print(str(UMet1) + " square kilometers is " + str(UMet * 3.280839895) + " acres.")
                        if UImp == 2:
                            print(str(UMet1) + " square kilometers is " + str(UMet * 3.861018768E-7) + " square miles.")
                        if UImp == 3:
                            print(str(UMet1) + " square kilometers is " + str(UMet * 10.763910417) + " square feet.")
                    if UInput == 7:
                        UMet1 = float(input("Enter the number of cubic meters that you have: "))
                        print("\n1 = Fluid Ounces")
                        print("2 = Pints")
                        print("3 = Quarts")
                        print("4 = Gallons\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = UMet1
                        if UImp == 1:
                            print(str(UMet1) + " cubic meters is " + str(UMet * 33814.038638) + " fluid ounces.")
                        if UImp == 2:
                            print(str(UMet1) + " cubic meters is " + str(UMet * 2113.3774149) + " pints.")
                        if UImp == 3:
                            print(str(UMet1) + " cubic meters is " + str(UMet * 1056.6887074) + " quarts.")
                        if UImp == 3:
                            print(str(UMet1) + " cubic meters is " + str(UMet * 264.17217686) + " gallons.")
                    if UInput == 8:
                        UMet1 = float(input("Enter the number of cubic millimeters that you have: "))
                        print("\n1 = Fluid Ounces")
                        print("2 = Pints")
                        print("3 = Quarts")
                        print("4 = Gallons\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = UMet1 / 1000
                        if UImp == 1:
                            print(str(UMet1) + " cubic millimeters is " + str(UMet * 33814.038638) + " fluid ounces.")
                        if UImp == 2:
                            print(str(UMet1) + " cubic millimeters is " + str(UMet * 2113.3774149) + " pints.")
                        if UImp == 3:
                            print(str(UMet1) + " cubic millimeters is " + str(UMet * 1056.6887074) + " quarts.")
                        if UImp == 3:
                            print(str(UMet1) + " cubic millimeters is " + str(UMet * 264.17217686) + " gallons.")
                    if UInput == 9:
                        UMet1 = float(input("Enter the number of cubic kilometers that you have: "))
                        print("\n1 = Fluid Ounces")
                        print("2 = Pints")
                        print("3 = Quarts")
                        print("4 = Gallons\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = UMet1 * 1000
                        if UImp == 1:
                            print(str(UMet1) + " cubic kilometers is " + str(UMet * 33814.038638) + " fluid ounces.")
                        if UImp == 2:
                            print(str(UMet1) + " cubic kilometers is " + str(UMet * 2113.3774149) + " pints.")
                        if UImp == 3:
                            print(str(UMet1) + " cubic kilometers is " + str(UMet * 1056.6887074) + " quarts.")
                        if UImp == 3:
                            print(str(UMet1) + " cubic kilometers is " + str(UMet * 264.17217686) + " gallons.")
                    if UInput == 10:
                        UMet1 = float(input("Enter the number of grams that you have: "))
                        print("\n1 = Pounds")
                        print("2 = Ounces")
                        print("3 = Tons\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = UMet1 * 0.0022046244
                        if UImp == 1:
                            print(str(UMet1) + " grams is " + str(UMet) + " pounds.")
                        if UImp == 2:
                            print(str(UMet1) + " grams is " + str(UMet * 16) + " ounces.")
                        if UImp == 3:
                            print(str(UMet1) + " grams is " + str(UMet / 2000) + " tons.")
                    if UInput == 11:
                        UMet1 = float(input("Enter the number of milligrams that you have: "))
                        print("\n1 = Pounds")
                        print("2 = Ounces")
                        print("3 = Tons\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = (UMet1 * 1000) * 0.0022046244
                        if UImp == 1:
                            print(str(UMet1) + " milligrams is " + str(UMet) + " pounds.")
                        if UImp == 2:
                            print(str(UMet1) + " milligrams is " + str(UMet * 16) + " ounces.")
                        if UImp == 3:
                            print(str(UMet1) + " milligrams is " + str(UMet / 2000) + " tons.")
                    if UInput == 12:
                        UMet1 = float(input("Enter the number of kilograms that you have: "))
                        print("\n1 = Pounds")
                        print("2 = Ounces")
                        print("3 = Tons\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = (UMet1 / 1000) * 0.0022046244
                        if UImp == 1:
                            print(str(UMet1) + " kilograms is " + str(UMet) + " pounds.")
                        if UImp == 2:
                            print(str(UMet1) + " kilograms is " + str(UMet * 16) + " ounces.")
                        if UImp == 3:
                            print(str(UMet1) + " kilograms is " + str(UMet / 2000) + " tons.")
                    if UInput == 13:
                        UMet1 = float(input("Enter the temperature in celsius that you have: "))
                        print("\n1 = Fahrenheit")
                        print("2 = Kelvin\n")
                        UImp = int(input("Enter the number of the imperial unit that you want to convert to: "))
                        print()
                        UMet = ((UMet1 * (9/5)) + 32)
                        if UImp == 1:
                            print(str(UMet1) + " celsius is " + str(UMet) + " fahrenheit.")
                        if UImp == 2:
                            print(str(UMet1) + " celsius is " + str(UMet1 + 273) + " kelvin.")


    if calculationType == 11:
        while True:
            sigFig = int(input("\n\nEnter the number of significant figures that you would like to round to, or \"0\" to exit: "))
            if sigFig == 0:
                break
            else:
                sigFigNum = float(input("\nEnter the number that you would like to round: "))
                sigFigAns = float(round(sigFigNum, sigfigs=sigFig))
                print()
                print(str(sigFigNum) + "rounded to " + str(sigFig) + "significant figures is " + str(sigFigAns) + " .")