## Proyecto: Intrepretador de PascalUSB
### Sintaxis del lenguajes con sus funciones

1. Estructura de un programa

2. Identificador de vairiables
	
		<nombre>  = [a-zA-Z]+[a-zA-Z0-9_]+

3. Tipos
	int
	bool
	inter

4. Intrucciones
	
	- Asignacion

			<var> := <exp>

	- Bloque
		
			begin
				declaracion
				instruccion 1 ;
				...
				instruccion n 
			end 

		Para declarar las variables
			declare
				x1,... xn as <tipo1>, <tipo2> ... <tipo n>;
				y1,... yn as <tipo1>, <tipo2> ... <tipo n>;
				...
				z1,... zn as <tipo>;`

	- Entrada

			read <variable>

		nota: Para los `<inter>` se debe aceptar este formato: `a..b`

	- Salida

			print x1,.. xn
			println x1,.. xn

	- Condicional if then else

			if <condicion> then <instruccion> else <instruccion>
			if <condicion> then <instruccion>

	- Condicional Case

			case <exp int> of 
				<exp inter> ==> <intruccion>
				<exp inter> ==> <intruccion>
				...
				<exp inter> ==> <intruccion>
			end

	- Iteración

			for <indentificador> in <inter> do <instruccion>

	- Iteración While

			while <condicion> do <instruccion>

5. Expresiones

	- Expresiones con enteros

		Por orden de precedencia 

		- \+ , \- (Binario)
		- \* , / , %
		- ..
		- \- (Unario)

	- Expresiones con intervalos
		
		- a .. b Construccion
		- a \+ b Union
		- a <> b Interseccion
		- a * b escala
		precedencia de union > interseccion

	- Expresiones Booleanas
		
		Por orden de precedencia
		- or
		- and
		- not 
		
		Operadores relacionales, por orden de precedencia
		- < , <= , > , >=
		- ==, /= 
		- in
		Si a y b son de tipo inter tienen criterios especiales.

	- Conversion de tipos y funciones embebidas

		- itoi(a) 
		- len(a)
		- max(a)
		- min(a)

6. Comentarios 

	Solo un tipo de comentario tipo C
	-  //

7. PostCondicion

		{Post: <expresion booleana>}
			(forall x | x in <inter> : <expresion booleana>)
			(exists x | x in <inter> : <expresion booleana>)



### Preguntas que hacer

- El alcance seria dinamico?
- While no es un bloque? es decir, solo begin y for
- 
