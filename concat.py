# Fonction de concaténation de fichier.
def concatenation(files, name):
    with open("Fichier_concat/"+name+".txt", "w") as new_file:
        for name in files:
            with open(name) as f:
                for line in f:
                    new_file.write(line)
                
                new_file.write("\n")