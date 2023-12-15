function add_cargo(){

    container = document.getElementById("form-cargo")
   
    html = "<br> <div class='row'> <div class='col-md'> <input type='text' placeholder='Função' class='form-control' name='funcao'> </div> <div class='col-md'> <input type='text' placeholder='Lotação' class='form-control' name='lotação'> </div> <div class='col-md'> <input type='text' placeholder='Turno' class='form-control' name='turno'>  </div>"



    container.innerHTML += html


}
