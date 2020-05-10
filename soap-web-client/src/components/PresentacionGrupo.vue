<template>
  <v-container class="ma-0 pa-0" style="max-width: 100%">
    <div
      class="title text-uppercase"
      align="center"
      justify="center"
    >INFB8080 - Redes y Comunicación de Datos</div>
    <div class="title" align="center" justify="center">Grupo 3</div>
    <v-row class="ma-0 pa-0">
      <v-col v-for="integrante in integrantes" v-bind:key="integrante.id">
        <v-col align-self="start" class="pa-0" cols="12" align="center" justify="center">
          <v-avatar class="profile" color="white" size="164">
            <v-img :src="integrante.imagenUrl"></v-img>
          </v-avatar>
        </v-col>
        <v-col class="py-0">
          <v-list-item>
            <v-list-item-content class="ma-0 pa-0" align="center" justify="center">
              <v-list-item-title class="title">{{integrante.nombre}}</v-list-item-title>
              <v-list-item-subtitle>{{integrante.rut}} <v-btn icon :href="'https://github.com/'+integrante.github">
                <v-icon>mdi-github</v-icon>
              </v-btn></v-list-item-subtitle>
            </v-list-item-content>
          </v-list-item>
        </v-col>
      </v-col>
    </v-row>
  </v-container>
</template>

<script>
export default {
  name: "presentacion-grupo",
  data() {
    return {
      integrantes: [
        {
          id: 1,
          nombre: "Camila Carrasco",
          rut: "18.530.563-5",
          github: "camila1907",
          imagenUrl:
            "https://avatars0.githubusercontent.com/u/63483430?s=460&u=b087edcc85ccd0f2ec7e5b740abb365c6af08cb0&v=4"
        },
        {
          id: 2,
          nombre: "Mariam Maldonado",
          rut: "19.634.546-9",
          github: "mariam6697",
          imagenUrl:
            "https://media-exp1.licdn.com/dms/image/C4D03AQGvLl49Y9E9Mg/profile-displayphoto-shrink_200_200/0?e=1594857600&v=beta&t=y07LcbDJEf4_7yP2m5OITuIbFSmZ153yATvW3W-4U9Y"
        },
        {
          id: 3,
          nombre: "Andrés Muñoz",
          rut: "19.164.393-3",
          github: "Andreesini",
          imagenUrl:
            "https://avatars0.githubusercontent.com/u/63484133?s=460&u=21c158417ede8d0594f58b5d108dddce87c1680f&v=4"
        },
        {
          id: 4,
          nombre: "Sebastián Santelices",
          rut: "19.378.023-7",
          github: "Seiseigy",
          imagenUrl:
            "https://avatars2.githubusercontent.com/u/18251746?s=460&u=5268df77816bbdc1e7b30bbf711f3db5b95476b8&v=4"
        }
      ]
    };
  }
};
</script>