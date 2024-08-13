import streamlit as st 
import matplotlib.pyplot as plt
from PIL import Image 
from tensorflow.keras.preprocessing.image import load_img, img_to_array 
import numpy as np 
from keras.models import load_model 
import google.generativeai as palm
import pyttsx3 
import pandas as pd
import streamlit.components.v1 as components


palm.configure(api_key="AIzaSyDW3Kc1rxsBLuaUnocaueIV9MR0P426uVM") 
model = load_model('b.h5',compile=False)


lab = {
 0: 'ABBOTTS BABBLER',
 1: 'ABBOTTS BOOBY',
 2: 'ABYSSINIAN GROUND HORNBILL',
 3: 'AFRICAN CROWNED CRANE',
 4: 'AFRICAN EMERALD CUCKOO',
 5: 'AFRICAN FIREFINCH',
 6: 'AFRICAN OYSTER CATCHER',
 7: 'AFRICAN PIED HORNBILL',
 8: 'AFRICAN PYGMY GOOSE',
 9: 'ALBATROSS',
 10: 'ALBERTS TOWHEE',
 11: 'ALEXANDRINE PARAKEET',
 12: 'ALPINE CHOUGH',
 13: 'ALTAMIRA YELLOWTHROAT',
 14: 'AMERICAN AVOCET',
 15: 'AMERICAN BITTERN',
 16: 'AMERICAN COOT',
 17: 'AMERICAN DIPPER',
 18: 'AMERICAN FLAMINGO',
 19: 'AMERICAN GOLDFINCH',
 20: 'AMERICAN KESTREL',
 21: 'AMERICAN PIPIT',
 22: 'AMERICAN REDSTART',
 23: 'AMERICAN ROBIN',
 24: 'AMERICAN WIGEON',
 25: 'AMETHYST WOODSTAR',
 26: 'ANDEAN GOOSE',
 27: 'ANDEAN LAPWING',
 28: 'ANDEAN SISKIN',
 29: 'ANHINGA',
 30: 'ANIANIAU',
 31: 'ANNAS HUMMINGBIRD',
 32: 'ANTBIRD',
 33: 'ANTILLEAN EUPHONIA',
 34: 'APAPANE',
 35: 'APOSTLEBIRD',
 36: 'ARARIPE MANAKIN',
 37: 'ASHY STORM PETREL',
 38: 'ASHY THRUSHBIRD',
 39: 'ASIAN CRESTED IBIS',
 40: 'ASIAN DOLLARD BIRD',
 41: 'ASIAN GREEN BEE EATER',
 42: 'ASIAN OPENBILL STORK',
 43: 'AUCKLAND SHAQ',
 44: 'AUSTRAL CANASTERO',
 45: 'AUSTRALASIAN FIGBIRD',
 46: 'AVADAVAT',
 47: 'AZARAS SPINETAIL',
 48: 'AZURE BREASTED PITTA',
 49: 'AZURE JAY',
 50: 'AZURE TANAGER',
 51: 'AZURE TIT',
 52: 'BAIKAL TEAL',
 53: 'BALD EAGLE',
 54: 'BALD IBIS',
 55: 'BALI STARLING',
 56: 'BALTIMORE ORIOLE',
 57: 'BANANAQUIT',
 58: 'BAND TAILED GUAN',
 59: 'BANDED BROADBILL',
 60: 'BANDED PITA',
 61: 'BANDED STILT',
 62: 'BAR-TAILED GODWIT',
 63: 'BARN OWL',
 64: 'BARN SWALLOW',
 65: 'BARRED PUFFBIRD',
 66: 'BARROWS GOLDENEYE',
 67: 'BAY-BREASTED WARBLER',
 68: 'BEARDED BARBET',
 69: 'BEARDED BELLBIRD',
 70: 'BEARDED REEDLING',
 71: 'BELTED KINGFISHER',
 72: 'BIRD OF PARADISE',
 73: 'BLACK AND YELLOW BROADBILL',
 74: 'BLACK BAZA',
 75: 'BLACK BREASTED PUFFBIRD',
 76: 'BLACK COCKATO',
 77: 'BLACK FACED SPOONBILL',
 78: 'BLACK FRANCOLIN',
 79: 'BLACK HEADED CAIQUE',
 80: 'BLACK NECKED STILT',
 81: 'BLACK SKIMMER',
 82: 'BLACK SWAN',
 83: 'BLACK TAIL CRAKE',
 84: 'BLACK THROATED BUSHTIT',
 85: 'BLACK THROATED HUET',
 86: 'BLACK THROATED WARBLER',
 87: 'BLACK VENTED SHEARWATER',
 88: 'BLACK VULTURE',
 89: 'BLACK-CAPPED CHICKADEE',
 90: 'BLACK-NECKED GREBE',
 91: 'BLACK-THROATED SPARROW',
 92: 'BLACKBURNIAM WARBLER',
 93: 'BLONDE CRESTED WOODPECKER',
 94: 'BLOOD PHEASANT',
 95: 'BLUE COAU',
 96: 'BLUE DACNIS',
 97: 'BLUE GRAY GNATCATCHER',
 98: 'BLUE GROSBEAK',
 99: 'BLUE GROUSE',
 100: 'BLUE HERON',
 101: 'BLUE MALKOHA',
 102: 'BLUE THROATED PIPING GUAN',
 103: 'BLUE THROATED TOUCANET',
 104: 'BOBOLINK',
 105: 'BORNEAN BRISTLEHEAD',
 106: 'BORNEAN LEAFBIRD',
 107: 'BORNEAN PHEASANT',
 108: 'BRANDT CORMARANT',
 109: 'BREWERS BLACKBIRD',
 110: 'BROWN CREPPER',
 111: 'BROWN HEADED COWBIRD',
 112: 'BROWN NOODY',
 113: 'BROWN THRASHER',
 114: 'BUFFLEHEAD',
 115: 'BULWERS PHEASANT',
 116: 'BURCHELLS COURSER',
 117: 'BUSH TURKEY',
 118: 'CAATINGA CACHOLOTE',
 119: 'CABOTS TRAGOPAN',
 120: 'CACTUS WREN',
 121: 'CALIFORNIA CONDOR',
 122: 'CALIFORNIA GULL',
 123: 'CALIFORNIA QUAIL',
 124: 'CAMPO FLICKER',
 125: 'CANARY',
 126: 'CANVASBACK',
 127: 'CAPE GLOSSY STARLING',
 128: 'CAPE LONGCLAW',
 129: 'CAPE MAY WARBLER',
 130: 'CAPE ROCK THRUSH',
 131: 'CAPPED HERON',
 132: 'CAPUCHINBIRD',
 133: 'CARMINE BEE-EATER',
 134: 'CASPIAN TERN',
 135: 'CASSOWARY',
 136: 'CEDAR WAXWING',
 137: 'CERULEAN WARBLER',
 138: 'CHARA DE COLLAR',
 139: 'CHATTERING LORY',
 140: 'CHESTNET BELLIED EUPHONIA',
 141: 'CHESTNUT WINGED CUCKOO',
 142: 'CHINESE BAMBOO PARTRIDGE',
 143: 'CHINESE POND HERON',
 144: 'CHIPPING SPARROW',
 145: 'CHUCAO TAPACULO',
 146: 'CHUKAR PARTRIDGE',
 147: 'CINNAMON ATTILA',
 148: 'CINNAMON FLYCATCHER',
 149: 'CINNAMON TEAL',
 150: 'CLARKS GREBE',
 151: 'CLARKS NUTCRACKER',
 152: 'COCK OF THE  ROCK',
 153: 'COCKATOO',
 154: 'COLLARED ARACARI',
 155: 'COLLARED CRESCENTCHEST',
 156: 'COMMON FIRECREST',
 157: 'COMMON GRACKLE',
 158: 'COMMON HOUSE MARTIN',
 159: 'COMMON IORA',
 160: 'COMMON LOON',
 161: 'COMMON POORWILL',
 162: 'COMMON STARLING',
 163: 'COPPERSMITH BARBET',
 164: 'COPPERY TAILED COUCAL',
 165: 'CRAB PLOVER',
 166: 'CRANE HAWK',
 167: 'CREAM COLORED WOODPECKER',
 168: 'CRESTED AUKLET',
 169: 'CRESTED CARACARA',
 170: 'CRESTED COUA',
 171: 'CRESTED FIREBACK',
 172: 'CRESTED KINGFISHER',
 173: 'CRESTED NUTHATCH',
 174: 'CRESTED OROPENDOLA',
 175: 'CRESTED SERPENT EAGLE',
 176: 'CRESTED SHRIKETIT',
 177: 'CRESTED WOOD PARTRIDGE',
 178: 'CRIMSON CHAT',
 179: 'CRIMSON SUNBIRD',
 180: 'CROW',
 181: 'CUBAN TODY',
 182: 'CUBAN TROGON',
 183: 'CURL CRESTED ARACURI',
 184: 'D-ARNAUDS BARBET',
 185: 'DALMATIAN PELICAN',
 186: 'DARJEELING WOODPECKER',
 187: 'DARK EYED JUNCO',
 188: 'DAURIAN REDSTART',
 189: 'DEMOISELLE CRANE',
 190: 'DOUBLE BARRED FINCH',
 191: 'DOUBLE BRESTED CORMARANT',
 192: 'DOUBLE EYED FIG PARROT',
 193: 'DOWNY WOODPECKER',
 194: 'DUNLIN',
 195: 'DUSKY LORY',
 196: 'DUSKY ROBIN',
 197: 'EARED PITA',
 198: 'EASTERN BLUEBIRD',
 199: 'EASTERN BLUEBONNET',
 200: 'EASTERN GOLDEN WEAVER',
 201: 'EASTERN MEADOWLARK',
 202: 'EASTERN ROSELLA',
 203: 'EASTERN TOWEE',
 204: 'EASTERN WIP POOR WILL',
 205: 'EASTERN YELLOW ROBIN',
 206: 'ECUADORIAN HILLSTAR',
 207: 'EGYPTIAN GOOSE',
 208: 'ELEGANT TROGON',
 209: 'ELLIOTS  PHEASANT',
 210: 'EMERALD TANAGER',
 211: 'EMPEROR PENGUIN',
 212: 'EMU',
 213: 'ENGGANO MYNA',
 214: 'EURASIAN BULLFINCH',
 215: 'EURASIAN GOLDEN ORIOLE',
 216: 'EURASIAN MAGPIE',
 217: 'EUROPEAN GOLDFINCH',
 218: 'EUROPEAN TURTLE DOVE',
 219: 'EVENING GROSBEAK',
 220: 'FAIRY BLUEBIRD',
 221: 'FAIRY PENGUIN',
 222: 'FAIRY TERN',
 223: 'FAN TAILED WIDOW',
 224: 'FASCIATED WREN',
 225: 'FIERY MINIVET',
 226: 'FIORDLAND PENGUIN',
 227: 'FIRE TAILLED MYZORNIS',
 228: 'FLAME BOWERBIRD',
 229: 'FLAME TANAGER',
 230: 'FOREST WAGTAIL',
 231: 'FRIGATE',
 232: 'FRILL BACK PIGEON',
 233: 'GAMBELS QUAIL',
 234: 'GANG GANG COCKATOO',
 235: 'GILA WOODPECKER',
 236: 'GILDED FLICKER',
 237: 'GLOSSY IBIS',
 238: 'GO AWAY BIRD',
 239: 'GOLD WING WARBLER',
 240: 'GOLDEN BOWER BIRD',
 241: 'GOLDEN CHEEKED WARBLER',
 242: 'GOLDEN CHLOROPHONIA',
 243: 'GOLDEN EAGLE',
 244: 'GOLDEN PARAKEET',
 245: 'GOLDEN PHEASANT',
 246: 'GOLDEN PIPIT',
 247: 'GOULDIAN FINCH',
 248: 'GRANDALA',
 249: 'GRAY CATBIRD',
 250: 'GRAY KINGBIRD',
 251: 'GRAY PARTRIDGE',
 252: 'GREAT ARGUS',
 253: 'GREAT GRAY OWL',
 254: 'GREAT JACAMAR',
 255: 'GREAT KISKADEE',
 256: 'GREAT POTOO',
 257: 'GREAT TINAMOU',
 258: 'GREAT XENOPS',
 259: 'GREATER PEWEE',
 260: 'GREATER PRAIRIE CHICKEN',
 261: 'GREATOR SAGE GROUSE',
 262: 'GREEN BROADBILL',
 263: 'GREEN JAY',
 264: 'GREEN MAGPIE',
 265: 'GREEN WINGED DOVE',
 266: 'GREY CUCKOOSHRIKE',
 267: 'GREY HEADED CHACHALACA',
 268: 'GREY HEADED FISH EAGLE',
 269: 'GREY PLOVER',
 270: 'GROVED BILLED ANI',
 271: 'GUINEA TURACO',
 272: 'GUINEAFOWL',
 273: 'GURNEYS PITTA',
 274: 'GYRFALCON',
 275: 'HAMERKOP',
 276: 'HARLEQUIN DUCK',
 277: 'HARLEQUIN QUAIL',
 278: 'HARPY EAGLE',
 279: 'HAWAIIAN GOOSE',
 280: 'HAWFINCH',
 281: 'HELMET VANGA',
 282: 'HEPATIC TANAGER',
 283: 'HIMALAYAN BLUETAIL',
 284: 'HIMALAYAN MONAL',
 285: 'HOATZIN',
 286: 'HOODED MERGANSER',
 287: 'HOOPOES',
 288: 'HORNED GUAN',
 289: 'HORNED LARK',
 290: 'HORNED SUNGEM',
 291: 'HOUSE FINCH',
 292: 'HOUSE SPARROW',
 293: 'HYACINTH MACAW',
 294: 'IBERIAN MAGPIE',
 295: 'IBISBILL',
 296: 'IMPERIAL SHAQ',
 297: 'INCA TERN',
 298: 'INDIAN BUSTARD',
 299: 'INDIAN PITTA',
 300: 'INDIAN ROLLER',
 301: 'INDIAN VULTURE',
 302: 'INDIGO BUNTING',
 303: 'INDIGO FLYCATCHER',
 304: 'INLAND DOTTEREL',
 305: 'IVORY BILLED ARACARI',
 306: 'IVORY GULL',
 307: 'IWI',
 308: 'JABIRU',
 309: 'JACK SNIPE',
 310: 'JACOBIN PIGEON',
 311: 'JANDAYA PARAKEET',
 312: 'JAPANESE ROBIN',
 313: 'JAVA SPARROW',
 314: 'JOCOTOCO ANTPITTA',
 315: 'KAGU',
 316: 'KAKAPO',
 317: 'KILLDEAR',
 318: 'KING EIDER',
 319: 'KING VULTURE',
 320: 'KIWI',
 321: 'KNOB BILLED DUCK',
 322: 'KOOKABURRA',
 323: 'LARK BUNTING',
 324: 'LAUGHING GULL',
 325: 'LAZULI BUNTING',
 326: 'LESSER ADJUTANT',
 327: 'LILAC ROLLER',
 328: 'LIMPKIN',
 329: 'LITTLE AUK',
 330: 'LOGGERHEAD SHRIKE',
 331: 'LONG-EARED OWL',
 332: 'LOONEY BIRDS',
 333: 'LUCIFER HUMMINGBIRD',
 334: 'MAGPIE GOOSE',
 335: 'MALABAR HORNBILL',
 336: 'MALACHITE KINGFISHER',
 337: 'MALAGASY WHITE EYE',
 338: 'MALEO',
 339: 'MALLARD DUCK',
 340: 'MANDRIN DUCK',
 341: 'MANGROVE CUCKOO',
 342: 'MARABOU STORK',
 343: 'MASKED BOBWHITE',
 344: 'MASKED BOOBY',
 345: 'MASKED LAPWING',
 346: 'MCKAYS BUNTING',
 347: 'MERLIN',
 348: 'MIKADO  PHEASANT',
 349: 'MILITARY MACAW',
 350: 'MOURNING DOVE',
 351: 'MYNA',
 352: 'NICOBAR PIGEON',
 353: 'NOISY FRIARBIRD',
 354: 'NORTHERN BEARDLESS TYRANNULET',
 355: 'NORTHERN CARDINAL',
 356: 'NORTHERN FLICKER',
 357: 'NORTHERN FULMAR',
 358: 'NORTHERN GANNET',
 359: 'NORTHERN GOSHAWK',
 360: 'NORTHERN JACANA',
 361: 'NORTHERN MOCKINGBIRD',
 362: 'NORTHERN PARULA',
 363: 'NORTHERN RED BISHOP',
 364: 'NORTHERN SHOVELER',
 365: 'OCELLATED TURKEY',
 366: 'OILBIRD',
 367: 'OKINAWA RAIL',
 368: 'ORANGE BREASTED TROGON',
 369: 'ORANGE BRESTED BUNTING',
 370: 'ORIENTAL BAY OWL',
 371: 'ORNATE HAWK EAGLE',
 372: 'OSPREY',
 373: 'OSTRICH',
 374: 'OVENBIRD',
 375: 'OYSTER CATCHER',
 376: 'PAINTED BUNTING',
 377: 'PALILA',
 378: 'PALM NUT VULTURE',
 379: 'PARADISE TANAGER',
 380: 'PARAKETT  AUKLET',
 381: 'PARUS MAJOR',
 382: 'PATAGONIAN SIERRA FINCH',
 383: 'PEACOCK',
 384: 'PEREGRINE FALCON',
 385: 'PHAINOPEPLA',
 386: 'PHILIPPINE EAGLE',
 387: 'PINK ROBIN',
 388: 'PLUSH CRESTED JAY',
 389: 'POMARINE JAEGER',
 390: 'PUFFIN',
 391: 'PUNA TEAL',
 392: 'PURPLE FINCH',
 393: 'PURPLE GALLINULE',
 394: 'PURPLE MARTIN',
 395: 'PURPLE SWAMPHEN',
 396: 'PYGMY KINGFISHER',
 397: 'PYRRHULOXIA',
 398: 'QUETZAL',
 399: 'RAINBOW LORIKEET',
 400: 'RAZORBILL',
 401: 'RED BEARDED BEE EATER',
 402: 'RED BELLIED PITTA',
 403: 'RED BILLED TROPICBIRD',
 404: 'RED BROWED FINCH',
 405: 'RED CROSSBILL',
 406: 'RED FACED CORMORANT',
 407: 'RED FACED WARBLER',
 408: 'RED FODY',
 409: 'RED HEADED DUCK',
 410: 'RED HEADED WOODPECKER',
 411: 'RED KNOT',
 412: 'RED LEGGED HONEYCREEPER',
 413: 'RED NAPED TROGON',
 414: 'RED SHOULDERED HAWK',
 415: 'RED TAILED HAWK',
 416: 'RED TAILED THRUSH',
 417: 'RED WINGED BLACKBIRD',
 418: 'RED WISKERED BULBUL',
 419: 'REGENT BOWERBIRD',
 420: 'RING-NECKED PHEASANT',
 421: 'ROADRUNNER',
 422: 'ROCK DOVE',
 423: 'ROSE BREASTED COCKATOO',
 424: 'ROSE BREASTED GROSBEAK',
 425: 'ROSEATE SPOONBILL',
 426: 'ROSY FACED LOVEBIRD',
 427: 'ROUGH LEG BUZZARD',
 428: 'ROYAL FLYCATCHER',
 429: 'RUBY CROWNED KINGLET',
 430: 'RUBY THROATED HUMMINGBIRD',
 431: 'RUDDY SHELDUCK',
 432: 'RUDY KINGFISHER',
 433: 'RUFOUS KINGFISHER',
 434: 'RUFOUS TREPE',
 435: 'RUFUOS MOTMOT',
 436: 'SAMATRAN THRUSH',
 437: 'SAND MARTIN',
 438: 'SANDHILL CRANE',
 439: 'SATYR TRAGOPAN',
 440: 'SAYS PHOEBE',
 441: 'SCARLET CROWNED FRUIT DOVE',
 442: 'SCARLET FACED LIOCICHLA',
 443: 'SCARLET IBIS',
 444: 'SCARLET MACAW',
 445: 'SCARLET TANAGER',
 446: 'SHOEBILL',
 447: 'SHORT BILLED DOWITCHER',
 448: 'SMITHS LONGSPUR',
 449: 'SNOW GOOSE',
 450: 'SNOW PARTRIDGE',
 451: 'SNOWY EGRET',
 452: 'SNOWY OWL',
 453: 'SNOWY PLOVER',
 454: 'SNOWY SHEATHBILL',
 455: 'SORA',
 456: 'SPANGLED COTINGA',
 457: 'SPLENDID WREN',
 458: 'SPOON BILED SANDPIPER',
 459: 'SPOTTED CATBIRD',
 460: 'SPOTTED WHISTLING DUCK',
 461: 'SQUACCO HERON',
 462: 'SRI LANKA BLUE MAGPIE',
 463: 'STEAMER DUCK',
 464: 'STORK BILLED KINGFISHER',
 465: 'STRIATED CARACARA',
 466: 'STRIPED OWL',
 467: 'STRIPPED MANAKIN',
 468: 'STRIPPED SWALLOW',
 469: 'SUNBITTERN',
 470: 'SUPERB STARLING',
 471: 'SURF SCOTER',
 472: 'SWINHOES PHEASANT',
 473: 'TAILORBIRD',
 474: 'TAIWAN MAGPIE',
 475: 'TAKAHE',
 476: 'TASMANIAN HEN',
 477: 'TAWNY FROGMOUTH',
 478: 'TEAL DUCK',
 479: 'TIT MOUSE',
 480: 'TOUCHAN',
 481: 'TOWNSENDS WARBLER',
 482: 'TREE SWALLOW',
 483: 'TRICOLORED BLACKBIRD',
 484: 'TROPICAL KINGBIRD',
 485: 'TRUMPTER SWAN',
 486: 'TURKEY VULTURE',
 487: 'TURQUOISE MOTMOT',
 488: 'UMBRELLA BIRD',
 489: 'VARIED THRUSH',
 490: 'VEERY',
 491: 'VENEZUELIAN TROUPIAL',
 492: 'VERDIN',
 493: 'VERMILION FLYCATHER',
 494: 'VICTORIA CROWNED PIGEON',
 495: 'VIOLET BACKED STARLING',
 496: 'VIOLET CUCKOO',
 497: 'VIOLET GREEN SWALLOW',
 498: 'VIOLET TURACO',
 499: 'VISAYAN HORNBILL',
 500: 'VULTURINE GUINEAFOWL',
 501: 'WALL CREAPER',
 502: 'WATTLED CURASSOW',
 503: 'WATTLED LAPWING',
 504: 'WHIMBREL',
 505: 'WHITE BREASTED WATERHEN',
 506: 'WHITE BROWED CRAKE',
 507: 'WHITE CHEEKED TURACO',
 508: 'WHITE CRESTED HORNBILL',
 509: 'WHITE EARED HUMMINGBIRD',
 510: 'WHITE NECKED RAVEN',
 511: 'WHITE TAILED TROPIC',
 512: 'WHITE THROATED BEE EATER',
 513: 'WILD TURKEY',
 514: 'WILLOW PTARMIGAN',
 515: 'WILSONS BIRD OF PARADISE',
 516: 'WOOD DUCK',
 517: 'WOOD THRUSH',
 518: 'WOODLAND KINGFISHER',
 519: 'WRENTIT',
 520: 'YELLOW BELLIED FLOWERPECKER',
 521: 'YELLOW BREASTED CHAT',
 522: 'YELLOW CACIQUE',
 523: 'YELLOW HEADED BLACKBIRD',
 524: 'ZEBRA DOVE'
 }

