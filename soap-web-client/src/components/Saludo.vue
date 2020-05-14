<template>
  <v-container class="ma-0 pa-0" style="max-width: 100%">
    <div>
      <v-alert
        type="success"
        v-if="respuesta != null && respuesta.estado == 1"
      >{{ `${respuesta.mensaje}` }}</v-alert>

      <v-alert
        type="error"
        v-if="respuesta != null && respuesta.estado == 2"
      >{{ `${respuesta.mensaje}` }}</v-alert>

      <v-alert
        type="warning"
        v-if="respuesta != null && respuesta.estado == 3"
      >{{ `${respuesta.mensaje}` }}</v-alert>
    </div>
    <v-row class="ma-0 pa-0" align="center" justify="center">
      <v-col cols="2">
        <v-text-field label="Nombres" v-model="datos.nombres"></v-text-field>
      </v-col>
      <v-col cols="2">
        <v-text-field label="Apellido paterno" v-model="datos.paterno"></v-text-field>
      </v-col>
      <v-col cols="2">
        <v-text-field label="Apellido materno" v-model="datos.materno"></v-text-field>
      </v-col>
      <v-col cols="1">
        <v-combobox label="Género" v-model="datos.genero" :items="generos"></v-combobox>
      </v-col>
    </v-row>
    <v-row class="ma-0 pa-0" align="center" justify="center">
      <v-btn class="mr-5" @click="generarSaludo()" color="secondary">
        <v-icon dark left>mdi-autorenew</v-icon>Generar saludo
      </v-btn>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "saludo",
  data() {
    return {
      datos: {
        nombres: null,
        paterno: null,
        materno: null,
        genero: null
      },
      generos: ["F", "M"],
      respuesta: null
    };
  },
  methods: {
    generarSaludo() {
      if (this.datos != null) {
        this.datos.nombres =
          this.datos.nombres == "" ? null : this.datos.nombres;
        this.datos.paterno =
          this.datos.paterno == "" ? null : this.datos.paterno;
        this.datos.materno =
          this.datos.materno == "" ? null : this.datos.materno;
        this.datos.genero = this.datos.genero == "" ? null : this.datos.genero;
        let xmls = `<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spy="spyne.webservice.soap">\
            <soapenv:Header/>\
            <soapenv:Body>\
                <spy:nombre>\
                  <spy:nombres>${this.datos.nombres}</spy:nombres>\
                  <spy:paterno>${this.datos.paterno}</spy:paterno>\
                  <spy:materno>${this.datos.materno}</spy:materno>\
                  <spy:genero>${this.datos.genero}</spy:genero>\
                </spy:nombre>\
            </soapenv:Body>\
          </soapenv:Envelope>`;
          console.log(new Date().toLocaleString(), "Datos enviados:", this.datos)
        axios
          .post(this.$apiUrl, xmls)
          .then(res => {
            var xml = new DOMParser().parseFromString(res.data, "text/xml");
            console.log(new Date().toLocaleString(), "Respuesta en XML:", res.data);
            this.respuesta = {
              estado: xml.getElementsByTagName("s0:estado")[0].innerHTML == 'true' ? 1 : 2,
              mensaje: xml.getElementsByTagName("s0:mensaje")[0].innerHTML
            };
            console.log(new Date().toLocaleString(), "Respuesta parseada:", this.respuesta);
          })
          .catch(err => {
            console.log(new Date().toLocaleString(), err);
          });
      } else {
        this.respuesta = {
          estado: 3,
          mensaje: "Ingrese todos los datos"
        };
        console.log(new Date().toLocaleString(), "Error:", this.respuesta);
      }
    }
  }
};
</script>