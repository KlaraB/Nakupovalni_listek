__author__ = 'U269074'

nakupovalni_seznam = []

odgovor = "da"

while odgovor == "da":
    odgovor = raw_input("Ali zelis dodati izdelek na seznam (da/ne)?" )
    if odgovor == "da":
        dodani_izdelek = raw_input("Napisi izdelek, ki ga zelis dodati: ")
        nakupovalni_seznam.append(dodani_izdelek)
        print ("Nakupovalni seznam je naslednji: ")+ str(nakupovalni_seznam)


    elif odgovor == "ne":
        print ("Nakupovalni seznam je naslednji: ")+ str(nakupovalni_seznam)
        break

