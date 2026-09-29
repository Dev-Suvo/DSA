userobj = {
    name: "suvo",
    age: 23,
    salary: 25000,
    emp_id: "A54"
}
function APIDATA(api) {
    return `Name is ${api.name} and age is ${api.age} & employee id is ${api.emp_id} and salary is ${api.salary}`
}

console.log(APIDATA(userobj));