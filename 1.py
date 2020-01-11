function myBiodata(biodata){
  let biodataObj = {
    "name": 'Ilham Ramadhan',
    "age": '25',
    "address": 'Jalan Mitra Batik Gang Narip No. 15 Bojong RT 002 RW 010 Kelurahan Cipedes Kecamatan Cipedes Kota Tasikmalaya',
    "hobbies": [
      'Camping', 'Watching movies', 'Fishing', 'Travel' 
    ],
    "is_married": false,
    "school": [
     {
      "name": 'Universitas Siliwangi',
      "year_in": '2015',
      "year_out": '2020'
    },
     {
      
    "skills": [
      {
        "HTML5": "90 %",
        "CSS": "80 %",
        "Javascript": "95 %",
        "VueJS": "35 %",
        "C++": "50 %",
        "Bootstrap": "95 %",
        "GIT": "80 %",
      }
    ]
  }

  return biodataObj
}
console.log(myBiodata('ari'));
