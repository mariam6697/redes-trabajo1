<template>
  <div>
    <div>
      <div class="notification is-success is-light" v-if="respuesta.estado == 1">
          <button class="delete"></button>
        {{ `${respuesta.mensaje}` }}
      </div>

      <div class="notification is-warning is-light" v-if="respuesta.estado == 3">
          <button class="delete"></button>
        {{ `${respuesta.mensaje}` }}
      </div>

      <div class="notification is-danger is-light" v-if="respuesta.estado == 2">
          <button class="delete"></button>
        {{ `${respuesta.mensaje}` }}
      </div>
    </div>
    <div class="column" style="display: flex; justify-content: center;">
      <div
        class="column"
        style="display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;"
      >
      <b-field label="RUT">
        <b-input type="text" placeholder="Ingrese RUT..." v-model="rut" />
      </b-field>
        <br />
        <br />
        <button style="margin: 10px" @click="enviaRut">Comprobar RUT</button>
        <br />
      </div>
    </div>
  </div>
</template>

<script>
import axios from "axios";
export default {
  name: "Validarut",
  data() {
    return {
      rut: null,
      estadorut: null,
      respuesta: {}
    };
  },
  methods: {
    enviaRut() {
      console.log(new Date().toLocaleString(), "Rut enviado:", this.rut);
      axios
        .post("http://localhost:3000/validarut", {
          rut: this.rut
        })
        .then(response => {
          console.log(new Date().toLocaleString(), "Respuesta:", response.data);
          this.respuesta = response.data;
          console.log(
            new Date().toLocaleString(),
            "Respuesta:",
            this.respuesta
          );
        })
        .catch(e => {
          console.log(new Date().toLocaleString(), e);
        });
    }
  }
};
</script>