# Create a pyttsx3 engine instance
engine = pyttsx3.init()

# Function to process the uploaded image
def processed_img(img_path): 
    try:
        # Load and preprocess the image
        img = load_img(img_path, target_size=(224, 224, 3)) 
        img_array = img_to_array(img) 
        img_array = np.expand_dims(img_array, 0) 
        # Make predictions 
        predictions = model.predict(img_array) 
        predicted_index = np.argmax(predictions[0])
        predicted_class = lab[predicted_index]
        
        # Calculate confidence percentage
        confidence = np.max(predictions[0])
        accuracy_percentage = confidence * 100 if confidence >= 0.5 else (1 - confidence) * 100

        # Get ornithological information
        ornithological_info = get_ornithological_info(predicted_class)
        
        return predicted_class, accuracy_percentage, ornithological_info
    
    except Exception as e:
        st.error(f"An error occurred: {str(e)}")
        return None, None, None

# Function to get ornithological information for a bird species
def get_ornithological_info(bird_name):
    ornithological_info = {
        "ABBOTTS BABBLER": {
            "Common name": "Abbott's Babbler",
            "Scientific name": "Malacocincla abbotti",
            "Species": "M. abbotti",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Order": "Passeriformes",
                "Family": "Timaliidae",
                "Genus": "Malacocincla"
            }
        },
        "ABBOTTS BOOBY": {
            "Common name": "Abbott's Booby",
            "Scientific name": "Papasula abbotti",
            "Species": "P. abbotti",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Order": "Suliformes",
                "Family": "Sulidae",
                "Genus": "Papasula"
            }
        },
        "ABYSSINIAN GROUND HORNBILL": {
            "Common name": "Abyssinian Ground Hornbill",
            "Scientific name": "Bucorvus abyssinicus",
            "Species": "B. abyssinicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Order": "Bucerotiformes",
                "Family": "Bucorvidae",
                "Genus": "Bucorvus"
            }
        },
        "AFRICAN CROWNED CRANE": {
            "Common name": "African Crowned Crane",
            "Scientific name": "Balearica pavonina",
            "Species": "B. pavonina",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Order": "Gruiformes",
                "Family": "Gruidae",
                "Genus": "Balearica"
            }
        },
        "AFRICAN EMERALD CUCKOO": {
            "Common name": "African Emerald Cuckoo",
            "Scientific name": "Chrysococcyx cupreus",
            "Species": "C. cupreus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Order": "Cuculiformes",
                "Family": "Cuculidae",
                "Genus": "Chrysococcyx"
            }
        },
        "AFRICAN FIREFINCH": {
            "Common name": "African Firefinch",
            "Scientific name": "Lagonosticta rubricata",
            "Species": "L. rubricata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Order": "Passeriformes",
                "Family": "Estrildidae",
                "Genus": "Lagonosticta"
            }
        },
        "AFRICAN OYSTER CATCHER": {
            "Common name": "African Oystercatcher",
            "Scientific name": "Haematopus moquini",
            "Species": "H. moquini",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Order": "Charadriiformes",
                "Family": "Haematopodidae",
                "Genus": "Haematopus"
            }
        },
        "AFRICAN PIED HORNBILL": {
            "Common name": "African Pied Hornbill",
            "Scientific name": "Tockus fasciatus",
            "Species": "T. fasciatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Order": "Bucerotiformes",
                "Family": "Bucerotidae",
                "Genus": "Tockus"
            }
        },
        "AFRICAN PYGMY GOOSE": {
            "Common name": "African Pygmy Goose",
            "Scientific name": "Nettapus auritus",
            "Species": "N. auritus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Order": "Anseriformes",
                "Family": "Anatidae",
                "Genus": "Nettapus"
            }
        },
        "ALBATROSS": {
            "Common name": "Albatross",
            "Scientific name": "Diomedea",
            "Species": "Various species within the genus Diomedea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Order": "Procellariiformes",
                "Family": "Diomedeidae",
                "Genus": "Diomedea"
            }
        },
        "ALBERTS TOWHEE": {
            "Common name": "Albert's Towhee",
            "Scientific name": "Melozone alberti",
            "Species": "M. alberti",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Order": "Passeriformes",
                "Family": "Passerellidae",
                "Genus": "Melozone"
            }
        },
        "ALEXANDRINE PARAKEET": {
            "Common name": "Alexandrine Parakeet",
            "Scientific name": "Psittacula eupatria",
            "Species": "P. eupatria",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Order": "Psittaciformes",
                "Family": "Psittaculidae",
                "Genus": "Psittacula"
            }
        },
        "ALPINE CHOUGH": {
            "Common name": "Alpine Chough",
            "Scientific name": "Pyrrhocorax graculus",
            "Species": "P. graculus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Pyrrhocorax"
            }
        },
        "ALTAMIRA YELLOWTHROAT": {
            "Common name": "Altamira Yellowthroat",
            "Scientific name": "Geothlypis flavovelata",
            "Species": "G. flavovelata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Geothlypis"
            }
        },
        "AMERICAN AVOCET": {
            "Common name": "American Avocet",
            "Scientific name": "Recurvirostra americana",
            "Species": "R. americana",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Recurvirostridae",
                "Genus": "Recurvirostra"
            }
        },
        "AMERICAN BITTERN": {
            "Common name": "American Bittern",
            "Scientific name": "Botaurus lentiginosus",
            "Species": "B. lentiginosus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ardeidae",
                "Genus": "Botaurus"
            }
        },
        "AMERICAN COOT": {
            "Common name": "American Coot",
            "Scientific name": "Fulica americana",
            "Species": "F. americana",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rallidae",
                "Genus": "Fulica"
            }
        },
        "AMERICAN DIPPER": {
            "Common name": "American Dipper",
            "Scientific name": "Cinclus mexicanus",
            "Species": "C. mexicanus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cinclidae",
                "Genus": "Cinclus"
            }
        },
        "AMERICAN FLAMINGO": {
            "Common name": "American Flamingo",
            "Scientific name": "Phoenicopterus ruber",
            "Species": "P. ruber",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phoenicopteridae",
                "Genus": "Phoenicopterus"
            }
        },
        "AMERICAN GOLDFINCH": {
            "Common name": "American Goldfinch",
            "Scientific name": "Spinus tristis",
            "Species": "S. tristis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Spinus"
            }
        },
        "AMERICAN KESTREL": {
            "Common name": "American Kestrel",
            "Scientific name": "Falco sparverius",
            "Species": "F. sparverius",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Falconidae",
                "Genus": "Falco"
            }
        },
        "AMERICAN PIPIT": {
            "Common name": "American Pipit",
            "Scientific name": "Anthus rubescens",
            "Species": "A. rubescens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Motacillidae",
                "Genus": "Anthus"
            }
        },
        "AMERICAN REDSTART": {
            "Common name": "American Redstart",
            "Scientific name": "Setophaga ruticilla",
            "Species": "S. ruticilla",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Setophaga"
            }
        },
        "AMERICAN ROBIN": {
            "Common name": "American Robin",
            "Scientific name": "Turdus migratorius",
            "Species": "T. migratorius",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Turdidae",
                "Genus": "Turdus"
            }
        },
        "AMERICAN WIGEON": {
            "Common name": "American Wigeon",
            "Scientific name": "Mareca americana",
            "Species": "M. americana",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Mareca"
            }
        },
        "AMETHYST WOODSTAR": {
            "Common name": "Amethyst Woodstar",
            "Scientific name": "Calliphlox amethystina",
            "Species": "C. amethystina",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Trochilidae",
                "Genus": "Calliphlox"
            }
        },
        "ANDEAN GOOSE": {
            "Common name": "Andean Goose",
            "Scientific name": "Chloephaga melanoptera",
            "Species": "C. melanoptera",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Chloephaga"
            }
        },
        "ANDEAN LAPWING": {
            "Common name": "Andean Lapwing",
            "Scientific name": "Vanellus resplendens",
            "Species": "V. resplendens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Charadriidae",
                "Genus": "Vanellus"
            }
        },
        "ANDEAN SISKIN": {
            "Common name": "Andean Siskin",
            "Scientific name": "Spinus spinescens",
            "Species": "S. spinescens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Spinus"
            }
        },
        "ANHINGA": {
            "Common name": "Anhinga",
            "Scientific name": "Anhinga anhinga",
            "Species": "A. anhinga",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anhingidae",
                "Genus": "Anhinga"
            }
        },
        "ANIANIAU": {
            "Common name": "Anianiau",
            "Scientific name": "Magumma parva",
            "Species": "M. parva",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Magumma"
            }
        },
        "ANNAS HUMMINGBIRD": {
            "Common name": "Anna's Hummingbird",
            "Scientific name": "Calypte anna",
            "Species": "C. anna",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Trochilidae",
                "Genus": "Calypte"
            }
        },
        "ANTBIRD": {
            "Common name": "Antbird",
            "Scientific name": "Thamnophilidae",
            "Species": "Various species within the family Thamnophilidae",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Thamnophilidae"
            }
        },
        "ANTILLEAN EUPHONIA": {
            "Common name": "Antillean Euphonia",
            "Scientific name": "Euphonia musica",
            "Species": "E. musica",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Euphonia"
            }
        },
        "APAPANE": {
            "Common name": "Apapane",
            "Scientific name": "Himatione sanguinea",
            "Species": "H. sanguinea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Himatione"
            }
        },
        "APOSTLEBIRD": {
            "Common name": "Apostlebird",
            "Scientific name": "Struthidea cinerea",
            "Species": "S. cinerea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corcoracidae",
                "Genus": "Struthidea"
            }
        },
        "ARARIPE MANAKIN": {
            "Common name": "Araripe Manakin",
            "Scientific name": "Antilophia bokermanni",
            "Species": "A. bokermanni",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Pipridae",
                "Genus": "Antilophia"
            }
        },
        "ASHY STORM PETREL": {
            "Common name": "Ashy Storm Petrel",
            "Scientific name": "Oceanodroma homochroa",
            "Species": "O. homochroa",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Hydrobatidae",
                "Genus": "Oceanodroma"
            }
        },
        "ASHY THRUSHBIRD": {
            "Common name": "Ashy Thrushbird",
            "Scientific name": "Saxicoloides fulicatus",
            "Species": "S. fulicatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Muscicapidae",
                "Genus": "Saxicoloides"
            }
        },
        "ASIAN CRESTED IBIS": {
            "Common name": "Asian Crested Ibis",
            "Scientific name": "Nipponia nippon",
            "Species": "N. nippon",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Threskiornithidae",
                "Genus": "Nipponia"
            }
        },
        "ASIAN DOLLARD BIRD": {
            "Common name": "Asian Dollard Bird",
            "Scientific name": "Crypsirina temia",
            "Species": "C. temia",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Crypsirina"
            }
        },
        "ASIAN GREEN BEE EATER": {
            "Common name": "Asian Green Bee Eater",
            "Scientific name": "Merops orientalis",
            "Species": "M. orientalis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Meropidae",
                "Genus": "Merops"
            }
        },
        "ASIAN OPENBILL STORK": {
            "Common name": "Asian Openbill Stork",
            "Scientific name": "Anastomus oscitans",
            "Species": "A. oscitans",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ciconiidae",
                "Genus": "Anastomus"
            }
        },
        "AUCKLAND SHAQ": {
            "Common name": "Auckland Shag",
            "Scientific name": "Leucocarbo colensoi",
            "Species": "L. colensoi",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phalacrocoracidae",
                "Genus": "Leucocarbo"
            }
        },
        "AUSTRAL CANASTERO": {
            "Common name": "Austral Canastero",
            "Scientific name": "Asthenes anthoides",
            "Species": "A. anthoides",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Furnariidae",
                "Genus": "Asthenes"
            }
        },
        "AUSTRALASIAN FIGBIRD": {
            "Common name": "Australasian Figbird",
            "Scientific name": "Sphecotheres vieilloti",
            "Species": "S. vieilloti",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Oriolidae",
                "Genus": "Sphecotheres"
            }
        },
        "AVADAVAT": {
            "Common name": "Avadavat",
            "Scientific name": "Amandava amandava",
            "Species": "A. amandava",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Estrildidae",
                "Genus": "Amandava"
            }
        },
        "AZARAS SPINETAIL": {
            "Common name": "Azara's Spinetail",
            "Scientific name": "Synallaxis azarae",
            "Species": "S. azarae",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Furnariidae",
                "Genus": "Synallaxis"
            }
        },
        "AZURE BREASTED PITTA": {
            "Common name": "Azure-breasted Pitta",
            "Scientific name": "Pitta steerii",
            "Species": "P. steerii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Pittidae",
                "Genus": "Pitta"
            }
        },
        "AZURE JAY": {
            "Common name": "Azure Jay",
            "Scientific name": "Cyanocorax caeruleus",
            "Species": "C. caeruleus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Cyanocorax"
            }
        },
        "AZURE TANAGER": {
            "Common name": "Azure Tanager",
            "Scientific name": "Thraupis episcopus",
            "Species": "T. episcopus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Thraupidae",
                "Genus": "Thraupis"
            }
        },
        "AZURE TIT": {
            "Common name": "Azure Tit",
            "Scientific name": "Cyanistes cyanus",
            "Species": "C. cyanus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Paridae",
                "Genus": "Cyanistes"
            }
        },
        "BAIKAL TEAL": {
            "Common name": "Baikal Teal",
            "Scientific name": "Sibirionetta formosa",
            "Species": "S. formosa",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Sibirionetta"
            }
        },
        "BALD EAGLE": {
            "Common name": "Bald Eagle",
            "Scientific name": "Haliaeetus leucocephalus",
            "Species": "H. leucocephalus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Haliaeetus"
            }
        },
        "BALD IBIS": {
            "Common name": "Bald Ibis",
            "Scientific name": "Geronticus calvus",
            "Species": "G. calvus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Threskiornithidae",
                "Genus": "Geronticus"
            }
        },
        "BALI STARLING": {
            "Common name": "Bali Starling",
            "Scientific name": "Leucopsar rothschildi",
            "Species": "L. rothschildi",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Sturnidae",
                "Genus": "Leucopsar"
            }
        },
        "BALTIMORE ORIOLE": {
            "Common name": "Baltimore Oriole",
            "Scientific name": "Icterus galbula",
            "Species": "I. galbula",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Icteridae",
                "Genus": "Icterus"
            }
        },
        "BANANAQUIT": {
            "Common name": "Bananaquit",
            "Scientific name": "Coereba flaveola",
            "Species": "C. flaveola",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Thraupidae",
                "Genus": "Coereba"
            }
        },
        "BAND TAILED GUAN": {
            "Common name": "Band-tailed Guan",
            "Scientific name": "Penelope argyrotis",
            "Species": "P. argyrotis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cracidae",
                "Genus": "Penelope"
            }
        },
        "BANDED BROADBILL": {
            "Common name": "Banded Broadbill",
            "Scientific name": "Eurylaimus javanicus",
            "Species": "E. javanicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Eurylaimidae",
                "Genus": "Eurylaimus"
            }
        },
        "BANDED PITA": {
            "Common name": "Banded Pita",
            "Scientific name": "Hydromoschus semimarmoratus",
            "Species": "H. semimarmoratus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Hirundinidae",
                "Genus": "Hydromoschus"
            }
        },
        "BANDED STILT": {
            "Common name": "Banded Stilt",
            "Scientific name": "Cladorhynchus leucocephalus",
            "Species": "C. leucocephalus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Recurvirostridae",
                "Genus": "Cladorhynchus"
            }
        },
        "BAR-TAILED GODWIT": {
            "Common name": "Bar-tailed Godwit",
            "Scientific name": "Limosa lapponica",
            "Species": "L. lapponica",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Scolopacidae",
                "Genus": "Limosa"
            }
        },
        "BARN OWL": {
            "Common name": "Barn Owl",
            "Scientific name": "Tyto alba",
            "Species": "T. alba",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tytonidae",
                "Genus": "Tyto"
            }
        },
        "BARN SWALLOW": {
            "Common name": "Barn Swallow",
            "Scientific name": "Hirundo rustica",
            "Species": "H. rustica",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Hirundinidae",
                "Genus": "Hirundo"
            }
        },
        "BARRED PUFFBIRD": {
            "Common name": "Barred Puffbird",
            "Scientific name": "Nystalus radiatus",
            "Species": "N. radiatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Bucconidae",
                "Genus": "Nystalus"
            }
        },
        "BARROWS GOLDENEYE": {
            "Common name": "Barrow's Goldeneye",
            "Scientific name": "Bucephala islandica",
            "Species": "B. islandica",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Bucephala"
            }
        },
        "BAY-BREASTED WARBLER": {
            "Common name": "Bay-breasted Warbler",
            "Scientific name": "Setophaga castanea",
            "Species": "S. castanea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Setophaga"
            }
        },
        "BEARDED BARBET": {
            "Common name": "Bearded Barbet",
            "Scientific name": "Lybius dubius",
            "Species": "L. dubius",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Lybiidae",
                "Genus": "Lybius"
            }
        },
        "BEARDED BELLBIRD": {
            "Common name": "Bearded Bellbird",
            "Scientific name": "Procnias averano",
            "Species": "P. averano",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cotingidae",
                "Genus": "Procnias"
            }
        },
        "BEARDED REEDLING": {
            "Common name": "Bearded Reedling",
            "Scientific name": "Panurus biarmicus",
            "Species": "P. biarmicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Panuridae",
                "Genus": "Panurus"
            }
        },
        "BELTED KINGFISHER": {
            "Common name": "Belted Kingfisher",
            "Scientific name": "Megaceryle alcyon",
            "Species": "M. alcyon",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcedinidae",
                "Genus": "Megaceryle"
            }
        },
        "BIRD OF PARADISE": {
            "Common name": "Bird of Paradise",
            "Scientific name": "Paradisaeidae",
            "Species": "Various species within the family Paradisaeidae",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Paradisaeidae"
            }
        },
        "BLACK AND YELLOW BROADBILL": {
            "Common name": "Black-and-yellow Broadbill",
            "Scientific name": "Eurylaimus ochromalus",
            "Species": "E. ochromalus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Eurylaimidae",
                "Genus": "Eurylaimus"
            }
        },
        "BLACK BAZA": {
            "Common name": "Black Baza",
            "Scientific name": "Aviceda leuphotes",
            "Species": "A. leuphotes",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Aviceda"
            }
        },
        "BLACK BREASTED PUFFBIRD": {
            "Common name": "Black-breasted Puffbird",
            "Scientific name": "Notharchus pectoralis",
            "Species": "N. pectoralis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Bucconidae",
                "Genus": "Notharchus"
            }
        },
        "BLACK COCKATOO": {
            "Common name": "Black Cockatoo",
            "Scientific name": "Calyptorhynchus sp.",
            "Species": "Various species within the genus Calyptorhynchus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cacatuidae",
                "Genus": "Calyptorhynchus"
            }
        },
        "BLACK FACED SPOONBILL": {
            "Common name": "Black-faced Spoonbill",
            "Scientific name": "Platalea minor",
            "Species": "P. minor",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Threskiornithidae",
                "Genus": "Platalea"
            }
        },
        "BLACK FRANCOLIN": {
            "Common name": "Black Francolin",
            "Scientific name": "Francolinus francolinus",
            "Species": "F. francolinus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Francolinus"
            }
        },
        "BLACK HEADED CAIQUE": {
            "Common name": "Black-headed Caique",
            "Scientific name": "Pionites melanocephalus",
            "Species": "P. melanocephalus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittacidae",
                "Genus": "Pionites"
            }
        },
        "BLACK NECKED STILT": {
            "Common name": "Black-necked Stilt",
            "Scientific name": "Himantopus mexicanus",
            "Species": "H. mexicanus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Recurvirostridae",
                "Genus": "Himantopus"
            }
        },
        "BLACK SKIMMER": {
            "Common name": "Black Skimmer",
            "Scientific name": "Rynchops niger",
            "Species": "R. niger",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rynchopidae",
                "Genus": "Rynchops"
            }
        },
        "BLACK SWAN": {
            "Common name": "Black Swan",
            "Scientific name": "Cygnus atratus",
            "Species": "C. atratus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Cygnus"
            }
        },
        "BLACK TAIL CRAKE": {
            "Common name": "Black-tailed Crake",
            "Scientific name": "Amaurolimnas concolor",
            "Species": "A. concolor",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rallidae",
                "Genus": "Amaurolimnas"
            }
        },
        "BLACK THROATED BUSHTIT": {
            "Common name": "Black-throated Bushtit",
            "Scientific name": "Aegithalos concinnus",
            "Species": "A. concinnus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Aegithalidae",
                "Genus": "Aegithalos"
            }
        },
        "BLACK THROATED HUET": {
            "Common name": "Black-throated Huet-huet",
            "Scientific name": "Pteroptochos tarnii",
            "Species": "P. tarnii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rhinocryptidae",
                "Genus": "Pteroptochos"
            }
        },
        "BLACK THROATED WARBLER": {
            "Common name": "Black-throated Warbler",
            "Scientific name": "Setophaga nigrescens",
            "Species": "S. nigrescens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Setophaga"
            }
        },
        "BLACK VENTED SHEARWATER": {
            "Common name": "Black-vented Shearwater",
            "Scientific name": "Puffinus opisthomelas",
            "Species": "P. opisthomelas",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Procellariidae",
                "Genus": "Puffinus"
            }
        },
        "BLACK VULTURE": {
            "Common name": "Black Vulture",
            "Scientific name": "Coragyps atratus",
            "Species": "C. atratus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cathartidae",
                "Genus": "Coragyps"
            }
        },
        "BLACK-CAPPED CHICKADEE": {
            "Common name": "Black-capped Chickadee",
            "Scientific name": "Poecile atricapillus",
            "Species": "P. atricapillus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Paridae",
                "Genus": "Poecile"
            }
        },
        "BLACK-NECKED GREBE": {
            "Common name": "Black-necked Grebe",
            "Scientific name": "Podiceps nigricollis",
            "Species": "P. nigricollis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Podicipedidae",
                "Genus": "Podiceps"
            }
        },
        "BLACK-THROATED SPARROW": {
            "Common name": "Black-throated Sparrow",
            "Scientific name": "Amphispiza bilineata",
            "Species": "A. bilineata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Passerellidae",
                "Genus": "Amphispiza"
            }
        },
        "BLACKBURNIAM WARBLER": {
            "Common name": "Blackburnian Warbler",
            "Scientific name": "Setophaga fusca",
            "Species": "S. fusca",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Setophaga"
            }
        },
        "BLONDE CRESTED WOODPECKER": {
            "Common name": "Blonde-crested Woodpecker",
            "Scientific name": "Celeus flavescens",
            "Species": "C. flavescens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Picidae",
                "Genus": "Celeus"
            }
        },
        "BLOOD PHEASANT": {
            "Common name": "Blood Pheasant",
            "Scientific name": "Ithaginis cruentus",
            "Species": "I. cruentus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Ithaginis"
            }
        },
        "BLUE COAU": {
            "Common name": "Blue Coua",
            "Scientific name": "Coua caerulea",
            "Species": "C. caerulea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cuculidae",
                "Genus": "Coua"
            }
        },
        "BLUE DACNIS": {
            "Common name": "Blue Dacnis",
            "Scientific name": "Dacnis cayana",
            "Species": "D. cayana",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Thraupidae",
                "Genus": "Dacnis"
            }
        },
        "BLUE GRAY GNATCATCHER": {
            "Common name": "Blue-gray Gnatcatcher",
            "Scientific name": "Polioptila caerulea",
            "Species": "P. caerulea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Polioptilidae",
                "Genus": "Polioptila"
            }
        },
        "BLUE GROSBEAK": {
            "Common name": "Blue Grosbeak",
            "Scientific name": "Passerina caerulea",
            "Species": "P. caerulea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cardinalidae",
                "Genus": "Passerina"
            }
        },
        "BLUE GROUSE": {
            "Common name": "Blue Grouse",
            "Scientific name": "Dendragapus obscurus",
            "Species": "D. obscurus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Dendragapus"
            }
        },
        "BLUE HERON": {
            "Common name": "Blue Heron",
            "Scientific name": "Ardea herodias",
            "Species": "A. herodias",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ardeidae",
                "Genus": "Ardea"
            }
        },
        "BLUE MALKOHA": {
            "Common name": "Blue Malkoha",
            "Scientific name": "Ceuthmochares aereus",
            "Species": "C. aereus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cuculidae",
                "Genus": "Ceuthmochares"
            }
        },
        "BLUE THROATED PIPING GUAN": {
            "Common name": "Blue-throated Piping Guan",
            "Scientific name": "Pipile cumanensis",
            "Species": "P. cumanensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cracidae",
                "Genus": "Pipile"
            }
        },
        "BLUE THROATED TOUCANET": {
            "Common name": "Blue-throated Toucanet",
            "Scientific name": "Aulacorhynchus caeruleogularis",
            "Species": "A. caeruleogularis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ramphastidae",
                "Genus": "Aulacorhynchus"
            }
        },
        "BOBOLINK": {
            "Common name": "Bobolink",
            "Scientific name": "Dolichonyx oryzivorus",
            "Species": "D. oryzivorus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Icteridae",
                "Genus": "Dolichonyx"
            }
        },
        "BORNEAN BRISTLEHEAD": {
            "Common name": "Bornean Bristlehead",
            "Scientific name": "Pityriasis gymnocephala",
            "Species": "P. gymnocephala",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Pityriaseidae",
                "Genus": "Pityriasis"
            }
        },
        "BORNEAN LEAFBIRD": {
            "Common name": "Bornean Leafbird",
            "Scientific name": "Chloropsis kinabaluensis",
            "Species": "C. kinabaluensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Chloropseidae",
                "Genus": "Chloropsis"
            }
        },
        "BORNEAN PHEASANT": {
            "Common name": "Bornean Pheasant",
            "Scientific name": "Rheinardia ocellata",
            "Species": "R. ocellata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Rheinardia"
            }
        },
        "BRANDT CORMARANT": {
            "Common name": "Brandt's Cormorant",
            "Scientific name": "Phalacrocorax penicillatus",
            "Species": "P. penicillatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phalacrocoracidae",
                "Genus": "Phalacrocorax"
            }
        },
        "BREWERS BLACKBIRD": {
            "Common name": "Brewer's Blackbird",
            "Scientific name": "Euphagus cyanocephalus",
            "Species": "E. cyanocephalus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Icteridae",
                "Genus": "Euphagus"
            }
        },
        "BROWN CREPPER": {
            "Common name": "Brown Creeper",
            "Scientific name": "Certhia americana",
            "Species": "C. americana",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Certhiidae",
                "Genus": "Certhia"
            }
        },
        "BROWN HEADED COWBIRD": {
            "Common name": "Brown-headed Cowbird",
            "Scientific name": "Molothrus ater",
            "Species": "M. ater",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Icteridae",
                "Genus": "Molothrus"
            }
        },
        "BROWN NOODY": {
            "Common name": "Brown Noddy",
            "Scientific name": "Anous stolidus",
            "Species": "A. stolidus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Laridae",
                "Genus": "Anous"
            }
        },
        "BROWN THRASHER": {
            "Common name": "Brown Thrasher",
            "Scientific name": "Toxostoma rufum",
            "Species": "T. rufum",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Mimidae",
                "Genus": "Toxostoma"
            }
        },
        "BUFFLEHEAD": {
            "Common name": "Bufflehead",
            "Scientific name": "Bucephala albeola",
            "Species": "B. albeola",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Bucephala"
            }
        },
        "BULWERS PHEASANT": {
            "Common name": "Bulwer's Pheasant",
            "Scientific name": "Lophura bulweri",
            "Species": "L. bulweri",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Lophura"
            }
        },
        "BURCHELLS COURSER": {
            "Common name": "Burchell's Courser",
            "Scientific name": "Cursorius rufus",
            "Species": "C. rufus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Glareolidae",
                "Genus": "Cursorius"
            }
        },
        "BUSH TURKEY": {
            "Common name": "Bush Turkey",
            "Scientific name": "Alectura lathami",
            "Species": "A. lathami",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Megapodiidae",
                "Genus": "Alectura"
            }
        },
        "CAATINGA CACHOLOTE": {
            "Common name": "Caatinga Cacholote",
            "Scientific name": "Pseudoseisura cristata",
            "Species": "P. cristata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Furnariidae",
                "Genus": "Pseudoseisura"
            }
        },
        "CABOTS TRAGOPAN": {
            "Common name": "Cabot's Tragopan",
            "Scientific name": "Tragopan caboti",
            "Species": "T. caboti",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Tragopan"
            }
        },
        "CACTUS WREN": {
            "Common name": "Cactus Wren",
            "Scientific name": "Campylorhynchus brunneicapillus",
            "Species": "C. brunneicapillus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Troglodytidae",
                "Genus": "Campylorhynchus"
            }
        },
        "CALIFORNIA CONDOR": {
            "Common name": "California Condor",
            "Scientific name": "Gymnogyps californianus",
            "Species": "G. californianus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cathartidae",
                "Genus": "Gymnogyps"
            }
        },
        "CALIFORNIA GULL": {
            "Common name": "California Gull",
            "Scientific name": "Larus californicus",
            "Species": "L. californicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Laridae",
                "Genus": "Larus"
            }
        },
        "CALIFORNIA QUAIL": {
            "Common name": "California Quail",
            "Scientific name": "Callipepla californica",
            "Species": "C. californica",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Odontophoridae",
                "Genus": "Callipepla"
            }
        },
        "CAMPO FLICKER": {
            "Common name": "Campo Flicker",
            "Scientific name": "Colaptes campestris",
            "Species": "C. campestris",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Picidae",
                "Genus": "Colaptes"
            }
        },
        "CANARY": {
            "Common name": "Canary",
            "Scientific name": "Serinus canaria",
            "Species": "S. canaria",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Serinus"
            }
        },
        "CANVASBACK": {
            "Common name": "Canvasback",
            "Scientific name": "Aythya valisineria",
            "Species": "A. valisineria",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Aythya"
            }
        },
        "CAPE GLOSSY STARLING": {
            "Common name": "Cape Glossy Starling",
            "Scientific name": "Lamprotornis nitens",
            "Species": "L. nitens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Sturnidae",
                "Genus": "Lamprotornis"
            }
        },
        "CAPE LONGCLAW": {
            "Common name": "Cape Longclaw",
            "Scientific name": "Macronyx capensis",
            "Species": "M. capensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Motacillidae",
                "Genus": "Macronyx"
            }
        },
        "CAPE MAY WARBLER": {
            "Common name": "Cape May Warbler",
            "Scientific name": "Setophaga tigrina",
            "Species": "S. tigrina",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Setophaga"
            }
        },
        "CAPE ROCK THRUSH": {
            "Common name": "Cape Rock Thrush",
            "Scientific name": "Monticola rupestris",
            "Species": "M. rupestris",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Muscicapidae",
                "Genus": "Monticola"
            }
        },
        "CAPPED HERON": {
            "Common name": "Capped Heron",
            "Scientific name": "Pilherodius pileatus",
            "Species": "P. pileatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ardeidae",
                "Genus": "Pilherodius"
            }
        },
        "CAPUCHINBIRD": {
            "Common name": "Capuchinbird",
            "Scientific name": "Perissocephalus tricolor",
            "Species": "P. tricolor",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cotingidae",
                "Genus": "Perissocephalus"
            }
        },
        "CARMINE BEE-EATER": {
            "Common name": "Carmine Bee-eater",
            "Scientific name": "Merops nubicoides",
            "Species": "M. nubicoides",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Meropidae",
                "Genus": "Merops"
            }
        },
        "CASPIAN TERN": {
            "Common name": "Caspian Tern",
            "Scientific name": "Hydroprogne caspia",
            "Species": "H. caspia",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Laridae",
                "Genus": "Hydroprogne"
            }
        },
        "CASSOWARY": {
            "Common name": "Cassowary",
            "Scientific name": "Casuarius",
            "Species": "Various species within the genus Casuarius",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Casuariidae",
                "Genus": "Casuarius"
            }
        },
        "CEDAR WAXWING": {
            "Common name": "Cedar Waxwing",
            "Scientific name": "Bombycilla cedrorum",
            "Species": "B. cedrorum",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Bombycillidae",
                "Genus": "Bombycilla"
            }
        },
        "CERULEAN WARBLER": {
            "Common name": "Cerulean Warbler",
            "Scientific name": "Setophaga cerulea",
            "Species": "S. cerulea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Setophaga"
            }
        },
        "CHARA DE COLLAR": {
            "Common name": "Chara de Collar",
            "Scientific name": "Starnoenas cyanocephala",
            "Species": "S. cyanocephala",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Columbidae",
                "Genus": "Starnoenas"
            }
        },
        "CHATTERING LORY": {
            "Common name": "Chattering Lory",
            "Scientific name": "Lorius garrulus",
            "Species": "L. garrulus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittaculidae",
                "Genus": "Lorius"
            }
        },
        "CHESTNET BELLIED EUPHONIA": {
            "Common name": "Chestnut-bellied Euphonia",
            "Scientific name": "Euphonia pectoralis",
            "Species": "E. pectoralis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Euphonia"
            }
        },
        "CHESTNUT WINGED CUCKOO": {
            "Common name": "Chestnut-winged Cuckoo",
            "Scientific name": "Clamator coromandus",
            "Species": "C. coromandus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cuculidae",
                "Genus": "Clamator"
            }
        },
        "CHINESE BAMBOO PARTRIDGE": {
            "Common name": "Chinese Bamboo Partridge",
            "Scientific name": "Bambusicola thoracicus",
            "Species": "B. thoracicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Bambusicola"
            }
        },
        "CHINESE POND HERON": {
            "Common name": "Chinese Pond Heron",
            "Scientific name": "Ardeola bacchus",
            "Species": "A. bacchus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ardeidae",
                "Genus": "Ardeola"
            }
        },
        "CHIPPING SPARROW": {
            "Common name": "Chipping Sparrow",
            "Scientific name": "Spizella passerina",
            "Species": "S. passerina",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Passerellidae",
                "Genus": "Spizella"
            }
        },
        "CHUCAO TAPACULO": {
            "Common name": "Chucao Tapaculo",
            "Scientific name": "Scelorchilus rubecula",
            "Species": "S. rubecula",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rhinocryptidae",
                "Genus": "Scelorchilus"
            }
        },
        "CHUKAR PARTRIDGE": {
            "Common name": "Chukar Partridge",
            "Scientific name": "Alectoris chukar",
            "Species": "A. chukar",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Alectoris"
            }
        },
        "CINNAMON ATTILA": {
            "Common name": "Cinnamon Attila",
            "Scientific name": "Attila cinnamomeus",
            "Species": "A. cinnamomeus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tyrannidae",
                "Genus": "Attila"
            }
        },
        "CINNAMON FLYCATCHER": {
            "Common name": "Cinnamon Flycatcher",
            "Scientific name": "Pyrrhomyias cinnamomeus",
            "Species": "P. cinnamomeus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tyrannidae",
                "Genus": "Pyrrhomyias"
            }
        },
        "CINNAMON TEAL": {
            "Common name": "Cinnamon Teal",
            "Scientific name": "Spatula cyanoptera",
            "Species": "S. cyanoptera",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Spatula"
            }
        },
        "CLARKS GREBE": {
            "Common name": "Clark's Grebe",
            "Scientific name": "Aechmophorus clarkii",
            "Species": "A. clarkii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Podicipedidae",
                "Genus": "Aechmophorus"
            }
        },
        "CLARKS NUTCRACKER": {
            "Common name": "Clark's Nutcracker",
            "Scientific name": "Nucifraga columbiana",
            "Species": "N. columbiana",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Nucifraga"
            }
        },
        "COCK OF THE ROCK": {
            "Common name": "Cock-of-the-rock",
            "Scientific name": "Rupicola",
            "Species": "Various species within the genus Rupicola",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cotingidae",
                "Genus": "Rupicola"
            }
        },
        "COCKATOO": {
            "Common name": "Cockatoo",
            "Scientific name": "Cacatuidae",
            "Species": "Various species within the family Cacatuidae",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cacatuidae",
                "Genus": "Varies"
            }
        },
        "COLLARED ARACARI": {
            "Common name": "Collared Aracari",
            "Scientific name": "Pteroglossus torquatus",
            "Species": "P. torquatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ramphastidae",
                "Genus": "Pteroglossus"
            }
        },
        "COLLARED CRESCENTCHEST": {
            "Common name": "Collared Crescentchest",
            "Scientific name": "Melanopareia torquata",
            "Species": "M. torquata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Melanopareiidae",
                "Genus": "Melanopareia"
            }
        },
        "COMMON FIRECREST": {
            "Common name": "Common Firecrest",
            "Scientific name": "Regulus ignicapilla",
            "Species": "R. ignicapilla",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Regulidae",
                "Genus": "Regulus"
            }
        },
        "COMMON GRACKLE": {
            "Common name": "Common Grackle",
            "Scientific name": "Quiscalus quiscula",
            "Species": "Q. quiscula",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Icteridae",
                "Genus": "Quiscalus"
            }
        },
        "COMMON HOUSE MARTIN": {
            "Common name": "Common House Martin",
            "Scientific name": "Delichon urbicum",
            "Species": "D. urbicum",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Hirundinidae",
                "Genus": "Delichon"
            }
        },
        "COMMON IORA": {
            "Common name": "Common Iora",
            "Scientific name": "Aegithina tiphia",
            "Species": "A. tiphia",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Aegithinidae",
                "Genus": "Aegithina"
            }
        },
        "COMMON LOON": {
            "Common name": "Common Loon",
            "Scientific name": "Gavia immer",
            "Species": "G. immer",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Gaviidae",
                "Genus": "Gavia"
            }
        },
        "COMMON POORWILL": {
            "Common name": "Common Poorwill",
            "Scientific name": "Phalaenoptilus nuttallii",
            "Species": "P. nuttallii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Caprimulgidae",
                "Genus": "Phalaenoptilus"
            }
        },
        "COMMON STARLING": {
            "Common name": "Common Starling",
            "Scientific name": "Sturnus vulgaris",
            "Species": "S. vulgaris",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Sturnidae",
                "Genus": "Sturnus"
            }
        },
        "COPPERSMITH BARBET": {
            "Common name": "Coppersmith Barbet",
            "Scientific name": "Psilopogon haemacephalus",
            "Species": "P. haemacephalus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Megalaimidae",
                "Genus": "Psilopogon"
            }
        },
        "COPPERY TAILED COUCAL": {
            "Common name": "Coppery-tailed Coucal",
            "Scientific name": "Centropus cupreicaudus",
            "Species": "C. cupreicaudus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cuculidae",
                "Genus": "Centropus"
            }
        },
        "CRAB PLOVER": {
            "Common name": "Crab Plover",
            "Scientific name": "Dromas ardeola",
            "Species": "D. ardeola",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Dromadidae",
                "Genus": "Dromas"
            }
        },
        "CRANE HAWK": {
            "Common name": "Crane Hawk",
            "Scientific name": "Geranospiza caerulescens",
            "Species": "G. caerulescens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Geranospiza"
            }
        },
        "CREAM COLORED WOODPECKER": {
            "Common name": "Cream-colored Woodpecker",
            "Scientific name": "Celeus flavus",
            "Species": "C. flavus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Picidae",
                "Genus": "Celeus"
            }
        },
        "CRESTED AUKLET": {
            "Common name": "Crested Auklet",
            "Scientific name": "Aethia cristatella",
            "Species": "A. cristatella",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcidae",
                "Genus": "Aethia"
            }
        },
        "CRESTED CARACARA": {
            "Common name": "Crested Caracara",
            "Scientific name": "Caracara cheriway",
            "Species": "C. cheriway",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Falconidae",
                "Genus": "Caracara"
            }
        },
        "CRESTED COUA": {
            "Common name": "Crested Coua",
            "Scientific name": "Coua cristata",
            "Species": "C. cristata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cuculidae",
                "Genus": "Coua"
            }
        },
        "CRESTED FIREBACK": {
            "Common name": "Crested Fireback",
            "Scientific name": "Lophura ignita",
            "Species": "L. ignita",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Lophura"
            }
        },
        "CRESTED KINGFISHER": {
            "Common name": "Crested Kingfisher",
            "Scientific name": "Megaceryle lugubris",
            "Species": "M. lugubris",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcedinidae",
                "Genus": "Megaceryle"
            }
        },
        "CRESTED NUTHATCH": {
            "Common name": "Crested Nuthatch",
            "Scientific name": "Sitta frontalis",
            "Species": "S. frontalis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Sittidae",
                "Genus": "Sitta"
            }
        },
        "CRESTED OROPENDOLA": {
            "Common name": "Crested Oropendola",
            "Scientific name": "Psarocolius decumanus",
            "Species": "P. decumanus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Icteridae",
                "Genus": "Psarocolius"
            }
        },
        "CRESTED SERPENT EAGLE": {
            "Common name": "Crested Serpent Eagle",
            "Scientific name": "Spilornis cheela",
            "Species": "S. cheela",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Spilornis"
            }
        },
        "CRESTED SHRIKETIT": {
            "Common name": "Crested Shriketit",
            "Scientific name": "Falcunculus frontatus",
            "Species": "F. frontatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Pachycephalidae",
                "Genus": "Falcunculus"
            }
        },
        "CRESTED WOOD PARTRIDGE": {
            "Common name": "Crested Wood Partridge",
            "Scientific name": "Rollulus rouloul",
            "Species": "R. rouloul",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Rollulus"
            }
        },
        "CRIMSON CHAT": {
            "Common name": "Crimson Chat",
            "Scientific name": "Epthianura tricolor",
            "Species": "E. tricolor",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Meliphagidae",
                "Genus": "Epthianura"
            }
        },
        "CRIMSON SUNBIRD": {
            "Common name": "Crimson Sunbird",
            "Scientific name": "Aethopyga siparaja",
            "Species": "A. siparaja",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Nectariniidae",
                "Genus": "Aethopyga"
            }
        },
        "CROW": {
            "Common name": "Crow",
            "Scientific name": "Corvus",
            "Species": "Multiple species within the genus Corvus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Corvus"
            }
        },
        "CUBAN TODY": {
            "Common name": "Cuban Tody",
            "Scientific name": "Todus multicolor",
            "Species": "T. multicolor",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Todidae",
                "Genus": "Todus"
            }
        },
        "CUBAN TROGON": {
            "Common name": "Cuban Trogon",
            "Scientific name": "Priotelus temnurus",
            "Species": "P. temnurus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Trogonidae",
                "Genus": "Priotelus"
            }
        },
        "CURL CRESTED ARACURI": {
            "Common name": "Curl-crested Aracari",
            "Scientific name": "Pteroglossus beauharnaesii",
            "Species": "P. beauharnaesii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ramphastidae",
                "Genus": "Pteroglossus"
            }
        },
        "D-ARNAUDS BARBET": {
            "Common name": "D'Arnaud's Barbet",
            "Scientific name": "Trachyphonus darnaudii",
            "Species": "T. darnaudii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Lybiidae",
                "Genus": "Trachyphonus"
            }
        },
        "DALMATIAN PELICAN": {
            "Common name": "Dalmatian Pelican",
            "Scientific name": "Pelecanus crispus",
            "Species": "P. crispus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Pelecanidae",
                "Genus": "Pelecanus"
            }
        },
        "DARJEELING WOODPECKER": {
            "Common name": "Darjeeling Woodpecker",
            "Scientific name": "Dendrocopos darjellensis",
            "Species": "D. darjellensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Picidae",
                "Genus": "Dendrocopos"
            }
        },
        "DARK EYED JUNCO": {
            "Common name": "Dark-eyed Junco",
            "Scientific name": "Junco hyemalis",
            "Species": "J. hyemalis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Passerellidae",
                "Genus": "Junco"
            }
        },
        "DAURIAN REDSTART": {
            "Common name": "Daurian Redstart",
            "Scientific name": "Phoenicurus auroreus",
            "Species": "P. auroreus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Muscicapidae",
                "Genus": "Phoenicurus"
            }
        },
        "DEMOISELLE CRANE": {
            "Common name": "Demoiselle Crane",
            "Scientific name": "Grus virgo",
            "Species": "G. virgo",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Gruidae",
                "Genus": "Grus"
            }
        },
        "DOUBLE BARRED FINCH": {
            "Common name": "Double-barred Finch",
            "Scientific name": "Taeniopygia bichenovii",
            "Species": "T. bichenovii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Estrildidae",
                "Genus": "Taeniopygia"
            }
        },
        "DOUBLE BRESTED CORMARANT": {
            "Common name": "Double-crested Cormorant",
            "Scientific name": "Nannopterum auritus",
            "Species": "N. auritus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phalacrocoracidae",
                "Genus": "Nannopterum"
            }
        },
        "DOUBLE EYED FIG PARROT": {
            "Common name": "Double-eyed Fig Parrot",
            "Scientific name": "Cyclopsitta diophthalma",
            "Species": "C. diophthalma",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittaculidae",
                "Genus": "Cyclopsitta"
            }
        },
        "DOWNY WOODPECKER": {
            "Common name": "Downy Woodpecker",
            "Scientific name": "Dryobates pubescens",
            "Species": "D. pubescens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Picidae",
                "Genus": "Dryobates"
            }
        },
        "DUNLIN": {
            "Common name": "Dunlin",
            "Scientific name": "Calidris alpina",
            "Species": "C. alpina",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Scolopacidae",
                "Genus": "Calidris"
            }
        },
        "DUSKY LORY": {
            "Common name": "Dusky Lory",
            "Scientific name": "Pseudeos fuscata",
            "Species": "P. fuscata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittaculidae",
                "Genus": "Pseudeos"
            }
        },
        "DUSKY ROBIN": {
            "Common name": "Dusky Robin",
            "Scientific name": "Melanodryas vittata",
            "Species": "M. vittata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Petroicidae",
                "Genus": "Melanodryas"
            }
        },
        "EARED PITA": {
            "Common name": "Eared Pitta",
            "Scientific name": "Hydrornis phayrei",
            "Species": "H. phayrei",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Pittidae",
                "Genus": "Hydrornis"
            }
        },
        "EASTERN BLUEBIRD": {
            "Common name": "Eastern Bluebird",
            "Scientific name": "Sialia sialis",
            "Species": "S. sialis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Turdidae",
                "Genus": "Sialia"
            }
        },
        "EASTERN BLUEBONNET": {
            "Common name": "Eastern Bluebonnet",
            "Scientific name": "Northiella haematogaster",
            "Species": "N. haematogaster",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittacidae",
                "Genus": "Northiella"
            }
        },
        "EASTERN GOLDEN WEAVER": {
            "Common name": "Eastern Golden Weaver",
            "Scientific name": "Ploceus subaureus",
            "Species": "P. subaureus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ploceidae",
                "Genus": "Ploceus"
            }
        },
        "EASTERN MEADOWLARK": {
            "Common name": "Eastern Meadowlark",
            "Scientific name": "Sturnella magna",
            "Species": "S. magna",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Icteridae",
                "Genus": "Sturnella"
            }
        },
        "EASTERN ROSELLA": {
            "Common name": "Eastern Rosella",
            "Scientific name": "Platycercus eximius",
            "Species": "P. eximius",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittaculidae",
                "Genus": "Platycercus"
            }
        },
        "EASTERN TOWEE": {
            "Common name": "Eastern Towee",
            "Scientific name": "Pipilo erythrophthalmus",
            "Species": "P. erythrophthalmus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Passerellidae",
                "Genus": "Pipilo"
            }
        },
        "EASTERN WIP POOR WILL": {
            "Common name": "Eastern Whip-poor-will",
            "Scientific name": "Antrostomus vociferus",
            "Species": "A. vociferus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Caprimulgidae",
                "Genus": "Antrostomus"
            }
        },
        "EASTERN YELLOW ROBIN": {
            "Common name": "Eastern Yellow Robin",
            "Scientific name": "Eopsaltria australis",
            "Species": "E. australis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Petroicidae",
                "Genus": "Eopsaltria"
            }
        },
        "ECUADORIAN HILLSTAR": {
            "Common name": "Ecuadorian Hillstar",
            "Scientific name": "Oreotrochilus chimborazo",
            "Species": "O. chimborazo",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Trochilidae",
                "Genus": "Oreotrochilus"
            }
        },
        "EGYPTIAN GOOSE": {
            "Common name": "Egyptian Goose",
            "Scientific name": "Alopochen aegyptiaca",
            "Species": "A. aegyptiaca",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Alopochen"
            }
        },
        "ELEGANT TROGON": {
            "Common name": "Elegant Trogon",
            "Scientific name": "Trogon elegans",
            "Species": "T. elegans",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Trogonidae",
                "Genus": "Trogon"
            }
        },
        "ELLIOTS PHEASANT": {
            "Common name": "Elliot's Pheasant",
            "Scientific name": "Syrmaticus ellioti",
            "Species": "S. ellioti",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Syrmaticus"
            }
        },
        "EMERALD TANAGER": {
            "Common name": "Emerald Tanager",
            "Scientific name": "Tangara florida",
            "Species": "T. florida",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Thraupidae",
                "Genus": "Tangara"
            }
        },
        "EMPEROR PENGUIN": {
            "Common name": "Emperor Penguin",
            "Scientific name": "Aptenodytes forsteri",
            "Species": "A. forsteri",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Spheniscidae",
                "Genus": "Aptenodytes"
            }
        },
        "EMU": {
            "Common name": "Emu",
            "Scientific name": "Dromaius novaehollandiae",
            "Species": "D. novaehollandiae",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Casuariidae",
                "Genus": "Dromaius"
            }
        },
        "ENGGANO MYNA": {
            "Common name": "Enggano Myna",
            "Scientific name": "Gracula enganensis",
            "Species": "G. enganensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Sturnidae",
                "Genus": "Gracula"
            }
        },
        "EURASIAN BULLFINCH": {
            "Common name": "Eurasian Bullfinch",
            "Scientific name": "Pyrrhula pyrrhula",
            "Species": "P. pyrrhula",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Pyrrhula"
            }
        },
         "EURASIAN GOLDEN ORIOLE": {
            "Common name": "Eurasian Golden Oriole",
            "Scientific name": "Oriolus oriolus",
            "Species": "O. oriolus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Oriolidae",
                "Genus": "Oriolus"
            }
        },
        "EURASIAN MAGPIE": {
            "Common name": "Eurasian Magpie",
            "Scientific name": "Pica pica",
            "Species": "P. pica",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Pica"
            }
        },
        "EUROPEAN GOLDFINCH": {
            "Common name": "European Goldfinch",
            "Scientific name": "Carduelis carduelis",
            "Species": "C. carduelis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Carduelis"
            }
        },
        "EUROPEAN TURTLE DOVE": {
            "Common name": "European Turtle Dove",
            "Scientific name": "Streptopelia turtur",
            "Species": "S. turtur",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Columbidae",
                "Genus": "Streptopelia"
            }
        },
        "EVENING GROSBEAK": {
            "Common name": "Evening Grosbeak",
            "Scientific name": "Coccothraustes vespertinus",
            "Species": "C. vespertinus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Coccothraustes"
            }
        },
        "FAIRY BLUEBIRD": {
            "Common name": "Fairy Bluebird",
            "Scientific name": "Irena puella",
            "Species": "I. puella",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Irenidae",
                "Genus": "Irena"
            }
        },
        "FAIRY PENGUIN": {
            "Common name": "Fairy Penguin",
            "Scientific name": "Eudyptula minor",
            "Species": "E. minor",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Spheniscidae",
                "Genus": "Eudyptula"
            }
        },
        "FAIRY TERN": {
            "Common name": "Fairy Tern",
            "Scientific name": "Sternula nereis",
            "Species": "S. nereis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Laridae",
                "Genus": "Sternula"
            }
        },
        "FAN TAILED WIDOW": {
            "Common name": "Fan-tailed Widowbird",
            "Scientific name": "Euplectes axillaris",
            "Species": "E. axillaris",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ploceidae",
                "Genus": "Euplectes"
            }
        },
        "FASCIATED WREN": {
            "Common name": "Fasciated Wren",
            "Scientific name": "Campylorhynchus fasciatus",
            "Species": "C. fasciatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Troglodytidae",
                "Genus": "Campylorhynchus"
            }
        },
        "FIERY MINIVET": {
            "Common name": "Fiery Minivet",
            "Scientific name": "Pericrocotus igneus",
            "Species": "P. igneus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Campephagidae",
                "Genus": "Pericrocotus"
            }
        },
        "FIORDLAND PENGUIN": {
            "Common name": "Fiordland Penguin",
            "Scientific name": "Eudyptes pachyrhynchus",
            "Species": "E. pachyrhynchus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Spheniscidae",
                "Genus": "Eudyptes"
            }
        },
        "FIRE TAILLED MYZORNIS": {
            "Common name": "Fire-tailed Myzornis",
            "Scientific name": "Myzornis pyrrhoura",
            "Species": "M. pyrrhoura",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Leiothrichidae",
                "Genus": "Myzornis"
            }
        },
        "FLAME BOWERBIRD": {
            "Common name": "Flame Bowerbird",
            "Scientific name": "Sericulus aureus",
            "Species": "S. aureus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ptilonorhynchidae",
                "Genus": "Sericulus"
            }
        },
        "FLAME TANAGER": {
            "Common name": "Flame Tanager",
            "Scientific name": "Piranga bidentata",
            "Species": "P. bidentata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cardinalidae",
                "Genus": "Piranga"
            }
        },
        "FOREST WAGTAIL": {
            "Common name": "Forest Wagtail",
            "Scientific name": "Dendronanthus indicus",
            "Species": "D. indicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Motacillidae",
                "Genus": "Dendronanthus"
            }
        },
        "FRIGATE": {
            "Common name": "Frigatebird",
            "Scientific name": "Fregata",
            "Species": "Various species within the genus Fregata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fregatidae",
                "Genus": "Fregata"
            }
        },
        "FRILL BACK PIGEON": {
            "Common name": "Frillback Pigeon",
            "Scientific name": "Columba livia domestica",
            "Species": "C. livia domestica",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Columbidae",
                "Genus": "Columba"
            }
        },
        "GAMBELS QUAIL": {
            "Common name": "Gambel's Quail",
            "Scientific name": "Callipepla gambelii",
            "Species": "C. gambelii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Odontophoridae",
                "Genus": "Callipepla"
            }
        },
        "GANG GANG COCKATOO": {
            "Common name": "Gang-gang Cockatoo",
            "Scientific name": "Callocephalon fimbriatum",
            "Species": "C. fimbriatum",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cacatuidae",
                "Genus": "Callocephalon"
            }
        },
        "GILA WOODPECKER": {
            "Common name": "Gila Woodpecker",
            "Scientific name": "Melanerpes uropygialis",
            "Species": "M. uropygialis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Picidae",
                "Genus": "Melanerpes"
            }
        },
        "GILDED FLICKER": {
            "Common name": "Gilded Flicker",
            "Scientific name": "Colaptes chrysoides",
            "Species": "C. chrysoides",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Picidae",
                "Genus": "Colaptes"
            }
        },
        "GLOSSY IBIS": {
            "Common name": "Glossy Ibis",
            "Scientific name": "Plegadis falcinellus",
            "Species": "P. falcinellus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Threskiornithidae",
                "Genus": "Plegadis"
            }
        },
        "GO AWAY BIRD": {
            "Common name": "Go-away Bird",
            "Scientific name": "Corythaixoides concolor",
            "Species": "C. concolor",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Musophagidae",
                "Genus": "Corythaixoides"
            }
        },
        "GOLD WING WARBLER": {
            "Common name": "Golden-winged Warbler",
            "Scientific name": "Vermivora chrysoptera",
            "Species": "V. chrysoptera",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Vermivora"
            }
        },
        "GOLDEN BOWER BIRD": {
            "Common name": "Golden Bowerbird",
            "Scientific name": "Amblyornis newtonianus",
            "Species": "A. newtonianus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ptilonorhynchidae",
                "Genus": "Amblyornis"
            }
        },
        "GOLDEN CHEEKED WARBLER": {
            "Common name": "Golden-cheeked Warbler",
            "Scientific name": "Setophaga chrysoparia",
            "Species": "S. chrysoparia",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Setophaga"
            }
        },
        "GOLDEN CHLOROPHONIA": {
            "Common name": "Golden-browed Chlorophonia",
            "Scientific name": "Chlorophonia callophrys",
            "Species": "C. callophrys",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Chlorophonia"
            }
        },
        "GOLDEN EAGLE": {
            "Common name": "Golden Eagle",
            "Scientific name": "Aquila chrysaetos",
            "Species": "A. chrysaetos",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Aquila"
            }
        },
        "GOLDEN PARAKEET": {
            "Common name": "Golden Parakeet",
            "Scientific name": "Guaruba guarouba",
            "Species": "G. guarouba",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittacidae",
                "Genus": "Guaruba"
            }
        },
        "GOLDEN PHEASANT": {
            "Common name": "Golden Pheasant",
            "Scientific name": "Chrysolophus pictus",
            "Species": "C. pictus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Chrysolophus"
            }
        },
        "GOLDEN PIPIT": {
            "Common name": "Golden Pipit",
            "Scientific name": "Tmetothylacus tenellus",
            "Species": "T. tenellus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Motacillidae",
                "Genus": "Tmetothylacus"
            }
        },
        "GOULDIAN FINCH": {
            "Common name": "Gouldian Finch",
            "Scientific name": "Erythrura gouldiae",
            "Species": "E. gouldiae",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Estrildidae",
                "Genus": "Erythrura"
            }
        },
        "GRANDALA": {
            "Common name": "Grandala",
            "Scientific name": "Grandala coelicolor",
            "Species": "G. coelicolor",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Muscicapidae",
                "Genus": "Grandala"
            }
        },
        "GRAY CATBIRD": {
            "Common name": "Gray Catbird",
            "Scientific name": "Dumetella carolinensis",
            "Species": "D. carolinensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Mimidae",
                "Genus": "Dumetella"
            }
        },
        "GRAY KINGBIRD": {
            "Common name": "Gray Kingbird",
            "Scientific name": "Tyrannus dominicensis",
            "Species": "T. dominicensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tyrannidae",
                "Genus": "Tyrannus"
            }
        },
        "GRAY PARTRIDGE": {
            "Common name": "Gray Partridge",
            "Scientific name": "Perdix perdix",
            "Species": "P. perdix",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Perdix"
            }
        },
        "GREAT ARGUS": {
            "Common name": "Great Argus",
            "Scientific name": "Argusianus argus",
            "Species": "A. argus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Argusianus"
            }
        },
        "GREAT GRAY OWL": {
            "Common name": "Great Gray Owl",
            "Scientific name": "Strix nebulosa",
            "Species": "S. nebulosa",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Strigidae",
                "Genus": "Strix"
            }
        },
        "GREAT JACAMAR": {
            "Common name": "Great Jacamar",
            "Scientific name": "Jacamerops aureus",
            "Species": "J. aureus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Galbulidae",
                "Genus": "Jacamerops"
            }
        },
        "GREAT KISKADEE": {
            "Common name": "Great Kiskadee",
            "Scientific name": "Pitangus sulphuratus",
            "Species": "P. sulphuratus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tyrannidae",
                "Genus": "Pitangus"
            }
        },
        "GREAT POTOO": {
            "Common name": "Great Potoo",
            "Scientific name": "Nyctibius grandis",
            "Species": "N. grandis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Nyctibiidae",
                "Genus": "Nyctibius"
            }
        },
        "GREAT TINAMOU": {
            "Common name": "Great Tinamou",
            "Scientific name": "Tinamus major",
            "Species": "T. major",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tinamidae",
                "Genus": "Tinamus"
            }
        },
        "GREAT XENOPS": {
            "Common name": "Great Xenops",
            "Scientific name": "Megaxenops parnaguae",
            "Species": "M. parnaguae",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Furnariidae",
                "Genus": "Megaxenops"
            }
        },
        "GREATER PEWEE": {
            "Common name": "Greater Pewee",
            "Scientific name": "Contopus pertinax",
            "Species": "C. pertinax",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tyrannidae",
                "Genus": "Contopus"
            }
        },
        "GREATER PRAIRIE CHICKEN": {
            "Common name": "Greater Prairie-Chicken",
            "Scientific name": "Tympanuchus cupido",
            "Species": "T. cupido",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Tympanuchus"
            }
        },
        "GREATER SAGE GROUSE": {
            "Common name": "Greater Sage-Grouse",
            "Scientific name": "Centrocercus urophasianus",
            "Species": "C. urophasianus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Centrocercus"
            }
        },
        "GREEN BROADBILL": {
            "Common name": "Green Broadbill",
            "Scientific name": "Calyptomena viridis",
            "Species": "C. viridis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Eurylaimidae",
                "Genus": "Calyptomena"
            }
        },
        "GREEN JAY": {
            "Common name": "Green Jay",
            "Scientific name": "Cyanocorax yncas",
            "Species": "C. yncas",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Cyanocorax"
            }
        },
        "GREEN MAGPIE": {
            "Common name": "Green Magpie",
            "Scientific name": "Cissa chinensis",
            "Species": "C. chinensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Cissa"
            }
        },
        "GREEN WINGED DOVE": {
            "Common name": "Green-winged Dove",
            "Scientific name": "Chalcophaps indica",
            "Species": "C. indica",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Columbidae",
                "Genus": "Chalcophaps"
            }
        },
        "GREY CUCKOOSHRIKE": {
            "Common name": "Grey Cuckooshrike",
            "Scientific name": "Coracina caesia",
            "Species": "C. caesia",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Campephagidae",
                "Genus": "Coracina"
            }
        },
        "GREY HEADED CHACHALACA": {
            "Common name": "Grey-headed Chachalaca",
            "Scientific name": "Ortalis cinereiceps",
            "Species": "O. cinereiceps",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cracidae",
                "Genus": "Ortalis"
            }
        },
        "GREY HEADED FISH EAGLE": {
            "Common name": "Grey-headed Fish Eagle",
            "Scientific name": "Ichthyophaga ichthyaetus",
            "Species": "I. ichthyaetus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Ichthyophaga"
            }
        },
        "GREY PLOVER": {
            "Common name": "Grey Plover",
            "Scientific name": "Pluvialis squatarola",
            "Species": "P. squatarola",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Charadriidae",
                "Genus": "Pluvialis"
            }
        },
        "GROVED BILLED ANI": {
            "Common name": "Groove-billed Ani",
            "Scientific name": "Crotophaga sulcirostris",
            "Species": "C. sulcirostris",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cuculidae",
                "Genus": "Crotophaga"
            }
        },
        "GUINEA TURACO": {
            "Common name": "Guinea Turaco",
            "Scientific name": "Tauraco persa",
            "Species": "T. persa",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Musophagidae",
                "Genus": "Tauraco"
            }
        },
        "GUINEAFOWL": {
            "Common name": "Guineafowl",
            "Scientific name": "Numididae (Family name for guineafowl)",
            "Species": "Various species within the family Numididae",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Numididae"
            }
        },
        "GURNEYS PITTA": {
            "Common name": "Gurney's Pitta",
            "Scientific name": "Hydrornis gurneyi",
            "Species": "H. gurneyi",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Pittidae",
                "Genus": "Hydrornis"
            }
        },
        "GYRFALCON": {
            "Common name": "Gyrfalcon",
            "Scientific name": "Falco rusticolus",
            "Species": "F. rusticolus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Falconidae",
                "Genus": "Falco"
            }
        },
        "HAMERKOP": {
            "Common name": "Hamerkop",
            "Scientific name": "Scopus umbretta",
            "Species": "S. umbretta",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Scopidae",
                "Genus": "Scopus"
            }
        },
        "HARLEQUIN DUCK": {
            "Common name": "Harlequin Duck",
            "Scientific name": "Histrionicus histrionicus",
            "Species": "H. histrionicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Histrionicus"
            }
        },
        "HARLEQUIN QUAIL": {
            "Common name": "Harlequin Quail",
            "Scientific name": "Coturnix delegorguei",
            "Species": "C. delegorguei",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Coturnix"
            }
        },
        "HARPY EAGLE": {
            "Common name": "Harpy Eagle",
            "Scientific name": "Harpia harpyja",
            "Species": "H. harpyja",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Harpia"
            }
        },
        "HAWAIIAN GOOSE": {
            "Common name": "Hawaiian Goose",
            "Scientific name": "Branta sandvicensis",
            "Species": "B. sandvicensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Branta"
            }
        },
        "HAWFINCH": {
            "Common name": "Hawfinch",
            "Scientific name": "Coccothraustes coccothraustes",
            "Species": "C. coccothraustes",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Coccothraustes"
            }
        },
        "HELMET VANGA": {
            "Common name": "Helmet Vanga",
            "Scientific name": "Euryceros prevostii",
            "Species": "E. prevostii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Vangidae",
                "Genus": "Euryceros"
            }
        },
        "HEPATIC TANAGER": {
            "Common name": "Hepatic Tanager",
            "Scientific name": "Piranga flava",
            "Species": "P. flava",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cardinalidae",
                "Genus": "Piranga"
            }
        },
        "HIMALAYAN BLUETAIL": {
            "Common name": "Himalayan Bluetail",
            "Scientific name": "Tarsiger rufilatus",
            "Species": "T. rufilatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Muscicapidae",
                "Genus": "Tarsiger"
            }
        },
        "HIMALAYAN MONAL": {
            "Common name": "Himalayan Monal",
            "Scientific name": "Lophophorus impejanus",
            "Species": "L. impejanus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Lophophorus"
            }
        },
        "HOATZIN": {
            "Common name": "Hoatzin",
            "Scientific name": "Opisthocomus hoazin",
            "Species": "O. hoazin",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Opisthocomidae",
                "Genus": "Opisthocomus"
            }
        },
        "HOODED MERGANSER": {
            "Common name": "Hooded Merganser",
            "Scientific name": "Lophodytes cucullatus",
            "Species": "L. cucullatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Lophodytes"
            }
        },
        "HOOPOES": {
            "Common name": "Hoopoes",
            "Scientific name": "Upupidae (Family name for hoopoes)",
            "Species": "Various species within the family Upupidae",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Upupidae"
            }
        },
        "HORNED GUAN": {
            "Common name": "Horned Guan",
            "Scientific name": "Oreophasis derbianus",
            "Species": "O. derbianus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cracidae",
                "Genus": "Oreophasis"
            }
        },
        "HORNED LARK": {
            "Common name": "Horned Lark",
            "Scientific name": "Eremophila alpestris",
            "Species": "E. alpestris",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alaudidae",
                "Genus": "Eremophila"
            }
        },
        "HORNED SUNGEM": {
            "Common name": "Horned Sungem",
            "Scientific name": "Heliactin bilophus",
            "Species": "H. bilophus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Trochilidae",
                "Genus": "Heliactin"
            }
        },
        "HOUSE FINCH": {
            "Common name": "House Finch",
            "Scientific name": "Haemorhous mexicanus",
            "Species": "H. mexicanus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Haemorhous"
            }
        },
        "HOUSE SPARROW": {
            "Common name": "House Sparrow",
            "Scientific name": "Passer domesticus",
            "Species": "P. domesticus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Passeridae",
                "Genus": "Passer"
            }
        },
        "HYACINTH MACAW": {
            "Common name": "Hyacinth Macaw",
            "Scientific name": "Anodorhynchus hyacinthinus",
            "Species": "A. hyacinthinus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittacidae",
                "Genus": "Anodorhynchus"
            }
        },
        "IBERIAN MAGPIE": {
            "Common name": "Iberian Magpie",
            "Scientific name": "Cyanopica cooki",
            "Species": "C. cooki",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Cyanopica"
            }
        },
        "IBISBILL": {
            "Common name": "Ibisbill",
            "Scientific name": "Ibidorhyncha struthersii",
            "Species": "I. struthersii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ibidorhynchidae",
                "Genus": "Ibidorhyncha"
            }
        },
        "IMPERIAL SHAQ": {
            "Common name": "Imperial Shag",
            "Scientific name": "Leucocarbo atriceps",
            "Species": "L. atriceps",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phalacrocoracidae",
                "Genus": "Leucocarbo"
            }
        },
        "INCA TERN": {
            "Common name": "Inca Tern",
            "Scientific name": "Larosterna inca",
            "Species": "L. inca",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Sternidae",
                "Genus": "Larosterna"
            }
        },
        "INDIAN BUSTARD": {
            "Common name": "Indian Bustard",
            "Scientific name": "Ardeotis nigriceps",
            "Species": "A. nigriceps",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Otididae",
                "Genus": "Ardeotis"
            }
        },
        "INDIAN PITTA": {
            "Common name": "Indian Pitta",
            "Scientific name": "Pitta brachyura",
            "Species": "P. brachyura",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Pittidae",
                "Genus": "Pitta"
            }
        },
        "INDIAN ROLLER": {
            "Common name": "Indian Roller",
            "Scientific name": "Coracias benghalensis",
            "Species": "C. benghalensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Coraciidae",
                "Genus": "Coracias"
            }
        },
        "INDIAN VULTURE": {
            "Common name": "Indian Vulture",
            "Scientific name": "Gyps indicus",
            "Species": "G. indicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Gyps"
            }
        },
        "INDIGO BUNTING": {
            "Common name": "Indigo Bunting",
            "Scientific name": "Passerina cyanea",
            "Species": "P. cyanea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cardinalidae",
                "Genus": "Passerina"
            }
        },
        "INDIGO FLYCATCHER": {
            "Common name": "Indigo Flycatcher",
            "Scientific name": "Eumyias indigo",
            "Species": "E. indigo",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Muscicapidae",
                "Genus": "Eumyias"
            }
        },
        "INLAND DOTTEREL": {
            "Common name": "Inland Dotterel",
            "Scientific name": "Charadrius obscurus",
            "Species": "C. obscurus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Charadriidae",
                "Genus": "Charadrius"
            }
        },
        "IVORY BILLED ARACARI": {
            "Common name": "Ivory-billed Aracari",
            "Scientific name": "Pteroglossus azara",
            "Species": "P. azara",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ramphastidae",
                "Genus": "Pteroglossus"
            }
        },
        "IVORY GULL": {
            "Common name": "Ivory Gull",
            "Scientific name": "Pagophila eburnea",
            "Species": "P. eburnea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Laridae",
                "Genus": "Pagophila"
            }
        },
        "IWI": {
            "Common name": "Iwi",
            "Scientific name": "Drepanis coccinea",
            "Species": "D. coccinea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Drepanis"
            }
        },
        "JABIRU": {
            "Common name": "Jabiru",
            "Scientific name": "Jabiru mycteria",
            "Species": "J. mycteria",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ciconiidae",
                "Genus": "Jabiru"
            }
        },
        "JACK SNIPE": {
            "Common name": "Jack Snipe",
            "Scientific name": "Lymnocryptes minimus",
            "Species": "L. minimus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Scolopacidae",
                "Genus": "Lymnocryptes"
            }
        },
        "JACOBIN PIGEON": {
            "Common name": "Jacobin Pigeon",
            "Scientific name": "Columba janthina",
            "Species": "C. janthina",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Columbidae",
                "Genus": "Columba"
            }
        },
        "JANDAYA PARAKEET": {
            "Common name": "Jandaya Parakeet",
            "Scientific name": "Aratinga jandaya",
            "Species": "A. jandaya",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittacidae",
                "Genus": "Aratinga"
            }
        },
        "JAPANESE ROBIN": {
            "Common name": "Japanese Robin",
            "Scientific name": "Larvivora akahige",
            "Species": "L. akahige",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Muscicapidae",
                "Genus": "Larvivora"
            }
        },
        "JAVA SPARROW": {
            "Common name": "Java Sparrow",
            "Scientific name": "Lonchura oryzivora",
            "Species": "L. oryzivora",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Estrildidae",
                "Genus": "Lonchura"
            }
        },
        "JOCOTOCO ANTPITTA": {
            "Common name": "Jocotoco Antpitta",
            "Scientific name": "Grallaria ridgelyi",
            "Species": "G. ridgelyi",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Grallariidae",
                "Genus": "Grallaria"
            }
        },
        "KAGU": {
            "Common name": "Kagu",
            "Scientific name": "Rhynochetos jubatus",
            "Species": "R. jubatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rhynochetidae",
                "Genus": "Rhynochetos"
            }
        },
        "KAKAPO": {
            "Common name": "Kakapo",
            "Scientific name": "Strigops habroptilus",
            "Species": "S. habroptilus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Strigopidae",
                "Genus": "Strigops"
            }
        },
        "KILLDEAR": {
            "Common name": "Killdeer",
            "Scientific name": "Charadrius vociferus",
            "Species": "C. vociferus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Charadriidae",
                "Genus": "Charadrius"
            }
        },
        "KING EIDER": {
            "Common name": "King Eider",
            "Scientific name": "Somateria spectabilis",
            "Species": "S. spectabilis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Somateria"
            }
        },
        "KING VULTURE": {
            "Common name": "King Vulture",
            "Scientific name": "Sarcoramphus papa",
            "Species": "S. papa",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cathartidae",
                "Genus": "Sarcoramphus"
            }
        },
        "KIWI": {
            "Common name": "Kiwi",
            "Scientific name": "Apteryx",
            "Species": "Various species within the genus Apteryx",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Apterygidae",
                "Genus": "Apteryx"
            }
        },
        "KNOB BILLED DUCK": {
            "Common name": "Knob-billed Duck",
            "Scientific name": "Sarkidiornis melanotos",
            "Species": "S. melanotos",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Sarkidiornis"
            }
        },
        "KOOKABURRA": {
            "Common name": "Kookaburra",
            "Scientific name": "Dacelo",
            "Species": "Various species within the genus Dacelo",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcedinidae",
                "Genus": "Dacelo"
            }
        },
        "LARK BUNTING": {
            "Common name": "Lark Bunting",
            "Scientific name": "Calamospiza melanocorys",
            "Species": "C. melanocorys",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Emberizidae",
                "Genus": "Calamospiza"
            }
        },
        "LAUGHING GULL": {
            "Common name": "Laughing Gull",
            "Scientific name": "Leucophaeus atricilla",
            "Species": "L. atricilla",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Laridae",
                "Genus": "Leucophaeus"
            }
        },
        "LAZULI BUNTING": {
            "Common name": "Lazuli Bunting",
            "Scientific name": "Passerina amoena",
            "Species": "P. amoena",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cardinalidae",
                "Genus": "Passerina"
            }
        },
        "LESSER ADJUTANT": {
            "Common name": "Lesser Adjutant",
            "Scientific name": "Leptoptilos javanicus",
            "Species": "L. javanicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ciconiidae",
                "Genus": "Leptoptilos"
            }
        },
        "LILAC ROLLER": {
            "Common name": "Lilac-breasted Roller",
            "Scientific name": "Coracias caudatus",
            "Species": "C. caudatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Coraciidae",
                "Genus": "Coracias"
            }
        },
        "LIMPKIN": {
            "Common name": "Limpkin",
            "Scientific name": "Aramus guarauna",
            "Species": "A. guarauna",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Aramidae",
                "Genus": "Aramus"
            }
        },
        "LITTLE AUK": {
            "Common name": "Little Auk",
            "Scientific name": "Alle alle",
            "Species": "A. alle",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcidae",
                "Genus": "Alle"
            }
        },
        "LOGGERHEAD SHRIKE": {
            "Common name": "Loggerhead Shrike",
            "Scientific name": "Lanius ludovicianus",
            "Species": "L. ludovicianus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Laniidae",
                "Genus": "Lanius"
            }
        },
        "LONG-EARED OWL": {
            "Common name": "Long-eared Owl",
            "Scientific name": "Asio otus",
            "Species": "A. otus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Strigidae",
                "Genus": "Asio"
            }
        },
        "LOONEY BIRDS": {
            "Common name": "Loon",
            "Scientific name": "Gavia",
            "Species": "Various species within the genus Gavia",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Gaviidae",
                "Genus": "Gavia"
            }
        },
        "LUCIFER HUMMINGBIRD": {
            "Common name": "Lucifer Hummingbird",
            "Scientific name": "Calothorax lucifer",
            "Species": "C. lucifer",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Trochilidae",
                "Genus": "Calothorax"
            }
        },
        "MAGPIE GOOSE": {
            "Common name": "Magpie Goose",
            "Scientific name": "Anseranas semipalmata",
            "Species": "A. semipalmata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anseranatidae",
                "Genus": "Anseranas"
            }
        },
        "MALABAR HORNBILL": {
            "Common name": "Malabar Hornbill",
            "Scientific name": "Anthracoceros coronatus",
            "Species": "A. coronatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Bucerotidae",
                "Genus": "Anthracoceros"
            }
        },
        "MALACHITE KINGFISHER": {
            "Common name": "Malachite Kingfisher",
            "Scientific name": "Corythornis cristatus",
            "Species": "C. cristatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcedinidae",
                "Genus": "Corythornis"
            }
        },
        "MALAGASY WHITE EYE": {
            "Common name": "Malagasy White Eye",
            "Scientific name": "Zosterops maderaspatanus",
            "Species": "Z. maderaspatanus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Zosteropidae",
                "Genus": "Zosterops"
            }
        },
        "MALEO": {
            "Common name": "Maleo",
            "Scientific name": "Macrocephalon maleo",
            "Species": "M. maleo",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Megapodiidae",
                "Genus": "Macrocephalon"
            }
        },
        "MALLARD DUCK": {
            "Common name": "Mallard Duck",
            "Scientific name": "Anas platyrhynchos",
            "Species": "A. platyrhynchos",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Anas"
            }
        },
        "MANDRIN DUCK": {
            "Common name": "Mandarin Duck",
            "Scientific name": "Aix galericulata",
            "Species": "A. galericulata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Aix"
            }
        },
        "MANGROVE CUCKOO": {
            "Common name": "Mangrove Cuckoo",
            "Scientific name": "Coccyzus minor",
            "Species": "C. minor",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cuculidae",
                "Genus": "Coccyzus"
            }
        },
        "MARABOU STORK": {
            "Common name": "Marabou Stork",
            "Scientific name": "Leptoptilos crumeniferus",
            "Species": "L. crumeniferus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ciconiidae",
                "Genus": "Leptoptilos"
            }
        },
        "MASKED BOBWHITE": {
            "Common name": "Masked Bobwhite",
            "Scientific name": "Colinus virginianus ridgwayi",
            "Species": "C. virginianus ridgwayi",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Odontophoridae",
                "Genus": "Colinus"
            }
        },
        "MASKED BOOBY": {
            "Common name": "Masked Booby",
            "Scientific name": "Sula dactylatra",
            "Species": "S. dactylatra",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Sulidae",
                "Genus": "Sula"
            }
        },
        "MASKED LAPWING": {
            "Common name": "Masked Lapwing",
            "Scientific name": "Vanellus miles",
            "Species": "V. miles",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Charadriidae",
                "Genus": "Vanellus"
            }
        },
        "MCKAYS BUNTING": {
            "Common name": "McKay's Bunting",
            "Scientific name": "Plectrophenax hyperboreus",
            "Species": "P. hyperboreus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Emberizidae",
                "Genus": "Plectrophenax"
            }
        },
        "MERLIN": {
            "Common name": "Merlin",
            "Scientific name": "Falco columbarius",
            "Species": "F. columbarius",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Falconidae",
                "Genus": "Falco"
            }
        },
        "MIKADO PHEASANT": {
            "Common name": "Mikado Pheasant",
            "Scientific name": "Syrmaticus mikado",
            "Species": "S. mikado",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Syrmaticus"
            }
        },
        "MILITARY MACAW": {
            "Common name": "Military Macaw",
            "Scientific name": "Ara militaris",
            "Species": "A. militaris",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittacidae",
                "Genus": "Ara"
            }
        },
        "MOURNING DOVE": {
            "Common name": "Mourning Dove",
            "Scientific name": "Zenaida macroura",
            "Species": "Z. macroura",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Columbidae",
                "Genus": "Zenaida"
            }
        },
        "MYNA": {
            "Common name": "Myna",
            "Scientific name": "Acridotheres tristis",
            "Species": "A. tristis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Sturnidae",
                "Genus": "Acridotheres"
            }
        },
        "NICOBAR PIGEON": {
            "Common name": "Nicobar Pigeon",
            "Scientific name": "Caloenas nicobarica",
            "Species": "C. nicobarica",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Columbidae",
                "Genus": "Caloenas"
            }
        },
        "NOISY FRIARBIRD": {
            "Common name": "Noisy Friarbird",
            "Scientific name": "Philemon corniculatus",
            "Species": "P. corniculatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Meliphagidae",
                "Genus": "Philemon"
            }
        },
        "NORTHERN BEARDLESS TYRANNULET": {
            "Common name": "Northern Beardless Tyrannulet",
            "Scientific name": "Camptostoma imberbe",
            "Species": "C. imberbe",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tyrannidae",
                "Genus": "Camptostoma"
            }
        },
        "NORTHERN CARDINAL": {
            "Common name": "Northern Cardinal",
            "Scientific name": "Cardinalis cardinalis",
            "Species": "C. cardinalis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cardinalidae",
                "Genus": "Cardinalis"
            }
        },
        "NORTHERN FLICKER": {
            "Common name": "Northern Flicker",
            "Scientific name": "Colaptes auratus",
            "Species": "C. auratus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Picidae",
                "Genus": "Colaptes"
            }
        },
        "NORTHERN FULMAR": {
            "Common name": "Northern Fulmar",
            "Scientific name": "Fulmarus glacialis",
            "Species": "F. glacialis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Procellariidae",
                "Genus": "Fulmarus"
            }
        },
        "NORTHERN GANNET": {
            "Common name": "Northern Gannet",
            "Scientific name": "Morus bassanus",
            "Species": "M. bassanus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Sulidae",
                "Genus": "Morus"
            }
        },
        "NORTHERN GOSHAWK": {
            "Common name": "Northern Goshawk",
            "Scientific name": "Accipiter gentilis",
            "Species": "A. gentilis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Accipiter"
            }
        },
        "NORTHERN JACANA": {
            "Common name": "Northern Jacana",
            "Scientific name": "Jacana spinosa",
            "Species": "J. spinosa",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Jacanidae",
                "Genus": "Jacana"
            }
        },
        "NORTHERN MOCKINGBIRD": {
            "Common name": "Northern Mockingbird",
            "Scientific name": "Mimus polyglottos",
            "Species": "M. polyglottos",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Mimidae",
                "Genus": "Mimus"
            }
        },
        "NORTHERN PARULA": {
            "Common name": "Northern Parula",
            "Scientific name": "Setophaga americana",
            "Species": "S. americana",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Setophaga"
            }
        },
        "NORTHERN RED BISHOP": {
            "Common name": "Northern Red Bishop",
            "Scientific name": "Euplectes franciscanus",
            "Species": "E. franciscanus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ploceidae",
                "Genus": "Euplectes"
            }
        },
        "NORTHERN SHOVELER": {
            "Common name": "Northern Shoveler",
            "Scientific name": "Spatula clypeata",
            "Species": "S. clypeata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Spatula"
            }
        },
        "OCELLATED TURKEY": {
            "Common name": "Ocellated Turkey",
            "Scientific name": "Meleagris ocellata",
            "Species": "M. ocellata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Meleagris"
            }
        },
        "OILBIRD": {
            "Common name": "Oilbird",
            "Scientific name": "Steatornis caripensis",
            "Species": "S. caripensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Steatornithidae",
                "Genus": "Steatornis"
            }
        },
        "OKINAWA RAIL": {
            "Common name": "Okinawa Rail",
            "Scientific name": "Gallirallus okinawae",
            "Species": "G. okinawae",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rallidae",
                "Genus": "Gallirallus"
            }
        },
        "ORANGE BREASTED TROGON": {
            "Common name": "Orange-breasted Trogon",
            "Scientific name": "Harpactes oreskios",
            "Species": "H. oreskios",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Trogonidae",
                "Genus": "Harpactes"
            }
        },
        "ORANGE BRESTED BUNTING": {
            "Common name": "Orange-breasted Bunting",
            "Scientific name": "Emberiza aureola",
            "Species": "E. aureola",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Emberizidae",
                "Genus": "Emberiza"
            }
        },
        "ORIENTAL BAY OWL": {
            "Common name": "Oriental Bay Owl",
            "Scientific name": "Phodilus badius",
            "Species": "P. badius",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tytonidae",
                "Genus": "Phodilus"
            }
        },
        "ORNATE HAWK EAGLE": {
            "Common name": "Ornate Hawk-Eagle",
            "Scientific name": "Spizaetus ornatus",
            "Species": "S. ornatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Spizaetus"
            }
        },
        "OSPREY": {
            "Common name": "Osprey",
            "Scientific name": "Pandion haliaetus",
            "Species": "P. haliaetus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Pandionidae",
                "Genus": "Pandion"
            }
        },
        "OSTRICH": {
            "Common name": "Ostrich",
            "Scientific name": "Struthio camelus",
            "Species": "S. camelus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Struthionidae",
                "Genus": "Struthio"
            }
        },
        "OVENBIRD": {
            "Common name": "Ovenbird",
            "Scientific name": "Seiurus aurocapilla",
            "Species": "S. aurocapilla",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Seiurus"
            }
        },
        "OYSTER CATCHER": {
            "Common name": "Oystercatcher",
            "Scientific name": "Haematopus",
            "Species": "Various species within the genus Haematopus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Haematopodidae",
                "Genus": "Haematopus"
            }
        },
        "PAINTED BUNTING": {
            "Common name": "Painted Bunting",
            "Scientific name": "Passerina ciris",
            "Species": "P. ciris",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cardinalidae",
                "Genus": "Passerina"
            }
        },
        "PALILA": {
            "Common name": "Palila",
            "Scientific name": "Loxioides bailleui",
            "Species": "L. bailleui",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Loxioides"
            }
        },
        "PALM NUT VULTURE": {
            "Common name": "Palm-nut Vulture",
            "Scientific name": "Gypohierax angolensis",
            "Species": "G. angolensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Gypohierax"
            }
        },
        "PARADISE TANAGER": {
            "Common name": "Paradise Tanager",
            "Scientific name": "Tangara chilensis",
            "Species": "T. chilensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Thraupidae",
                "Genus": "Tangara"
            }
        },
        "PARAKETT AUKLET": {
            "Common name": "Parakeet Auklet",
            "Scientific name": "Aethia psittacula",
            "Species": "A. psittacula",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcidae",
                "Genus": "Aethia"
            }
        },
        "PARUS MAJOR": {
            "Common name": "Great Tit",
            "Scientific name": "Parus major",
            "Species": "P. major",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Paridae",
                "Genus": "Parus"
            }
        },
        "PATAGONIAN SIERRA FINCH": {
            "Common name": "Patagonian Sierra Finch",
            "Scientific name": "Phrygilus patagonicus",
            "Species": "P. patagonicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Thraupidae",
                "Genus": "Phrygilus"
            }
        },
        "PEACOCK": {
            "Common name": "Peacock",
            "Scientific name": "Pavo cristatus",
            "Species": "P. cristatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Pavo"
            }
        },
        "PEREGRINE FALCON": {
            "Common name": "Peregrine Falcon",
            "Scientific name": "Falco peregrinus",
            "Species": "F. peregrinus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Falconidae",
                "Genus": "Falco"
            }
        },
        "PHAINOPEPLA": {
            "Common name": "Phainopepla",
            "Scientific name": "Phainopepla nitens",
            "Species": "P. nitens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ptiliogonatidae",
                "Genus": "Phainopepla"
            }
        },
        "PHILIPPINE EAGLE": {
            "Common name": "Philippine Eagle",
            "Scientific name": "Pithecophaga jefferyi",
            "Species": "P. jefferyi",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Pithecophaga"
            }
        },
        "PINK ROBIN": {
            "Common name": "Pink Robin",
            "Scientific name": "Petroica rodinogaster",
            "Species": "P. rodinogaster",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Petroicidae",
                "Genus": "Petroica"
            }
        },
        "PLUSH CRESTED JAY": {
            "Common name": "Plush-crested Jay",
            "Scientific name": "Cyanocorax chrysops",
            "Species": "C. chrysops",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Cyanocorax"
            }
        },
        "POMARINE JAEGER": {
            "Common name": "Pomarine Jaeger",
            "Scientific name": "Stercorarius pomarinus",
            "Species": "S. pomarinus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Stercorariidae",
                "Genus": "Stercorarius"
            }
        },
        "PUFFIN": {
            "Common name": "Puffin",
            "Scientific name": "Fratercula",
            "Species": "Various species within the genus Fratercula",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcidae",
                "Genus": "Fratercula"
            }
        },
        "PUNA TEAL": {
            "Common name": "Puna Teal",
            "Scientific name": "Spatula puna",
            "Species": "S. puna",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Spatula"
            }
        },
        "PURPLE FINCH": {
            "Common name": "Purple Finch",
            "Scientific name": "Haemorhous purpureus",
            "Species": "H. purpureus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Haemorhous"
            }
        },
        "PURPLE GALLINULE": {
            "Common name": "Purple Gallinule",
            "Scientific name": "Porphyrio martinicus",
            "Species": "P. martinicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rallidae",
                "Genus": "Porphyrio"
            }
        },
        "PURPLE MARTIN": {
            "Common name": "Purple Martin",
            "Scientific name": "Progne subis",
            "Species": "P. subis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Hirundinidae",
                "Genus": "Progne"
            }
        },
        "PURPLE SWAMPHEN": {
            "Common name": "Purple Swamphen",
            "Scientific name": "Porphyrio porphyrio",
            "Species": "P. porphyrio",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rallidae",
                "Genus": "Porphyrio"
            }
        },
        "PYGMY KINGFISHER": {
            "Common name": "Pygmy Kingfisher",
            "Scientific name": "Ceyx cyanopectus",
            "Species": "C. cyanopectus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcedinidae",
                "Genus": "Ceyx"
            }
        },
        "PYRRHULOXIA": {
            "Common name": "Pyrrhuloxia",
            "Scientific name": "Cardinalis sinuatus",
            "Species": "C. sinuatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cardinalidae",
                "Genus": "Cardinalis"
            }
        },
        "QUETZAL": {
            "Common name": "Quetzal",
            "Scientific name": "Pharomachrus mocinno",
            "Species": "P. mocinno",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Trogonidae",
                "Genus": "Pharomachrus"
            }
        },
        "RAINBOW LORIKEET": {
            "Common name": "Rainbow Lorikeet",
            "Scientific name": "Trichoglossus moluccanus",
            "Species": "T. moluccanus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittaculidae",
                "Genus": "Trichoglossus"
            }
        },
        "RAZORBILL": {
            "Common name": "Razorbill",
            "Scientific name": "Alca torda",
            "Species": "A. torda",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcidae",
                "Genus": "Alca"
            }
        },
        "RED BEARDED BEE EATER": {
            "Common name": "Red-bearded Bee-eater",
            "Scientific name": "Nyctyornis amictus",
            "Species": "N. amictus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Meropidae",
                "Genus": "Nyctyornis"
            }
        },
        "RED BELLIED PITTA": {
            "Common name": "Red-bellied Pitta",
            "Scientific name": "Pitta erythrogaster",
            "Species": "P. erythrogaster",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Pittidae",
                "Genus": "Pitta"
            }
        },
        "RED BILLED TROPICBIRD": {
            "Common name": "Red-billed Tropicbird",
            "Scientific name": "Phaethon aethereus",
            "Species": "P. aethereus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phaethontidae",
                "Genus": "Phaethon"
            }
        },
        "RED BROWED FINCH": {
            "Common name": "Red-browed Finch",
            "Scientific name": "Neochmia temporalis",
            "Species": "N. temporalis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Estrildidae",
                "Genus": "Neochmia"
            }
        },
        "RED CROSSBILL": {
            "Common name": "Red Crossbill",
            "Scientific name": "Loxia curvirostra",
            "Species": "L. curvirostra",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Fringillidae",
                "Genus": "Loxia"
            }
        },
        "RED FACED CORMORANT": {
            "Common name": "Red-faced Cormorant",
            "Scientific name": "Phalacrocorax urile",
            "Species": "P. urile",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phalacrocoracidae",
                "Genus": "Phalacrocorax"
            }
        },
        "RED FACED WARBLER": {
            "Common name": "Red-faced Warbler",
            "Scientific name": "Cardellina rubrifrons",
            "Species": "C. rubrifrons",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Cardellina"
            }
        },
        "RED FODY": {
            "Common name": "Red Fody",
            "Scientific name": "Foudia madagascariensis",
            "Species": "F. madagascariensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ploceidae",
                "Genus": "Foudia"
            }
        },
        "RED HEADED DUCK": {
            "Common name": "Red-headed Duck",
            "Scientific name": "Aythya americana",
            "Species": "A. americana",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Aythya"
            }
        },
        "RED HEADED WOODPECKER": {
            "Common name": "Red-headed Woodpecker",
            "Scientific name": "Melanerpes erythrocephalus",
            "Species": "M. erythrocephalus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Picidae",
                "Genus": "Melanerpes"
            }
        },
        "RED KNOT": {
            "Common name": "Red Knot",
            "Scientific name": "Calidris canutus",
            "Species": "C. canutus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Scolopacidae",
                "Genus": "Calidris"
            }
        },
        "RED LEGGED HONEYCREEPER": {
            "Common name": "Red-legged Honeycreeper",
            "Scientific name": "Cyanerpes cyaneus",
            "Species": "C. cyaneus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Thraupidae",
                "Genus": "Cyanerpes"
            }
        },
        "RED NAPED TROGON": {
            "Common name": "Red-naped Trogon",
            "Scientific name": "Harpactes kasumba",
            "Species": "H. kasumba",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Trogonidae",
                "Genus": "Harpactes"
            }
        },
        "RED SHOULDERED HAWK": {
            "Common name": "Red-shouldered Hawk",
            "Scientific name": "Buteo lineatus",
            "Species": "B. lineatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Buteo"
            }
        },
        "RED TAILED HAWK": {
            "Common name": "Red-tailed Hawk",
            "Scientific name": "Buteo jamaicensis",
            "Species": "B. jamaicensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Buteo"
            }
        },
        "RED TAILED THRUSH": {
            "Common name": "Red-tailed Thrush",
            "Scientific name": "Turdus rufitorques",
            "Species": "T. rufitorques",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Turdidae",
                "Genus": "Turdus"
            }
        },
        "RED WINGED BLACKBIRD": {
            "Common name": "Red-winged Blackbird",
            "Scientific name": "Agelaius phoeniceus",
            "Species": "A. phoeniceus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Icteridae",
                "Genus": "Agelaius"
            }
        },
        "RED WISKERED BULBUL": {
            "Common name": "Red-whiskered Bulbul",
            "Scientific name": "Pycnonotus jocosus",
            "Species": "P. jocosus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Pycnonotidae",
                "Genus": "Pycnonotus"
            }
        },
        "REGENT BOWERBIRD": {
            "Common name": "Regent Bowerbird",
            "Scientific name": "Sericulus chrysocephalus",
            "Species": "S. chrysocephalus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ptilonorhynchidae",
                "Genus": "Sericulus"
            }
        },
        "RING-NECKED PHEASANT": {
            "Common name": "Ring-necked Pheasant",
            "Scientific name": "Phasianus colchicus",
            "Species": "P. colchicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Phasianus"
            }
        },
        "ROADRUNNER": {
            "Common name": "Roadrunner",
            "Scientific name": "Geococcyx californianus",
            "Species": "G. californianus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cuculidae",
                "Genus": "Geococcyx"
            }
        },
        "ROCK DOVE": {
            "Common name": "Rock Dove",
            "Scientific name": "Columba livia",
            "Species": "C. livia",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Columbidae",
                "Genus": "Columba"
            }
        },
        "ROSE BREASTED COCKATOO": {
            "Common name": "Rose-breasted Cockatoo",
            "Scientific name": "Eolophus roseicapilla",
            "Species": "E. roseicapilla",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cacatuidae",
                "Genus": "Eolophus"
            }
        },
        "ROSE BREASTED GROSBEAK": {
            "Common name": "Rose-breasted Grosbeak",
            "Scientific name": "Pheucticus ludovicianus",
            "Species": "P. ludovicianus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cardinalidae",
                "Genus": "Pheucticus"
            }
        },
        "ROSEATE SPOONBILL": {
            "Common name": "Roseate Spoonbill",
            "Scientific name": "Platalea ajaja",
            "Species": "P. ajaja",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Threskiornithidae",
                "Genus": "Platalea"
            }
        },
        "ROSY FACED LOVEBIRD": {
            "Common name": "Rosy-faced Lovebird",
            "Scientific name": "Agapornis roseicollis",
            "Species": "A. roseicollis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittaculidae",
                "Genus": "Agapornis"
            }
        },
        "ROUGH LEG BUZZARD": {
            "Common name": "Rough-legged Buzzard",
            "Scientific name": "Buteo lagopus",
            "Species": "B. lagopus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Accipitridae",
                "Genus": "Buteo"
            }
        },
        "ROYAL FLYCATCHER": {
            "Common name": "Royal Flycatcher",
            "Scientific name": "Onychorhynchus coronatus",
            "Species": "O. coronatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tyrannidae",
                "Genus": "Onychorhynchus"
            }
        },
        "RUBY CROWNED KINGLET": {
            "Common name": "Ruby-crowned Kinglet",
            "Scientific name": "Regulus calendula",
            "Species": "R. calendula",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Regulidae",
                "Genus": "Regulus"
            }
        },
        "RUBY THROATED HUMMINGBIRD": {
            "Common name": "Ruby-throated Hummingbird",
            "Scientific name": "Archilochus colubris",
            "Species": "A. colubris",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Trochilidae",
                "Genus": "Archilochus"
            }
        },
        "RUDDY SHELDUCK": {
            "Common name": "Ruddy Shelduck",
            "Scientific name": "Tadorna ferruginea",
            "Species": "T. ferruginea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Tadorna"
            }
        },
        "RUDY KINGFISHER": {
            "Common name": "Ruddy Kingfisher",
            "Scientific name": "Halcyon coromanda",
            "Species": "H. coromanda",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcedinidae",
                "Genus": "Halcyon"
            }
        },
        "RUFOUS KINGFISHER": {
            "Common name": "Rufous Kingfisher",
            "Scientific name": "Actenoides concretus",
            "Species": "A. concretus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcedinidae",
                "Genus": "Actenoides"
            }
        },
        "RUFOUS TREPE": {
            "Common name": "Rufous Treepie",
            "Scientific name": "Dendrocitta vagabunda",
            "Species": "D. vagabunda",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Dendrocitta"
            }
        },
        "RUFUOS MOTMOT": {
            "Common name": "Rufous Motmot",
            "Scientific name": "Baryphthengus martii",
            "Species": "B. martii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Momotidae",
                "Genus": "Baryphthengus"
            }
        },
        "SAMATRAN THRUSH": {
            "Common name": "Sumatran Thrush",
            "Scientific name": "Zoothera monticola",
            "Species": "Z. monticola",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Turdidae",
                "Genus": "Zoothera"
            }
        },
        "SAND MARTIN": {
            "Common name": "Sand Martin",
            "Scientific name": "Riparia riparia",
            "Species": "R. riparia",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Hirundinidae",
                "Genus": "Riparia"
            }
        },
        "SANDHILL CRANE": {
            "Common name": "Sandhill Crane",
            "Scientific name": "Antigone canadensis",
            "Species": "A. canadensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Gruidae",
                "Genus": "Antigone"
            }
        },
        "SATYR TRAGOPAN": {
            "Common name": "Satyr Tragopan",
            "Scientific name": "Tragopan satyra",
            "Species": "T. satyra",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Tragopan"
            }
        },
        "SAYS PHOEBE": {
            "Common name": "Say's Phoebe",
            "Scientific name": "Sayornis saya",
            "Species": "S. saya",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tyrannidae",
                "Genus": "Sayornis"
            }
        },
        "SCARLET CROWNED FRUIT DOVE": {
            "Common name": "Scarlet-crowned Fruit Dove",
            "Scientific name": "Ptilinopus porphyraceus",
            "Species": "P. porphyraceus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Columbidae",
                "Genus": "Ptilinopus"
            }
        },
        "SCARLET FACED LIOCICHLA": {
            "Common name": "Scarlet-faced Liocichla",
            "Scientific name": "Liocichla ripponi",
            "Species": "L. ripponi",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Leiothrichidae",
                "Genus": "Liocichla"
            }
        },
        "SCARLET IBIS": {
            "Common name": "Scarlet Ibis",
            "Scientific name": "Eudocimus ruber",
            "Species": "E. ruber",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Threskiornithidae",
                "Genus": "Eudocimus"
            }
        },
        "SCARLET MACAW": {
            "Common name": "Scarlet Macaw",
            "Scientific name": "Ara macao",
            "Species": "A. macao",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Psittacidae",
                "Genus": "Ara"
            }
        },
        "SCARLET TANAGER": {
            "Common name": "Scarlet Tanager",
            "Scientific name": "Piranga olivacea",
            "Species": "P. olivacea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cardinalidae",
                "Genus": "Piranga"
            }
        },
        "SHOEBILL": {
            "Common name": "Shoebill",
            "Scientific name": "Balaeniceps rex",
            "Species": "B. rex",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Balaenicipitidae",
                "Genus": "Balaeniceps"
            }
        },
        "SHORT BILLED DOWITCHER": {
            "Common name": "Short-billed Dowitcher",
            "Scientific name": "Limnodromus griseus",
            "Species": "L. griseus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Scolopacidae",
                "Genus": "Limnodromus"
            }
        },
        "SMITHS LONGSPUR": {
            "Common name": "Smith's Longspur",
            "Scientific name": "Calcarius pictus",
            "Species": "C. pictus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Calcariidae",
                "Genus": "Calcarius"
            }
        },
        "SNOW GOOSE": {
            "Common name": "Snow Goose",
            "Scientific name": "Anser caerulescens",
            "Species": "A. caerulescens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Anser"
            }
        },
        "SNOW PARTRIDGE": {
            "Common name": "Snow Partridge",
            "Scientific name": "Lerwa lerwa",
            "Species": "L. lerwa",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Lerwa"
            }
        },
        "SNOWY EGRET": {
            "Common name": "Snowy Egret",
            "Scientific name": "Egretta thula",
            "Species": "E. thula",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ardeidae",
                "Genus": "Egretta"
            }
        },
        "SNOWY OWL": {
            "Common name": "Snowy Owl",
            "Scientific name": "Bubo scandiacus",
            "Species": "B. scandiacus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Strigidae",
                "Genus": "Bubo"
            }
        },
        "SNOWY PLOVER": {
            "Common name": "Snowy Plover",
            "Scientific name": "Charadrius nivosus",
            "Species": "C. nivosus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Charadriidae",
                "Genus": "Charadrius"
            }
        },
        "SNOWY SHEATHBILL": {
            "Common name": "Snowy Sheathbill",
            "Scientific name": "Chionis albus",
            "Species": "C. albus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Chionidae",
                "Genus": "Chionis"
            }
        },
         "SORA": {
            "Common name": "Sora",
            "Scientific name": "Porzana carolina",
            "Species": "P. carolina",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rallidae",
                "Genus": "Porzana"
            }
        },
        "SPANGLED COTINGA": {
            "Common name": "Spangled Cotinga",
            "Scientific name": "Cotinga cayana",
            "Species": "C. cayana",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cotingidae",
                "Genus": "Cotinga"
            }
        },
        "SPLENDID WREN": {
            "Common name": "Splendid Wren",
            "Scientific name": "Malurus splendens",
            "Species": "M. splendens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Maluridae",
                "Genus": "Malurus"
            }
        },
        "SPOON BILED SANDPIPER": {
            "Common name": "Spoon-billed Sandpiper",
            "Scientific name": "Calidris pygmaea",
            "Species": "C. pygmaea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Scolopacidae",
                "Genus": "Calidris"
            }
        },
        "SPOTTED CATBIRD": {
            "Common name": "Spotted Catbird",
            "Scientific name": "Ailuroedus melanotis",
            "Species": "A. melanotis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ptilonorhynchidae",
                "Genus": "Ailuroedus"
            }
        },
        "SPOTTED WHISTLING DUCK": {
            "Common name": "Spotted Whistling Duck",
            "Scientific name": "Dendrocygna guttata",
            "Species": "D. guttata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Dendrocygna"
            }
        },
        "SQUACCO HERON": {
            "Common name": "Squacco Heron",
            "Scientific name": "Ardeola ralloides",
            "Species": "A. ralloides",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ardeidae",
                "Genus": "Ardeola"
            }
        },
        "SRI LANKA BLUE MAGPIE": {
            "Common name": "Sri Lanka Blue Magpie",
            "Scientific name": "Urocissa ornata",
            "Species": "U. ornata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Urocissa"
            }
        },
        "STEAMER DUCK": {
            "Common name": "Steamer Duck",
            "Scientific name": "Tachyeres pteneres",
            "Species": "T. pteneres",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Tachyeres"
            }
        },
        "STORK BILLED KINGFISHER": {
            "Common name": "Stork-billed Kingfisher",
            "Scientific name": "Pelargopsis capensis",
            "Species": "P. capensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcedinidae",
                "Genus": "Pelargopsis"
            }
        },
        "STRIATED CARACARA": {
            "Common name": "Striated Caracara",
            "Scientific name": "Phalcoboenus australis",
            "Species": "P. australis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Falconidae",
                "Genus": "Phalcoboenus"
            }
        },
        "STRIPED OWL": {
            "Common name": "Striped Owl",
            "Scientific name": "Pseudoscops clamator",
            "Species": "P. clamator",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Strigidae",
                "Genus": "Pseudoscops"
            }
        },
        "STRIPPED MANAKIN": {
            "Common name": "Stripped Manakin",
            "Scientific name": "Machaeropterus regulus",
            "Species": "M. regulus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Pipridae",
                "Genus": "Machaeropterus"
            }
        },
        "STRIPPED SWALLOW": {
            "Common name": "Stripped Swallow",
            "Scientific name": "Cecropis cucullata",
            "Species": "C. cucullata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Hirundinidae",
                "Genus": "Cecropis"
            }
        },
        "SUNBITTERN": {
            "Common name": "Sunbittern",
            "Scientific name": "Eurypyga helias",
            "Species": "E. helias",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Eurypygidae",
                "Genus": "Eurypyga"
            }
        },
        "SUPERB STARLING": {
            "Common name": "Superb Starling",
            "Scientific name": "Lamprotornis superbus",
            "Species": "L. superbus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Sturnidae",
                "Genus": "Lamprotornis"
            }
        },
        "SURF SCOTER": {
            "Common name": "Surf Scoter",
            "Scientific name": "Melanitta perspicillata",
            "Species": "M. perspicillata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Melanitta"
            }
        },
        "SWINHOES PHEASANT": {
            "Common name": "Swinhoe's Pheasant",
            "Scientific name": "Lophura swinhoii",
            "Species": "L. swinhoii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Lophura"
            }
        },
        "TAILORBIRD": {
            "Common name": "Tailorbird",
            "Scientific name": "Orthotomus sutorius",
            "Species": "O. sutorius",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cisticolidae",
                "Genus": "Orthotomus"
            }
        },
        "TAIWAN MAGPIE": {
            "Common name": "Taiwan Magpie",
            "Scientific name": "Urocissa caerulea",
            "Species": "U. caerulea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Urocissa"
            }
        },
        "TAKAHE": {
            "Common name": "Takahe",
            "Scientific name": "Porphyrio hochstetteri",
            "Species": "P. hochstetteri",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rallidae",
                "Genus": "Porphyrio"
            }
        },
        "TASMANIAN HEN": {
            "Common name": "Tasmanian Hen",
            "Scientific name": "Tribonyx mortierii",
            "Species": "T. mortierii",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rallidae",
                "Genus": "Tribonyx"
            }
        },
        "TAWNY FROGMOUTH": {
            "Common name": "Tawny Frogmouth",
            "Scientific name": "Podargus strigoides",
            "Species": "P. strigoides",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Podargidae",
                "Genus": "Podargus"
            }
        },
        "TEAL DUCK": {
            "Common name": "Teal Duck",
            "Scientific name": "Anas crecca",
            "Species": "A. crecca",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Anas"
            }
        },
        "TIT MOUSE": {
            "Common name": "Tit Mouse",
            "Scientific name": "Parus major",
            "Species": "P. major",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Paridae",
                "Genus": "Parus"
            }
        },
        "TOUCHAN": {
            "Common name": "Touchan",
            "Scientific name": "Ramphastos toco",
            "Species": "R. toco",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Ramphastidae",
                "Genus": "Ramphastos"
            }
        },
        "TOWNSENDS WARBLER": {
            "Common name": "Townsend's Warbler",
            "Scientific name": "Setophaga townsendi",
            "Species": "S. townsendi",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Setophaga"
            }
        },
        "TREE SWALLOW": {
            "Common name": "Tree Swallow",
            "Scientific name": "Tachycineta bicolor",
            "Species": "T. bicolor",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Hirundinidae",
                "Genus": "Tachycineta"
            }
        },
        "TRICOLORED BLACKBIRD": {
            "Common name": "Tricolored Blackbird",
            "Scientific name": "Agelaius tricolor",
            "Species": "A. tricolor",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Icteridae",
                "Genus": "Agelaius"
            }
        },
        "TROPICAL KINGBIRD": {
            "Common name": "Tropical Kingbird",
            "Scientific name": "Tyrannus melancholicus",
            "Species": "T. melancholicus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tyrannidae",
                "Genus": "Tyrannus"
            }
        },
        "TRUMPTER SWAN": {
            "Common name": "Trumpeter Swan",
            "Scientific name": "Cygnus buccinator",
            "Species": "C. buccinator",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Cygnus"
            }
        },
        "TURKEY VULTURE": {
            "Common name": "Turkey Vulture",
            "Scientific name": "Cathartes aura",
            "Species": "C. aura",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cathartidae",
                "Genus": "Cathartes"
            }
        },
        "TURQUOISE MOTMOT": {
            "Common name": "Turquoise Motmot",
            "Scientific name": "Eumomota superciliosa",
            "Species": "E. superciliosa",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Momotidae",
                "Genus": "Eumomota"
            }
        },
        "UMBRELLA BIRD": {
            "Common name": "Umbrella Bird",
            "Scientific name": "Cephalopterus ornatus",
            "Species": "C. ornatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cotingidae",
                "Genus": "Cephalopterus"
            }
        },
        "VARIED THRUSH": {
            "Common name": "Varied Thrush",
            "Scientific name": "Ixoreus naevius",
            "Species": "I. naevius",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Turdidae",
                "Genus": "Ixoreus"
            }
        },
        "VEERY": {
            "Common name": "Veery",
            "Scientific name": "Catharus fuscescens",
            "Species": "C. fuscescens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Turdidae",
                "Genus": "Catharus"
            }
        },
        "VENEZUELIAN TROUPIAL": {
            "Common name": "Venezuelan Troupial",
            "Scientific name": "Icterus icterus",
            "Species": "I. icterus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Icteridae",
                "Genus": "Icterus"
            }
        },
        "VERDIN": {
            "Common name": "Verdin",
            "Scientific name": "Auriparus flaviceps",
            "Species": "A. flaviceps",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Remizidae",
                "Genus": "Auriparus"
            }
        },
        "VERMILION FLYCATHER": {
            "Common name": "Vermilion Flycatcher",
            "Scientific name": "Pyrocephalus rubinus",
            "Species": "P. rubinus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tyrannidae",
                "Genus": "Pyrocephalus"
            }
        },
        "VICTORIA CROWNED PIGEON": {
            "Common name": "Victoria Crowned Pigeon",
            "Scientific name": "Goura victoria",
            "Species": "G. victoria",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Columbidae",
                "Genus": "Goura"
            }
        },
        "VIOLET BACKED STARLING": {
            "Common name": "Violet-backed Starling",
            "Scientific name": "Cinnyricinclus leucogaster",
            "Species": "C. leucogaster",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Sturnidae",
                "Genus": "Cinnyricinclus"
            }
        },
        "VIOLET CUCKOO": {
            "Common name": "Violet Cuckoo",
            "Scientific name": "Chrysococcyx xanthorhynchus",
            "Species": "C. xanthorhynchus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cuculidae",
                "Genus": "Chrysococcyx"
            }
        },
        "VIOLET GREEN SWALLOW": {
            "Common name": "Violet-green Swallow",
            "Scientific name": "Tachycineta thalassina",
            "Species": "T. thalassina",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Hirundinidae",
                "Genus": "Tachycineta"
            }
        },
        "VIOLET TURACO": {
            "Common name": "Violet Turaco",
            "Scientific name": "Musophaga violacea",
            "Species": "M. violacea",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Musophagidae",
                "Genus": "Musophaga"
            }
        },
        "VISAYAN HORNBILL": {
            "Common name": "Visayan Hornbill",
            "Scientific name": "Penelopides panini",
            "Species": "P. panini",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Bucerotidae",
                "Genus": "Penelopides"
            }
        },
        "VULTURINE GUINEAFOWL": {
            "Common name": "Vulturine Guineafowl",
            "Scientific name": "Acryllium vulturinum",
            "Species": "A. vulturinum",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Numididae",
                "Genus": "Acryllium"
            }
        },
        "WALL CREAPER": {
            "Common name": "Wallcreeper",
            "Scientific name": "Tichodroma muraria",
            "Species": "T. muraria",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Tichodromidae",
                "Genus": "Tichodroma"
            }
        },
        "WATTLED CURASSOW": {
            "Common name": "Wattled Curassow",
            "Scientific name": "Crax globulosa",
            "Species": "C. globulosa",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Cracidae",
                "Genus": "Crax"
            }
        },
        "WATTLED LAPWING": {
            "Common name": "Wattled Lapwing",
            "Scientific name": "Vanellus senegallus",
            "Species": "V. senegallus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Charadriidae",
                "Genus": "Vanellus"
            }
        },
        "WHIMBREL": {
            "Common name": "Whimbrel",
            "Scientific name": "Numenius phaeopus",
            "Species": "N. phaeopus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Scolopacidae",
                "Genus": "Numenius"
            }
        },
        "WHITE BREASTED WATERHEN": {
            "Common name": "White-breasted Waterhen",
            "Scientific name": "Amaurornis phoenicurus",
            "Species": "A. phoenicurus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rallidae",
                "Genus": "Amaurornis"
            }
        },
        "WHITE BROWED CRAKE": {
            "Common name": "White-browed Crake",
            "Scientific name": "Poliolimnas cinereus",
            "Species": "P. cinereus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Rallidae",
                "Genus": "Poliolimnas"
            }
        },
        "WHITE CHEEKED TURACO": {
            "Common name": "White-cheeked Turaco",
            "Scientific name": "Tauraco leucotis",
            "Species": "T. leucotis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Musophagidae",
                "Genus": "Tauraco"
            }
        },
        "WHITE CRESTED HORNBILL": {
            "Common name": "White-crested Hornbill",
            "Scientific name": "Berenicornis comatus",
            "Species": "B. comatus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Bucerotidae",
                "Genus": "Berenicornis"
            }
        },
        "WHITE EARED HUMMINGBIRD": {
            "Common name": "White-eared Hummingbird",
            "Scientific name": "Basilinna leucotis",
            "Species": "B. leucotis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Trochilidae",
                "Genus": "Basilinna"
            }
        },
        "WHITE NECKED RAVEN": {
            "Common name": "White-necked Raven",
            "Scientific name": "Corvus albicollis",
            "Species": "C. albicollis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Corvidae",
                "Genus": "Corvus"
            }
        },
        "WHITE TAILED TROPIC": {
            "Common name": "White-tailed Tropicbird",
            "Scientific name": "Phaethon lepturus",
            "Species": "P. lepturus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phaethontidae",
                "Genus": "Phaethon"
            }
        },
        "WHITE THROATED BEE EATER": {
            "Common name": "White-throated Bee-eater",
            "Scientific name": "Merops albicollis",
            "Species": "M. albicollis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Meropidae",
                "Genus": "Merops"
            }
        },
        "WILD TURKEY": {
            "Common name": "Wild Turkey",
            "Scientific name": "Meleagris gallopavo",
            "Species": "M. gallopavo",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Meleagris"
            }
        },
        "WILLOW PTARMIGAN": {
            "Common name": "Willow Ptarmigan",
            "Scientific name": "Lagopus lagopus",
            "Species": "L. lagopus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Phasianidae",
                "Genus": "Lagopus"
            }
        },
        "WILSONS BIRD OF PARADISE": {
            "Common name": "Wilson's Bird of Paradise",
            "Scientific name": "Cicinnurus respublica",
            "Species": "C. respublica",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Paradisaeidae",
                "Genus": "Cicinnurus"
            }
        },
        "WOOD DUCK": {
            "Common name": "Wood Duck",
            "Scientific name": "Aix sponsa",
            "Species": "A. sponsa",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Anatidae",
                "Genus": "Aix"
            }
        },
        "WOOD THRUSH": {
            "Common name": "Wood Thrush",
            "Scientific name": "Hylocichla mustelina",
            "Species": "H. mustelina",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Turdidae",
                "Genus": "Hylocichla"
            }
        },
        "WOODLAND KINGFISHER": {
            "Common name": "Woodland Kingfisher",
            "Scientific name": "Halcyon senegalensis",
            "Species": "H. senegalensis",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Alcedinidae",
                "Genus": "Halcyon"
            }
        },
        "WRENTIT": {
            "Common name": "Wrentit",
            "Scientific name": "Chamaea fasciata",
            "Species": "C. fasciata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Timaliidae",
                "Genus": "Chamaea"
            }
        },
        "YELLOW BELLIED FLOWERPECKER": {
            "Common name": "Yellow-bellied Flowerpecker",
            "Scientific name": "Dicaeum melanoxanthum",
            "Species": "D. melanoxanthum",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Dicaeidae",
                "Genus": "Dicaeum"
            }
        },
        "YELLOW BREASTED CHAT": {
            "Common name": "Yellow-breasted Chat",
            "Scientific name": "Icteria virens",
            "Species": "I. virens",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Parulidae",
                "Genus": "Icteria"
            }
        },
        "YELLOW CACIQUE": {
            "Common name": "Yellow Cacique",
            "Scientific name": "Cacicus cela",
            "Species": "C. cela",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Icteridae",
                "Genus": "Cacicus"
            }
        },
        "YELLOW HEADED BLACKBIRD": {
            "Common name": "Yellow-headed Blackbird",
            "Scientific name": "Xanthocephalus xanthocephalus",
            "Species": "X. xanthocephalus",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Icteridae",
                "Genus": "Xanthocephalus"
            }
        },
        "ZEBRA DOVE": {
            "Common name": "Zebra Dove",
            "Scientific name": "Geopelia striata",
            "Species": "G. striata",
            "Scientific Classification": {
                "Kingdom": "Animalia",
                "Phylum": "Chordata",
                "Subphylum": "Vertebrata",
                "Class": "Aves",
                "Family": "Columbidae",
                "Genus": "Geopelia"
            }
        },
        "Bird not found in database": {
            "Common name": "N/A",
            "Scientific name": "N/A",
            "Species": "N/A",
            "Scientific Classification": {
                "Kingdom": "N/A",
                "Phylum": "N/A",
                "Subphylum": "N/A",
                "Class": "N/A",
                "Order": "N/A",
                "Family": "N/A",
                "Genus": "N/A"
            }
        }
    }
    
    return ornithological_info.get(bird_name, ornithological_info["Bird not found in database"])


