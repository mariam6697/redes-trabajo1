<template> 
<div>

  <h1>Cliente para REST web services </h1>

  <h3> Validador de rut </h3>
   <input type="text" placeholder="Ingrese Rut..." v-model="rut">&nbsp;
   <button  @click="enviaRut" > Comprobar RUT</button>
   <h4>{{estadorut}}</h4>
    
    <h3>Generador de Saludo</h3>
   
    
    <input type="text" placeholder="Ingrese Nombres..." v-model="nombres"> <br/>
    <input type="text" placeholder="Ingrese Paterno..." v-model="paterno"> <br/>
    <input type="text" placeholder="Ingrese Materno..." v-model="materno"> <br/>
    <input type="text" placeholder="Ingrese Genero (F,M)..." v-model="genero">
    <br/> <br/>
    <button @click="enviaSaludo" > Generar Saludo</button>
    <h4>{{estadosaludo}}</h4>
  


</div>



</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      rut: null,
      estadorut: null,
      nombres: null,
      paterno: null,
      materno: null,
      genero: null,
      estadosaludo: null
    };
  },
  mounted() {},

  methods: {
    enviaRut() {
      //funcion nueva que enviara el rut ingresado por pantalla a la propiedad estado
      axios
        .post("http://localhost:3000/validarut", {
          rut: this.rut
        })
        .then(response => {
          console.log(response);
          this.estadorut = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    },
    enviaSaludo() {
      //funcion nueva que enviara los valores ingresados a las propiedades de saludo
      axios
        .post("http://localhost:3000/saludo", {
          nombres: this.nombres,
          paterno: this.paterno,
          materno: this.materno,
          genero: this.genero
        })
        .then(response => {
          console.log(response);
          this.estadosaludo = response.data;
        });
    }
  }
};
</script>

<style>
body {
  background-color: gainsboro;
}
button {
  background-color: rgba(190, 53, 53, 0.952);
  padding: 4px;
  font-weight: 500;
  color: white;
  border-radius: 100px;
  border: 0px;
}
button:hover {
  color: rgb(96, 122, 209);
  background-color: #ffffff;
}
h1 {
  font-family: Arial;
  color: white;
  font-size: 25px;
  text-align: center;
  background: rgba(190, 53, 53, 0.952);
  padding: 20px;
  border-radius: 25px;
}
h3 {
  font-family: Arial;
  color: rgb(53, 21, 21);
  font-size: 25px;
}
h4 {
  font-family: Arial;
  color: rgb(96, 122, 209);
  font-size: 19px;
}
</style>