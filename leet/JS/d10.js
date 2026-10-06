const mySym = Symbol('key1')


const JsUser = {
    name: "Suvo",
    "full_name": "Suvo Dey",
    [mySym]: "mykey1",
    age: 20,
    location: "wb",
    email: "suvo@google.com",
    isLoggedIn: false,
    lastLoginDays: ["Monday", "Saturday"]
}


JsUser.greeting = function () {
    console.log(JsUser);
}

JsUser.greetingTwo = function () {
    console.log(`hello ${this.name}`);
}


