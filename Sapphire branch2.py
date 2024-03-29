{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import sys \n",
    "import difflib \n",
    "import requests  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "html1 = \"\"\" \n",
    "12. CONTENIDO\n",
    "12.1. CONTENIDO BÁSICO 12.2. CONTENIDO DETALLADO\n",
    "1. Funciones y Modelos\n",
    "1.1. Cuatro maneras de representar una función, definición de función,\n",
    "1.2. Funciones definidas a tramos, valor absoluto, simetría, función par,\n",
    "1.3. Catálogo de funciones básicas: polinomios (grado, raíces, función\n",
    "1.4. Transformaciones de funciones: desplazamientos verticales y\n",
    "1.5. Álgebra de funciones, composición de funciones\n",
    "1.6. Funciones exponenciales: gráficas, leyes de los exponentes,\n",
    "1.7. Función inversa: función uno a uno, prueba de la recta horizontal,\n",
    "1.8. Funciones logarítmicas: definición, gráficas, leyes de los logaritmos,\n",
    "1.9. Funciones trigonométricas inversas: función seno inverso, función \n",
    "2. Límites y Derivadas\n",
    "2.1. Límite de una función: definición intuitiva, ejemplos gráficos,\n",
    "2.2. Cálculo de límites: reglas básicas para el cálculo de límites, límites\n",
    "2.3. Continuidad: definición, continuidad por la derecha y por la izquierda,\n",
    "2.4. Límites que comprenden el infinito: límites infinitos y asíntotas\n",
    "2.5. Tangentes, velocidades y otras razones de cambio.\n",
    "2.6. Definición de derivada, interpretación de la derivada como la\n",
    "2.7. La derivada como una función, notaciones de la derivada, relación\n",
    "2.8. ¿Qué dice f’ acerca de f? ¿Qué dice f’’ acerca de f?\n",
    "3. Reglas de Derivación. \n",
    "3.1. Derivadas de polinomios y de funciones exponenciales. Las reglas\n",
    "3.2. Derivación de funciones trigonométricas. La regla de la cadena.\n",
    "3.3. Derivación implícita. Derivadas de las funciones trigonométricas\n",
    "4. Aplicaciones de la derivación.\n",
    "4.1. Razones de cambio de variables relacionadas.\n",
    "4.2. Valores máximo y mínimo absolutos de una función. Extremos\n",
    "4.3. Derivadas y las formas de las curvas: teorema del valor medio,\n",
    "4.4. Definición de concavidad y puntos de inflexión. Prueba de\n",
    "4.5. Ejemplos de trazado de gráficas. Formas indeterminadas y la regla\n",
    "4.6. Problemas de optimización.\n",
    "4.7. Antiderivadas: definición, tabla de fórmulas de antiderivación, \n",
    "\n",
    "\"\"\" \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "html2 = \"\"\" \n",
    "12. CONTENIDO\n",
    "12.1. CONTENIDO BÁSICO 12.2. CONTENIDO DETALLADO\n",
    "1. Funciones y Modelos\n",
    "1.1. Cuatro maneras de representar una función, definición de función,\n",
    "1.2. Funciones definidas a tramos, valor absoluto, simetría, función par,\n",
    "1.3. Catálogo de funciones básicas: polinomios (grado, raíces, función\n",
    "1.4. Transformaciones de funciones: desplazamientos verticales y\n",
    "1.5. Álgebra de funciones, composición de funciones\n",
    "1.6. Funciones exponenciales: gráficas, leyes de los exponentes,\n",
    "1.7. Función inversa: función uno a uno, prueba de la recta horizontal,\n",
    "1.8. Funciones logarítmicas: definición, gráficas, leyes de los logaritmos,\n",
    "1.9. Funciones trigonométricas inversas: función seno inverso, función \n",
    "2. Límites y Derivadas\n",
    "2.1. Límite de una función: definición intuitiva, ejemplos gráficos,\n",
    "2.2. Cálculo de límites: reglas básicas para el cálculo de límites, límites\n",
    "2.3. Continuidad: definición, continuidad por la derecha y por la izquierda,\n",
    "2.4. Límites que comprenden el infinito: límites infinitos y asíntotas\n",
    "2.5. Tangentes, velocidades y otras razones de cambio.\n",
    "2.6. Definición de derivada, interpretación de la derivada como la\n",
    "2.7. La derivada como una función, notaciones de la derivada, relación\n",
    "2.8. ¿Qué dice f’ acerca de f? ¿Qué dice f’’ acerca de f?\n",
    "3. Reglas de Derivación. \n",
    "3.1. Derivadas de polinomios y de funciones exponenciales. Las reglas\n",
    "3.2. Derivación de funciones trigonométricas. La regla de la cadena.\n",
    "3.3. Derivación implícita. Derivadas de las funciones trigonométricas\n",
    "\"\"\" \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [],
   "source": [
    "lineas1 = html1.splitlines() \n",
    "lineas2 = html2.splitlines() \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "lineas1 <class 'list'> lineas2 <class 'list'>\n",
      "   \n",
      "  12. CONTENIDO\n",
      "  12.1. CONTENIDO BÁSICO 12.2. CONTENIDO DETALLADO\n",
      "  1. Funciones y Modelos\n",
      "  1.1. Cuatro maneras de representar una función, definición de función,\n",
      "  1.2. Funciones definidas a tramos, valor absoluto, simetría, función par,\n",
      "  1.3. Catálogo de funciones básicas: polinomios (grado, raíces, función\n",
      "  1.4. Transformaciones de funciones: desplazamientos verticales y\n",
      "  1.5. Álgebra de funciones, composición de funciones\n",
      "  1.6. Funciones exponenciales: gráficas, leyes de los exponentes,\n",
      "  1.7. Función inversa: función uno a uno, prueba de la recta horizontal,\n",
      "  1.8. Funciones logarítmicas: definición, gráficas, leyes de los logaritmos,\n",
      "  1.9. Funciones trigonométricas inversas: función seno inverso, función \n",
      "  2. Límites y Derivadas\n",
      "  2.1. Límite de una función: definición intuitiva, ejemplos gráficos,\n",
      "  2.2. Cálculo de límites: reglas básicas para el cálculo de límites, límites\n",
      "  2.3. Continuidad: definición, continuidad por la derecha y por la izquierda,\n",
      "  2.4. Límites que comprenden el infinito: límites infinitos y asíntotas\n",
      "  2.5. Tangentes, velocidades y otras razones de cambio.\n",
      "  2.6. Definición de derivada, interpretación de la derivada como la\n",
      "  2.7. La derivada como una función, notaciones de la derivada, relación\n",
      "  2.8. ¿Qué dice f’ acerca de f? ¿Qué dice f’’ acerca de f?\n",
      "  3. Reglas de Derivación. \n",
      "  3.1. Derivadas de polinomios y de funciones exponenciales. Las reglas\n",
      "  3.2. Derivación de funciones trigonométricas. La regla de la cadena.\n",
      "  3.3. Derivación implícita. Derivadas de las funciones trigonométricas\n",
      "- 4. Aplicaciones de la derivación.\n",
      "- 4.1. Razones de cambio de variables relacionadas.\n",
      "- 4.2. Valores máximo y mínimo absolutos de una función. Extremos\n",
      "- 4.3. Derivadas y las formas de las curvas: teorema del valor medio,\n",
      "- 4.4. Definición de concavidad y puntos de inflexión. Prueba de\n",
      "- 4.5. Ejemplos de trazado de gráficas. Formas indeterminadas y la regla\n",
      "- 4.6. Problemas de optimización.\n",
      "- 4.7. Antiderivadas: definición, tabla de fórmulas de antiderivación, \n",
      "- \n"
     ]
    }
   ],
   "source": [
    "diferencia = difflib.Differ() \n",
    "generador_diferencia = diferencia.compare(lineas1, lineas2) \n",
    "print('lineas1', type(lineas1), 'lineas2', type(lineas2)) \n",
    "print('\\n'.join(generador_diferencia)) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "lineas1 <class 'list'> lineas2 <class 'list'>\n",
      "   \n",
      "  12. CONTENIDO\n",
      "  12.1. CONTENIDO BÁSICO 12.2. CONTENIDO DETALLADO\n",
      "  1. Funciones y Modelos\n",
      "  1.1. Cuatro maneras de representar una función, definición de función,\n",
      "  1.2. Funciones definidas a tramos, valor absoluto, simetría, función par,\n",
      "  1.3. Catálogo de funciones básicas: polinomios (grado, raíces, función\n",
      "  1.4. Transformaciones de funciones: desplazamientos verticales y\n",
      "  1.5. Álgebra de funciones, composición de funciones\n",
      "  1.6. Funciones exponenciales: gráficas, leyes de los exponentes,\n",
      "  1.7. Función inversa: función uno a uno, prueba de la recta horizontal,\n",
      "  1.8. Funciones logarítmicas: definición, gráficas, leyes de los logaritmos,\n",
      "  1.9. Funciones trigonométricas inversas: función seno inverso, función \n",
      "  2. Límites y Derivadas\n",
      "  2.1. Límite de una función: definición intuitiva, ejemplos gráficos,\n",
      "  2.2. Cálculo de límites: reglas básicas para el cálculo de límites, límites\n",
      "  2.3. Continuidad: definición, continuidad por la derecha y por la izquierda,\n",
      "  2.4. Límites que comprenden el infinito: límites infinitos y asíntotas\n",
      "  2.5. Tangentes, velocidades y otras razones de cambio.\n",
      "  2.6. Definición de derivada, interpretación de la derivada como la\n",
      "  2.7. La derivada como una función, notaciones de la derivada, relación\n",
      "  2.8. ¿Qué dice f’ acerca de f? ¿Qué dice f’’ acerca de f?\n",
      "  3. Reglas de Derivación. \n",
      "  3.1. Derivadas de polinomios y de funciones exponenciales. Las reglas\n",
      "  3.2. Derivación de funciones trigonométricas. La regla de la cadena.\n",
      "  3.3. Derivación implícita. Derivadas de las funciones trigonométricas\n",
      "- 4. Aplicaciones de la derivación.\n",
      "- 4.1. Razones de cambio de variables relacionadas.\n",
      "- 4.2. Valores máximo y mínimo absolutos de una función. Extremos\n",
      "- 4.3. Derivadas y las formas de las curvas: teorema del valor medio,\n",
      "- 4.4. Definición de concavidad y puntos de inflexión. Prueba de\n",
      "- 4.5. Ejemplos de trazado de gráficas. Formas indeterminadas y la regla\n",
      "- 4.6. Problemas de optimización.\n",
      "- 4.7. Antiderivadas: definición, tabla de fórmulas de antiderivación, \n",
      "- \n",
      "0.8694148169501297\n",
      "86.94%\n"
     ]
    }
   ],
   "source": [
    "diferencia = difflib.Differ() \n",
    "generador_diferencia = diferencia.compare(lineas1, lineas2) \n",
    "print('lineas1', type(lineas1), 'lineas2', type(lineas2)) \n",
    "print('\\n'.join(generador_diferencia)) \n",
    "# Obtiene diferencias graficamente en html5 \n",
    "dif1 = difflib.SequenceMatcher(lambda x: x == \" \\t\", html1, html2) \n",
    "diff1=float(100 * dif1.ratio()) \n",
    "print(dif1.ratio()) \n",
    "print(\"%.2f%%\" % (100 * dif1.ratio())) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "encabezado = '<!DOCTYPE html><html lang=\"en\"><head>  <title>Indicadores de Similitud en Contenido de Asignaturas para homologación de Estudiantes en la Institución Universitaria Salazar y Herrera</title> <meta charset=\"utf-8\">  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">  <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css\">  <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js\"></script>  <script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js\"></script>  <meta http-equiv=\"Content-Type\"      content=\"text/html; charset=utf-8\" /><title></title><style type=\"text/css\">    table.diff {font-family:Courier; border:medium;}    .diff_header {background-color:#e0e0e0}    td.diff_header {text-align:right}    .diff_next {background-color:#c0c0c0}    .diff_add {background-color:#aaffaa}    .diff_chg {background-color:#ffff77}    .diff_sub {background-color:#ffaaaa}</style></head><body><div class=\"jumbotron text-center\">  <a class=\"logo\" href=\"http://www.iush.edu.co/\"><img src=\"http://www.iush.edu.co/Uploads/Logo-IUSH-luto.png\" height=\"80\" alt=\"Logo IUSH\" /></a>  <h2>Indicadores de Similitud en Contenido de Asignaturas para homologación de Estudiantes en la Institución Universitaria Salazar y Herrera</h2> <h3>Porcentaje Similitud</h3> <h3>%f</h3>  </div>  <div class=\"container\">  <div class=\"row\">    <div class=\"col-sm-12\">' %diff1 \n",
    "pie = '</div>  </div></div></body></html>'  \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<!DOCTYPE html><html lang=\"en\"><head>  <title>Indicadores de Similitud en Contenido de Asignaturas para homologación de Estudiantes en la Institución Universitaria Salazar y Herrera</title> <meta charset=\"utf-8\">  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">  <link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/css/bootstrap.min.css\">  <script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js\"></script>  <script src=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.4.0/js/bootstrap.min.js\"></script>  <meta http-equiv=\"Content-Type\"      content=\"text/html; charset=utf-8\" /><title></title><style type=\"text/css\">    table.diff {font-family:Courier; border:medium;}    .diff_header {background-color:#e0e0e0}    td.diff_header {text-align:right}    .diff_next {background-color:#c0c0c0}    .diff_add {background-color:#aaffaa}    .diff_chg {background-color:#ffff77}    .diff_sub {background-color:#ffaaaa}</style></head><body><div class=\"jumbotron text-center\">  <a class=\"logo\" href=\"http://www.iush.edu.co/\"><img src=\"http://www.iush.edu.co/Uploads/Logo-IUSH-luto.png\" height=\"80\" alt=\"Logo IUSH\" /></a>  <h2>Indicadores de Similitud en Contenido de Asignaturas para homologación de Estudiantes en la Institución Universitaria Salazar y Herrera</h2> <h3>Porcentaje Similitud</h3> <h3>86.941482</h3>  </div>  <div class=\"container\">  <div class=\"row\">    <div class=\"col-sm-12\">\n",
      "<!DOCTYPE html PUBLIC \"-//W3C//DTD XHTML 1.0 Transitional//EN\"\n",
      "          \"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd\">\n",
      "\n",
      "<html>\n",
      "\n",
      "<head>\n",
      "    <meta http-equiv=\"Content-Type\"\n",
      "          content=\"text/html; charset=utf-8\" />\n",
      "    <title></title>\n",
      "    <style type=\"text/css\">\n",
      "        table.diff {font-family:Courier; border:medium;}\n",
      "        .diff_header {background-color:#e0e0e0}\n",
      "        td.diff_header {text-align:right}\n",
      "        .diff_next {background-color:#c0c0c0}\n",
      "        .diff_add {background-color:#aaffaa}\n",
      "        .diff_chg {background-color:#ffff77}\n",
      "        .diff_sub {background-color:#ffaaaa}\n",
      "    </style>\n",
      "</head>\n",
      "\n",
      "<body>\n",
      "    \n",
      "    <table class=\"diff\" id=\"difflib_chg_to0__top\"\n",
      "           cellspacing=\"0\" cellpadding=\"0\" rules=\"groups\" >\n",
      "        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>\n",
      "        <colgroup></colgroup> <colgroup></colgroup> <colgroup></colgroup>\n",
      "        \n",
      "        <tbody>\n",
      "            <tr><td class=\"diff_next\"><a href=\"#difflib_chg_to0__0\">f</a></td><td class=\"diff_header\" id=\"from0_1\">1</td><td nowrap=\"nowrap\">&nbsp;</td><td class=\"diff_next\"><a href=\"#difflib_chg_to0__0\">f</a></td><td class=\"diff_header\" id=\"to0_1\">1</td><td nowrap=\"nowrap\">&nbsp;</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_2\">2</td><td nowrap=\"nowrap\">12.&nbsp;CONTENIDO</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_2\">2</td><td nowrap=\"nowrap\">12.&nbsp;CONTENIDO</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_3\">3</td><td nowrap=\"nowrap\">12.1.&nbsp;CONTENIDO&nbsp;BÁSICO&nbsp;12.2.&nbsp;CONTENIDO&nbsp;DETALLADO</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_3\">3</td><td nowrap=\"nowrap\">12.1.&nbsp;CONTENIDO&nbsp;BÁSICO&nbsp;12.2.&nbsp;CONTENIDO&nbsp;DETALLADO</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_4\">4</td><td nowrap=\"nowrap\">1.&nbsp;Funciones&nbsp;y&nbsp;Modelos</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_4\">4</td><td nowrap=\"nowrap\">1.&nbsp;Funciones&nbsp;y&nbsp;Modelos</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_5\">5</td><td nowrap=\"nowrap\">1.1.&nbsp;Cuatro&nbsp;maneras&nbsp;de&nbsp;representar&nbsp;una&nbsp;función,&nbsp;definición&nbsp;de&nbsp;función,</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_5\">5</td><td nowrap=\"nowrap\">1.1.&nbsp;Cuatro&nbsp;maneras&nbsp;de&nbsp;representar&nbsp;una&nbsp;función,&nbsp;definición&nbsp;de&nbsp;función,</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_6\">6</td><td nowrap=\"nowrap\">1.2.&nbsp;Funciones&nbsp;definidas&nbsp;a&nbsp;tramos,&nbsp;valor&nbsp;absoluto,&nbsp;simetría,&nbsp;función&nbsp;par,</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_6\">6</td><td nowrap=\"nowrap\">1.2.&nbsp;Funciones&nbsp;definidas&nbsp;a&nbsp;tramos,&nbsp;valor&nbsp;absoluto,&nbsp;simetría,&nbsp;función&nbsp;par,</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_7\">7</td><td nowrap=\"nowrap\">1.3.&nbsp;Catálogo&nbsp;de&nbsp;funciones&nbsp;básicas:&nbsp;polinomios&nbsp;(grado,&nbsp;raíces,&nbsp;función</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_7\">7</td><td nowrap=\"nowrap\">1.3.&nbsp;Catálogo&nbsp;de&nbsp;funciones&nbsp;básicas:&nbsp;polinomios&nbsp;(grado,&nbsp;raíces,&nbsp;función</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_8\">8</td><td nowrap=\"nowrap\">1.4.&nbsp;Transformaciones&nbsp;de&nbsp;funciones:&nbsp;desplazamientos&nbsp;verticales&nbsp;y</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_8\">8</td><td nowrap=\"nowrap\">1.4.&nbsp;Transformaciones&nbsp;de&nbsp;funciones:&nbsp;desplazamientos&nbsp;verticales&nbsp;y</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_9\">9</td><td nowrap=\"nowrap\">1.5.&nbsp;Álgebra&nbsp;de&nbsp;funciones,&nbsp;composición&nbsp;de&nbsp;funciones</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_9\">9</td><td nowrap=\"nowrap\">1.5.&nbsp;Álgebra&nbsp;de&nbsp;funciones,&nbsp;composición&nbsp;de&nbsp;funciones</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_10\">10</td><td nowrap=\"nowrap\">1.6.&nbsp;Funciones&nbsp;exponenciales:&nbsp;gráficas,&nbsp;leyes&nbsp;de&nbsp;los&nbsp;exponentes,</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_10\">10</td><td nowrap=\"nowrap\">1.6.&nbsp;Funciones&nbsp;exponenciales:&nbsp;gráficas,&nbsp;leyes&nbsp;de&nbsp;los&nbsp;exponentes,</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_11\">11</td><td nowrap=\"nowrap\">1.7.&nbsp;Función&nbsp;inversa:&nbsp;función&nbsp;uno&nbsp;a&nbsp;uno,&nbsp;prueba&nbsp;de&nbsp;la&nbsp;recta&nbsp;horizontal,</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_11\">11</td><td nowrap=\"nowrap\">1.7.&nbsp;Función&nbsp;inversa:&nbsp;función&nbsp;uno&nbsp;a&nbsp;uno,&nbsp;prueba&nbsp;de&nbsp;la&nbsp;recta&nbsp;horizontal,</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_12\">12</td><td nowrap=\"nowrap\">1.8.&nbsp;Funciones&nbsp;logarítmicas:&nbsp;definición,&nbsp;gráficas,&nbsp;leyes&nbsp;de&nbsp;los&nbsp;logaritmos,</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_12\">12</td><td nowrap=\"nowrap\">1.8.&nbsp;Funciones&nbsp;logarítmicas:&nbsp;definición,&nbsp;gráficas,&nbsp;leyes&nbsp;de&nbsp;los&nbsp;logaritmos,</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_13\">13</td><td nowrap=\"nowrap\">1.9.&nbsp;Funciones&nbsp;trigonométricas&nbsp;inversas:&nbsp;función&nbsp;seno&nbsp;inverso,&nbsp;función&nbsp;</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_13\">13</td><td nowrap=\"nowrap\">1.9.&nbsp;Funciones&nbsp;trigonométricas&nbsp;inversas:&nbsp;función&nbsp;seno&nbsp;inverso,&nbsp;función&nbsp;</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_14\">14</td><td nowrap=\"nowrap\">2.&nbsp;Límites&nbsp;y&nbsp;Derivadas</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_14\">14</td><td nowrap=\"nowrap\">2.&nbsp;Límites&nbsp;y&nbsp;Derivadas</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_15\">15</td><td nowrap=\"nowrap\">2.1.&nbsp;Límite&nbsp;de&nbsp;una&nbsp;función:&nbsp;definición&nbsp;intuitiva,&nbsp;ejemplos&nbsp;gráficos,</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_15\">15</td><td nowrap=\"nowrap\">2.1.&nbsp;Límite&nbsp;de&nbsp;una&nbsp;función:&nbsp;definición&nbsp;intuitiva,&nbsp;ejemplos&nbsp;gráficos,</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_16\">16</td><td nowrap=\"nowrap\">2.2.&nbsp;Cálculo&nbsp;de&nbsp;límites:&nbsp;reglas&nbsp;básicas&nbsp;para&nbsp;el&nbsp;cálculo&nbsp;de&nbsp;límites,&nbsp;límites</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_16\">16</td><td nowrap=\"nowrap\">2.2.&nbsp;Cálculo&nbsp;de&nbsp;límites:&nbsp;reglas&nbsp;básicas&nbsp;para&nbsp;el&nbsp;cálculo&nbsp;de&nbsp;límites,&nbsp;límites</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_17\">17</td><td nowrap=\"nowrap\">2.3.&nbsp;Continuidad:&nbsp;definición,&nbsp;continuidad&nbsp;por&nbsp;la&nbsp;derecha&nbsp;y&nbsp;por&nbsp;la&nbsp;izquierda,</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_17\">17</td><td nowrap=\"nowrap\">2.3.&nbsp;Continuidad:&nbsp;definición,&nbsp;continuidad&nbsp;por&nbsp;la&nbsp;derecha&nbsp;y&nbsp;por&nbsp;la&nbsp;izquierda,</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_18\">18</td><td nowrap=\"nowrap\">2.4.&nbsp;Límites&nbsp;que&nbsp;comprenden&nbsp;el&nbsp;infinito:&nbsp;límites&nbsp;infinitos&nbsp;y&nbsp;asíntotas</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_18\">18</td><td nowrap=\"nowrap\">2.4.&nbsp;Límites&nbsp;que&nbsp;comprenden&nbsp;el&nbsp;infinito:&nbsp;límites&nbsp;infinitos&nbsp;y&nbsp;asíntotas</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_19\">19</td><td nowrap=\"nowrap\">2.5.&nbsp;Tangentes,&nbsp;velocidades&nbsp;y&nbsp;otras&nbsp;razones&nbsp;de&nbsp;cambio.</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_19\">19</td><td nowrap=\"nowrap\">2.5.&nbsp;Tangentes,&nbsp;velocidades&nbsp;y&nbsp;otras&nbsp;razones&nbsp;de&nbsp;cambio.</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_20\">20</td><td nowrap=\"nowrap\">2.6.&nbsp;Definición&nbsp;de&nbsp;derivada,&nbsp;interpretación&nbsp;de&nbsp;la&nbsp;derivada&nbsp;como&nbsp;la</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_20\">20</td><td nowrap=\"nowrap\">2.6.&nbsp;Definición&nbsp;de&nbsp;derivada,&nbsp;interpretación&nbsp;de&nbsp;la&nbsp;derivada&nbsp;como&nbsp;la</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_21\">21</td><td nowrap=\"nowrap\">2.7.&nbsp;La&nbsp;derivada&nbsp;como&nbsp;una&nbsp;función,&nbsp;notaciones&nbsp;de&nbsp;la&nbsp;derivada,&nbsp;relación</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_21\">21</td><td nowrap=\"nowrap\">2.7.&nbsp;La&nbsp;derivada&nbsp;como&nbsp;una&nbsp;función,&nbsp;notaciones&nbsp;de&nbsp;la&nbsp;derivada,&nbsp;relación</td></tr>\n",
      "            <tr><td class=\"diff_next\" id=\"difflib_chg_to0__0\"></td><td class=\"diff_header\" id=\"from0_22\">22</td><td nowrap=\"nowrap\">2.8.&nbsp;¿Qué&nbsp;dice&nbsp;f’&nbsp;acerca&nbsp;de&nbsp;f?&nbsp;¿Qué&nbsp;dice&nbsp;f’’&nbsp;acerca&nbsp;de&nbsp;f?</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_22\">22</td><td nowrap=\"nowrap\">2.8.&nbsp;¿Qué&nbsp;dice&nbsp;f’&nbsp;acerca&nbsp;de&nbsp;f?&nbsp;¿Qué&nbsp;dice&nbsp;f’’&nbsp;acerca&nbsp;de&nbsp;f?</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_23\">23</td><td nowrap=\"nowrap\">3.&nbsp;Reglas&nbsp;de&nbsp;Derivación.&nbsp;</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_23\">23</td><td nowrap=\"nowrap\">3.&nbsp;Reglas&nbsp;de&nbsp;Derivación.&nbsp;</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_24\">24</td><td nowrap=\"nowrap\">3.1.&nbsp;Derivadas&nbsp;de&nbsp;polinomios&nbsp;y&nbsp;de&nbsp;funciones&nbsp;exponenciales.&nbsp;Las&nbsp;reglas</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_24\">24</td><td nowrap=\"nowrap\">3.1.&nbsp;Derivadas&nbsp;de&nbsp;polinomios&nbsp;y&nbsp;de&nbsp;funciones&nbsp;exponenciales.&nbsp;Las&nbsp;reglas</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_25\">25</td><td nowrap=\"nowrap\">3.2.&nbsp;Derivación&nbsp;de&nbsp;funciones&nbsp;trigonométricas.&nbsp;La&nbsp;regla&nbsp;de&nbsp;la&nbsp;cadena.</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_25\">25</td><td nowrap=\"nowrap\">3.2.&nbsp;Derivación&nbsp;de&nbsp;funciones&nbsp;trigonométricas.&nbsp;La&nbsp;regla&nbsp;de&nbsp;la&nbsp;cadena.</td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_26\">26</td><td nowrap=\"nowrap\">3.3.&nbsp;Derivación&nbsp;implícita.&nbsp;Derivadas&nbsp;de&nbsp;las&nbsp;funciones&nbsp;trigonométricas</td><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"to0_26\">26</td><td nowrap=\"nowrap\">3.3.&nbsp;Derivación&nbsp;implícita.&nbsp;Derivadas&nbsp;de&nbsp;las&nbsp;funciones&nbsp;trigonométricas</td></tr>\n",
      "            <tr><td class=\"diff_next\"><a href=\"#difflib_chg_to0__top\">t</a></td><td class=\"diff_header\" id=\"from0_27\">27</td><td nowrap=\"nowrap\"><span class=\"diff_sub\">4.&nbsp;Aplicaciones&nbsp;de&nbsp;la&nbsp;derivación.</span></td><td class=\"diff_next\"><a href=\"#difflib_chg_to0__top\">t</a></td><td class=\"diff_header\"></td><td nowrap=\"nowrap\"></td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_28\">28</td><td nowrap=\"nowrap\"><span class=\"diff_sub\">4.1.&nbsp;Razones&nbsp;de&nbsp;cambio&nbsp;de&nbsp;variables&nbsp;relacionadas.</span></td><td class=\"diff_next\"></td><td class=\"diff_header\"></td><td nowrap=\"nowrap\"></td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_29\">29</td><td nowrap=\"nowrap\"><span class=\"diff_sub\">4.2.&nbsp;Valores&nbsp;máximo&nbsp;y&nbsp;mínimo&nbsp;absolutos&nbsp;de&nbsp;una&nbsp;función.&nbsp;Extremos</span></td><td class=\"diff_next\"></td><td class=\"diff_header\"></td><td nowrap=\"nowrap\"></td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_30\">30</td><td nowrap=\"nowrap\"><span class=\"diff_sub\">4.3.&nbsp;Derivadas&nbsp;y&nbsp;las&nbsp;formas&nbsp;de&nbsp;las&nbsp;curvas:&nbsp;teorema&nbsp;del&nbsp;valor&nbsp;medio,</span></td><td class=\"diff_next\"></td><td class=\"diff_header\"></td><td nowrap=\"nowrap\"></td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_31\">31</td><td nowrap=\"nowrap\"><span class=\"diff_sub\">4.4.&nbsp;Definición&nbsp;de&nbsp;concavidad&nbsp;y&nbsp;puntos&nbsp;de&nbsp;inflexión.&nbsp;Prueba&nbsp;de</span></td><td class=\"diff_next\"></td><td class=\"diff_header\"></td><td nowrap=\"nowrap\"></td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_32\">32</td><td nowrap=\"nowrap\"><span class=\"diff_sub\">4.5.&nbsp;Ejemplos&nbsp;de&nbsp;trazado&nbsp;de&nbsp;gráficas.&nbsp;Formas&nbsp;indeterminadas&nbsp;y&nbsp;la&nbsp;regla</span></td><td class=\"diff_next\"></td><td class=\"diff_header\"></td><td nowrap=\"nowrap\"></td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_33\">33</td><td nowrap=\"nowrap\"><span class=\"diff_sub\">4.6.&nbsp;Problemas&nbsp;de&nbsp;optimización.</span></td><td class=\"diff_next\"></td><td class=\"diff_header\"></td><td nowrap=\"nowrap\"></td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_34\">34</td><td nowrap=\"nowrap\"><span class=\"diff_sub\">4.7.&nbsp;Antiderivadas:&nbsp;definición,&nbsp;tabla&nbsp;de&nbsp;fórmulas&nbsp;de&nbsp;antiderivación,&nbsp;</span></td><td class=\"diff_next\"></td><td class=\"diff_header\"></td><td nowrap=\"nowrap\"></td></tr>\n",
      "            <tr><td class=\"diff_next\"></td><td class=\"diff_header\" id=\"from0_35\">35</td><td nowrap=\"nowrap\"><span class=\"diff_sub\">&nbsp;</span></td><td class=\"diff_next\"></td><td class=\"diff_header\"></td><td nowrap=\"nowrap\"></td></tr>\n",
      "        </tbody>\n",
      "    </table>\n",
      "    <table class=\"diff\" summary=\"Legends\">\n",
      "        <tr> <th colspan=\"2\"> Legends </th> </tr>\n",
      "        <tr> <td> <table border=\"\" summary=\"Colors\">\n",
      "                      <tr><th> Colors </th> </tr>\n",
      "                      <tr><td class=\"diff_add\">&nbsp;Added&nbsp;</td></tr>\n",
      "                      <tr><td class=\"diff_chg\">Changed</td> </tr>\n",
      "                      <tr><td class=\"diff_sub\">Deleted</td> </tr>\n",
      "                  </table></td>\n",
      "             <td> <table border=\"\" summary=\"Links\">\n",
      "                      <tr><th colspan=\"2\"> Links </th> </tr>\n",
      "                      <tr><td>(f)irst change</td> </tr>\n",
      "                      <tr><td>(n)ext change</td> </tr>\n",
      "                      <tr><td>(t)op</td> </tr>\n",
      "                  </table></td> </tr>\n",
      "    </table>\n",
      "</body>\n",
      "\n",
      "</html></div>  </div></div></body></html>\n"
     ]
    }
   ],
   "source": [
    "lineas1 = html1.splitlines() \n",
    "lineas2 = html2.splitlines() \n",
    "diferencia_html = difflib.HtmlDiff() \n",
    "archivo_html = diferencia_html.make_file(lineas1, lineas2) \n",
    "pagina1 = encabezado + archivo_html + pie \n",
    "print(pagina1) "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
