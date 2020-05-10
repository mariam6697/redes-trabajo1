<template>
  <div>
  <input type="text" placeholder="Ingrese Rut..." v-model="rut">&nbsp;
   <button  @click="enviaRut" > Comprobar RUT</button>
   <h4>{{estadorut}}</h4>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Validarut",
  data() {
    return {
      rut: null,
      estadorut: null
    };
  },
  methods: {
    enviaRut() {
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
    }
  }
};
</script>

