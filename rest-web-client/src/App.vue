<template>
  <div style="height: 100%;">
    <nav class="navbar" style="justify-content: center; background-color: rgba(190, 53, 53, 0.952)">
      <div
        class="navbar-brand"
        style="align-items: center; color: #ffffff; margin-left: 2%;"
      >Cliente para REST Web Service</div>
      <div class="navbar-end">
        <div class="navbar-item">
          <div class="buttons">
            <a
              href="https://github.com/mariam6697/redes-trabajo1"
              style="padding: 5px; color: #ffffff"
            >
              <b-icon icon="github"></b-icon>
            </a>
          </div>
        </div>
      </div>
    </nav>
    <section>
      <b-tabs size="is-medium" position="is-centered" class="block">
        <b-tab-item label="Presentación">
          <section class="hero">
            <div class="hero-body">
              <div class="container has-text-centered">
                <h1 class="title">INFB8080 - Redes y Comunicación de Datos</h1>
                <h2 class="subtitle">Grupo 3</h2>
              </div>
            </div>
          </section>
          <presentacion-grupo></presentacion-grupo>
        </b-tab-item>
        <b-tab-item label="Validador de RUT">
          <Validarut></Validarut>
        </b-tab-item>
        <b-tab-item label="Generador de saludo">
          <Saludo></Saludo>
        </b-tab-item>
      </b-tabs>
    </section>
  </div>
</template>

<script>
import Saludo from "./components/Saludo.vue";
import Validarut from "./components/Validarut.vue";
import PresentacionGrupo from "./components/PresentacionGrupo";

export default {
  name: "App",
  components: {
    Saludo,
    Validarut,
    PresentacionGrupo
  }
};
</script>

<style>
html,
body {
  background-color: gainsboro;
  height: 100%;
  min-height: 100%;
}
button {
  background-color: rgba(190, 53, 53, 0.952);
  padding: 4px;
  font-weight: 500;
  color: white;
  border-radius: 100px;
  border: 0px;
}
button:hover {
  color: rgb(96, 122, 209);
  background-color: #ffffff;
}
/* h1 {
  font-family: Arial;
  color: white;
  font-size: 25px;
  text-align: center;
  background: rgba(190, 53, 53, 0.952);
  padding: 20px;
  border-radius: 25px;
}
h3 {
  font-family: Arial;
  color: rgb(53, 21, 21);
  font-size: 25px;
}
h4 {
  font-family: Arial;
  color: rgb(96, 122, 209);
  font-size: 19px;
} */
</style>