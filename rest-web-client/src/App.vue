<template> 
<div>

  <h1>Cliente para REST web services </h1>
  <h3> Validador de rut </h3>
  <Validarut></Validarut>
  <h3>Generador de Saludo</h3>
  <Saludo></Saludo>

</div>



</template>

<script>
import Saludo from "./components/Saludo.vue";
import Validarut from "./components/Validarut.vue";

export default {
  name: "App",
  components: {
    Saludo,
    Validarut
  }
};
</script>

<style>
body {
  background-color: gainsboro;
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
h1 {
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
}
</style>