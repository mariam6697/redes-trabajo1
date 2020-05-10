<template>
  <div class="row" style="display: flex; justify-content: center;">
    <div v-for="integrante in integrantes" v-bind:key="integrante.id">
      <div
        class="column"
        style="display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;"
      >
        <img style="border-radius: 100px; width: 150px;" :src="integrante.imagenUrl" />
        <span style="font-size: 16px; font-weight: bold;">{{ integrante.nombre }}</span>
        <span style="font-size: 14px">{{ integrante.rut }}</span>
        <a :href="integrante.github" style="padding: 5px; color: #000000">
          <b-icon icon="github"></b-icon>
        </a>
      </div>
    </div>
  </div>
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