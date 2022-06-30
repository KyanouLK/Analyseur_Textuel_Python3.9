import spacy
import matplotlib.pyplot as plt  
from wordcloud import WordCloud, STOPWORDS  
import codecs
from PIL import Image
import numpy as np
import nltk
from nltk.corpus import stopwords

# Chargement du module spacy version française
nlp = spacy.load("fr_core_news_sm")

nltk.download('stopwords')

# Initialisation du premier module de stopwords
stopWords = set(stopwords.words('french'))

# Fonction de lecture d'un fichier entier
def all_part_file(filepath):
    fichier = codecs.open(filepath, encoding='utf-8')
    f = fichier.readlines()
    fichier.close()
    return f

# Fonction de lecture de la première moitié d'un fichier (utilisé pour une version antérieur du programme)
# def first_part_file(filepath):
#     fichier = codecs.open(filepath, encoding='utf-8')
#     f = fichier.readlines()
#     nbline = len(f)
#     mid = int(nbline/2)
#     firstpart = f[:mid]
#     fichier.close()
#     return firstpart

# Fonction de lecture de la seconde partie d'un fichier (utilisé pour une version antérieur du programme)
# def last_part_file(filepath):
#     fichier = codecs.open(filepath, encoding='utf-8')
#     f = fichier.readlines()
#     nbline = len(f)
#     mid = int(nbline/2)
#     lastpart = f[mid:]
#     fichier.close()
#     return lastpart

# Fonction de de prétraitement récupérant tous les mots
def return_token(text):
    aux = []
    for sentence in text:
        doc = nlp(sentence) # Traitement d'une phrase avec spacy
        for X in doc:
            aux.append(X.text) # On ajoute chaque mots de la phrase dans le tableau
    return aux

# Fonction de de prétraitement récupérant tous les noms
def return_nouns(text):
    aux = []
    for sentence in text:
        doc = nlp(sentence) # Traitement d'une phrase avec spacy
        for chunk in doc.noun_chunks:
            aux.append(chunk.text) # On ajoute chaque noms de la phrase dans le tableau
    return aux

# Fonction de de prétraitement récupérant tous les verbes
def return_verbs(text):
    aux = []
    for sentence in text:
        doc = nlp(sentence) # Traitement d'une phrase avec spacy
        for token in doc:
            if token.pos_ == "VERB":
                aux.append(token.lemma_) # On ajoute chaque verbe de la phrase dans le tableau
    return aux

# Fonction pour appliquer une liste de stopwords au texte
def cleaner(fic, sw_list):
    clean_words = []
    for token in fic:
        if token not in sw_list: # On compare chaque mots du texte aux mots contenus dans la liste de stopwords
            clean_words.append(token)
    return clean_words

# Seconde liste de stopwords (fait main)
stoppeur = {"l'",
            "L'",
            "d'", 
            "D'",
            "s'",
            "S'",
            "c'",
            "C'",
            "n'",
            "N'",
            "qu'",
            "Qu'",
            "ni",
            "Ni",
            "en",
            "En",
            "Sans",
            "sans",
            "jamais",
            "Jamais",
            "Jusqu'",
            "jusqu'",
            "j'",
            "J'",
            "A",
            "À",
            "ça",
            "Ça",
            "Là",
            "là",
            "km",
            "KM",
            "Km",
            "Be",
            "BE",
            "m'",
            "M'",
            "DEE",
            "dee",
            "cc",
            "CC",
            "Dee",
            "EEE",
            "CCE",
            "CU",
            "EE",
            "EC",
            "ECC",
            "CCC",
            "eee",
            "ee",
            "CT",
            "CU",
            "Cu",
            "EME",
            "c",
            "ur",
            "c ur",
            "C",
            "UR",
            "C UR"}

