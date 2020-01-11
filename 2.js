function isAcceptedUsername(username) {
    var Regex = /^[aiueoAIUEO]{3}[a-z0-9]{5,12}$/i ;
    return Regex.test(username) ;
}
// Cara menggunakan fungsi di atas
if (isAcceptedUsername("aaat3st1ng")) {
    alert("Username Is Valid") ;
} else {
    alert("Username Is Invalid") ;
}


function requirePassWord(pass) {
  for (var a = 0; a < pass.length; a++) {
    if (email[a] !== email[a].toUpperCase()) {
      return "Password anda tidak valid";
    }
  }
  var at = email.indexOf('0,1,2,3,4,5,6,7,8,9')
  if(at > 1){
    return 'Email anda valid'
  } else {
    return 'Email anda tidak valid'
  }

}
console.log(requireEmail("ILHAM&4"));
