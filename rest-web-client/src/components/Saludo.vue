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
    <b-field label="Nombres">
      <b-input type="text" placeholder="Ingrese Nombres..." v-model="nombres" />
    </b-field>
      <br />
      <b-field label="Apellido paterno">
      <b-input type="text" placeholder="Ingrese Paterno..." v-model="paterno" />
      </b-field>
      <br />
      <b-field label="Apellido materno">
      <b-input type="text" placeholder="Ingrese Materno..." v-model="materno" />
      </b-field>
      <br />
      <b-field label="Género">
      <b-input type="text" placeholder="Ingrese Genero (F,M)..." v-model="genero" />
      </b-field>
      <br />
      <br />
      <button style="margin: 10px" @click="enviaSaludo">Generar Saludo</button>
    </div>
    </div>
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
      respuesta: {},
      estadosaludo: null
    };
  },
   watch: {
      nombres: function() {
          this.nombres = this.nombres == "" ? null : this.nombres;
      },
      paterno: function() {
          this.paterno = this.paterno == "" ? null : this.paterno;
      },
      materno: function() {
          this.materno = this.materno == "" ? null : this.materno;
      },
      genero: function() {
          this.genero = this.genero == "" ? null : this.genero;
      }
  },
  methods: {
    enviaSaludo() {
      axios
        .post(this.$apiUrl + "/saludo", {
          nombres: this.nombres,
          paterno: this.paterno,
          materno: this.materno,
          genero: this.genero
        })
        .then(response => {
          console.log(new Date().toLocaleString(), "Respuesta:", response.data);
          this.respuesta = response.data;
        })
        .catch(e => {
          console.log(e);
        });
    }
  }
};
</script>
