import pygame

screen = pygame.display.set_mode((1800, 900))

WHITE      = (255, 255, 255)
BLACK      = (0  , 0  , 0  )
RED        = (255, 0  , 0  )
GREEN      = (0  , 255, 0  )
BLUE       = (0  , 0  , 255)
PURPLE     = (128, 0  , 128)
ORANGE     = (255, 165, 0  ) 
YELLOW     = (255, 255, 0  )
BROWN      = (149, 95 , 32 )
GOLDEN     = (239, 184, 16 )
DARK_GREEN = (45 , 87 , 44 )
DARK_GRAY  = (51 , 47 , 44 )
DARK_RED   = (150, 0  , 0  )
GRAY       = (130, 130, 130)

casillas = {
    "0":  {"num":0,  "color":GREEN},
    "1":  {"num":1,  "color":RED  },
    "2":  {"num":2,  "color":BLACK},
    "3":  {"num":3,  "color":RED  },
    "4":  {"num":4,  "color":BLACK},
    "5":  {"num":5,  "color":RED  },
    "6":  {"num":6,  "color":BLACK},
    "7":  {"num":7,  "color":RED  },
    "8":  {"num":8,  "color":BLACK},
    "9":  {"num":9,  "color":RED  },
    "10": {"num":10, "color":BLACK},
    "11": {"num":11, "color":BLACK},
    "12": {"num":12, "color":RED  },
    "13": {"num":13, "color":BLACK},
    "14": {"num":14, "color":RED  },
    "15": {"num":15, "color":BLACK},
    "16": {"num":16, "color":RED  },
    "17": {"num":17, "color":BLACK},
    "18": {"num":18, "color":RED  },
    "19": {"num":19, "color":RED  },
    "20": {"num":20, "color":BLACK},
    "21": {"num":21, "color":RED  },
    "22": {"num":22, "color":BLACK},
    "23": {"num":23, "color":RED  },
    "24": {"num":24, "color":BLACK},
    "25": {"num":25, "color":RED  },
    "26": {"num":26, "color":BLACK},
    "27": {"num":27, "color":RED  },
    "28": {"num":28, "color":BLACK},
    "29": {"num":29, "color":BLACK},
    "30": {"num":30, "color":RED  },
    "31": {"num":31, "color":BLACK},
    "32": {"num":32, "color":RED  },
    "33": {"num":33, "color":BLACK},
    "34": {"num":34, "color":RED  },
    "35": {"num":35, "color":BLACK},
    "36": {"num":36, "color":RED  }
}

CENTRO = (300,300)
RADIO = 210
orden_ruleta = [
    "0" , "32", "15", "19", "4", "21" , 
    "2" , "25", "17", "34", "6", "27" ,
    "13", "36", "11", "30", "8", "23" , 
    "10", "5" , "24", "16", "33", "1" , 
    "20", "14", "31", "9" , "22", "18",
    "29", "7" , "28", "12", "35", "3" , 
    "26"
]

NUMEROS = len(orden_ruleta)