# Troisième liste de stopwords trouver sur internet
last_stopwords = ["a","à","â","abord","afin","ah","ai","aie","ainsi","allaient","allo","allô","allons","après","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","auquel","aura","auront","aussi","autre","autres","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","ayant","b","bah","beaucoup","bien","bigre","boum","bravo","brrr","brusquemer","c","ça","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chaque","cher","chère","chères","chers","chez","chiche","chut","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","delà","depuis","derrière","des","dès","désormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","différent","différente","différentes","différents","dire","divers","diverse","diverses","dix","dix-huit","dixième","dix-neuf","dix-sept","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","e","effet","eh","elle","elle-même","elles","elles-mêmes","en","encore","entre","envers","environ","es","ès","est","et","etant","étaient","étais","était","étant","etc","été","etre","être","eu","euh","eux","eux-mêmes","excepté","f","façon","fais","faisaient","faisant","fait","feront","fi","flac","floc","font","g","gens","h","ha","hé","hein","hélas","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","i","il","ils","importe","j","je","jusqu","jusque","k","l","la","là","laquelle","las","le","lequel","les","lès","lesquelles","lesquels","leur","leurs","longtemps","lorsque","lui","lui-même","m","ma","maint","mais","malgré","me","même","mêmes","merci","mes","mien","mienne","miennes","miens","mille","mince","moi","moi-même","moins","mon","moyennant","n","na","ne","néanmoins","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notre","nôtre","nôtres","nous","nous-mêmes","nul","o","o|","ô","oh","ohé","olé","ollé","on","ont","onze","onzième","ore","ou","où","ouf","ouias","oust","ouste","outre","p","paf","pan","par","parmi","partant","particulier","particulière","particulièrement","pas","passé","pendant","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","plein","plouf","plus","plusieurs","plutôt","pouah","pour","pourquoi","premier","première","premièrement","près","proche","psitt","puisque","q","qu","Q","Qu","quand","quant","quanta","quant-à-soi","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelque","quelques","quelqu'un","quels","qui","quiconque","quinze","quoi","quoique","r","revoici","revoilà","rien","s","sa","sacrebleu","sans","sapristi","sauf","se","seize","selon","sept","septième","sera","seront","ses","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","stop","suis","suivant","sur","surtout","t","ta","tac","tant","te","té","tel","telle","tellement","telles","tels","tenant","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutes","treize","trente","très","trois","troisième","troisièmement","trop","tsoin","tsouin","tu","u","un","une","unes","uns","v","va","vais","vas","vé","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vôtre","vôtres","vous","vous-mêmes","vu","w","x","y","z","zut","alors","aucuns","bon","devrait","dos","droite","début","essai","faites","fois","force","haut","ici","juste","maintenant","mine","mot","nommés","nouveaux","parce","parole","personnes","pièce","plupart","seulement","soyez","sujet","tandis","valeur","voie","voient","état","étions"]

# Fonction d'écriture du texte dans un autre fichier texte sans les stopwords
def writer(filepath, clean_tab):
    filefp = open(filepath, "w+")

    for element in clean_tab:
        content = str(element)
        filefp.write(content)
        filefp.write("\n")

    filefp.close()

# Fonction de lecture d'un fichier texte pour utilisation du nuage de mots
def reader(filepath):
    file = open(filepath, "r")
    content = file.read()
    file.close()
    return content

# Création et génération d'un wordcloud
def cloud_creator(fp, lp, nbmots, forme_nuage, forme_mots, name_file1, name_file2):

    mask = None

    if forme_nuage != "None":
        mask = np.array(Image.open('WordCloud/'+forme_nuage+'.jpg')) # Récupération de la forme du nuage choisie

    font = None

    if forme_mots != "None":
        font = 'Font/'+forme_mots+'.ttf' # Récupération de la police d'écriture choisie
    
    wc = WordCloud(stopwords = set(stopwords.words('french')),
                font_path=font,
                mask = mask, 
                background_color = (255, 255, 255),
                max_words = nbmots,
                max_font_size = 1000,
                random_state = 42)
    
    wc.generate(fp) # génération du nuage de mots du premier fichier
    plt.figure(figsize=[10,5])
    plt.subplot(1,2,1)
    plt.title(name_file1)
    plt.imshow(wc, interpolation = "bilinear")
    plt.axis('off')
    wc.generate(lp) # génération du nuage de mots du second fichier
    plt.subplot(1,2,2)
    plt.title(name_file2)
    plt.imshow(wc, interpolation = "bilinear")
    plt.axis('off')
    plt.show()
