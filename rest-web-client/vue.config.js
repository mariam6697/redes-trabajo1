module.exports = {
    lintOnSave: false,
    publicPath: process.env.NODE_ENV == "production" ? "/redes-trabajo1/" : "/",
    transpileDependencies: ["buefy"]
  };