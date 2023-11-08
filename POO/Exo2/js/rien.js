const prompt = require("prompt");


console.log("entrer la valeur de a");
prompt.start();
var a;
prompt.get(["val"], (err, data) => {
    if(err) throw err;
    //console.log("a = " + data.reponse);
    a = parseInt(data.val);
});
//console.log("a = " + a);
//var a=(prompt("entrer la valeur de a"));
//console.log(a);
