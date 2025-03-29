// count = 0


// function Callme(el) {
//     count++

//     el.innerHTML = "U click" + " " + count+ " " + "time"
//     if (count == 10) {
//         el.style.background = "red"
//     }
// }


// function onInput(el) {
//     if (el.value == "Hello") 
//         alert("U too!")


    



// }

let count = 0
let a = setInterval(func , 1000) 

function func() {
    count++
    alert("Прошло" + count + "секунд")
    if (count == 5) {
        clearInterval(a)
        alert("Прошло 5 секунд этого достаточно")
    }
}