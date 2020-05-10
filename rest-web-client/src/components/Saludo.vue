<template>
    <div>
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
  name: "Saludo",
  data() {
    return {
      nombres: null,
      paterno: null,
      materno: null,
      genero: null,
      estadosaludo: null
    };
  },
  methods: {
    enviaSaludo() {
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
        
        })
        .catch(e => {
        console.log(e);
        })
    }
  }
};
</script>
