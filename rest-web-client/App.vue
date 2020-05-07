<template> 
<div>
  
  
  <h1>Cliente para REST web services </h1>
  <hr/>
   <input type="text" placeholder="Ingrese Rut..." v-model="rut"> &nbsp; 
   <button @click="enviaRut" > Comprobar rut</button>
   <h3>{{estadorut}}</h3>
    
    <hr/>
    <ul>
    <li><input type="text" placeholder="Ingrese Nombre..." v-model="nombres"> &nbsp;</li>
    <li><input type="text" placeholder="Ingrese Paterno..." v-model="paterno"> &nbsp;</li>
    <li><input type="text" placeholder="Ingrese Materno.." v-model="materno"> &nbsp;</li>
    <li><input type="text" placeholder="Ingrese Genero..." v-model="genero"> &nbsp;</li>
    <button @click="enviaSaludo" > Generar Saludo</button>
    <h3>{{estadosaludo}}</h3>
   </ul>


</div>



</template>

<script>
import axios from "axios"; //importamos el cliente http

export default {
  data() {
    return {
      rut: null, // Para validarut
      estadorut: null, // me devuelve el estado del rut
      nombres: null, // Para saludo
      paterno: null, // Para saludo
      materno: null, // Para saludo
      genero: null, // Para saludo
      estadosaludo: null // me devuelve el saludo
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
          nombres: this.nombres ,
          paterno:this.paterno,
          materno: this.materno,
          genero: this.genero
        })
        .then(response => {
          console.log(response);
          //this.nombres = response.data;
          //this.paterno = response.data;
          //this.materno = response.data;
          //this.genero = response.data;
          this.estadosaludo = response.data;
        });
    }
  }
};
</script>

<style>
</style>
