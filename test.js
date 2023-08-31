 let number;


function roll() {
    const response =  fetch('http://127.0.0.1:8000/api/users/');
    number = response;
}

roll()

console.log(number.json());
