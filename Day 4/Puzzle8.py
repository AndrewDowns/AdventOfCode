import re

def byr_valid(byr):
    if byr!=None:
        try:
            byr = int(byr)
        except:
            return False
        if byr>=1920 and byr<=2002:
            return True
        else:
            return False
    else:
        return False

def iyr_valid(iyr):
    if iyr!=None:
        try:
            iyr = int(iyr)
        except:
            return False
        if iyr>=2010 and iyr<=2020:
            return True
        else:
            return False
    else:
        return False

def eyr_valid(eyr):
    if eyr!=None:
        try:
            eyr = int(eyr)
        except:
            return False
        if eyr>=2020 and eyr<=2030:
            return True
        else:
            return False
    else:
        return False


def hgt_valid(hgt):
    if hgt != None:
        if re.match('[0-9]+[cm]', hgt):
            hgt = hgt.replace("cm","")
            hgt = int(hgt)
            if hgt>=150 and hgt<=193:
                return True
            else:
                return False

        elif re.match('[0-9]+[in]', hgt):
            hgt = hgt.replace("in", "")
            hgt = int(hgt)
            if hgt>=59 and hgt<=76:
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def hcl_valid(hcl):
    if hcl != None:
        if re.match('[#][0-9 a-f]+', hcl) and len(hcl)==7:
            return True
        else:
            return False
    else:
        return False

def ecl_valid(ecl):
    colours = ["amb", "blu", "brn", "gry", "grn" ,"hzl", "oth"]
    if ecl != None:
        if ecl in colours:
            return True
        else:
            return False
    else:
        return False

def pid_valid(pid):
    if pid != None:
        if len(pid)==9:
            return True
        else:
            return False
    else:
        return False

def cid_valid(cid):
    return True

def passportValid(passport):
    if byr_valid(passport.get("byr")) and eyr_valid(passport.get("eyr")) and iyr_valid(passport.get("iyr")) and hgt_valid(passport.get("hgt")) and hcl_valid(passport.get("hcl")) and ecl_valid(passport.get("ecl")) and pid_valid(passport.get("pid")) and cid_valid(passport.get("cid")):
        return True
    else:
        return False

def populatePossiblePassports():
    clean_possible_passports = []
    fh = open("Passports.txt")
    passports_txt = fh.read()
    possible_passports = passports_txt.split("\n\n")

    for i in range(len(possible_passports)):
        possible_passports[i] = possible_passports[i].replace("\n"," ")

    for passport in possible_passports:
        fields = passport.split()
        passport_dict = dict()
        for field in fields:
            keyValue = field.split(":")
            passport_dict[keyValue[0]] = keyValue[1]
        clean_possible_passports.append(passport_dict)

    return clean_possible_passports

possible_passports = populatePossiblePassports()

valid_passports = []
for passport in possible_passports:
    if passportValid(passport):
        valid_passports.append(passport)

print(len(valid_passports))
