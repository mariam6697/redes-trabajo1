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
        <v-text-field label="RUT" v-model="rut"></v-text-field>
      </v-col>
      <v-col cols="1">
        <v-btn class="mr-5" @click="validarRut()" color="secondary">
          <v-icon dark left>mdi-send-check</v-icon>Validar
        </v-btn>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
import axios from "axios";

export default {
  name: "validar-rut",
  data() {
    return {
      rut: null,
      respuesta: null
    };
  },
  methods: {
    validarRut() {
      if (this.rut != null && this.rut != "") {
        let xmls =
          `<soapenv:Envelope xmlns:soapenv="http://schemas.xmlsoap.org/soap/envelope/" xmlns:spy="spyne.webservice.soap">\
            <soapenv:Header/>\
            <soapenv:Body>\
                <spy:rut>\
                  <spy:rut>${this.rut}</spy:rut>\
                </spy:rut>\
            </soapenv:Body>\
          </soapenv:Envelope>`;
          console.log(new Date().toLocaleString(), "Rut enviado:", this.rut)
        axios
          .post(
            this.$apiUrl,
            xmls
          )
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
          mensaje: "Ingrese un RUT"
        };
      }
    }
  }
};
</script>