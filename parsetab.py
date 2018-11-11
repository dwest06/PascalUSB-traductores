
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'rightTkItoirightTkPrintlnTkPrintrightTkReadrightTkBeginleftTkAndleftTkOrrightTkNotnonassocTkEqualnonassocTkGreaterTkLessTkGeqTkLeqleftTkPlusTkMinusleftTkMultTkDivTkModrightUMINUSrightTkProgramTkAnd TkArrow TkAs TkAsig TkBegin TkBool TkCap TkCase TkCloseBra TkClosePar TkComma TkComment TkDeclare TkDiv TkDo TkElse TkEnd TkEqual TkExists TkFalse TkFor TkForall TkGeq TkGreater TkId TkIf TkIn TkInt TkInter TkItoi TkLen TkLeq TkLess TkMax TkMin TkMinus TkMod TkMult TkNEqual TkNot TkNum TkOf TkOpenBra TkOpenPar TkOr TkPipe TkPlus TkPoint TkPost TkPrint TkPrintln TkProgram TkRead TkSemicolon TkSoForth TkString TkThen TkTrue TkTwoPoints TkWhile\n    PROGRAMA : TkProgram INSTRUCCION\n    \n    BLOQUE : TkBegin VACIO TkEnd  \n           | TkBegin INSTRUCCION TkEnd VACIO\n           | TkBegin TkDeclare DECL_VAR INSTRUCCION TkEnd  \n           | TkBegin TkDeclare DECL_VAR INSTRUCCION TkEnd VACIO \n    \n    INSTRUCCION : POST\n                | ASIGNACION \n                | ENTRADA \n                | SALIDA \n                | CONVERTIR\n                | CONDICIONAL_IF\n                | CONDICIONAL_CASE\n                | ITERACION_FOR\n                | ITERACION_WHILE\n                | BLOQUE\n                | INSTRUCCION TkSemicolon INSTRUCCION\n    \n    IDENTIFICADOR : TkId\n    \n    ASIGNACION : EXPRESION TkAsig EXPRESION\n    \n    ENTRADA : TkRead IDENTIFICADOR\n    \n    SALIDA : TkPrint LISTA_VAR\n           | TkPrintln LISTA_VAR\n           | TkPrint CADENA\n           | TkPrintln CADENA\n    \n    CADENA : TkString\n    \n    CONDICIONAL_IF : TkIf EXP_BOOL TkThen INSTRUCCION TkElse INSTRUCCION\n              | TkIf EXP_BOOL TkThen INSTRUCCION\n    \n    CONDICIONAL_CASE : TkCase EXPRESION TkOf LISTA_CASE TkEnd\n                   \n    \n    LISTA_CASE : EXPRESION TkArrow INSTRUCCION\n               | EXPRESION TkArrow INSTRUCCION LISTA_CASE\n    \n    ITERACION_FOR : TkFor IDENTIFICADOR TkIn EXPRESION TkDo INSTRUCCION\n    \n    ITERACION_WHILE : TkWhile EXP_BOOL TkDo INSTRUCCION\n    \n    DECL_VAR : LISTA_VAR TkAs LISTA_TIPO \n    \n    LISTA_VAR : IDENTIFICADOR\n              | IDENTIFICADOR TkComma LISTA_VAR\n    \n    LISTA_TIPO : DATO\n              | DATO TkComma LISTA_TIPO\n    \n    DATO : TkInt\n         | TkBool\n         | TkInter\n    \n    EXPRESION : TkNum\n              | IDENTIFICADOR\n              | EXP_ENTEROS\n              | EXP_INTERVALOS\n              | EXP_BOOL\n              | TkOpenPar EXPRESION TkClosePar\n    \n    EXP_ENTEROS : EXPRESION TkMod EXPRESION\n                | EXPRESION TkMult EXPRESION\n                | EXPRESION TkDiv EXPRESION\n                | EXPRESION TkPlus EXPRESION\n                | EXPRESION TkMinus EXPRESION %prec UMINUS\n    \n    EXP_INTERVALOS : EXPRESION TkSoForth EXPRESION\n                  | EXPRESION TkCap EXPRESION\n    \n    EXP_BOOL : TkTrue\n             | TkFalse\n             | TkNot EXP_BOOL\n             | EXPRESION TkAnd EXPRESION\n             | EXPRESION TkOr EXPRESION\n             | EXPRESION TkIn EXPRESION\n             | EXPRESION TkEqual EXPRESION\n             | EXPRESION TkNEqual EXPRESION\n             | EXPRESION TkGreater EXPRESION\n             | EXPRESION TkGeq EXPRESION\n             | EXPRESION TkLess EXPRESION\n             | EXPRESION TkLeq EXPRESION\n    \n    CONVERTIR : TkItoi TkOpenPar IDENTIFICADOR TkClosePar\n              | TkLen TkOpenPar IDENTIFICADOR TkClosePar\n              | TkMax TkOpenPar IDENTIFICADOR TkClosePar\n              | TkMin TkOpenPar IDENTIFICADOR TkClosePar\n    \n    POST : TkOpenBra TkPost TkTwoPoints EXP_CUANTIFICADOR TkCloseBra\n    \n    EXP_CUANTIFICADOR : TkOpenPar TkForall IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_CUANTIFICADOR TkClosePar\n                      | TkOpenPar TkForall IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_BOOL TkClosePar\n    \n    EXP_CUANTIFICADOR : TkOpenPar TkExists IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_CUANTIFICADOR TkClosePar\n                      | TkOpenPar TkExists IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_BOOL TkClosePar\n    \n    VACIO : \n    '
    
