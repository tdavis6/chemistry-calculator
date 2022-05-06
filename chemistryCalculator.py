import math
print("Chemistry Calculator")
print("Developed by Tyler Davis")
print("2022")
print("Version 1-beta.0.0")
print()
print("*****THIS IS A BETA VERSION*****")
print()
#Notes:
#Code for molar mass calculations was created by @elibroftw on GitHub can be found here: https://gist.github.com/elibroftw/22e3b4c1eb7fa0a6c83d099d24200f95
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
while True:
    #Get type of calculation
    print()
    print("Main Menu")
    print()
    print("1 = Molar Mass Calculator")
    print("2 = Stoichiometry Calculations")
    print("3 = Molarity Calculations")
    print("4 = Dilution Calculations")
    print("5 = pH/pOH/H+ Concentration/OH- Concentration Converter")
    print("6 = Gas Law Calculations")
    print()
    calculationType = int(input("Enter the number of the calculation shown above that you would like to be completed, or \"0\" to quit: "))
    #Go to calculation type
    if calculationType == 0:
        break


    if calculationType == 1:
        while True:
            MMCInput = input(str('\nEnter Compound Formula (capitalize elements, eg. Mn instead of mn) or enter \"0\" to quit: '))
            if MMCInput == "0":
                break
            else:
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

                    user_input = MMCInput
                    print()
                    print(f'The molar mass of {user_input} is {molar_mass(user_input, DECIMAL_PLACES)} g/mol')


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
            if SType == 0:
                break
            #Code for molar mass calculations can be found here: https://gist.github.com/elibroftw/22e3b4c1eb7fa0a6c83d099d24200f95
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

                if (SType == 1) or (SType == 2) or (SType == 3) or (SType == 4):
                    SFormula1 = input('Enter the first (X) compound formula (please capitalize elements, eg. Mn instead of mn): ')
                SCoefficient1 = int(input("What is the coefficient of the first (X) compount (Please make sure the reaction is balanced)? "))
                SAmount1 = float(input("Enter the amount of the first (X) item you have (eg. 5g, 2.4 mol, 7.0E23 particles, or 15.4L [do not include the unit]): "))
                SFormula2 = input('Enter the second (Y) compound formula (please capitalize elements, eg. Mn instead of mn): ')
                SCoefficient2 = int(input("What is the coefficient of the second (Y) compount (Please make sure the reaction is balanced)? "))
                #Format prints like this:
                #print(f'The molar mass of {user_input} is {molar_mass(user_input, DECIMAL_PLACES)} g/mol')
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
        print()
        print("1 = Molarity")
        print("2 = Moles of Solute")
        print("3 = Liters of Solution")
        print()
        while True:
            #Get type of calculation
            MType = int(input("Enter the number of the number that you would like to find, or \"0\" to quit: "))
            print()
            #Do the calculation
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
                print()
                print("There is", MMolesOfSolute, "moles of the solute.")
            if MType == 3:
                MMolesOfSolute = float(input("How many moles of solute is there? "))
                MMolarity = float(input("What is the molarity of this solution? "))
                MLitersOfSolution = MMolesOfSolute/MMolarity
                print()
                print("There is", MLitersOfSolution, "liters of solution.")


    if calculationType == 4:
        print()
        print("Note: Please use liters for volume and moles for molarity.")
        print("1 = Molarity")
        print("2 = Volume")
        print()
        while True:
            DType = int(input("Enter the number of the variable you would like to solve for, or \"0\" to quit: "))
            if DType == 0:
                break
            if DType == 1:
                DM1 = float(input("Enter the value of the initial molarity (M1): "))
                DV1 = float(input("Enter the value of the initial volume (V1): "))
                DV2 = float(input("Enter the value of the final volume (V2): "))
                DANS1 = ((DM1*DV1)/DV2)
                print()
                print(DANS1, "is the final molarity.")
                print()
            if DType == 2:
                DM1 = float(input("Enter the value of the initial molarity (M1): "))
                DV1 = float(input("Enter the value of the initial volume (V1): "))
                DM2 = float(input("Enter the value of the final molarity (M2): "))
                DANS2 = ((DM1*DV1)/DM2)
                print()
                print(DANS2, "is the final molarity.")
                print()


    if calculationType == 5:
        # Get type of conversion
        print()
        print("1 = pH to pOH")
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
        print("12 = OH- Concentration to H+ Concentration")
        print()
        while True:
            print()
            pHtype = int(input("Enter the number of the conversion shown above that you would like to be done, or \"0\" to quit: "))
            #option to quit
            if pHtype == 0:
                break
            #get both numbers
            pHnumber = float(input("What is the number that you would like to convert? "))
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
        print()
        print("1 = Boyle's Law (Pressure and Volume)")
        print("2 = Charles' Law (Volume and Temperature)")
        print("3 = Gay-Lussac's Law (Pressure and Temperature)")
        print("4 = Avogadro's Law (Volume and Moles)")
        print("5 = Combined Gas Law")
        print("6 = Ideal Gas Law")

        while True:
            print()
            GLType = int((input("Enter the number of the gas law calculation shown above that you would like to be done, or \"0\" to quit: ")))
            if GLType == 0:
                break
            if GLType == 1:
                print()
                print("Note: All values must be in atmospheres or liters, respectively.")
                print("1 = Pressure")
                print("2 = Volume")
                GLType2 = int(input("Enter the number of the variable you would like to solve for: "))
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
                print()
                print("Note: All values must be in liters or kelvin, respectively.")
                print("1 = Volume")
                print("2 = Temperature")
                print()
                GLType2 = int(input("Enter the number of the variable you would like to solve for: "))
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
                print()
                print("Note: All values must be in atmospheres or kelvin, respectively.")
                print("1 = Pressure")
                print("2 = Temperature")
                print()
                GLType2 = int(input("Enter the number of the variable you would like to solve for: "))
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
                print()
                print("Note: All values must be in liters or moles, respectively.")
                print("1 = Volume")
                print("2 = Moles")
                print()
                GLType2 = int(input("Enter the number of the variable you would like to solve for: "))
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
                print()
                print("Note: All values must be in atmospheres, liters, or kelvin, respectively.")
                print("1 = Pressure")
                print("2 = Volume")
                print("3 = Temperature")
                print()
                GLType2 = int(input("Enter the number of the variable you would like to solve for: "))
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
                print()
                print("Note: All values must be in atmospheres, liters, moles, or kelvin, respectively.")
                print("1 = Pressure")
                print("2 = Volume")
                print("3 = Moles")
                print("4 = Temperature")
                print()
                GLType2 = int(input("Enter the number of the variable you would like to solve for: "))
                R = float(0.082057366080960)
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



#Chuck needs a GF

#Never gonna give you up
#Never gonna let you down
#Never gonna run around and desert you
#Never gonna make you cry
#Never gonna say goodbye
#Never gonna tell a lie and hurt you