function requireUserName(name){
  for (var a = 0; a < name.length; a++) {
    if (name[a] !== name[a].toLowerCase()) {
      return "Username anda tidak valid";
    }
  }
  return 'Username valid'
}
console.log(requireUserName('arisupriatna'))

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
