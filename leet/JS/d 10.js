const mySym = Symbol('key1')


const JsUser = {
    name: "Suvo",
    "full_name": "Suvo Dey",
    [mySym]: "mykey1",
    age: 18,
    location: "wb",
    email: "hitesh@google.com",
    isLoggedIn: false,
    lastLoginDays: ["Monday", "Saturday"]
}


JsUser.greeting = function () {
    console.log(JsUser);
}

JsUser.greetingTwo = function () {
    console.log(`hello ${this.name}`);
}


