<template>
  <div id="app">
    <v-app>
      <div class="fill-height">
        <div>
          <v-app-bar
            
            color="#084387"
            dark
            src="https://wallpaperaccess.com/full/1567666.png"
          >
            <v-app-bar-nav-icon>
              <v-icon>mdi-web</v-icon>
            </v-app-bar-nav-icon>

            <v-toolbar-title>Cliente Web SOAP</v-toolbar-title>

            <v-spacer></v-spacer>

            <v-btn icon href="https://github.com/mariam6697/WS-SOAP-REST">
              <v-icon>mdi-source-repository</v-icon>
            </v-btn>
          </v-app-bar>
        </div>
        <v-content class="fill-height" style="background-color: #f1f1f1">
          <v-expansion-panels accordion v-model="panelAbierto" class="pa-3">
            <v-expansion-panel>
              <v-expansion-panel-header>
                <v-list-item-title class="title text-uppercase">Validar RUT</v-list-item-title>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                  <validar-rut ref="validarRut"/>
              </v-expansion-panel-content>
            </v-expansion-panel>
            <v-expansion-panel>
              <v-expansion-panel-header>
                <v-list-item-title class="title text-uppercase">Saludo personalizado</v-list-item-title>
              </v-expansion-panel-header>
              <v-expansion-panel-content>
                  <saludo ref="saludo"/>
              </v-expansion-panel-content>
            </v-expansion-panel>
          </v-expansion-panels>
        </v-content>
      </div>
    </v-app>
  </div>
</template>

<script>
import ValidarRut from "./components/ValidarRut";
import Saludo from "./components/Saludo";
export default {
  components: {
      ValidarRut,
      Saludo
  },
  data() {
    return {
        panelAbierto: 0
    };
  },
  computed: {
  },
  created() {
  },
  beforeDestroy() {
  },
  mounted() {
  },
  updated: function() {
  },
  watch: {
  },
  methods: {
  }
};
</script>
