$('document').ready(function() {
    let user = JSON.parse(localStorage.getItem('User'))
    console.log(user)
    console.log(user.actors[0].name)
    const actor =  user.actors[0].name
    const api_key = "c3c63420556c1043a8d6eac9948f427c";
    const base_url = `https://api.themoviedb.org/3`;
    const acotr_url = `${base_url}/search/person?api_key=${api_key}&query=${actor}`
    fetch(acotr_url).then((response) => response.json()).then((data) => console.log(data))
})