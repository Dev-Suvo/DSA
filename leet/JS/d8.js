userobj = {
    name: "suvo",
    age: 23,
    salary: 25000
}

function APIDATA(api) {
    return `Name is ${api.name} and age is ${api.age} and salary is ${api.salary}`
}

console.log(APIDATA(userobj));