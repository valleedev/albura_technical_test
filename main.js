let option = prompt("Seleccione la prueba lógica deseada 1-2: ")

if(option == 1) {
    let num = prompt("Ingrese un número: ");

    if (num % 2 == 0) {
        console.log("El número es par.")
    } else {
        console.log("El número es impar.")
    }

    console.log("Tabla de multiplicar")
    for( let i=0; i<=10; i++) {
        console.log(num + " x " + i + " = " + num*i)
    }
} else if (option == 2) {
    let limit = prompt("Ingrese el número límite para hacer la serie fibonacci: ")

    let fibonacci = [0,1]

    for(let i=2; i<=limit; i++){
        fiboNum = fibonacci[i -1] + fibonacci[i-2]
        fibonacci.push(fiboNum);
    }

    i=0
    while(i<fibonacci.length) {
        console.log(fibonacci[i])
        i++
    }
} else {
    alert("Debe ingresar un valor válido")
}