def run():
    img1 = Image.open('D:\Birds_image_classification\static\logo.png')
    img1 = img1.resize((270,250)) 
    st.image(img1, use_column_width=False) 
    st.title("Eagle’s Eye - Bird Species Prediction")
    st.markdown('''
        With Eagle's Eye, you can upload an image of a bird and get its species predicted along with ornithological information.
        Let's explore the avian world together!
    ''')
    img_file = st.file_uploader("Choose an image of bird", type=["jpg", "png"]) 
    if img_file is not None: 
        st.image(img_file, use_column_width=False) 
        save_image_path = 'uploads/'+img_file.name 
        with open(save_image_path, "wb") as f: 
            f.write(img_file.getbuffer()) 
        if st.button("Predict"): 
            predicted_class, accuracy_percentage, ornithological_info = processed_img(save_image_path)
            if predicted_class is not None:
                st.success("Predicted Bird is: " + predicted_class)             
                st.info(f"Accuracy: {accuracy_percentage:.2f}%")
                col1, col2 = st.columns(2)
                
                with col1:
                    st.subheader("Ornithological Information")
                    st.write("Common name:", ornithological_info.get('Common name', 'N/A'))
                    st.write("Scientific name:", ornithological_info.get('Scientific name', 'N/A'))
                    st.write("Species:", ornithological_info.get('Species', 'N/A'))

                with col2:
                    st.subheader("Scientific Classification")
                    st.write("Kingdom:", ornithological_info.get('Scientific Classification', {}).get('Kingdom', 'N/A'))
                    st.write("Phylum:", ornithological_info.get('Scientific Classification', {}).get('Phylum', 'N/A'))
                    st.write("Subphylum:", ornithological_info.get('Scientific Classification', {}).get('Subphylum', 'N/A'))
                    st.write("Class:", ornithological_info.get('Scientific Classification', {}).get('Class', 'N/A'))
                    st.write("Family:", ornithological_info.get('Scientific Classification', {}).get('Family', 'N/A'))
                    st.write("Genus:", ornithological_info.get('Scientific Classification', {}).get('Genus', 'N/A'))
                
                # Generate description
                description_result = palm.generate_text(prompt="short description about " + predicted_class + " bird in 200 words") 
                description = description_result.result
                st.success(description)

                from bmap import bmap
                bmap(predicted_class)
                path_to_html = "static\\birdmap.html"
                with open(path_to_html, 'r') as f:
                    html_content = f.read()
                components.html(html_content, height=400)


                # Speak the prediction
                engine.say(f"Predicted Bird is: {predicted_class}. Accuracy: {accuracy_percentage:.2f}%. Description: {description}")
                engine.runAndWait()     


    else:
        st.info("Please upload an image.")
run()