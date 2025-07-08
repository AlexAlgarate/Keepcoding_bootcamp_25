// Variables

let cadena1 = 'Hola';

let cadena2 = 'Mundo';
let resultado = cadena1 + ' ' + cadena2;
console.log(cadena1);
console.log(cadena2);
console.log(cadena1 + cadena2);
console.log(resultado);

console.log(`${cadena1} ${cadena2}`);

console.log('Operadores lógicos', `${'a' === 'b'} returns False`);
console.log('Operadores lógicos', `${'a' !== 'b'} returns True`);
console.log('Operadores lógicos AND', `${true && false} returns True`);
console.log('Operadores lógicos OR', `${'a' || 'b'} returns True`);

// Funciones

function helloFunction() {
  return 'hola soy una funcion';
}

function helloFunctionWithArguments(cadena1, cadena2) {
  return `hola soy una funcion con dos argumentos: ${cadena1} y ${cadena2}`;
}

// Es anonima porque no lleva nombre después de la declaración de la funcion
let anonymousFunction = function () {
  return 'Hola funcion anonima';
};

// Similar a *arg en Python, los rest parameter...
function restParamsFunction(...names) {
  console.log(`Los invitados a la fiesta son: ${names} `);
}

console.log(helloFunction());
console.log(anonymousFunction());
console.log(helloFunctionWithArguments('primer argumento', 'segundo argumento'));
console.log(restParamsFunction('Vicky', 'Sombra', 'Shuri', 'Luna'));
