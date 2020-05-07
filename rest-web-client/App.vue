<template> 
<div>
  <h1>Cliente para REST web services </h1>
   <input type="text" placeholder="Ingrese Rut..." v-model="rut"> &nbsp; 
   <button @click="enviaRut" > Comprobar rut</button>
   <h3>{{estado}}</h3>
</div>



</template>

<script>
import axios from "axios"; //importamos el cliente http

export default {
  data() {
    return {
      rut: null,
      estado: null,
    };
  },
  mounted() {},

  methods: {
    enviaRut() {
      //funcion nueva que enviara el rut ingresado por pantalla al obj estado
      axios
        .post("http://localhost:3000/validarut", {
          rut: this.rut
        })
        .then(response => {
          console.log(response);
          this.estado = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    }
  }
};
</script>

<style>
</style>
