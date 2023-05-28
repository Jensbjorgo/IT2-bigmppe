# alder=int(input"fødselsår..")
# fodsel= 2023-alder
# print(f"Fødselsår:{fodsel}")



while True:
    try:
        alder= int(input( "fødselsår.."))
        assert alder>= 0
        break
    except:
        print("alder må være heltall...")

fodsel= 2023-alder
print(f"år:{fodsel}")
