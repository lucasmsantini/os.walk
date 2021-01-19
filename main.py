import os
main_path = './t11'

for root, subfolder, filename in os.walk(main_path):
    #for folder in subfolder:
    #    print(folder)
    for npl in filename:
        TemNPL = False
        if '.npl' in npl:
            temNPL = True
            print(npl)
            print(temNPL)
            print(npl.count('.npl'))