_lr_action_items = {'TkProgram':([0,],[2,]),'$end':([1,3,4,5,6,7,8,9,10,11,12,13,17,26,31,32,33,34,35,36,57,58,59,60,61,62,63,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,107,108,113,114,115,116,117,118,122,123,126,131,133,141,143,144,],[0,-1,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-41,-44,-40,-42,-43,-17,-53,-54,-19,-20,-22,-33,-24,-21,-23,-55,-16,-18,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,-2,-74,-34,-65,-66,-67,-68,-26,-31,-3,-69,-27,-4,-25,-30,-5,]),'TkOpenBra':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[14,14,14,14,14,14,14,14,14,-32,-35,-37,-38,-39,-36,]),'TkRead':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[16,16,16,16,16,16,16,16,16,-32,-35,-37,-38,-39,-36,]),'TkPrint':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[18,18,18,18,18,18,18,18,18,-32,-35,-37,-38,-39,-36,]),'TkPrintln':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[19,19,19,19,19,19,19,19,19,-32,-35,-37,-38,-39,-36,]),'TkItoi':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[20,20,20,20,20,20,20,20,20,-32,-35,-37,-38,-39,-36,]),'TkLen':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[22,22,22,22,22,22,22,22,22,-32,-35,-37,-38,-39,-36,]),'TkMax':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[23,23,23,23,23,23,23,23,23,-32,-35,-37,-38,-39,-36,]),'TkMin':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[24,24,24,24,24,24,24,24,24,-32,-35,-37,-38,-39,-36,]),'TkIf':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[25,25,25,25,25,25,25,25,25,-32,-35,-37,-38,-39,-36,]),'TkCase':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[27,27,27,27,27,27,27,27,27,-32,-35,-37,-38,-39,-36,]),'TkFor':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[28,28,28,28,28,28,28,28,28,-32,-35,-37,-38,-39,-36,]),'TkWhile':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[29,29,29,29,29,29,29,29,29,-32,-35,-37,-38,-39,-36,]),'TkBegin':([2,30,38,103,106,109,129,130,132,134,135,136,137,138,149,],[30,30,30,30,30,30,30,30,30,-32,-35,-37,-38,-39,-36,]),'TkNum':([2,4,5,6,7,8,9,10,11,12,13,17,21,25,26,27,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,103,104,105,106,107,108,109,113,114,115,116,117,118,122,123,126,129,130,131,132,133,134,135,136,137,138,141,142,143,144,149,156,157,158,],[31,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-41,31,31,-44,31,31,31,-40,-42,-43,-17,-53,-54,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,31,-19,-20,-22,-33,-24,-21,-23,-55,-16,-18,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,31,31,31,31,-2,-74,31,-34,-65,-66,-67,-68,-26,-31,-3,-69,31,31,-27,31,-4,-32,-35,-37,-38,-39,-25,31,-30,-5,-36,31,31,31,]),'TkOpenPar':([2,4,5,6,7,8,9,10,11,12,13,17,20,21,22,23,24,25,26,27,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,77,78,79,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,103,104,105,106,107,108,109,113,114,115,116,117,118,122,123,126,129,130,131,132,133,134,135,136,137,138,141,142,143,144,149,156,157,158,],[21,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-41,64,21,66,67,68,21,-44,21,21,21,-40,-42,-43,-17,-53,-54,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,21,-19,-20,-22,-33,-24,-21,-23,-55,-16,112,-18,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,21,21,21,21,-2,-74,21,-34,-65,-66,-67,-68,-26,-31,-3,-69,21,21,-27,21,-4,-32,-35,-37,-38,-39,-25,21,-30,-5,-36,158,158,21,]),'TkId':([2,4,5,6,7,8,9,10,11,12,13,16,17,18,19,21,25,26,27,28,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,64,66,67,68,76,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,97,99,103,104,105,106,107,108,109,113,114,115,116,117,118,122,123,126,127,128,129,130,131,132,133,134,135,136,137,138,141,142,143,144,146,147,149,152,153,156,157,158,],[34,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,34,-41,34,34,34,34,-44,34,34,34,34,-40,-42,-43,-17,-53,-54,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,34,-19,-20,-22,-33,-24,-21,-23,34,34,34,34,34,-55,-16,-18,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,34,-45,34,34,34,34,-2,-74,34,-34,-65,-66,-67,-68,-26,-31,-3,-69,34,34,34,34,-27,34,-4,-32,-35,-37,-38,-39,-25,34,-30,-5,34,34,-36,34,34,34,34,34,]),'TkTrue':([2,4,5,6,7,8,9,10,11,12,13,17,21,25,26,27,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,103,104,105,106,107,108,109,113,114,115,116,117,118,122,123,126,129,130,131,132,133,134,135,136,137,138,141,142,143,144,149,156,157,158,],[35,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-41,35,35,-44,35,35,35,-40,-42,-43,-17,-53,-54,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,35,-19,-20,-22,-33,-24,-21,-23,-55,-16,-18,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,35,35,35,35,-2,-74,35,-34,-65,-66,-67,-68,-26,-31,-3,-69,35,35,-27,35,-4,-32,-35,-37,-38,-39,-25,35,-30,-5,-36,35,35,35,]),'TkFalse':([2,4,5,6,7,8,9,10,11,12,13,17,21,25,26,27,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,103,104,105,106,107,108,109,113,114,115,116,117,118,122,123,126,129,130,131,132,133,134,135,136,137,138,141,142,143,144,149,156,157,158,],[36,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-41,36,36,-44,36,36,36,-40,-42,-43,-17,-53,-54,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,36,-19,-20,-22,-33,-24,-21,-23,-55,-16,-18,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,36,36,36,36,-2,-74,36,-34,-65,-66,-67,-68,-26,-31,-3,-69,36,36,-27,36,-4,-32,-35,-37,-38,-39,-25,36,-30,-5,-36,36,36,36,]),'TkNot':([2,4,5,6,7,8,9,10,11,12,13,17,21,25,26,27,29,30,31,32,33,34,35,36,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,57,58,59,60,61,62,63,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,103,104,105,106,107,108,109,113,114,115,116,117,118,122,123,126,129,130,131,132,133,134,135,136,137,138,141,142,143,144,149,156,157,158,],[37,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-41,37,37,-44,37,37,37,-40,-42,-43,-17,-53,-54,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,37,-19,-20,-22,-33,-24,-21,-23,-55,-16,-18,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,37,37,37,37,-2,-74,37,-34,-65,-66,-67,-68,-26,-31,-3,-69,37,37,-27,37,-4,-32,-35,-37,-38,-39,-25,37,-30,-5,-36,37,37,37,]),'TkSemicolon':([3,4,5,6,7,8,9,10,11,12,13,17,26,31,32,33,34,35,36,57,58,59,60,61,62,63,75,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,107,108,113,114,115,116,117,118,122,123,124,126,131,133,141,142,143,144,],[38,-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-41,-44,-40,-42,-43,-17,-53,-54,-19,-20,-22,-33,-24,-21,-23,38,-55,38,-18,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,-2,-74,-34,-65,-66,-67,-68,38,38,-3,38,-69,-27,-4,38,38,38,-5,]),'TkEnd':([4,5,6,7,8,9,10,11,12,13,17,26,30,31,32,33,34,35,36,57,58,59,60,61,62,63,74,75,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,107,108,113,114,115,116,117,118,120,122,123,124,126,131,133,141,142,143,144,148,],[-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-41,-44,-74,-40,-42,-43,-17,-53,-54,-19,-20,-22,-33,-24,-21,-23,107,108,-55,-16,-18,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,-2,-74,-34,-65,-66,-67,-68,-26,131,-31,-3,133,-69,-27,-4,-25,-28,-30,-5,-29,]),'TkElse':([4,5,6,7,8,9,10,11,12,13,17,26,31,32,33,34,35,36,57,58,59,60,61,62,63,77,78,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,107,108,113,114,115,116,117,118,122,123,126,131,133,141,143,144,],[-6,-7,-8,-9,-10,-11,-12,-13,-14,-15,-41,-44,-40,-42,-43,-17,-53,-54,-19,-20,-22,-33,-24,-21,-23,-55,-16,-18,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,-2,-74,-34,-65,-66,-67,-68,129,-31,-3,-69,-27,-4,-25,-30,-5,]),'TkPost':([14,],[39,]),'TkAsig':([15,17,26,31,32,33,34,35,36,77,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,],[40,-41,-44,-40,-42,-43,-17,-53,-54,-55,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,]),'TkMod':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[41,-41,-44,-40,-42,-43,-17,-53,-54,41,-44,41,41,-44,-44,41,-46,-47,-48,41,-50,41,41,41,41,41,41,41,41,41,41,41,-45,41,41,-44,-44,]),'TkMult':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[42,-41,-44,-40,-42,-43,-17,-53,-54,42,-44,42,42,-44,-44,42,-46,-47,-48,42,-50,42,42,42,42,42,42,42,42,42,42,42,-45,42,42,-44,-44,]),'TkDiv':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[43,-41,-44,-40,-42,-43,-17,-53,-54,43,-44,43,43,-44,-44,43,-46,-47,-48,43,-50,43,43,43,43,43,43,43,43,43,43,43,-45,43,43,-44,-44,]),'TkPlus':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[44,-41,-44,-40,-42,-43,-17,-53,-54,44,-44,44,44,-44,-44,44,-46,-47,-48,-49,-50,44,44,44,44,44,44,44,44,44,44,44,-45,44,44,-44,-44,]),'TkMinus':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[45,-41,-44,-40,-42,-43,-17,-53,-54,45,-44,45,45,-44,-44,45,-46,-47,-48,-49,-50,45,45,45,45,45,45,45,45,45,45,45,-45,45,45,-44,-44,]),'TkSoForth':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[46,-41,-44,-40,-42,-43,-17,-53,-54,46,-44,46,46,-44,-44,46,-46,-47,-48,-49,-50,46,46,-56,-57,46,-59,46,-61,-62,-63,-64,-45,46,46,-44,-44,]),'TkCap':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[47,-41,-44,-40,-42,-43,-17,-53,-54,47,-44,47,47,-44,-44,47,-46,-47,-48,-49,-50,47,47,-56,-57,47,-59,47,-61,-62,-63,-64,-45,47,47,-44,-44,]),'TkAnd':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[48,-41,-44,-40,-42,-43,-17,-53,-54,48,-44,48,48,-44,-44,48,-46,-47,-48,-49,-50,48,48,-56,-57,48,-59,48,-61,-62,-63,-64,-45,48,48,-44,-44,]),'TkOr':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[49,-41,-44,-40,-42,-43,-17,-53,-54,49,-44,49,49,-44,-44,49,-46,-47,-48,-49,-50,49,49,49,-57,49,-59,49,-61,-62,-63,-64,-45,49,49,-44,-44,]),'TkIn':([15,17,26,31,32,33,34,35,36,65,69,70,71,72,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,150,151,160,162,],[50,-41,-44,-40,-42,-43,-17,-53,-54,50,-44,50,50,105,-44,-44,50,-46,-47,-48,-49,-50,50,50,-56,-57,50,-59,50,-61,-62,-63,-64,-45,50,50,152,153,-44,-44,]),'TkEqual':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[51,-41,-44,-40,-42,-43,-17,-53,-54,51,-44,51,51,-44,-44,51,-46,-47,-48,-49,-50,51,51,51,51,51,None,51,-61,-62,-63,-64,-45,51,51,-44,-44,]),'TkNEqual':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[52,-41,-44,-40,-42,-43,-17,-53,-54,52,-44,52,52,-44,-44,52,-46,-47,-48,-49,-50,52,52,-56,-57,52,-59,52,-61,-62,-63,-64,-45,52,52,-44,-44,]),'TkGreater':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[53,-41,-44,-40,-42,-43,-17,-53,-54,53,-44,53,53,-44,-44,53,-46,-47,-48,-49,-50,53,53,53,53,53,53,53,None,None,None,None,-45,53,53,-44,-44,]),'TkGeq':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[54,-41,-44,-40,-42,-43,-17,-53,-54,54,-44,54,54,-44,-44,54,-46,-47,-48,-49,-50,54,54,54,54,54,54,54,None,None,None,None,-45,54,54,-44,-44,]),'TkLess':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[55,-41,-44,-40,-42,-43,-17,-53,-54,55,-44,55,55,-44,-44,55,-46,-47,-48,-49,-50,55,55,55,55,55,55,55,None,None,None,None,-45,55,55,-44,-44,]),'TkLeq':([15,17,26,31,32,33,34,35,36,65,69,70,71,73,77,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,121,160,162,],[56,-41,-44,-40,-42,-43,-17,-53,-54,56,-44,56,56,-44,-44,56,-46,-47,-48,-49,-50,56,56,56,56,56,56,56,None,None,None,None,-45,56,56,-44,-44,]),'TkClosePar':([17,26,31,32,33,34,35,36,65,77,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,98,99,100,101,102,159,160,161,162,163,164,165,166,],[-41,-44,-40,-42,-43,-17,-53,-54,99,-55,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,114,-45,115,116,117,163,164,165,166,-70,-71,-72,-73,]),'TkOf':([17,26,31,32,33,34,35,36,71,77,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,],[-41,-44,-40,-42,-43,-17,-53,-54,104,-55,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,]),'TkThen':([17,26,31,32,33,34,35,36,69,77,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,],[-41,-44,-40,-42,-43,-17,-53,-54,103,-55,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,]),'TkDo':([17,26,31,32,33,34,35,36,73,77,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,121,],[-41,-44,-40,-42,-43,-17,-53,-54,106,-55,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,132,]),'TkArrow':([17,26,31,32,33,34,35,36,77,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,99,119,],[-41,-44,-40,-42,-43,-17,-53,-54,-55,-46,-47,-48,-49,-50,-51,-52,-56,-57,-58,-59,-60,-61,-62,-63,-64,-45,130,]),'TkString':([18,19,],[61,61,]),'TkDeclare':([30,],[76,]),'TkComma':([34,60,135,136,137,138,],[-17,97,145,-37,-38,-39,]),'TkAs':([34,60,110,113,],[-17,-33,125,-34,]),'TkPipe':([34,139,140,],[-17,146,147,]),'TkTwoPoints':([34,39,154,155,],[-17,79,156,157,]),'TkCloseBra':([111,163,164,165,166,],[126,-70,-71,-72,-73,]),'TkForall':([112,158,],[127,127,]),'TkExists':([112,158,],[128,128,]),'TkInt':([125,145,],[136,136,]),'TkBool':([125,145,],[137,137,]),'TkInter':([125,145,],[138,138,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'PROGRAMA':([0,],[1,]),'INSTRUCCION':([2,30,38,103,106,109,129,130,132,],[3,75,78,118,122,124,141,142,143,]),'POST':([2,30,38,103,106,109,129,130,132,],[4,4,4,4,4,4,4,4,4,]),'ASIGNACION':([2,30,38,103,106,109,129,130,132,],[5,5,5,5,5,5,5,5,5,]),'ENTRADA':([2,30,38,103,106,109,129,130,132,],[6,6,6,6,6,6,6,6,6,]),'SALIDA':([2,30,38,103,106,109,129,130,132,],[7,7,7,7,7,7,7,7,7,]),'CONVERTIR':([2,30,38,103,106,109,129,130,132,],[8,8,8,8,8,8,8,8,8,]),'CONDICIONAL_IF':([2,30,38,103,106,109,129,130,132,],[9,9,9,9,9,9,9,9,9,]),'CONDICIONAL_CASE':([2,30,38,103,106,109,129,130,132,],[10,10,10,10,10,10,10,10,10,]),'ITERACION_FOR':([2,30,38,103,106,109,129,130,132,],[11,11,11,11,11,11,11,11,11,]),'ITERACION_WHILE':([2,30,38,103,106,109,129,130,132,],[12,12,12,12,12,12,12,12,12,]),'BLOQUE':([2,30,38,103,106,109,129,130,132,],[13,13,13,13,13,13,13,13,13,]),'EXPRESION':([2,21,25,27,29,30,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,103,104,105,106,109,129,130,132,142,156,157,158,],[15,65,70,71,70,15,70,15,80,81,82,83,84,85,86,87,88,89,90,91,92,93,94,95,96,15,119,121,15,15,15,15,15,119,70,70,65,]),'IDENTIFICADOR':([2,16,18,19,21,25,27,28,29,30,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,64,66,67,68,76,97,103,104,105,106,109,127,128,129,130,132,142,146,147,152,153,156,157,158,],[17,57,60,60,17,17,17,72,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,17,98,100,101,102,60,60,17,17,17,17,17,139,140,17,17,17,17,150,151,154,155,17,17,17,]),'EXP_BOOL':([2,21,25,27,29,30,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,103,104,105,106,109,129,130,132,142,156,157,158,],[26,26,69,26,73,26,77,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,26,160,162,26,]),'EXP_ENTEROS':([2,21,25,27,29,30,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,103,104,105,106,109,129,130,132,142,156,157,158,],[32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,32,]),'EXP_INTERVALOS':([2,21,25,27,29,30,37,38,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54,55,56,103,104,105,106,109,129,130,132,142,156,157,158,],[33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,33,]),'LISTA_VAR':([18,19,76,97,],[58,62,110,113,]),'CADENA':([18,19,],[59,63,]),'VACIO':([30,108,133,],[74,123,144,]),'DECL_VAR':([76,],[109,]),'EXP_CUANTIFICADOR':([79,156,157,],[111,159,161,]),'LISTA_CASE':([104,142,],[120,148,]),'LISTA_TIPO':([125,145,],[134,149,]),'DATO':([125,145,],[135,135,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> PROGRAMA","S'",1,None,None,None),
  ('PROGRAMA -> TkProgram INSTRUCCION','PROGRAMA',2,'p_programa','parser.py',36),
  ('BLOQUE -> TkBegin VACIO TkEnd','BLOQUE',3,'p_bloque','parser.py',44),
  ('BLOQUE -> TkBegin INSTRUCCION TkEnd VACIO','BLOQUE',4,'p_bloque','parser.py',45),
  ('BLOQUE -> TkBegin TkDeclare DECL_VAR INSTRUCCION TkEnd','BLOQUE',5,'p_bloque','parser.py',46),
  ('BLOQUE -> TkBegin TkDeclare DECL_VAR INSTRUCCION TkEnd VACIO','BLOQUE',6,'p_bloque','parser.py',47),
  ('INSTRUCCION -> POST','INSTRUCCION',1,'p_instruccion','parser.py',57),
  ('INSTRUCCION -> ASIGNACION','INSTRUCCION',1,'p_instruccion','parser.py',58),
  ('INSTRUCCION -> ENTRADA','INSTRUCCION',1,'p_instruccion','parser.py',59),
  ('INSTRUCCION -> SALIDA','INSTRUCCION',1,'p_instruccion','parser.py',60),
  ('INSTRUCCION -> CONVERTIR','INSTRUCCION',1,'p_instruccion','parser.py',61),
  ('INSTRUCCION -> CONDICIONAL_IF','INSTRUCCION',1,'p_instruccion','parser.py',62),
  ('INSTRUCCION -> CONDICIONAL_CASE','INSTRUCCION',1,'p_instruccion','parser.py',63),
  ('INSTRUCCION -> ITERACION_FOR','INSTRUCCION',1,'p_instruccion','parser.py',64),
  ('INSTRUCCION -> ITERACION_WHILE','INSTRUCCION',1,'p_instruccion','parser.py',65),
  ('INSTRUCCION -> BLOQUE','INSTRUCCION',1,'p_instruccion','parser.py',66),
  ('INSTRUCCION -> INSTRUCCION TkSemicolon INSTRUCCION','INSTRUCCION',3,'p_instruccion','parser.py',67),
  ('IDENTIFICADOR -> TkId','IDENTIFICADOR',1,'p_identificador','parser.py',78),
  ('ASIGNACION -> EXPRESION TkAsig EXPRESION','ASIGNACION',3,'p_asignacion','parser.py',86),
  ('ENTRADA -> TkRead IDENTIFICADOR','ENTRADA',2,'p_entrada','parser.py',94),
  ('SALIDA -> TkPrint LISTA_VAR','SALIDA',2,'p_salida','parser.py',102),
  ('SALIDA -> TkPrintln LISTA_VAR','SALIDA',2,'p_salida','parser.py',103),
  ('SALIDA -> TkPrint CADENA','SALIDA',2,'p_salida','parser.py',104),
  ('SALIDA -> TkPrintln CADENA','SALIDA',2,'p_salida','parser.py',105),
  ('CADENA -> TkString','CADENA',1,'p_cadena','parser.py',113),
  ('CONDICIONAL_IF -> TkIf EXP_BOOL TkThen INSTRUCCION TkElse INSTRUCCION','CONDICIONAL_IF',6,'p_condicional_if','parser.py',121),
  ('CONDICIONAL_IF -> TkIf EXP_BOOL TkThen INSTRUCCION','CONDICIONAL_IF',4,'p_condicional_if','parser.py',122),
  ('CONDICIONAL_CASE -> TkCase EXPRESION TkOf LISTA_CASE TkEnd','CONDICIONAL_CASE',5,'p_condicional_case','parser.py',132),
  ('LISTA_CASE -> EXPRESION TkArrow INSTRUCCION','LISTA_CASE',3,'p_lista_case','parser.py',141),
  ('LISTA_CASE -> EXPRESION TkArrow INSTRUCCION LISTA_CASE','LISTA_CASE',4,'p_lista_case','parser.py',142),
  ('ITERACION_FOR -> TkFor IDENTIFICADOR TkIn EXPRESION TkDo INSTRUCCION','ITERACION_FOR',6,'p_iteracion_for','parser.py',152),
  ('ITERACION_WHILE -> TkWhile EXP_BOOL TkDo INSTRUCCION','ITERACION_WHILE',4,'p_iteracion_while','parser.py',159),
  ('DECL_VAR -> LISTA_VAR TkAs LISTA_TIPO','DECL_VAR',3,'p_declaracion_var','parser.py',166),
  ('LISTA_VAR -> IDENTIFICADOR','LISTA_VAR',1,'p_lista_var','parser.py',173),
  ('LISTA_VAR -> IDENTIFICADOR TkComma LISTA_VAR','LISTA_VAR',3,'p_lista_var','parser.py',174),
  ('LISTA_TIPO -> DATO','LISTA_TIPO',1,'p_lista_tipo','parser.py',185),
  ('LISTA_TIPO -> DATO TkComma LISTA_TIPO','LISTA_TIPO',3,'p_lista_tipo','parser.py',186),
  ('DATO -> TkInt','DATO',1,'p_dato','parser.py',196),
  ('DATO -> TkBool','DATO',1,'p_dato','parser.py',197),
  ('DATO -> TkInter','DATO',1,'p_dato','parser.py',198),
  ('EXPRESION -> TkNum','EXPRESION',1,'p_expresion','parser.py',205),
  ('EXPRESION -> IDENTIFICADOR','EXPRESION',1,'p_expresion','parser.py',206),
  ('EXPRESION -> EXP_ENTEROS','EXPRESION',1,'p_expresion','parser.py',207),
  ('EXPRESION -> EXP_INTERVALOS','EXPRESION',1,'p_expresion','parser.py',208),
  ('EXPRESION -> EXP_BOOL','EXPRESION',1,'p_expresion','parser.py',209),
  ('EXPRESION -> TkOpenPar EXPRESION TkClosePar','EXPRESION',3,'p_expresion','parser.py',210),
  ('EXP_ENTEROS -> EXPRESION TkMod EXPRESION','EXP_ENTEROS',3,'p_exp_enteros','parser.py',220),
  ('EXP_ENTEROS -> EXPRESION TkMult EXPRESION','EXP_ENTEROS',3,'p_exp_enteros','parser.py',221),
  ('EXP_ENTEROS -> EXPRESION TkDiv EXPRESION','EXP_ENTEROS',3,'p_exp_enteros','parser.py',222),
  ('EXP_ENTEROS -> EXPRESION TkPlus EXPRESION','EXP_ENTEROS',3,'p_exp_enteros','parser.py',223),
  ('EXP_ENTEROS -> EXPRESION TkMinus EXPRESION','EXP_ENTEROS',3,'p_exp_enteros','parser.py',224),
  ('EXP_INTERVALOS -> EXPRESION TkSoForth EXPRESION','EXP_INTERVALOS',3,'p_exp_intervalo','parser.py',244),
  ('EXP_INTERVALOS -> EXPRESION TkCap EXPRESION','EXP_INTERVALOS',3,'p_exp_intervalo','parser.py',245),
  ('EXP_BOOL -> TkTrue','EXP_BOOL',1,'p_exp_bool','parser.py',252),
  ('EXP_BOOL -> TkFalse','EXP_BOOL',1,'p_exp_bool','parser.py',253),
  ('EXP_BOOL -> TkNot EXP_BOOL','EXP_BOOL',2,'p_exp_bool','parser.py',254),
  ('EXP_BOOL -> EXPRESION TkAnd EXPRESION','EXP_BOOL',3,'p_exp_bool','parser.py',255),
  ('EXP_BOOL -> EXPRESION TkOr EXPRESION','EXP_BOOL',3,'p_exp_bool','parser.py',256),
  ('EXP_BOOL -> EXPRESION TkIn EXPRESION','EXP_BOOL',3,'p_exp_bool','parser.py',257),
  ('EXP_BOOL -> EXPRESION TkEqual EXPRESION','EXP_BOOL',3,'p_exp_bool','parser.py',258),
  ('EXP_BOOL -> EXPRESION TkNEqual EXPRESION','EXP_BOOL',3,'p_exp_bool','parser.py',259),
  ('EXP_BOOL -> EXPRESION TkGreater EXPRESION','EXP_BOOL',3,'p_exp_bool','parser.py',260),
  ('EXP_BOOL -> EXPRESION TkGeq EXPRESION','EXP_BOOL',3,'p_exp_bool','parser.py',261),
  ('EXP_BOOL -> EXPRESION TkLess EXPRESION','EXP_BOOL',3,'p_exp_bool','parser.py',262),
  ('EXP_BOOL -> EXPRESION TkLeq EXPRESION','EXP_BOOL',3,'p_exp_bool','parser.py',263),
  ('CONVERTIR -> TkItoi TkOpenPar IDENTIFICADOR TkClosePar','CONVERTIR',4,'p_convertir','parser.py',287),
  ('CONVERTIR -> TkLen TkOpenPar IDENTIFICADOR TkClosePar','CONVERTIR',4,'p_convertir','parser.py',288),
  ('CONVERTIR -> TkMax TkOpenPar IDENTIFICADOR TkClosePar','CONVERTIR',4,'p_convertir','parser.py',289),
  ('CONVERTIR -> TkMin TkOpenPar IDENTIFICADOR TkClosePar','CONVERTIR',4,'p_convertir','parser.py',290),
  ('POST -> TkOpenBra TkPost TkTwoPoints EXP_CUANTIFICADOR TkCloseBra','POST',5,'p_postcondicion','parser.py',297),
  ('EXP_CUANTIFICADOR -> TkOpenPar TkForall IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_CUANTIFICADOR TkClosePar','EXP_CUANTIFICADOR',10,'p_exp_cuantificador_forall','parser.py',305),
  ('EXP_CUANTIFICADOR -> TkOpenPar TkForall IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_BOOL TkClosePar','EXP_CUANTIFICADOR',10,'p_exp_cuantificador_forall','parser.py',306),
  ('EXP_CUANTIFICADOR -> TkOpenPar TkExists IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_CUANTIFICADOR TkClosePar','EXP_CUANTIFICADOR',10,'p_exp_cuantificador_exist','parser.py',314),
  ('EXP_CUANTIFICADOR -> TkOpenPar TkExists IDENTIFICADOR TkPipe IDENTIFICADOR TkIn IDENTIFICADOR TkTwoPoints EXP_BOOL TkClosePar','EXP_CUANTIFICADOR',10,'p_exp_cuantificador_exist','parser.py',315),
  ('VACIO -> <empty>','VACIO',0,'p_vacio','parser.py',323),
]