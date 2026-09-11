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

console.log(JsUser);

console.log(JsUser.name);
console.log(JsUser['email']);

console.log(JsUser[mySym]);