#!/usr/env/bin python3

import collections

TeamMember = collections.namedtuple("TeamMember",
                                "ID FamilyName FirstName Gender")

PPT = []

PPT.append(TeamMember(1, "Taylor", "Joe", "Male"))
PPT.append(TeamMember(2, "Hesford", "Catherine", "Female"))
PPT.append(TeamMember(3, "Warburton", "Amy", "Female"))
PPT.append(TeamMember(4, "Stanton", "Tom", "Male"))
PPT.append(TeamMember(Gender = "Male", FamilyName = "Dunman",
                      FirstName = "Natalie", ID = 5))

#Example extractions
print(PPT)
print(PPT[1])
print(PPT[1][1])
print(PPT[1][-2])

print("")
print(PPT[0].FirstName)
print(PPT[0].FirstName +" "+PPT[0].FamilyName)

print("")
for TeamMember in PPT:
    print(TeamMember.FirstName +" "+TeamMember.FamilyName)

